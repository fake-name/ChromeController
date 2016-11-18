
import distutils.spawn
import os.path
import subprocess
import signal
import time
import pprint
import requests.exceptions

from .transport import ChromeSocketManager


class ChromeError(RuntimeError):
	pass

class ChromeInterface():
	"""

	"""

	def __init__(self, binary=None):
		"""
		Base chromium transport initialization.

		The binary to execute is assumed to be named `chromium`, and on $PATH
		if not specified in the `binary` parameter.

		The chromium binary is launched with the arg `--remote-debugging-port=9222` if found.

		"""

		if binary is None:
			binary = "chromium"
		if not os.path.exists(binary):
			fixed = distutils.spawn.find_executable(binary)
			if fixed:
				binary = fixed
		if not binary or not os.path.exists(binary):
			raise RuntimeError("Could not find binary '%s'" % binary)


		argv = [binary, '--remote-debugging-port=9222']
		self.cr_proc = subprocess.Popen(argv,
										stdin=open(os.path.devnull, "r"),
										stdout=subprocess.PIPE,
										stderr=subprocess.PIPE)

		print("Spawned process:", self.cr_proc)



		# Allow the subprocess to start.
		for x in range(3):
			try:
				self.transport = ChromeSocketManager()
				print(self.transport)
				break
			except requests.exceptions.ConnectionError:
				time.sleep(1)


	def __check_ret(self, ret):
		if 'error' in ret:
			err = pprint.pformat(ret)
			raise ChromeError("Error in response: \n{}".format(err))

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
		ret = self.transport.synchronous_command(*args, **kwargs)
		self.__check_ret(ret)
		return ret

	def drain_transport(self):
		'''
		"Drain" the transport connection.

		This command simply returns all waiting messages sent from the remote chrome
		instance. This can be useful when waiting for a specific asynchronous message
		from chrome, but higher level calls are better suited for managing wait-for-message
		type needs.

		'''
		return self.transport.drain()

	def close(self):
		'''
		Close the remote chromium instance.

		This command is normally executed as part of the class destructor.
		It can be called early without issue, but calling ANY class functions
		after the remote chromium instance is shut down will have unknown effects.
		'''


		print("Sending sigint to chromium")
		self.cr_proc.send_signal(signal.SIGINT)
		self.cr_proc.terminate()

	def __del__(self):
		try:
			self.close()
		except:
			pass

if __name__ == '__main__':
	import doctest
	doctest.testmod()

