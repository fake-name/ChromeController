
import os.path
import subprocess
import signal
import time
import pprint
import logging
import traceback
import distutils.spawn
from . import cr_exceptions

from .transport import ChromeSocketManager



class ChromeInterface():
	"""

	"""

	def __init__(self, binary=None, dbg_port=None, *args, **kwargs):
		"""
		Base chromium transport initialization.

		The binary to execute is assumed to be named `chromium`, and on $PATH
		if not specified in the `binary` parameter.

		The chromium binary is launched with the arg `--remote-debugging-port={dbg_port}` if found.

		Note that the dbg_port must be GLOBALLY unique on a per-computer basis. If not specified, it
		defaults to 9222.

		Duplication of the dbg_port parameter can often lead to cr_exceptions.ChromeStartupException
		exceptions. If these happen, you may need to call ChromeInterface.close() to force shutdown
		of chromium instances, if you are not trying to instantiate multiple instances of chromium
		at once.

		"""
		self.log = logging.getLogger("Main.ChromeInterface")

		self.log.debug("Binary: %s", binary)
		self.log.debug("Args: %s", args)
		self.log.debug("Kwargs: %s", kwargs)

		if binary is None:
			binary = "chromium"
		if dbg_port is None:
			dbg_port = 9222
		if not os.path.exists(binary):
			fixed = distutils.spawn.find_executable(binary)
			if fixed:
				binary = fixed
		if not binary or not os.path.exists(binary):
			raise RuntimeError("Could not find binary '%s'" % binary)


		argv = [
				binary,
				'--headless',
				'--disable-gpu',
				'--remote-debugging-port={dbg_port}'.format(dbg_port=dbg_port)
			]

		self.cr_proc = subprocess.Popen(argv,
										stdin=open(os.path.devnull, "r"),
										stdout=subprocess.PIPE,
										stderr=subprocess.PIPE)

		self.log.debug("Spawned process: %s", self.cr_proc)


		self.transport = None
		# Allow the subprocess to start.
		for x in range(3):
			try:
				self.transport = ChromeSocketManager(port=dbg_port)
				break
			except cr_exceptions.ChromeConnectFailure:

				self.__check_process_ded()
				time.sleep(1)

		if not self.transport:
			raise cr_exceptions.ChromeStartupException("Could not start chromium! This can be caused by dangling chromium processes.")


	def __check_ret(self, ret):
		if 'error' in ret:
			err = pprint.pformat(ret)
			raise cr_exceptions.ChromeError("Error in response: \n{}".format(err))

	def __check_process_ded(self):
		self.cr_proc.poll()
		if self.cr_proc.returncode != None:
			stdout, stderr = self.cr_proc.communicate()
			raise cr_exceptions.ChromeError("Chromium process died unexpectedly! Don't know how to continue!\n	Chromium stdout: {}\n	Chromium stderr: {}".format(stdout.decode("utf-8"), stderr.decode("utf-8")))



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
		self.__check_process_ded()
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
		self.__check_process_ded()
		return self.transport.drain()

	def close(self):
		'''
		Close the remote chromium instance.

		This command is normally executed as part of the class destructor.
		It can be called early without issue, but calling ANY class functions
		after the remote chromium instance is shut down will have unknown effects.

		Note that if you are rapidly creating and destroying ChromeController instances,
		you may need to *explicitly* call this before destruction.
		'''


		self.log.debug("Sending sigint to chromium")
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

