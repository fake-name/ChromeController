

import os.path
import pprint

import WebRequest

import ChromeController.manager as mgr
import ChromeController



def test():

	# ua = dict(WebRequest.getUserAgent())
	# print(ua)

	# crbin = os.path.abspath("../Chromium/src/out/Headless/headless_shell")
	cr = ChromeController.ChromeRemoteDebugInterface()

	# print(cr)
	resp = cr.Emulation_setVisibleSize(1500, 1000)
	# print("Viewport size", resp)

	# resp = cr.update_headers(ua)
	# print("Set extra headers: ", resp)

	resp = cr.blocking_navigate("http://www.whatarecookies.com/cookietest.asp", timeout=10)
	cooks1 = cr.get_cookies()
	resp = cr.blocking_navigate("http://google.com", timeout=10)


	cooks2 = cr.get_cookies()
	print()
	print("Cookies after first 'Page.navigate' command:")
	for cookie in cooks1:
		print('	', cookie)

	print()
	print("Cookies after second 'Page.navigate' command:")
	for cookie in cooks2:
		print('	', cookie)

	# for cook in cooks1:
	# 	ret = cr.set_cookie(cook)
	# 	print(ret)

	# print()
	# print("Reinstated cookies:")
	# cooks3 = cr.get_cookies()
	# for cookie in cooks3:
	# 	print(cookie)

	wait_time = 5
	for x in range(wait_time):
		data = cr.drain_transport()
		# pprint.pprint(data)
		print("Sleeping: ", wait_time-x)

	# print("Draining!")
	# pprint.pprint(cr.drain_transport())

def gen():
	# print("Manager: ", mgr)
	cls_def = mgr.gen.get_source()
	with open("class.py", "w") as fp:
		fp.write(cls_def)
	# print(cls_def)
	# pass
	# ChromeController.test()


if __name__ == '__main__':
	test()
	# gen()
	# docstring_dbg()
