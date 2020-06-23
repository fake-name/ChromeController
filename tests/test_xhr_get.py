import unittest
import socket
import json
import base64
import zlib
import gzip
import pprint
import ChromeController
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from . import testing_server


CHROME_BINARY_NAME = "google-chrome"

class TestChromium(unittest.TestCase):
	def setUp(self):
		self.cr = ChromeController.TabPooledChromium("google-chrome")
		# self.mock_server_port, self.mock_server, self.mock_server_thread = testing_server.start_server(self, {})

	def tearDown(self):
		self.mock_server.shutdown()
		del self.cr

	def fetch_check_headers(self, expect_headers):
		try:
			# Configure mock server.
			self.mock_server_port, self.mock_server, self.mock_server_thread = testing_server.start_server(self, expect_headers)
			intermediate_url = "http://localhost:{}/ignore-headers".format(self.mock_server_port)
			target_url       = "http://localhost:{}/json/valid".format(self.mock_server_port)
			with ChromeController.ChromeContext(CHROME_BINARY_NAME) as cr:
				ret = cr.update_headers(expect_headers)
				# print("update_headers return:")
				# print(ret)
				# print("")
				first_nav = cr.blocking_navigate_and_get_source(intermediate_url)
				# print("First nav to '%s'" % intermediate_url)
				# print(first_nav)

				# print("Doing XHR to '%s'" % target_url)
				ret = cr.xhr_fetch(target_url)

				# pprint.pprint(ret)


			self.assertEqual(ret['response'], '{"oh" : "hai"}')
			self.assertEqual(ret['code'], 200)
			self.assertEqual(ret['mimetype'], "application/json")
		finally:
			self.mock_server.shutdown()


	def test_basic_fetch_1(self):

		self.fetch_check_headers({})


	def test_custom_ua_1(self):
		'''
		Dumb basic check
		'''
		expect_headers = {
			'User-Agent' : r"Test test testy test testttttttt"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_ua_2(self):
		'''
		Special chars to see if we can intentionally break something
		'''
		expect_headers = {
			'User-Agent' : r"Test !@#$%^&*(;;);_;+;\\///\\ \"':>?<|}{][;;][[p\\tblah"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_ua_3(self):
		'''
		What if it's empty?
		'''
		expect_headers = {
			'User-Agent' : r""
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_ua_4(self):
		'''
		Or ridiculously long
		'''
		expect_headers = {
			'User-Agent' : r"wat" * 5000
		}
		self.fetch_check_headers(expect_headers)


	def test_custom_ua_5(self):
		'''
		Or something that looks like a accept header
		'''
		expect_headers = {
			'User-Agent' : r"text/html, application/xhtml+xml, application/xml;q=0.9, */*, */*, */*, */*, */*, */*, */*, */*, */* "
		}
		self.fetch_check_headers(expect_headers)


	def test_custom_lang_1(self):
		'''
		Normal lang
		'''
		expect_headers = {
			'Accept-Language' : r"en-US,en;q=0.9"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_lang_2(self):
		'''
		Special chars
		'''
		expect_headers = {
			'Accept-Language' : r"Test !@#$%^&*(;;);_;+;\\///\\ \"':>?<|}{][;;][[p\\tb ''' \"\" \" lah"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_lang_3(self):
		'''
		What if it's empty?
		'''
		expect_headers = {
			'Accept-Language' : r""
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_lang_4(self):
		'''
		Or ridiculously long
		'''
		expect_headers = {
			'Accept-Language' : r"wat" * 5000
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_lang_5(self):
		'''
		Or something that looks like a accept header
		'''
		expect_headers = {
			'Accept-Language' : r"text/html, application/xhtml+xml, application/xml;q=0.9, */*, */*, */*, */*, */*, */*, */*, */*, */* "
		}
		self.fetch_check_headers(expect_headers)


	def test_custom_accept_1_1(self):
		'''
		Normal accept
		'''
		expect_headers = {
			'Accept-Encoding' : r"text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_1_2(self):
		expect_headers = {
			'Accept-Encoding' : r"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_1_3(self):
		expect_headers = {
			'Accept-Encoding' : r"text/html,application/xhtml+xml, application/xml;q=0.9, */*;q=0.8"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_2_1(self):
		'''
		Normal accept
		'''
		expect_headers = {
			'Accept' : r"text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.8"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_2_2(self):
		expect_headers = {
			'Accept' : r"text/html, application/xml;q=0.9,application/xhtml+xml,image/png,image/webp,image/jpeg, image/gif, image/x-xbitmap, */*;q=0.8"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_2_3(self):
		expect_headers = {
			'Accept' : r"text/html, application/xml;q=0.9,application/xhtml+xml, image/png,image/webp,image/jpeg, image/gif, image/x-xbitmap,   */*;q=0.8"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_3(self):
		'''
		Send garbage
		'''
		expect_headers = {
			'Accept' : r"Test !@#$%^&*(;;);_;+;\\///\\ \"':>?<|}{][;;][[p\\tb ''' \"\" \" lah"
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_4(self):
		'''
		What if it's empty?
		'''
		expect_headers = {
			'Accept' : r""
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_5(self):
		'''
		Or ridiculously long/repeated
		'''
		expect_headers = {
			'Accept' : r"text/html, " * 5
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_accept_6(self):
		'''
		I was sending this as a bug at one point
		'''
		expect_headers = {
			'Accept' : r"text/html, application/xhtml+xml, application/xml;q=0.9, */*, */*, */*, */*, */*, */*, */*, */*, */* "
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_1_1(self):
		'''
		Normal accept
		'''
		expect_headers = {
			'Accept-Encoding' : r'gzip'
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_1_2(self):
		expect_headers = {
			'Accept-Encoding' : r'gzip, deflate'
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_1_3(self):
		expect_headers = {
			'Accept-Encoding' : r'deflate, gzip'
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_1_4(self):
		expect_headers = {
			'Accept-Encoding' : r'gzip,    deflate'
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_1_5(self):
		expect_headers = {
			'Accept-Encoding' : r'gzip, deflate, sdch'
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_1_6(self):
		expect_headers = {
			'Accept-Encoding' : r'gzip,deflate, sdch'
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_1_7(self):
		expect_headers = {
			'Accept-Encoding' : r'sdch, gzip,deflate'
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_2(self):
		'''
		Send the wrong header
		'''
		expect_headers = {
			'Accept-Encoding' : r"text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.8"
		}
		self.fetch_check_headers(expect_headers)

	# def test_custom_encoding_3(self):
	# 	'''
	# 	Send garbage
	# 	'''
	# 	expect_headers = {
	# 		'Accept-Encoding' : r"Test !@#$%^&*(;;);_;+;\\///\\ \"':>?<|}{][;;][[p\\tb ''' \"\" \" lah"
	# 	}
	# 	self.fetch_check_headers(expect_headers)

	def test_custom_encoding_4(self):
		'''
		What if it's empty?
		'''
		expect_headers = {
			'Accept-Encoding' : r""
		}
		self.fetch_check_headers(expect_headers)

	def test_custom_encoding_5(self):
		'''
		Or ridiculously long/repeated
		'''
		expect_headers = {
			'Accept-Encoding' : r"gzip,deflate, sdch, " * 5
		}
		self.fetch_check_headers(expect_headers)

	@unittest.expectedFailure
	def test_setting_referrer_1(self):
		'''
		Referrers. See:
		https://bugs.chromium.org/p/chromium/issues/detail?id=795336
		https://bugs.chromium.org/p/chromium/issues/detail?id=767683 ?
		'''
		expect_headers = {
			'Referer' : r"http://www.googlez.com"
		}
		self.fetch_check_headers(expect_headers)

	@unittest.expectedFailure
	def test_setting_referrer_2(self):
		expect_headers = {
			'Referer' : r"htt;ljksdfhglkjshdg!@#$%^&*()_++_)(*&^%$#@!}{\":>?><|{|}{\\][\';//.,1209-82409587p://www.googlez.com"
		}
		self.fetch_check_headers(expect_headers)

	@unittest.expectedFailure
	def test_setting_referrer_3(self):
		expect_headers = {
			'Referer' : r"http://www.googlez.com"*2
		}
		self.fetch_check_headers(expect_headers)

	def test_setting_referrer_4(self):
		expect_headers = {
			'Referer' : r""
		}
		self.fetch_check_headers(expect_headers)

	# we can't set the host from a XHR, since it's a security issue.
	@unittest.expectedFailure
	def test_setting_host_1(self):
		expect_headers = {
			'Host' : r""
		}
		self.fetch_check_headers(expect_headers)

	@unittest.expectedFailure
	def test_setting_host_2(self):
		expect_headers = {
			'Host' : r"http://www.googlez.com"
		}
		self.fetch_check_headers(expect_headers)

	@unittest.expectedFailure
	def test_setting_host_3(self):
		expect_headers = {
			'Host' : r"www.googlez.com"
		}
		self.fetch_check_headers(expect_headers)

	@unittest.expectedFailure
	def test_setting_host_4(self):
		expect_headers = {
			'Host' : r"htt;ljksdfhglkjshdg!@#$%^&*()_++_)(*&^%$#@!}{\":>?><|{|}{\\][\';//.,1209-82409587p://www.googlez.com"
		}
		self.fetch_check_headers(expect_headers)

	@unittest.expectedFailure
	def test_setting_host_5(self):
		expect_headers = {
			'Host' : r"www.googlez.com"*50
		}
		self.fetch_check_headers(expect_headers)


	def test_setting_random_1(self):
		expect_headers = {
			'Pineapple' : r"Banana"
		}
		self.fetch_check_headers(expect_headers)

	def test_setting_random_2(self):
		expect_headers = {
			'Pineapple'*5 : r"Banana"*5
		}
		self.fetch_check_headers(expect_headers)

	def test_setting_random_3(self):
		expect_headers = {
			'Pineapple'*500 : r"Banana"*500
		}
		self.fetch_check_headers(expect_headers)

	def test_setting_random_4(self):
		expect_headers = {
			'Pineapple' : r"htt;ljksdfhglkjshdg!@#$%^&*()_++_)(*&^%$#@!}{\":>?><|{|}{\\][\';//.,1209-82409587p://www.googlez.com"
		}
		self.fetch_check_headers(expect_headers)


	# def test_setting_random_5(self):
	# 	expect_headers = {
	# 		'Pineapple;Pineapple' : r"htt;ljksdfhglkjshdg!@#$%^&*()_++_)(*&^%$#@!}{\":>?><|{|}{\\][\';//.,1209-82409587p://www.googlez.com"
	# 	}
	# 	self.fetch_check_headers(expect_headers)

	# def test_setting_random_6(self):
	# 	expect_headers = {
	# 		'Pineapple=Pineapple' : r"htt;ljksdfhglkjshdg!@#$%^&*()_++_)(*&^%$#@!}{\":>?><|{|}{\\][\';//.,1209-82409587p://www.googlez.com"
	# 	}
	# 	self.fetch_check_headers(expect_headers)

	# def test_setting_random_7(self):
	# 	expect_headers = {
	# 		'Pineapple=Pineapplehtt;ljksdfhglkjshdg!@#$%^&*()_++_)(*&^%$#@!}{\":>?><|{|}{\\][\';//.,1209-82409587p://www.googlez.com'
	# 			: r"htt;ljksdfhglkjshdg!@#$%^&*()_++_)(*&^%$#@!}{\":>?><|{|}{\\][\';//.,1209-82409587p://www.googlez.com"
	# 	}
	# 	self.fetch_check_headers(expect_headers)
