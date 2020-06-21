import unittest
import socket
import json
import base64
import zlib
import gzip
import ChromeController
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from . import testing_server


CHROME_BINARY_NAME = "google-chrome"

class TestChromium(unittest.TestCase):
	def setUp(self):
		self.cr = ChromeController.TabPooledChromium("google-chrome")
		self.mock_server_port, self.mock_server, self.mock_server_thread = testing_server.start_server(self, {})

	def tearDown(self):
		self.mock_server.shutdown()
		del self.cr

	def test_basic_fetch_1(self):

		# Configure mock server.
		tgturl = "http://localhost:{}".format(self.mock_server_port)
		with ChromeController.ChromeContext(CHROME_BINARY_NAME) as cr:
			cr.update_headers({})
			resp = cr.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

	def test_tab_repeatability_1(self):
		tgturl = "http://localhost:{}/".format(self.mock_server_port)
		with self.cr.tab(url=tgturl) as tab:
			resp = tab.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

		# print("Creating tab again!")
		with self.cr.tab(url=tgturl) as tab:
			at_url = tab.get_current_url()
			self.assertEqual(at_url, tgturl)


		# print("3rd tab context!")
		with self.cr.tab(url=tgturl) as tab:
			title, cur_url = tab.get_page_url_title()
			# print("title, cur_url", title, cur_url)
			self.assertEqual(cur_url, tgturl)


	def test_tab_flushing_1(self):
		tgturl = "http://localhost:{}/".format(self.mock_server_port)
		with self.cr.tab(url=tgturl) as tab:
			resp = tab.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

		for x in range(20):
			# print("Creating tab again!")
			with self.cr.tab(url=tgturl, extra_id=x) as tab:
				title, cur_url = tab.get_page_url_title()
				# print("title, cur_url", title, cur_url)

		# print("3rd tab context!")
		with self.cr.tab(url=tgturl) as tab:
			title, cur_url = tab.get_page_url_title()
			# print("title, cur_url", title, cur_url)
			self.assertNotEqual(cur_url, tgturl)

	def test_tab_flushing_2(self):
		tgturl = "http://localhost:{}/".format(self.mock_server_port)
		with self.cr.tab(url=tgturl) as tab:
			resp = tab.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

		for x in range(100):
			# print("Creating tab again!")
			with self.cr.tab(url=tgturl, extra_id=x) as tab:
				title, cur_url = tab.get_page_url_title()
				# print("title, cur_url", title, cur_url)

		# At this point, we should have fewer then 100 tabs, if nothing is broken.
		# print("3rd tab context!")
		with self.cr.tab(url=tgturl) as tab:
			targets = tab.Target_getTargets()
			assert 'result' in targets
			assert 'targetInfos' in targets['result']

			self.assertLess(len(targets['result']['targetInfos']), 20)

	def test_tab_size(self):
		tgturl = "http://localhost:{}/".format(self.mock_server_port)
		with self.cr.tab(url=tgturl) as tab:
			resp = tab.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

		for x in range(25):
			# print("Creating tab again!")
			with self.cr.tab(url=tgturl, extra_id=x) as tab:
				title, cur_url = tab.get_page_url_title()
				# print("title, cur_url", title, cur_url)

		tab_pool_tabs = self.cr.active_tabs()


		# At this point, we should have fewer then 100 tabs, if nothing is broken.
		# print("3rd tab context!")
		with self.cr.tab(url=tgturl) as tab:
			targets = tab.Target_getTargets()
			assert 'result' in targets
			assert 'targetInfos' in targets['result']

			# print("Active tabs:", len(targets['result']['targetInfos']))
			# print("Active tabs from manager:", tab_pool_tabs)
			self.assertLess(len(targets['result']['targetInfos']), 20)
			self.assertLess(tab_pool_tabs, 20)

	def test_tab_closing_1(self):
		tgturl = "http://localhost:{}/".format(self.mock_server_port)
		with self.cr.tab(url=tgturl) as tab:
			resp = tab.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

		for x in range(15):
			# print("Creating tab again!")
			with self.cr.tab(url=tgturl, extra_id=x) as tab:
				title, cur_url = tab.get_page_url_title()
				# print("title, cur_url", title, cur_url)



		# At this point, we should have fewer then 100 tabs, if nothing is broken.
		# print("3rd tab context!")
		with self.cr.tab(url=tgturl) as tab:
			targets = tab.Target_getTargets()
			assert 'result' in targets
			assert 'targetInfos' in targets['result']
			tab_pool_tabs_1 = self.cr.active_tabs()

			# print("Active tabs:", len(targets['result']['targetInfos']))
			# print("Active tabs from manager:", tab_pool_tabs_1)
			self.assertLess(len(targets['result']['targetInfos']), 15)
			self.assertLess(tab_pool_tabs_1, 15)

	def test_tab_closing_2(self):
		tgturl = "http://localhost:{}/".format(self.mock_server_port)
		with self.cr.tab(url=tgturl) as tab:
			resp = tab.blocking_navigate_and_get_source(tgturl)

		self.assertEqual(resp['content'], 'Root OK?')
		self.assertEqual(resp['binary'], False)
		self.assertEqual(resp['mimetype'], "text/html")

		for x in range(15):
			# print("Creating tab again!")
			with self.cr.tab(url=tgturl, extra_id=x) as tab:
				title, cur_url = tab.get_page_url_title()
				# print("title, cur_url", title, cur_url)

		self.cr.close_tabs()


		# At this point, we should have fewer then 100 tabs, if nothing is broken.
		# print("3rd tab context!")
		with self.cr.tab(url=tgturl) as tab:
			targets = tab.Target_getTargets()
			assert 'result' in targets
			assert 'targetInfos' in targets['result']
			tab_pool_tabs_1 = self.cr.active_tabs()

			# print("Active tabs:", len(targets['result']['targetInfos']))
			# print("Active tabs:", targets['result']['targetInfos'])
			# print("Active tabs from manager:", tab_pool_tabs_1)
			self.assertLess(len(targets['result']['targetInfos']), 5)
			self.assertLess(tab_pool_tabs_1, 2)
