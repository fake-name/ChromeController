
import distutils.spawn
import os.path
import subprocess
import signal
import time
import requests.exceptions

from .Generator import gen

CromeRemoteDebugInterfaceBase = gen.get_class_def()

class CromeRemoteDebugInterface(CromeRemoteDebugInterfaceBase):
	pass
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		resp1 = self.synchronous_command("Page.enable", {})
		resp2 = self.synchronous_command("DOM.enable", {})
		resp3 = self.synchronous_command("Network.enable", {})

		print(resp1)
		print(resp2)
		print(resp3)

		pass
	def blocking_navigate(self, url, timeout=30):
		ret = self.synchronous_command("Page.navigate", {"url": "http://www.google.com"})
		assert("params" in ret), "Missing return content"
		assert("frameId" in ret['params']), "Missing 'frameId' in return content"

		pass
