

import os.path
import time
import pprint
import ChromeController.manager as mgr
import ChromeController

def test():
	crbin = os.path.abspath("../AutoTriever/Headless/headless_shell")
	cr = ChromeController.CromeRemoteDebugInterface(binary=crbin)

	print(cr)
	resp = cr.set_viewport_size(1500, 1000)
	print("Viewport size", resp)
	resp = cr.blocking_navigate("http://www.google.com")
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
	mgr.build()
	crbin = os.path.abspath("../AutoTriever/Headless/headless_shell")
	cr = ChromeController.CromeRemoteDebugInterface(binary=crbin)
	# pass
	# ChromeController.test()


if __name__ == '__main__':
	test()
	# gen()
