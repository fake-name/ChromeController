import unittest
import concurrent.futures
import json
import base64
import zlib
import gzip
import bs4
import ChromeController
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from . import testing_server


CHROME_BINARY_NAME = "google-chrome"
PARALLEL_TESTERS   = 10

class TestParallelChromium(unittest.TestCase):
	def setUp(self):
		self.cr = ChromeController.TabPooledChromium("google-chrome")
		self.mock_server_port, self.mock_server, self.mock_server_thread = testing_server.start_server(self, {})

	def tearDown(self):
		del self.cr
		self.mock_server.shutdown()

	def test_basic(self):
		# Configure mock server.
		tgturl = "http://localhost:{}".format(self.mock_server_port)
		with ChromeController.ChromeContext(CHROME_BINARY_NAME) as cr:
			resp = cr.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

	def parallel_get_tabs(self):
		for _ in range(200):
			with self.cr.tab() as tab:
				tab.get_cookies()

	def parallel_tab_fetch(self):
		tgturl = "http://localhost:{}/counter".format(self.mock_server_port)
		print("Parallel tab fetch?")
		for x in range(50):
			with self.cr.tab() as tab:
				resp = tab.blocking_navigate_and_get_source(tgturl + "?x=" + str(x))
				print(resp)
				self.assertTrue(resp['content'].startswith('Counter: '))
				self.assertEqual(resp['binary'], False)
				self.assertEqual(resp['mimetype'], "text/html")

	def parallel_tab_fetch_huge(self):
		tgturl = "http://localhost:{}/counter_big".format(self.mock_server_port)
		print("Parallel tab fetch?")
		for x in range(10):
			with self.cr.tab() as tab:
				resp = tab.blocking_navigate_and_get_source(tgturl + "?x=" + str(x))
				print(resp)
				self.assertTrue(resp['content'].startswith('Counter: '))
				self.assertEqual(resp['content'].count("Counter"), 50000)
				self.assertEqual(resp['binary'], False)
				self.assertEqual(resp['mimetype'], "text/html")

	def test_basic_multitab(self):
		with concurrent.futures.ThreadPoolExecutor(max_workers=PARALLEL_TESTERS) as tp:

			res = [tp.submit(self.parallel_get_tabs) for _ in range(PARALLEL_TESTERS)]
			for result in res:
				result.result()

	def test_multitab_fetch_1(self):
		with concurrent.futures.ThreadPoolExecutor(max_workers=PARALLEL_TESTERS) as tp:

			res = [tp.submit(self.parallel_tab_fetch) for _ in range(PARALLEL_TESTERS)]
			for result in res:
				result.result()


	def test_multitab_fetch_2(self):
		with concurrent.futures.ThreadPoolExecutor(max_workers=PARALLEL_TESTERS) as tp:

			res = [tp.submit(self.parallel_tab_fetch_huge) for _ in range(PARALLEL_TESTERS)]
			for result in res:
				result.result()

