

from .manager import ChromeRemoteDebugInterface

class ChromeContext(object):
	'''
	Context manager for conveniently handling the lifetime of the underlying chromium instance.

	In general, this should be the preferred way to use an instance of `ChromeRemoteDebugInterface`.

	All parameters are forwarded through to the underlying ChromeRemoteDebugInterface() constructor.
	'''

	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		pass

	def __enter__(self):
		self.chrome_instance = ChromeRemoteDebugInterface(*self.args, **self.kwargs)
		return self.chrome_instance

	def __exit__(self, *args):
		self.chrome_instance.close()