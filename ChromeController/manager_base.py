
import time
import base64
import pprint
import gc
import uuid
import logging
import json
import traceback

from . import cr_exceptions
from .transport import ChromeExecutionManager


def decode_chrome_getResponseBody(message):
	'''
	Given a response dict from a Network.getResponseBody command,
	return either the properly decoded binary object, or the unicode
	string.

	'''
	assert 'body' in message
	assert 'base64Encoded' in message

	if message['base64Encoded']:
		# Binary message, decode it
		return base64.b64decode(message['body'])

	else:
		# Message is string, just return it
		return message['body']

def filter_stub(url, meta):
	return True

class ChromeListenerMixin():
	'''
	Docs plzzzz

	'''


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# install_listener_for_content() operates asynchronously, so we need
		# to track outstanding requests for the content that underpins each request ID.
		self.__request_id_to_url_mapping    = {}
		self.__request_id_to_response_meta  = {}
		self.__active_file_content_requests = {}

		self._precondition_check_want_content_request = filter_stub

		self.__requests_in_flight = 0


	def install_message_handler(self, handler):
		'''
		Add handler `handler` to the list of message handlers that will be called on all received messages.

		The handler will be called with the tab context for each message the tab generates.

		NOTE: Handler call order is not specified!

		'''
		def tab_context_closure(message):
			handler(self, message)

		self.transport.install_message_handler_for_tab_key(self.tab_id, tab_context_closure)


	def remove_handlers(self, handler):
		'''
		Remove handler `handler` from the list of message handlers that will be called
		on all received messages for the current tab.

		If the the handler is not present, a KeyError will be raised.
		'''


		def tab_context_closure(message):
			handler(self, message)

		self.transport.remove_handlers_for_tab_key(self.tab_id, tab_context_closure)


	def remove_all_handlers(self):
		'''
		Remove all message handlers for the current tab.

		'''
		try:
			self.transport.remove_all_handlers_for_tab_key(self.tab_id)
		except KeyError:
			pass

	def set_filter_func(self, func):
		'''
		Specify a function with a signature `func(url, meta)` to be used as the precondition filter
		for requesting full fetch results from the browser.

		Precondition check before executing the fetch of content for url `url` from the browser.
		This is mostly useful for preventing the overhead of requesting large binary files multiple times.

		Overriding and returning false on later requests prevents additionl `Network.getResponseBody` invocations
		being set to the browser.

		Note that specifying func=None is a special case where a empty pass function that always returns true will
		be used.

		Additionally, this function is *per tab*, and not automatically copied to a new tab when it is created.

		'''

		self.log.info("Updating getResponseBody precondition filter function to %s", func)

		if func:
			self._precondition_check_want_content_request = func
		else:
			self._precondition_check_want_content_request_ = filter_stub


	def install_listener_for_content(self, handler):
		'''
		Install a content handler.
		`handler` will be called for each received content item.
		Internally, this involves a larger set of handlers to track the mappings of request-id to actual URL,
		and asynchronously invoked Network.getResponseBody against the chromium tab instance.

		The handler is invoked as:
		`handler(self, req_url, response_body)` where self is the pointer to the local ChromeInterface instance.

		'''

		# TODO: The generic filtering of Network.loadingFinished and Network.responseReceived should
		# be moved into a single stand-alone handler that gets called first.
		def _handler(ctx, message):
			try:
				if 'method' in message and message['method'] == "Network.requestWillBeSent":
					# Network.requestWillBeSent
					request_id = message['params']['requestId']
					url = message['params']['request']['url']
					self.__request_id_to_url_mapping[request_id] = url
					self.__requests_in_flight += 1

				# elif 'method' in message and message['method'] == "Network.loadingFinished ":
				elif 'method' in message and message['method'] == "Network.responseReceived":
					request_id = message['params']['requestId']
					assert request_id in self.__request_id_to_url_mapping, "Cannot cross-reference request id %s to url! Presumably the RequestWillBeSent message was lost!" % (request_id, )
					assert self.__request_id_to_url_mapping[request_id] == message['params']['response']['url']
					self.__request_id_to_response_meta[request_id] = message['params']['response']

					self.__requests_in_flight -= 1
					if self.__requests_in_flight < 0:
						self.log.error("Lost a in-flight message? What")
						self.__requests_in_flight = 0

					if self._precondition_check_want_content_request(
								url  = self.__request_id_to_url_mapping[request_id],
								meta = message['params']['response']
							):
						content_request_id = ctx.asynchronous_command("Network.getResponseBody", requestId = request_id)
						self.__active_file_content_requests[content_request_id] = request_id

				if 'id' in message:
					message_id = message['id']
					if message_id in self.__active_file_content_requests:
						req_id = self.__active_file_content_requests[message_id]
						if req_id in self.__request_id_to_url_mapping:
							req_url  = self.__request_id_to_url_mapping[req_id]
							req_meta = self.__request_id_to_response_meta[req_id]
							if 'result' in message:
								response_body = decode_chrome_getResponseBody(message['result'])

								# This is kind of evil
								if handler.__code__.co_argcount == 3:
									handler(self, req_url, response_body)
								elif handler.__code__.co_argcount == 4:
									handler(self, req_url, response_body, meta=req_meta)
								else:
									raise RuntimeError("Only handler callback that accept 3 or 4 arguments permitted")
							else:
								self.log.error("Failed to extract content for request %s, url %s", req_id, req_url)
								self.log.error("Received response: %s", message)
			except KeyError:
				self.log.error("Failure when processing browser message!")
				for line in traceback.format_exc().split("\n"):
					self.log.error("Error -> %s", line)
				self.log.error("Exception occured while processing message:")
				msg_str = json.dumps(message, indent=4)
				for line in msg_str.split("\n"):
					self.log.error("Message -> %s", line)
				self.log.error("This may indicate lost messages, the current state may no longer be valid!")

		self.install_message_handler(_handler)

	def get_active_requests_in_flight(self):
		'''
		Return the number of requests that are currently in-flight.

		Ideally, if the dom has fully loaded, this will be zero. This mostly exists because
		waiting for the dom to appear idle seems to be inadequate to determine if the page
		has fully loaded.
		'''
		return self.__requests_in_flight

	def clear_content_listener_cache(self):
		'''
		The handlers installed by install_listener_for_content() have some persistant
		storage in the class to allow tracking request-id -> response body mappings.

		These shouldn't take much RAM, but extremely long chromium execution times can
		conceivably cause them to grow excessively.

		This call clears them. Note that calling this while a request is in-flight may cause
		strange callback errors.
		'''

		self.__request_id_to_response_meta  = {}
		self.__request_id_to_url_mapping    = {}
		self.__active_file_content_requests = {}



class ChromeInterface(ChromeListenerMixin):
	"""
	Document me, maybe?
	"""


	def __init__(self, binary, dbg_port, use_execution_manager, additional_options, *args, **kwargs):
		"""
		Base chromium transport initialization.

		The binary to execute is assumed to be named `chromium`, and on $PATH
		if not specified in the `binary` parameter.

		The chromium binary is launched with the arg `--remote-debugging-port={dbg_port}` if found.

		Note that the dbg_port must be GLOBALLY unique on a PER-COMPUTER basis. If not specified, it
		will default to an unused port >= 9222.

		Duplication of the dbg_port parameter can often lead to cr_exceptions.ChromeStartupException
		exceptions. If these happen, you may need to call ChromeInterface.close() to force shutdown
		of chromium instances, if you are not trying to instantiate multiple instances of chromium
		at once.


		All arguments that are not explicitly handled by ChromeInterface() are forwarded to the
		underlying ChromeExecutionManager() instace. This is how you can control the behaviour
		of the execution manager, including things like whether chromium is run in headless
		mode, etc...

		"""

		super().__init__()

		# Force cleanup of dangling processes (if any)
		# This is needed because the deletion of active chromium processes
		# can occur dignificantly after the corresponding object goes out-of-scope, which
		# leads to connecting to the wrong process, and then when it is GC'ed,
		# you get a connection-died error.
		gc.collect()


		self.log = logging.getLogger("Main.ChromeController.Interface")
		if use_execution_manager:
			self.is_root_session = False
			self.transport, self.tab_id = use_execution_manager
			# self.transport.connect(tab_key = self.tab_id)

		else:
			self.is_root_session = True
			self.log.debug("Binary: %s", binary)
			self.log.debug("Args: %s", args)
			self.log.debug("Kwargs: %s", kwargs)

			self.tab_id = uuid.uuid4()

			self.transport = ChromeExecutionManager(
					binary             = binary,
					port               = dbg_port,
					base_tab_key       = self.tab_id,
					additional_options = additional_options,
					*args,
					**kwargs
				)
			self.transport._check_process_dead()


		# To correlate request IDs to remote URLs, we have to track the relationship ourselves or
		# do a lot more querying. Ugh.
		self.__active_request_ids           = {}


	def __check_ret(self, ret):
		if ret is False or ret is None:
			raise cr_exceptions.ChromeError("Null response from Chromium (or timed out)!")

		if 'error' in ret:
			err = pprint.pformat(ret)
			raise cr_exceptions.ChromeError("Error in response: \n{}".format(err))

		self.log.debug("No exception in command response!")


	def synchronous_command(self, *args, **kwargs):
		'''
		Forward a command to the remote chrome instance via the transport
		connection, and check the return for an error.

		If the command resulted in an error, a `ChromeController.ChromeError` is raised,
		with the error string containing the response from the remote
		chrome instance describing the problem and it's cause.

		Otherwise, the decoded json data-structure returned from the remote instance is
		returned.

		'''

		self.transport._check_process_dead()
		ret = self.transport.synchronous_command(tab_key=self.tab_id, *args, **kwargs)
		self.transport._check_process_dead()
		self.__check_ret(ret)
		self.transport._check_process_dead()
		return ret


	def asynchronous_command(self, command, **kwargs):
		'''
		Forward a command to the remote chrome instance via the transport
		connection, returning the send_id for the sent command.

		This is primarily useful for writing intentionally async code that
		handles it's own responses via the install_message_handler facilities.
		'''

		self.log.debug("Asynchronous_command to tab %s (%s):", self.tab_id, self.transport._get_cr_tab_meta_for_key(self.tab_id))
		self.log.debug("	kwargs:  '%s'", kwargs)
		self.log.debug("	tab_key:  '%s'", self.tab_id)

		assert "tab_id" not in kwargs, "tab_id is an invalid parameter for an asynchronous command"

		self.transport._check_process_dead()
		send_id = self.transport.asynchronous_command(command=command, tab_key=self.tab_id, **kwargs)
		self.transport._check_process_dead()
		return send_id

	def process_available(self):
		'''
		Process all messages in the socket rx queue.

		Will block for at least 100 milliseconds.

		'''
		self.transport.process_available(self.tab_id)

	def drain_transport(self):
		'''
		"Drain" the transport connection.

		This command simply returns all waiting messages sent from the remote chrome
		instance. This can be useful when waiting for a specific asynchronous message
		from chrome, but higher level calls are better suited for managing wait-for-message
		type needs.

		'''
		self.transport._check_process_dead()
		ret = self.transport.drain(tab_key=self.tab_id)
		self.transport._check_process_dead()
		return ret


	def new_tab(self, *args, **kwargs):
		new = self.__class__(use_execution_manager=(self.transport, uuid.uuid4()), *args, **kwargs)

		self.transport._check_process_dead()
		return new

	def for_existing_tab(self, tab_id, *args, **kwargs):
		'''
		Create a interface object for an existing tab.

		tab_id is a UUID object as lsited in the transport tab_id_map
		'''

		new = self.__class__(use_execution_manager=(self.transport, tab_id), *args, **kwargs)

		self.transport._check_process_dead()
		return new

	def close(self):
		# The process shouldn't be dead before we explicitly kill it.
		self.transport._check_process_dead()

		if self.is_root_session:
			self.transport.close_all()
		else:
			self.transport.close_tab(tab_key=self.tab_id)

		gc.collect()



if __name__ == '__main__':
	import doctest
	doctest.testmod()

