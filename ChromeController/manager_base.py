
import time
import pprint
import uuid
import logging

from . import cr_exceptions
from .transport import ChromeExecutionManager



class ChromeInterface():
	"""
	Document me, maybe?
	"""

	def __init__(self, binary=None, dbg_port=None, use_execution_manager=None, *args, **kwargs):
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
		self.log = logging.getLogger("Main.ChromeController.Interface")
		if use_execution_manager:
			self.transport, self.tab_id = use_execution_manager
		else:
			self.log.debug("Binary: %s", binary)
			self.log.debug("Args: %s", args)
			self.log.debug("Kwargs: %s", kwargs)

			self.tab_id = uuid.uuid4()

			self.transport = None
			# Allow the subprocess to start.
			for x in range(3):
				try:
					self.transport = ChromeExecutionManager(binary=binary, port=dbg_port, base_tab_key=self.tab_id)
					self.transport.check_process_ded()

				except cr_exceptions.ChromeConnectFailure:

					time.sleep(1)

			if not self.transport:
				raise cr_exceptions.ChromeStartupException("Could not start chromium! This can be caused by dangling chromium processes.")


	def __check_ret(self, ret):
		if ret is False or ret is None:
			raise cr_exceptions.ChromeError("Null response from Chromium (or timed out)!")

		if 'error' in ret:
			err = pprint.pformat(ret)
			raise cr_exceptions.ChromeError("Error in response: \n{}".format(err))



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
		self.transport.check_process_ded()
		return self.transport.drain()

	def new_tab(self):
		new = self.__class__(use_execution_manager=(self.transport, uuid.uuid4()))
		return new




if __name__ == '__main__':
	import doctest
	doctest.testmod()

