
import distutils.spawn
import os.path
import subprocess
import signal
import time
import requests.exceptions

from .Generator import gen

CromeRemoteDebugInterface = gen.get_class_def()

def build():

	# print(gen.get_printed_ast())

	with open("test_class.py", "w") as fp:
		code = gen.get_source()
		fp.write(code)
		# print(code)

	# print(module)
	# print(dir(module))
	# print(module.CromeRemoteDebugInterface)
