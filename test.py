
import logging
import os.path
import gc
import pprint
import time

import astor
import WebRequest

import ChromeController.manager as mgr
import ChromeController


def test_delete_cookies():

	crbin = "google-chrome"
	cr = ChromeController.ChromeRemoteDebugInterface(binary=crbin, dbg_port=9232)

	canClear = cr.Network_canClearBrowserCookies()
	print("Can clear cookies: ", canClear)
	assert canClear['result']['result'] == True


	# print(cr)
	resp = cr.Emulation_setVisibleSize(1500, 1000)
	# print("Viewport size", resp)

	print("Navigating to whatarecookies.com")

	try:
		resp = cr.blocking_navigate_and_get_source("http://www.whatarecookies.com/cookietest.asp", timeout=10)
	except Exception as e:
		raise e

	print("Sampling cookies #1")
	cooks1 = cr.Network_getAllCookies()['result']['cookies']
	print("Doing cookie clear")
	res = cr.Network_clearBrowserCookies()
	print("Cookie clear result: ", res)

	print("Sampling cookies #2")
	cooks2 = cr.Network_getAllCookies()['result']['cookies']
	print("Navigating to goat.com")

	try:
		resp = cr.blocking_navigate_and_get_source("http://goat.com", timeout=10)
	except Exception as e:
		raise e
	print("Doing cookie clear")
	res = cr.Network_clearBrowserCookies()
	print("Cookie clear result: ", res)
	print("sleeping 15")
	time.sleep(15)
	print("Sampling cookies #3")
	cooks3 = cr.Network_getAllCookies()['result']['cookies']
	print("Doing cookie clear")
	res = cr.Network_clearBrowserCookies()
	print("Cookie clear result: ", res)
	print("sleeping 15")
	time.sleep(15)
	print("Sampling cookies #4")
	cooks4 = cr.Network_getAllCookies()['result']['cookies']


	print("Doing cookie clear")
	res = cr.clear_cookies()
	print("Cookie clear result: ", res)
	print("sleeping 15")
	time.sleep(15)
	print("Sampling cookies #4")
	cooks5 = cr.Network_getAllCookies()['result']['cookies']


	print()
	print("Uncleared Cookies (#1):")
	for cookie1 in cooks1:
		print("	", cookie1)

	print()
	print("Cleared cookies (#2):")
	for cookie2 in cooks2:
		print("	", cookie2)

	print()
	print("Navigated and cleared cookies after delay (#3):")
	for cookie3 in cooks3:
		print("	", cookie3)
	print()
	print("Navigated and cleared cookies after another delay (#4):")
	for cookie4 in cooks3:
		print("	", cookie4)


def test():
	print("Starting!")

	ua = dict(WebRequest.getUserAgent())
	# print(ua)

	crbin = os.path.abspath("./vendored/headless_shell")
	cr = ChromeController.ChromeRemoteDebugInterface(binary=crbin, dbg_port=9232)

	cooks1 = cr.get_cookies()

	resp = cr.update_headers(ua)
	print("Set user agent: ", resp)
	# print("Set extra headers: ", resp)


	# print(cr)
	resp = cr.Emulation_setVisibleSize(1500, 1000)
	# print("Viewport size", resp)
	print("Doing first navigation...")

	try:
		resp = cr.blocking_navigate_and_get_source("http://www.whatarecookies.com/cookietest.asp", timeout=10)

	except Exception as e:
		have = cr.drain_transport()
		for msg in have:
			pprint.pprint(msg)
		raise e


	# resp = cr.blocking_navigate_and_get_source("http://10.1.1.8:33507/index")
	# resp = cr.blocking_navigate_and_get_source("http://10.1.1.8:33507/index")

	cr.click_link_containing_url("/test")
	# print("Page.navigate", resp['content'])
	img = cr.take_screeshot()
	with open("screenshot.png", "wb") as fp:
		fp.write(img)
	# resp = cr.synchronous_command("Page.captureScreenshot", {})
	# print("Page.captureScreenshot", resp)


	ctnt = cr.get_rendered_page_source()
	# print("Source:")
	# print(ctnt)

	cooks1 = cr.get_cookies()

	print("Doing second navigation...")
	resp = cr.blocking_navigate_and_get_source("http://goat.com", timeout=10)
	# cr.Network_clearBrowserCookies()
	print("Getting cookies!")

	cooks2 = cr.get_cookies()
	cooks3 = cr.get_cookies(all_cookies=False)

	cr.Network_clearBrowserCookies()

	cooks4 = cr.get_cookies()
	print()
	print("Pre-clearing cookies:")
	for cookie in cooks1:
		print(cookie)
		print(cookie._rest)

	print()
	print("Global Cookies:")
	for cookie in cooks2:
		print(cookie)
		print(cookie._rest)

	print()
	print("Local only cookies:")
	for cookie in cooks3:
		print(cookie)
		print(cookie._rest)

	print()
	print("Cleared cookies:")
	for cookie in cooks4:
		print(cookie)
		print(cookie._rest)

	# for cook in cooks1:
	# 	ret = cr.set_cookie(cook)
	# 	print(ret)

	# print()
	# print("Reinstated cookies:")
	# cooks3 = cr.get_cookies()
	# for cookie in cooks3:
	# 	print(cookie)
	# 	print(cookie._rest)

	wait_time = 5
	for x in range(wait_time):
		data = cr.drain_transport()
		# pprint.pprint(data)
		print("Sleeping: ", wait_time - x)

	# print("Draining!")
	# pprint.pprint(cr.drain_transport())

def test_cycle():
	crbin = "google-chrome"
	for x in range(30):
		print("Starting loop %s" % x)
		with ChromeController.ChromeContext(crbin) as cr:
			print("Looping:", x)
			print(cr)
			cr.blocking_navigate('http://www.google.com')
			print("Deleted")
			print("Ending loop %s" % x)

def test_tabs():
	crbin = "google-chrome"
	for x in range(30):

		with ChromeController.ChromeContext(binary="google-chrome") as cr:
			print("Context manager entered")
			tabl = [cr.new_tab(), cr.new_tab(), cr]

			print("Tabs:", tabl)
			print("Transport:")
			print(tabl[0].transport)
			# cr.blocking_navigate("http://www.google.com", timeout=10)
			print("Loop")
			for idx, tab in enumerate(tabl):
				print("Fetching using tab %s -> %s" % (idx, tab))
				tab.blocking_navigate("http://www.google.com", timeout=10)
			print("Complete")

def test_url():

	crbin = "google-chrome"
	with ChromeController.ChromeContext(crbin) as cr:
		cr.blocking_navigate("http://www.google.com", timeout=10)
		print("Current URL:", cr.get_current_url())
		# cr.close()

def test_title():

	crbin = "google-chrome"
	with ChromeController.ChromeContext(crbin) as cr:
		cr.blocking_navigate("http://www.google.com", timeout=10)
		print("Current URL:", cr.get_current_url())
		print(cr.get_page_url_title())
		# cr.close()

def test_rendered_fetch():

	crbin = "google-chrome"
	cr = ChromeController.ChromeRemoteDebugInterface(binary=crbin)

	resp = cr.blocking_navigate("https://www.catatopatch.com/appraise-chapter-15", timeout=10)
	print("Current URL:", cr.get_current_url())
	rcnt = cr.get_rendered_page_source()
	print("content:", type(rcnt))
	# cr.close()

if __name__ == '__main__':
	import logSetup
	logSetup.initLogging(logging.DEBUG)
	# test()
	test_title()
	test_tabs()
	test_cycle()
	test_rendered_fetch()

	test_url()
	# test_delete_cookies()
	# docstring_dbg()
