
import time
import traceback
import pprint
import gc
import uuid
import logging

from . import cr_exceptions
from .transport import ChromeExecutionManager



class ChromeInterface():
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

		"""

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
			self.transport.check_process_ded()


		# To correlate request IDs to remote URLs, we have to track the relationship ourselves or
		# do a lot more querying. Ugh.
		self.__active_request_ids           = {}

		# install_listener_for_content() operates asynchronously, so we need
		# to track outstanding requests for the content that underpins each request ID.
		self.__active_file_content_requests = {}

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

		self.transport.check_process_ded()
		ret = self.transport.synchronous_command(tab_key=self.tab_id, *args, **kwargs)
		self.transport.check_process_ded()
		self.__check_ret(ret)
		self.transport.check_process_ded()
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

		self.transport.check_process_ded()
		send_id = self.transport.asynchronous_command(command=command, tab_key=self.tab_id, **kwargs)
		self.transport.check_process_ded()
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
		self.transport.check_process_ded()
		ret = self.transport.drain(tab_key=self.tab_id)
		self.transport.check_process_ded()
		return ret



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


	def remove_all_handlers(self, tab_key):
		'''
		Remove all message handlers for the current tab.

		'''

		self.transport.remove_all_handlers_for_tab_key(self.tab_id)


	def new_tab(self, *args, **kwargs):
		new = self.__class__(use_execution_manager=(self.transport, uuid.uuid4()), *args, **kwargs)
		self.transport.check_process_ded()
		return new

	def close(self):
		# The process shouldn't be dead before we explicitly kill it.
		self.transport.check_process_ded()

		if self.is_root_session:
			self.transport.close_all()
		else:
			self.transport.close_tab(tab_key=self.tab_id)

		gc.collect()



	def install_listener_for_content(self, handler):

		def handler(ctx, message):
			if 'method' in message and message['method'] == "Network.loadingFinished":
				# print("Handler call with context %s, for message %s" % (ctx, message))
				response_id = ctx.asynchronous_command("Network.getResponseBody", requestId = message['params']['requestId'])
				self.__active_file_content_requests[response_id] = {

				}
			if 'id' in message:
				pass




if __name__ == '__main__':
	import doctest
	doctest.testmod()

