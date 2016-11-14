

import os.path
import time
import ChromeController.manager as mgr
import ChromeController

def test():
	crbin = os.path.abspath("../AutoTriever/Headless/headless_shell")
	cr = ChromeController.CromeRemoteDebugInterface(binary=crbin)
	print(cr)
	resp = cr.blocking_navigate("http://www.google.com")
	print("Page.navigate", resp)
	resp = cr.synchronous_command("Page.captureScreenshot", {})
	print("Page.captureScreenshot", resp)

	wait_time = 5
	for x in range(wait_time):
		time.sleep(1)
		print("Sleeping: ", wait_time-x)

	print("Draining!")
	print(cr.drain_transport())

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
