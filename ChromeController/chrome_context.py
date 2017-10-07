

from .manager import ChromeRemoteDebugInterface

class ChromeContext(object):


	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		pass

	def __enter__(self):
		self.chrome_instance = ChromeRemoteDebugInterface(*self.args, **self.kwargs)
		return self.chrome_instance

	def __exit__(self, *args):
		print("Context manager exit!")
		self.chrome_instance.close()