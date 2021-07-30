""" Client for the Google Chrome browser's remote debugging api.

	> a = Shell(host='localhost', port=92222)


"""
import os
import json
import sys
import socket
import time
import pprint
import logging
import shlex
import os.path
import requests
import traceback
import signal
import websocket
import subprocess
import distutils.spawn
from . import cr_exceptions

if sys.platform == 'win32':
	import win32con
	import win32api

ACTIVE_PORTS = set()


class ChromeExecutionManager():
	"""
	Class for managing talking to a chromium instance, as well as
	managing the chromium instance's execution lifetime.

	"""

	def __init__(self,
			binary,
			base_tab_key,
			host               = 'localhost',
			port               = None,
			websocket_timeout  = 10,
			enable_gpu         = False,
			headless           = True,
			xvfb               = False,
			additional_options = [],
			):
		"""

		Start up a chromium instance binary `binary`, with the base debug port `port`,
		on host `localhost`.

		Note: If the port is set to None (the default), the port will be the next availble port accounting for other
		chrome instances in the current python process.

		If port is not none, and the port is already in use, you will get a ReusedPortError.

		base_tab_key is any hashable python object that is used for multi-tab interfacing.

		"""

		if port is None:
			port = 9222 + (os.getpid() & 0x3FFF)
			if port > 65530:
				port -= 5000
			while port in ACTIVE_PORTS:
				port += 1

		if port in ACTIVE_PORTS:
			raise cr_exceptions.ReusedPortError("Attempting to start chromium using a already-in-use debug port (%s, %s)!" % (port, ACTIVE_PORTS))

		ACTIVE_PORTS.add(port)

		self.binary             = binary
		self.host               = host
		self.port               = port
		self.headless           = headless
		self.xvfb               = xvfb
		self.enable_gpu         = enable_gpu
		self.msg_id             = 0
		self.websocket_timeout  = websocket_timeout
		self.additional_options = additional_options

		self.tablist = None
		self.soclist = {}
		self.tab_id_map = {}

		self.log = logging.getLogger("Main.ChromeController.ExecutionManager")


		self.log.info("Launching binary %s", self.binary)

		# We retry starting chromium a few times, because it's either brittle
		# or sometimes takes more then 10 seconds to start.
		# Not sure which.
		for x in range(999):
			try:
				self._launch_process(self.binary, self.port, base_tab_key, additional_options)
				break
			except cr_exceptions.ChromeConnectFailure:
				if x > 3:
					raise

		# self.log.info("Connecting to %s:%s", self.host, self.port)
		# self.connect_to_chromium(base_tab_key)

		self._messages = {}
		self._message_filters = {}


	def _launch_process(self, binary, dbg_port, base_tab_key, additional_options):

		if binary is None:
			binary = "chromium"

		binary, *args = shlex.split(binary)

		if not os.path.exists(binary):
			fixed = distutils.spawn.find_executable(binary)
			if fixed:
				binary = fixed
		if not binary or not os.path.exists(binary):
			self.log.warning("Could not find binary '%s'" % binary)

		if self.headless and self.xvfb:
			raise RuntimeError("Headless mode with XVFB does not make sense")

		prefix = []
		if self.xvfb:
			prefix = ['xvfb-run',
					 '-a',
					 '--server-args=-screen 0 1920x1080x24 -ac -nolisten tcp -dpi 96 +extension RANDR',
					 ]

		argv = prefix + [binary] + args + [
				'--remote-debugging-port={dbg_port}'.format(dbg_port=dbg_port),
				'--enable-features=NetworkService',
			]
		if self.headless:
			argv.append('--headless')

		if self.enable_gpu is False:
			argv.append('--disable-gpu')
		argv += additional_options


		# We need a separate process group on windows,
		# to make ctrl+c work properly.
		creationflags = 0
		if sys.platform == 'win32':
			creationflags |= subprocess.CREATE_NEW_PROCESS_GROUP

		preexec_fn = None
		if 'linux' in sys.platform:
			from . import exit_handler
			preexec_fn = exit_handler.on_parent_exit('SIGTERM')

		self.cr_proc = subprocess.Popen(argv,
										stdin         = open(os.path.devnull, "r"),
										stdout        = subprocess.PIPE,
										stderr        = subprocess.PIPE,
										creationflags = creationflags,
										preexec_fn    = preexec_fn,
									)

		self.log.debug("Spawned process: %s, PID: %s", self.cr_proc, self.cr_proc.pid)
		for x in range(100):
			try:
				self.tablist = self.fetch_tablist()

				if not self.tablist:
					raise cr_exceptions.ChromeStartupException("No tabs in started chromium?")

				# self.tab_id_map[base_tab_key] = self.tablist[0]['id']
				# print("Tab base key:", base_tab_key, self.tablist[0]['id'])
				return
			except cr_exceptions.ChromeConnectFailure as e:
				if x > 8:
					raise e
				time.sleep(2)

	def __close_internal_linux(self):
		'''
		Shut down the chrome process. On linux, this will call terminate() on the process
		if chrome does not shut down within the timeout (5 seconds).
		'''


		self.log.debug("Sending sigint to chromium")
		self.cr_proc.send_signal(signal.SIGINT)
		try:
			self._check_process_dead()  # Needed to flush the communcation pipes, sometimes
			self.log.debug("Waiting for chromium to exit")
			try:
				self.cr_proc.wait(timeout=5)
			except subprocess.TimeoutExpired:
				self.log.warning("Chromium failed to exit on sigint")

			try:
				self.cr_proc.terminate()
			except ProcessLookupError:
				self.log.debug("Process exited normally, no need to terminate.")

			self._check_process_dead()  # Processes may dangle until the pipes are closed.

			try:
				self.cr_proc.kill()
			except ProcessLookupError:
				self.log.debug("Process exited normally, no need to terminate.")

			self._check_process_dead()  # Processes may dangle until the pipes are closed.

		except cr_exceptions.ChromeDiedError:
			# Considering we're /trying/ to kill chrome, it
			# dying is OK.
			pass

		self.log.debug("Pid: %s, Return code: %s", self.cr_proc.pid, self.cr_proc.returncode)
		self.log.debug("Chromium closed!")

	def __close_internal_windows(self):
		'''
		Shut down the chrome process. On linux, this will emit a CTRL+C event to the process
		if chrome does not shut down within the timeout (5 seconds).
		'''

		self.log.debug("Sending CTRL_C_EVENT to chromium")

		win32api.GenerateConsoleCtrlEvent(win32con.CTRL_C_EVENT, self.cr_proc.pid)
		self.cr_proc.send_signal(signal.CTRL_BREAK_EVENT)
		self.cr_proc.send_signal(signal.CTRL_C_EVENT)
		self.cr_proc.send_signal(1)
		self.log.debug("Sent")
		try:
			self._check_process_dead()  # Needed to flush the communcation pipes, sometimes

			# I can't get this to fucking ever work,
			# so just skip and go straight to termination.
			# self.log.debug("Waiting for chromium to exit")
			# try:
			# 	self.cr_proc.wait(timeout=5)
			# except subprocess.TimeoutExpired:
			# 	pass

			try:
				self.cr_proc.terminate()
			except ProcessLookupError:
				self.log.debug("Process exited normally, no need to terminate.")

			self._check_process_dead()  # Processes may dangle until the pipes are closed.

			try:
				self.cr_proc.kill()
			except ProcessLookupError:
				self.log.debug("Process exited normally, no need to terminate.")

			self._check_process_dead()  # Processes may dangle until the pipes are closed.

		except cr_exceptions.ChromeDiedError:
			self.log.debug("ChromeDiedError while polling. Ignoring due to shutdown.")
			# Considering we're /trying/ to kill chrome, it
			# dying is OK.

		self.log.debug("Pid: %s, Return code: %s", self.cr_proc.pid, self.cr_proc.returncode)
		self.log.debug("Chromium closed!")


	def close_chromium(self):
		'''
		Close the remote chromium instance.

		This command is normally executed as part of the class destructor.
		It can be called early without issue, but calling ANY class functions
		after the remote chromium instance is shut down will have unknown effects.

		Note that if you are rapidly creating and destroying ChromeController instances,
		you may need to *explicitly* call this before destruction.
		'''
		if self.cr_proc:
			try:
				if sys.platform == 'win32':
					self.__close_internal_windows()
				else:
					self.__close_internal_linux()
			except Exception as e:
				for line in traceback.format_exc().split("\n"):
					self.log.error(line)



		ACTIVE_PORTS.discard(self.port)


	def _check_process_dead(self):
		'''
		Poll the chromium sub-process to check if it's still alive.

		Will raise cr_exceptions.ChromeDiedError if chrome is not alive.

		'''
		self.cr_proc.poll()
		if self.cr_proc.returncode != None:
			try:
				stdout, stderr = self.cr_proc.communicate()
				raise cr_exceptions.ChromeDiedError("Chromium process died unexpectedly! Don't know "
					"how to continue!\n	Chromium stdout: {}\n	Chromium stderr: {}".format(stdout.decode("utf-8"), stderr.decode("utf-8")))
			except ValueError:
				# The communcation pipes can go away if the process has exited.
				# If so, ignore the resulting error.
				raise cr_exceptions.ChromeDiedError("Chromium process died unexpectedly! Don't know how to continue!")


	def _get_tab_idx_for_key(self, tab_key):
		'''

		'''

		if tab_key not in self.tab_id_map:
			return None

		cr_tab_id = self.tab_id_map[tab_key]['id']

		for idx, tab_dat in enumerate(self.tablist):
			if tab_dat['id'] == cr_tab_id:
				return idx

		self.log.error("Missing tab %s from tab list!", tab_key)
		self.log.error("Corresponding cr tab id: %s!", cr_tab_id)
		for tab_key, cr_tab_id in self.tab_id_map.items():
			self.log.error("Tab pair %s -> %s", tab_key, cr_tab_id['id'])
		self.log.error("Chromium tabs (%s):", len(self.tablist))
		for tab in self.tablist:
			self.log.error("	cr tab id: %s", tab['id'])

		raise cr_exceptions.ChromeTabNotFoundError("Tab with ID %s (cr ID: %s) not found!" % (tab_key, cr_tab_id['id']))

	def _get_cr_tab_meta_for_key(self, tab_key):
		if tab_key not in self.tab_id_map:
			return None

		return self.tab_id_map[tab_key]

	def connect_to_chromium(self, tab_key):
		"""
		Open a websocket connection to remote browser, determined by
		self.host and self.port.  Each tab has it's own websocket
		endpoint.

		Note that the manager maintains a connection to a blank tab to
		prevent closing all remote tabs from causing the browser to exit.
		This tab is not used by anything.


		"""

		assert self.tablist is not None

		tab_idx = self._get_tab_idx_for_key(tab_key)

		if not self.tablist:
			self.tablist = self.fetch_tablist()

		for fails in range(9999):
			try:
				# If we're one past the end of the tablist, we need to create a new tab
				if tab_idx is None:
					self.log.debug("Creating new tab (%s active)", len(self.tablist))
					self.__create_new_tab(tab_key)

				self.__connect_to_tab(tab_key)
				break

			except cr_exceptions.ChromeConnectFailure as e:
				if fails > 6:
					self.log.error("Failed to fetch tab websocket URL after %s retries. Aborting!", fails)
					raise e
				self.log.info("Tab may not have started yet (%s tabs active). Recreating.", len(self.tablist))
				# self.log.info("Tag: %s", self.tablist[tab_idx])


				# For reasons I don't understand, sometimes a new tab doesn't get a websocket
				# debugger URL. Anyways, we close and re-open the tab if that happens.
				# TODO: Handle the case when this happens on the first tab. I think closing the first
				#       tab will kill chromium.
				self.__close_tab(tab_key)

	def __repr__(self):
		return "<ChromeExecutionManager for tabs \n%s\n>" % pprint.pformat(self.tab_id_map)

	def pprint_tablist(self):
		self.log.info("Tablist type: %s", type(self.tablist))
		for line in pprint.pformat(list(enumerate(self.tablist))).split("\n"):
			self.log.info("	%s", line)

	def __create_new_tab(self, tab_key, start_at_url=None):
		url = "http://%s:%s/json/new" % (self.host, self.port)
		if start_at_url:
			url += "?%s" % (start_at_url, )
		try:
			requests.get(url)
			self.tablist = self.fetch_tablist()
			known_tabs = list(self.tab_id_map.values())
			for tab in self.tablist:

				# Glom onto the first tab in the tablist that's not known.
				if tab['id'] not in [tmp['id'] for tmp in known_tabs]:
					self.log.debug("New tab created with ID: '%s'", tab['id'])
					self.tab_id_map[tab_key] = tab
					return


		except requests.exceptions.ConnectionError:
			raise cr_exceptions.ChromeConnectFailure("Failed to create a new tab in remote chromium!")

	def __connect_to_tab(self, tab_key):
		assert tab_key not in self.soclist

		cr_tab_meta = self._get_cr_tab_meta_for_key(tab_key)

		if not 'webSocketDebuggerUrl' in cr_tab_meta:
			raise cr_exceptions.ChromeConnectFailure("Tab %s has no 'webSocketDebuggerUrl' (%s)" % (tab_key, self.tablist))

		wsurl = cr_tab_meta['webSocketDebuggerUrl']

		try:
			self.log.info("Setting up websocket connection for key '%s'", tab_key)
			self.soclist[tab_key] = websocket.create_connection(wsurl)
			self.soclist[tab_key].settimeout(self.websocket_timeout)

		except (socket.timeout, websocket.WebSocketTimeoutException):
			raise cr_exceptions.ChromeCommunicationsError("Could not connect to remote chromium.")

	def __close_tab(self, tab_key, timeout=None):

		# traceback.print_stack()

		cr_tab_id = self.tab_id_map[tab_key]['id']

		url = "http://%s:%s/json/close/%s" % (self.host, self.port, cr_tab_id)
		requests.get(url, timeout=timeout)

		# Delete the now-removed tab from the tab map
		self.tab_id_map.pop(tab_key)

		self.log.info("Closing websocket connecton %s (%s)", tab_key, len(self.soclist))
		self.soclist.pop(tab_key, None)

		self.tablist = self.fetch_tablist()
		return self.tablist

	def close_tab(self, tab_key):
		self.log.info("Closing tab %s (cr ID: %s)", tab_key, self.tab_id_map[tab_key]['id'])
		self.__close_tab(tab_key)

		# If we've closed all the chrome tabs, shut down the interface.
		if not len(self.tab_id_map):
			self.log.info("All tabs are closed. Closing chromium!")
			self.close_websockets()
			self.close_chromium()

	def close_all(self):
		self.log.info("Closing all tabs.")
		for tab_key in list(self.tab_id_map.keys()):
			self.log.info("Closing tab %s (cr ID: %s)", tab_key, self.tab_id_map[tab_key]['id'])
			self.__close_tab(tab_key)

		self.log.info("All tabs are closed. Closing chromium!")
		self.close_websockets()
		self.close_chromium()

	def close_websockets(self):
		""" Close websocket connection to remote browser."""
		self.log.info("Websocket Teardown called")
		for key in list(self.soclist.keys()):
			if self.soclist[key]:
				self.soclist[key].close()
			self.soclist.pop(key)


	def fetch_tablist(self):
		"""Connect to host:port and request list of tabs
			 return list of dicts of data about open tabs."""
		# find websocket endpoint
		try:
			response = requests.get("http://%s:%s/json" % (self.host, self.port))
		except requests.exceptions.ConnectionError:
			raise cr_exceptions.ChromeConnectFailure("Failed to fetch configuration json from browser!")

		tablist = json.loads(response.text)

		return tablist

	def __check_open_socket(self, tab_key):
		# self.log.info("__check_open_socket -> %s", tab_key)
		if not tab_key in self.soclist:
			self.connect_to_chromium(tab_key=tab_key)
		if self.soclist[tab_key].connected is not True:
			self.connect_to_chromium(tab_key=tab_key)
		if not tab_key in self._messages:
			self._messages[tab_key] = []


	def asynchronous_command(self, command, tab_key, **params):
		"""
		Asynchronously send command `command` with params `params` in the
		remote chrome instance, returning the send_id for the sent command.
		"""
		self.log.debug("Asynchronous_command to tab %s (%s):", tab_key, self._get_cr_tab_meta_for_key(tab_key))
		self.log.debug("	command: '%s'", command)
		self.log.debug("	params:  '%s'", params)
		self.log.debug("	tab_key:  '%s'", tab_key)

		send_id = self.send(command=command, tab_key=tab_key, params=params)

		self.log.debug("	send_id: '%s'", send_id)

		# self.log.debug("	resolved tab idx %s:", self.tab_id_map[tab_key])
		return send_id

	def synchronous_command(self, command, tab_key, **params):
		"""
		Synchronously execute command `command` with params `params` in the
		remote chrome instance, returning the response from the chrome instance.

		"""
		self.log.debug("Synchronous_command to tab %s (%s):", tab_key, self._get_cr_tab_meta_for_key(tab_key))
		self.log.debug("	command: '%s'", command)
		self.log.debug("	params:  '%s'", params)
		self.log.debug("	tab_key:  '%s'", tab_key)

		send_id = self.send(command=command, tab_key=tab_key, params=params)
		resp = self.recv(message_id=send_id, tab_key=tab_key)

		self.log.debug("	Response: '%s'", str(resp).encode("ascii", 'ignore').decode("ascii"))

		# self.log.debug("	resolved tab idx %s:", self.tab_id_map[tab_key])
		return resp

	def send(self, command, tab_key, params=None):
		'''
		Send command `command` with optional parameters `params` to the
		remote chrome instance.

		The command `id` is automatically added to the outgoing message.

		return value is the command id, which can be used to match a command
		to it's associated response.
		'''
		self.__check_open_socket(tab_key)

		sent_id = self.msg_id

		command = {
				"id": self.msg_id,
				"method": command,
			}

		if params:
			command["params"] = params
		navcom = json.dumps(command)


		# self.log.debug("		Sending: '%s'", navcom)
		try:
			self.soclist[tab_key].send(navcom)
		except (socket.timeout, websocket.WebSocketTimeoutException):
			raise cr_exceptions.ChromeCommunicationsError("Failure sending command to chromium.")
		except websocket.WebSocketConnectionClosedException:
			raise cr_exceptions.ChromeCommunicationsError("Websocket appears to have been closed. Is the"
				" remote chromium instance dead?")


		self.msg_id += 1
		return sent_id


	def __recv(self, tab_key, timeout=None):
		try:
			if timeout:
				self.soclist[tab_key].settimeout(timeout)

			tmp = self.soclist[tab_key].recv()
			self.log.debug("		Received: '%s'", tmp)

			decoded = json.loads(tmp)

			# Run the new message through any message handler listeners (if present)
			if tab_key in self._message_filters:
				for handler in self._message_filters[tab_key]:
					handler(decoded)

			return decoded
		except (socket.timeout, websocket.WebSocketTimeoutException):
			return None
		except websocket.WebSocketConnectionClosedException:
			raise cr_exceptions.ChromeCommunicationsError("Websocket appears to have been closed. Is the"
				" remote chromium instance dead?")
		finally:
			self.soclist[tab_key].settimeout(self.websocket_timeout)

	def __check_console_log(self, message):
		'''
		Examine received message to determine if it was the output of a `console.xxx()` call, and
		optionally output it to stdout.
		'''

		# I haven't figured out how this is ever called with a None argument.
		if not message:
			return

		if 'method' not in message:
			return
		if message['method'] != "Runtime.consoleAPICalled":
			return
		if 'params' not in message:
			return

		params = message['params']

		if 'type' not in params:
			return
		if params['type'] != 'log':
			return

		if 'args' not in params:
			return

		output = " ".join([str(tmp.get("value", "")) for tmp in params['args']])
		self.log.info("Console output: %s", output)




	def recv_filtered(self, keycheck, tab_key, timeout=30, message=None):
		'''
		Receive a filtered message, using the callable `keycheck` to filter received messages
		for content.

		`keycheck` is expected to be a callable that takes a single parameter (the decoded response
		from chromium), and returns a boolean (true, if the command is the one filtered for, or false
		if the command is not the one filtered for).

		This is used internally, for example, by `recv()`, to filter the response for a specific ID:

		```
			def check_func(message):
				if message_id is None:
					return True
				if "id" in message:
					return message['id'] == message_id
				return False
			return self.recv_filtered(check_func, timeout)

		```

		Note that the function is defined dynamically, and `message_id` is captured via closure.

		'''


		self.__check_open_socket(tab_key)

		# First, check if the message has already been received.
		for idx in range(len(self._messages[tab_key])):
			if keycheck(self._messages[tab_key][idx]):
				return self._messages[tab_key].pop(idx)

		timeout_at = time.time() + timeout
		while 1:
			tmp = self.__recv(tab_key)

			self.__check_console_log(tmp)
			if keycheck(tmp):
				return tmp
			else:
				self._messages[tab_key].append(tmp)

			if time.time() > timeout_at:
				if message:
					raise cr_exceptions.ChromeResponseNotReceived("Failed to receive response in recv_filtered() (%s)" % message)
				else:
					raise cr_exceptions.ChromeResponseNotReceived("Failed to receive response in recv_filtered()")
			else:
				time.sleep(0.005)

	def recv_all_filtered(self, keycheck, tab_key, timeout=0.5):
		'''
		Receive a all messages matching a filter, using the callable `keycheck` to filter received messages
		for content.

		This function will *ALWAY* block for at least `timeout` seconds.

		If chromium is for some reason continuously streaming responses, it may block forever!

		`keycheck` is expected to be a callable that takes a single parameter (the decoded response
		from chromium), and returns a boolean (true, if the command is the one filtered for, or false
		if the command is not the one filtered for).

		```
			def check_func(message):
				if message_id is None:
					return True
				if "id" in message:
					return message['id'] == message_id
				return False
			return self.recv_filtered(check_func, timeout)

		```

		Note that the function is defined dynamically, and `message_id` is captured via closure.

		'''


		self.__check_open_socket(tab_key)
		# First, check if the message has already been received.
		ret           = [tmp for tmp in self._messages[tab_key] if keycheck(tmp)]
		self._messages[tab_key] = [tmp for tmp in self._messages[tab_key] if not keycheck(tmp)]

		self.log.debug("Waiting for all messages from the socket")
		timeout_at = time.time() + timeout
		while 1:
			tmp = self.__recv(tab_key, timeout=timeout)
			if keycheck(tmp):
				ret.append(tmp)
			else:
				self._messages[tab_key].append(tmp)

			if time.time() > timeout_at:
				return ret
			else:
				self.log.debug("Sleeping: %s, %s" % (timeout_at, time.time()))
				time.sleep(0.005)

	def process_available(self, tab_key, timeout=0.1):
		'''
		Process all messages in the socket rx queue.

		Will block for at least 100 milliseconds.

		'''
		self.__recv(tab_key, timeout=timeout)

	def recv(self, tab_key, message_id=None, timeout=30):
		'''
		Recieve a message, optionally filtering for a specified message id.

		If `message_id` is none, the first command in the receive queue is returned.
		If `message_id` is not none, the command waits untill a message is received with
		the specified id, or it times out.

		Timeout is the number of seconds to wait for a response, or `None` if the timeout
		has expired with no response.

		'''

		self.__check_open_socket(tab_key)

		# First, check if the message has already been received.
		for idx in range(len(self._messages[tab_key])):
			if self._messages[tab_key][idx]:
				if "id" in self._messages[tab_key][idx] and message_id:
					if self._messages[tab_key][idx]['id'] == message_id:
						return self._messages[tab_key].pop(idx)

		# Then spin untill we either have the message,
		# or have timed out.
		def check_func(message):
			if message_id is None:
				return True
			if not message:
				self.log.debug("Message is not true (%s)!", message)
				return False
			if "id" in message:
				return message['id'] == message_id
			return False

		return self.recv_filtered(check_func, tab_key, timeout)

	def flush(self, tab_key):
		'''
		Flush the pending RX buffer for a specific tab key.
		'''
		self._messages[tab_key] = []

	def drain(self, tab_key):
		'''
		Return all messages in waiting for the websocket connection.
		'''
		self.log.debug("Draining transport")
		ret = []
		while len(self._messages[tab_key]):
			ret.append(self._messages[tab_key].pop(0))

		self.log.debug("Polling socket")

		tmp = self.__recv(tab_key)
		while tmp is not None:
			ret.append(tmp)
			tmp = self.__recv(tab_key)

		self.log.debug("Drained %s messages", len(ret))
		return ret

	def __del__(self):
		self.log.debug("Transport destructor called. Tearing down chromium")
		try:
			self.close_chromium()
		except Exception:
			pass

		ACTIVE_PORTS.discard(self.port)

	def install_message_handler_for_tab_key(self, tab_key, handler):
		'''
		Add handler `handler` to the list of message handlers that will be called
		on all received messages for the tab with a key of `tab_key`.

		The handler will be called with the tab context for each message the tab generates.

		NOTE: Handler call order is not specified!

		'''

		self._message_filters.setdefault(tab_key, set())
		self._message_filters[tab_key].add(handler)


	def remove_handlers_for_tab_key(self, tab_key, handler):
		'''
		Remove handler `handler` from the list of message handlers that will be called
		on all received messages for the tab with a key of `tab_key`.

		If the tab_key is not present, or the handler is not present in the tab, a
		KeyError will be raised.

		This is potentially of little use, since the tab layer uses a dynamically
		defined closure to capture the calling tab context, so attempting to remove
		a defined funtion will fail since the function is no longer available.

		'''

		tab_set = self._message_filters[tab_key]  # Will error if tab_key is not a valid tab-key.
		tab_set.remove(handler)  # Remove the handler


	def remove_all_handlers_for_tab_key(self, tab_key):
		'''
		Add handler `handler` to the list of message handlers that will be called on all received messages.

		If the tab key is not present, no error will be raised.

		'''

		if tab_key in self._message_filters:
			tab_set = self._message_filters[tab_key]
			tab_set.clear()


if __name__ == '__main__':
	import doctest
	doctest.testmod()

