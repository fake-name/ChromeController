

import os.path
import astor
import pprint
import logging

from ChromeController import manager as mgr
from ChromeController.Generator import gen
import ChromeController


def gen_new_class():
	print("__file__", __file__)
	print("Generator: ", gen)
	print("Updating generated class")
	_ = gen.update_generated_class(output_diff=True, protocolversion="1.3-DEV")
	print("Class Updated")


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	gen_new_class()

