import unittest
import socket
import json
import base64
import zlib
import gzip
import urllib.parse
import pprint
import ChromeController
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from . import testing_server


CHROME_BINARY_NAME = "google-chrome"

class TestChromiumPost(unittest.TestCase):
	def setUp(self):
		self.cr = ChromeController.TabPooledChromium("google-chrome")
		self.mock_server_port, self.mock_server, self.mock_server_thread = testing_server.start_server(self, {})

	def tearDown(self):
		self.mock_server.shutdown()
		del self.cr

	def test_xhr_post_1(self):

		intermediate_url = "http://localhost:{}/ignore-headers".format(self.mock_server_port)
		target_url       = "http://localhost:{}/post/json_resp".format(self.mock_server_port)
		with ChromeController.ChromeContext(CHROME_BINARY_NAME) as cr:
			# print(ret)
			# print("")
			first_nav = cr.blocking_navigate_and_get_source(intermediate_url)
			# print("First nav to '%s'" % intermediate_url)
			# print(first_nav)

			# print("Doing XHR to '%s'" % target_url)
			ret = cr.xhr_fetch(target_url, post_data="test_post_1", post_type='application/json')

			pprint.pprint(ret)


		self.assertEqual(ret['response'], '{"oh" : "hai"}')
		self.assertEqual(ret['code'], 200)
		self.assertEqual(ret['mimetype'], "application/json")


	def test_xhr_post_2(self):

		intermediate_url = "http://localhost:{}/ignore-headers".format(self.mock_server_port)
		target_url       = "http://localhost:{}/post/form_urlencoded".format(self.mock_server_port)
		with ChromeController.ChromeContext(CHROME_BINARY_NAME) as cr:
			# print(ret)
			# print("")
			first_nav = cr.blocking_navigate_and_get_source(intermediate_url)
			# print("First nav to '%s'" % intermediate_url)
			# print(first_nav)

			# print("Doing XHR to '%s'" % target_url)
			data = urllib.parse.urlencode({'test' : 1, "moar": "two"})
			ret = cr.xhr_fetch(target_url, post_data=data, post_type='application/x-www-form-urlencoded')

			pprint.pprint(ret)


		self.assertEqual(ret['response'], '{"oh" : "hai"}')
		self.assertEqual(ret['code'], 200)
		self.assertEqual(ret['mimetype'], "application/json")

