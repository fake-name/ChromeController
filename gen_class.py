

import os.path
import astor
import pprint

import WebRequest

import ChromeController.manager as mgr
import ChromeController


def gen():
	# print("Manager: ", mgr)
	cls_def = mgr.gen.get_source()
	with open("class.py", "w") as fp:
		fp.write(cls_def)
	# print(cls_def)
	# pass
	# ChromeController.test()


if __name__ == '__main__':
	gen()
