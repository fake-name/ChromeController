""" Client for the Google Chrome browser's remote debugging api.

	> a = Shell(host='localhost', port=92222)


"""
import json
import socket
import time
import websocket
import logging
import requests
from . import cr_exceptions

class ChromeSocketManager():
	"""
	A remote debugging connection to Google Chrome.

	> a = ChromeSocketManager(host='localhost', port=9222)

	   """

	def __init__(self, host='localhost', port=9222, timeout=10):
		"""
		Create connection to remote host `host`, on port `port`.

		Websocket timeout is set to `timeout`.

		Assumes remote is listening for websocket connections.

		"""
		self.host = host
		self.port = port
		self.msg_id = 0
		self.timeout = timeout
		self.soc = None
		self.tablist = None

		self.log = logging.getLogger("Main.ChromeController.SocketTransport")
		self.log.info("Connecting to %s:%s", self.host, self.port)
		self.connect()

		self.messages = []

	def connect(self, tab_idx=None, update_tabs=True):
		"""
		Open a websocket connection to remote browser, determined by
		self.host and self.port.  Each tab has it's own websocket
		endpoint - you specify which with the tab parameter, defaulting
		to 0.  The parameter update_tabs, if True, will force a rescan
		of open tabs before connection.

		"""

		if update_tabs or not self.tablist:
			self.tablist = self.find_tabs(tab_idx)
		if not tab_idx:
			tab_idx = 0
		wsurl = self.tablist[tab_idx]['webSocketDebuggerUrl']
		try:
			if self.soc is not None and self.soc.connected:
				self.soc.close()
			self.soc = websocket.create_connection(wsurl)
			self.soc.settimeout(self.timeout)

		except (socket.timeout, websocket.WebSocketTimeoutException):
			raise cr_exceptions.ChromeCommunicationsError("Could not connect to remote chromium.")

	def close(self):
		""" Close websocket connection to remote browser."""
		if self.soc:
			self.soc.close()
			self.soc = None

	def find_tabs(self, tab_idx):
		"""Connect to host:port and request list of tabs
			 return list of dicts of data about open tabs."""
		# find websocket endpoint
		try:
			response = requests.get("http://%s:%s/json" % (self.host, self.port))
		except requests.exceptions.ConnectionError:
			raise cr_exceptions.ChromeConnectFailure("Failed to fetch configuration json from browser!")

		tablist = json.loads(response.text)

		if not tab_idx:
			tab_idx = 0
		if not tab_idx <= len(tablist):
			raise cr_exceptions.ChromeConnectFailure("Tab %s not found in tablist (%s)", (tab_idx, tablist))
		if not 'webSocketDebuggerUrl' in tablist[tab_idx]:
			raise cr_exceptions.ChromeConnectFailure("Tab %s has no 'webSocketDebuggerUrl' (%s)", (tab_idx, tablist))

		return tablist

	def __check_open_socket(self):
		if self.soc is None or (self.soc is not None and not self.soc.connected):
			self.connect()


	def synchronous_command(self, command, **params):
		"""
		Synchronously execute command `command` with params `params` in the
		remote chrome instance, returning the response from the chrome instance.

		"""

		self.log.debug("Synchronous_command:")
		self.log.debug("	command: '%s'", command)
		self.log.debug("	params:  '%s'", params)

		send_id = self.send(command, params)
		resp = self.recv(message_id=send_id)

		self.log.debug("	Response: '%s'", str(resp).encode("ascii", 'ignore').decode("ascii"))

		return resp

	def send(self, command, params=None):
		'''
		Send command `command` with optional parameters `params` to the
		remote chrome instance.

		The command `id` is automatically added to the outgoing message.

		return value is the command id, which can be used to match a command
		to it's associated response.
		'''
		self.__check_open_socket()

		sent_id = self.msg_id

		command = {
				"id": self.msg_id,
				"method": command,
			}

		if params:
			command["params"] = params
		navcom = json.dumps(command)


		self.log.debug("		Sending: '%s'", navcom)
		try:
			self.soc.send(navcom)
		except (socket.timeout, websocket.WebSocketTimeoutException):
			raise cr_exceptions.ChromeCommunicationsError("Failure sending command to chromium.")
		except websocket.WebSocketConnectionClosedException:
			raise cr_exceptions.ChromeCommunicationsError("Websocket appears to have been closed. Is the"
				" remote chromium instance dead?")


		self.msg_id += 1
		return sent_id


	def ___recv(self):
		try:
			tmp = self.soc.recv()
			self.log.debug("		Received: '%s'", tmp)

			decoded = json.loads(tmp)
			return decoded
		except (socket.timeout, websocket.WebSocketTimeoutException):
			return None
		except websocket.WebSocketConnectionClosedException:
			raise cr_exceptions.ChromeCommunicationsError("Websocket appears to have been closed. Is the"
				" remote chromium instance dead?")

	def recv_filtered(self, keycheck, timeout=30):
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


		self.__check_open_socket()

		# First, check if the message has already been received.
		for idx in range(len(self.messages)):
			if keycheck(self.messages[idx]):
				return self.messages.pop(idx)

		timeout_at = time.time() + timeout
		while 1:
			tmp = self.___recv()
			if keycheck(tmp):
				return tmp
			else:
				self.messages.append(tmp)

			if time.time() > timeout_at:
				return None


	def recv(self, message_id=None, timeout=30):
		'''
		Recieve a message, optionally filtering for a specified message id.

		If `message_id` is none, the first command in the receive queue is returned.
		If `message_id` is not none, the command waits untill a message is received with
		the specified id, or it times out.

		Timeout is the number of seconds to wait for a response, or `None` if the timeout
		has expired with no response.

		'''

		self.__check_open_socket()

		# First, check if the message has already been received.
		for idx in range(len(self.messages)):
			if self.messages[idx]:
				if "id" in self.messages[idx] and message_id:
					if self.messages[idx]['id'] == message_id:
						return self.messages.pop(idx)

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

		return self.recv_filtered(check_func, timeout)


	def drain(self):
		'''
		Return all messages in waiting for the websocket connection.
		'''

		ret = []
		while len(self.messages):
			ret.append(self.messages.pop(0))

		tmp = self.___recv()
		while tmp is not None:
			ret.append(tmp)
			tmp = self.___recv()
		return ret



if __name__ == '__main__':
	import doctest
	doctest.testmod()

