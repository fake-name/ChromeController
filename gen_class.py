

import os.path
import astor
import pprint
import logging

import WebRequest

import ChromeController.manager as mgr
import ChromeController


def gen():
	print("__file__", __file__)
	# print("Manager: ", mgr)
	print("Updating generated class")
	cls_def = mgr.gen.update_generated_class(force=True)
	print("Class Updated")


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	gen()
