
import distutils.spawn
import os.path
import subprocess
import signal
import time
import requests.exceptions

from .transport import ChromeSocketManager

class ChromeInterface():
	"""

	"""

	def __init__(self, binary=None):
		""" init """

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

		print(self.transport.find_tabs())

	def close(self):
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

