""" Client for the Google Chrome browser's remote debugging api.

	> a = Shell(host='localhost', port=92222)


"""
import json
import socket
import time
import websocket
import requests

TRANSPORT_DEBUG = True
TRANSPORT_TX_DEBUG = TRANSPORT_DEBUG
TRANSPORT_RX_DEBUG = TRANSPORT_DEBUG


class ChromeSocketManager():
	"""
	A remote debugging connection to Google Chrome.

	> a = ChromeSocketManager(host='localhost', port=9222)



	   """

	def __init__(self, host='localhost', port=9222):
		"""
		Create connection to remote host `host`, on port `port`.

		Assumes remote is listening for websocket connections.

		"""
		self.host = host
		self.port = port
		self.msg_id = 0
		self.soc = None
		self.tablist = None
		self.find_tabs()

		self.messages = []



	def connect(self, tab=None, update_tabs=True):
		"""
		Open a websocket connection to remote browser, determined by
		self.host and self.port.  Each tab has it's own websocket
		endpoint - you specify which with the tab parameter, defaulting
		to 0.  The parameter update_tabs, if True, will force a rescan
		of open tabs before connection.

		"""

		if update_tabs or not self.tablist:
			self.find_tabs()
		if not tab:
			tab = 0
		wsurl = self.tablist[tab]['webSocketDebuggerUrl']
		if self.soc is not None and self.soc.connected:
			self.soc.close()
		self.soc = websocket.create_connection(wsurl)
		self.soc.settimeout(1)

	def close(self):
		""" Close websocket connection to remote browser."""
		if self.soc:
			self.soc.close()
			self.soc = None

	def find_tabs(self):
		"""Connect to host:port and request list of tabs
			 return list of dicts of data about open tabs."""
		# find websocket endpoint
		response = requests.get("http://%s:%s/json" % (self.host, self.port))
		self.tablist = json.loads(response.text)
		return self.tablist


	def __check_open_socket(self):
		if self.soc is None or (self.soc is not None and not self.soc.connected):
			self.connect(tab=0)


	def synchronous_command(self, command, **params):
		"""
		Synchronously execute command `command` with params `params` in the
		remote chrome instance, returning the response from the chrome instance.

		"""

		if TRANSPORT_TX_DEBUG:
			print("Synchronous_command:")
			print("	command: '%s'" % command)
			print("	params:  '%s'" % params)

		send_id = self.send(command, params)
		resp = self.recv(message_id=send_id)

		if TRANSPORT_RX_DEBUG:
			print("	Response: '%s'" % str(resp).encode("ascii", 'ignore').decode("ascii"))

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


		if TRANSPORT_TX_DEBUG:
			print("		Sending: '%s'" % navcom)

		self.soc.send(navcom)

		self.msg_id += 1
		return sent_id


	def ___recv(self):
		try:
			tmp = self.soc.recv()
			if TRANSPORT_RX_DEBUG:
				print("		Received: '%s'" % tmp)

			decoded = json.loads(tmp)
			return decoded
		except (socket.timeout, websocket.WebSocketTimeoutException):
			return None

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
			if "id" in self.messages[idx] and message_id:
				if self.messages[idx]['id'] == message_id:
					return self.messages.pop(idx)

		# Then spin untill we either have the message,
		# or have timed out.
		def check_func(message):
			if message_id is None:
				return True
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

