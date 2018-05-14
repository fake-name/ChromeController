
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


	def __init__(self, binary, dbg_port, use_execution_manager, *args, **kwargs):
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
					binary       = binary,
					port         = dbg_port,
					base_tab_key = self.tab_id,
					*args,
					**kwargs
				)
			self.transport.check_process_ded()


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

	def new_tab(self, *args, **kwargs):
		new = self.__class__(use_execution_manager=(self.transport, uuid.uuid4()), *args, **kwargs)
		self.transport.check_process_ded()
		return new

	def close(self):
		self.transport.check_process_ded()
		if self.is_root_session:
			self.transport.close_all()
		else:
			self.transport.close_tab(tab_key=self.tab_id)

		gc.collect()



if __name__ == '__main__':
	import doctest
	doctest.testmod()

