

import os.path
import astor
import pprint

import WebRequest

import ChromeController.manager as mgr
import ChromeController


def gen():
	print("__file__", __file__)
	# print("Manager: ", mgr)
	cls_def = mgr.gen.update_generated_class()

	cls_def = mgr.gen.get_source()
	with open("class.py", "w") as fp:
		fp.write(cls_def)
	# print(cls_def)
	# pass
	# ChromeController.test()


if __name__ == '__main__':
	gen()
