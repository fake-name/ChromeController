""" Client for the Google Chrome browser's remote debugging api.

	> a = Shell(host='localhost', port=92222)

	a.tablist has a list of details on open tabs.

	> a.connect(tab=index, updateTabs=True)

	will connect a.soc to the webservice endpoint for tablist[index]'th
	tab.  index is an integer, and updateTabs is True or False. Both tab
	and updateTabs are optional, defaulting to 0 and True respectively.

	At this point a.soc.send and a.soc.recv will synchronously write
	commands and read responses.  The api is semi-asynchronous with
	responses for commands, but also spontaeneous events will be
	send by the browser. For this kind of advance usage, select/pol
	on soc is advised.

	As a convenience, the shell connection object offers a method that, by
	injecting JavaScript into the first tab, commands Chrome to open a URL
	in a new tab::

	a.open_url('http://www.aldaily.com/')

	You can also optionally specify a different tab to operate on.
"""
import json
import socket
import time
import websocket
import requests

TRANSPORT_DEBUG = False


class ChromeSocketManager():
	"""A remote debugging connection to Google Chrome.

	   > a = Shell(host='localhost', port=92222)

	   a.tablist has a list of details on open tabs.

	   > a.connect(tab=index, update_tabs=True)

	   will connect a.soc to the webservice endpoint for tablist[index]'th
	   tab.  index is an integer, and update_tabs is True or False. Both tab
	   and updateTabs are optional, defaulting to 0 and True respectively.

	   At this point a.soc.send and a.soc.recv will synchronously write
	   commands and read responses.  The api is semi-asynchronous with
	   responses for commands, but also spontaeneous events will be
	   send by the browser. For this kind of advance usage, select/pol
	   on soc is advised.  """

	def __init__(self, host='localhost', port=9222):
		""" init """
		self.host = host
		self.port = port
		self.msg_id = 0
		self.soc = None
		self.tablist = None
		self.find_tabs()

		self.messages = []



	def connect(self, tab=None, update_tabs=True):
		"""Open a websocket connection to remote browser, determined by
		   self.host and self.port.  Each tab has it's own websocket
		   endpoint - you specify which with the tab parameter, defaulting
		   to 0.  The parameter update_tabs, if True, will force a rescan
		   of open tabs before connection. """
		if update_tabs or not self.tablist:
			self.find_tabs()
		if not tab:
			tab = 0
		wsurl = self.tablist[tab]['webSocketDebuggerUrl']
		if self.soc is not None and self.soc.connected:
			self.soc.close()
		self.soc = websocket.create_connection(wsurl)
		self.soc.settimeout(1)
		return self.soc

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


	def synchronous_command(self, command, params):
		"""Open a URL in the oldest tab."""

		send_id = self.send(command, params)
		resp = self.recv(message_id=send_id)

		if TRANSPORT_DEBUG:
			print("Response: ", resp)

		return resp

	def send(self, command, params):
		self.__check_open_socket()

		sent_id = self.msg_id

		command = {
				"id": self.msg_id,
				"method": command,
			}

		if params:
			command["params"] = params
		navcom = json.dumps(command)


		if TRANSPORT_DEBUG:
			print("Sending: ", navcom)

		self.soc.send(navcom)

		self.msg_id += 1
		return sent_id


	def recv_filtered(self, keycheck, timeout=30):

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


	def ___recv(self):
		try:
			tmp = self.soc.recv()
			decoded = json.loads(tmp)
			return decoded
		except (socket.timeout, websocket.WebSocketTimeoutException):
			return None

	def recv(self, message_id=None):
		'''
		Recieve a message, optionally filtering for a specified message id.
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
			if "id" in message:
				return message['id'] == message_id
			return False

		return self.recv_filtered(check_func)


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

