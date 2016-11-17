

import os.path
import astor
import pprint

import WebRequest

import ChromeController.manager as mgr
import ChromeController

def test_func(a, b):
	"""
	Docstring!
	"""
	return a+b


def docstring_dbg():
	print(astor.dump_tree(astor.code_to_ast(test_func)))


def test():

	ua = dict(WebRequest.getUserAgent())
	print(ua)

	crbin = os.path.abspath("../AutoTriever/Headless/headless_shell")
	cr = ChromeController.CromeRemoteDebugInterface(binary=crbin)

	print(cr)
	resp = cr.set_viewport_size(1500, 1000)
	print("Viewport size", resp)

	resp = cr.set_user_agent_string(ua.pop('User-Agent'))
	print("Set user agent: ", resp)
	ua['X-Devtools-Emulate-Network-Conditions-Client-Id'] = None
	resp = cr.set_headers(ua)
	print("Set extra headers: ", resp)

	# resp = cr.blocking_navigate("http://www.google.com")
	resp = cr.blocking_navigate("http://10.1.1.8:33507/index")
	print("Page.navigate", resp)
	img = cr.take_screeshot()
	with open("screenshot.png", "wb") as fp:
		fp.write(img)
	# resp = cr.synchronous_command("Page.captureScreenshot", {})
	# print("Page.captureScreenshot", resp)

	wait_time = 5
	for x in range(wait_time):
		pprint.pprint(cr.drain_transport())
		print("Sleeping: ", wait_time-x)

	print("Draining!")
	pprint.pprint(cr.drain_transport())

def gen():
	print("Manager: ", mgr)
	cls_def = mgr.gen.get_source()
	print(cls_def)
	# pass
	# ChromeController.test()


if __name__ == '__main__':
	# test()
	gen()
	# docstring_dbg()
