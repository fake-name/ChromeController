
import logging
import contextlib
import traceback

from .manager import ChromeRemoteDebugInterface

@contextlib.contextmanager
def ChromeContext(*args, **kwargs):
	'''
	Context manager for conveniently handling the lifetime of the underlying chromium instance.

	In general, this should be the preferred way to use an instance of `ChromeRemoteDebugInterface`.

	All parameters are forwarded through to the underlying ChromeRemoteDebugInterface() constructor.
	'''
	log = logging.getLogger("Main.ChromeController.ChromeContext")
	try:
		chrome_instance = ChromeRemoteDebugInterface(*args, **kwargs)
		log.info("Entering chrome context")
		yield chrome_instance
	except Exception as e:

		log.error("Exception in chrome context!")
		for line in traceback.format_exc().split("\n"):
			log.error(line)
		raise e

	finally:
		log.info("Exiting chrome context")
		chrome_instance.close()



# class ChromeContext(object):
# 	'''
# 	Context manager for conveniently handling the lifetime of the underlying chromium instance.

# 	In general, this should be the preferred way to use an instance of `ChromeRemoteDebugInterface`.

# 	All parameters are forwarded through to the underlying ChromeRemoteDebugInterface() constructor.
# 	'''

# 	def __init__(self, *args, **kwargs):
# 		self.args = args
# 		self.kwargs = kwargs
# 		self.log = logging.getLogger("Main.ChromeController.ChromeContext")
# 		pass

# 	def __enter__(self):
# 		self.chrome_instance = ChromeRemoteDebugInterface(*self.args, **self.kwargs)
# 		self.log.info("Entering chrome context")
# 		return self.chrome_instance

# 	def __exit__(self, *args):
# 		self.log.info("Exiting chrome context")
# 		self.chrome_instance.close()
