import unittest
import socket
import json
import base64
import zlib
import gzip
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

import ChromeController
from . import testing_server

CHROME_BINARY_NAME = "google-chrome"
TIMEOUT_SECS       = 5

class TestPlainCreation(unittest.TestCase):
	def test_plain_instantiation_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			self.assertTrue(cr is not None)




class TestSimpleFetch(unittest.TestCase):
	def setUp(self):

		# Configure mock server.
		self.mock_server_port, self.mock_server, self.mock_server_thread = testing_server.start_server(self, {})

	def tearDown(self):
		self.mock_server.shutdown()
		self.mock_server_thread.join()

	def test_fetch_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			resp = cr.blocking_navigate_and_get_source("http://localhost:{}".format(self.mock_server_port), timeout=TIMEOUT_SECS)
			self.assertEqual(resp['content'], 'Root OK?')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	def test_fetch_decode_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			# text/html content should be decoded automatically.
			resp = cr.blocking_navigate_and_get_source("http://localhost:{}/html-decode".format(self.mock_server_port), timeout=TIMEOUT_SECS)
			self.assertEqual(resp['content'], 'Root OK?')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	def test_fetch_decode_json_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			resp = cr.blocking_navigate_and_get_source("http://localhost:{}/json/valid".format(self.mock_server_port), timeout=TIMEOUT_SECS)
			self.assertEqual(resp['content'], '{"oh" : "hai"}')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "application/json")

	def test_fetch_decode_json_2(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			resp = cr.blocking_navigate_and_get_source("http://localhost:{}/json/no-coding".format(self.mock_server_port), timeout=TIMEOUT_SECS)
			self.assertEqual(resp['content'], '{"oh" : "hai"}')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/plain")

	def test_fetch_decode_json_3(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			resp = cr.blocking_navigate_and_get_source("http://localhost:{}/json/invalid".format(self.mock_server_port), timeout=TIMEOUT_SECS)
			self.assertEqual(resp['content'], 'LOLWAT')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "application/json")

	def test_fetch_compressed_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			resp = cr.blocking_navigate_and_get_source("http://localhost:{}/compressed/gzip".format(self.mock_server_port), timeout=TIMEOUT_SECS)
			self.assertEqual(resp['content'], 'Root OK?')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	def test_fetch_compressed_2(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			resp = cr.blocking_navigate_and_get_source("http://localhost:{}/compressed/deflate".format(self.mock_server_port), timeout=TIMEOUT_SECS)
			self.assertEqual(resp['content'], 'Root OK?')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	########################################################################################################################
	########################################################################################################################
	########################################################################################################################

	def test_get_head_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			inurl_1 = "http://localhost:{}/".format(self.mock_server_port)

			cr.blocking_navigate(inurl_1)

			_, nurl_1 = cr.get_page_url_title()
			nurl2_1 = cr.get_current_url()

			self.assertEqual(nurl2_1, inurl_1)
			self.assertEqual(nurl_1,  inurl_1)

	# Binary shit is broken.
	# Siiigh.
	# def test_get_head_2(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		inurl_2 = "http://localhost:{}/filename_mime/content-disposition".format(self.mock_server_port)

	# 		cr.blocking_navigate(inurl_2)

	# 		nurl_2, _ = cr.get_page_url_title()
	# 		nurl2_2 = cr.get_current_url()

	# 		self.assertEqual(inurl_2, nurl_2)
	# 		self.assertEqual(inurl_2, nurl2_2)

	########################################################################################################################

	def test_redirect_handling_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:

			inurl_1 = "http://localhost:{}/redirect/from-1".format(self.mock_server_port)
			resp = cr.blocking_navigate_and_get_source(inurl_1, timeout=TIMEOUT_SECS)

			self.assertEqual(resp['content'], 'Redirect-To-1')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	# def test_redirect_handling_2(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		inurl_2 = "http://localhost:{}/redirect/from-2".format(self.mock_server_port)
	# 		resp = cr.blocking_navigate_and_get_source(inurl_2, timeout=TIMEOUT_SECS)

	# 		self.assertEqual(resp['content'], 'Redirect-To-2')
	# 		self.assertEqual(resp['binary'], False)
	# 		self.assertEqual(resp['mimetype'], "text/html")

	def test_redirect_handling_3(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			inurl_3 = "http://localhost:{}/redirect/from-3".format(self.mock_server_port)
			resp = cr.blocking_navigate_and_get_source(inurl_3, timeout=TIMEOUT_SECS)

			self.assertEqual(resp['content'], 'Redirect-To-3')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	def test_redirect_handling_4(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			inurl_3 = "http://localhost:{}/redirect/from-4".format(self.mock_server_port)
			resp = cr.blocking_navigate_and_get_source(inurl_3, timeout=TIMEOUT_SECS)

			self.assertEqual(resp['content'], 'Redirect-To-4')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	def test_redirect_handling_3(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			inurl_3 = "http://localhost:{}/redirect/from-1".format(self.mock_server_port)
			outurl_3 = "http://localhost:{}/redirect/to-1".format(self.mock_server_port)

			cr.blocking_navigate(inurl_3)
			_, nurl_3 = cr.get_page_url_title()
			nurl2_3 = cr.get_current_url()

			self.assertEqual(outurl_3, nurl_3)
			self.assertEqual(outurl_3, nurl2_3)

	# Broken
	# def test_redirect_handling_4(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		inurl_4 = "http://localhost:{}/redirect/from-2".format(self.mock_server_port)
	# 		outurl_4 = "http://localhost:{}/redirect/to-2".format(self.mock_server_port)

	# 		cr.blocking_navigate(inurl_4)
	# 		_, nurl_4 = cr.get_page_url_title()
	# 		nurl2_4 = cr.get_current_url()
	# 		self.assertEqual(outurl_4, nurl_4)
	# 		self.assertEqual(outurl_4, nurl2_4)

	# Broken too.
	# def test_redirect_handling_5(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		# This is a redirect without the actual redirect
	# 		with self.assertRaises(ValueError):
	# 			inurl_5 = "http://localhost:{}/redirect/bad-1".format(self.mock_server_port)
	# 			cr.blocking_navigate(inurl_5)

	def test_redirect_handling_6(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			# This is a infinitely recursive redirect.
			with self.assertRaises(ChromeController.ChromeResponseNotReceived):
				inurl_6 = "http://localhost:{}/redirect/bad-2".format(self.mock_server_port)
				cr.blocking_navigate(inurl_6)

	def test_redirect_handling_7(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			# This is a infinitely recursive redirect.
			with self.assertRaises(ChromeController.ChromeResponseNotReceived):
				inurl_6 = "http://localhost:{}/redirect/bad-3".format(self.mock_server_port)
				cr.blocking_navigate(inurl_6)

	def test_redirect_handling_8(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			inurl_7 = "http://localhost:{}/redirect/from-5".format(self.mock_server_port)
			# Assumes localhost seems to resolve to the listening address (here it's 0.0.0.0). Is this ever not true? IPv6?
			outurl_7 = "http://127.0.0.1:{}/".format(self.mock_server_port)

			cr.blocking_navigate(inurl_7)
			_, nurl_7 = cr.get_page_url_title()
			nurl2_7 = cr.get_current_url()
			self.assertEqual(outurl_7, nurl_7)
			self.assertEqual(outurl_7, nurl2_7)


	# def test_get_item_1(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		inurl_1 = "http://localhost:{}".format(self.mock_server_port)
	# 		content_1, fileN_1, mType_1 = self.wg.getItem(inurl_1)
	# 		self.assertEqual(content_1, 'Root OK?')
	# 		self.assertEqual(fileN_1, '')
	# 		self.assertEqual(mType_1, "text/html")


	# def test_get_item_2(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		inurl_2 = "http://localhost:{}/filename_mime/content-disposition".format(self.mock_server_port)
	# 		content_2, fileN_2, mType_2 = self.wg.getItem(inurl_2)

	# 		# Lack of an explicit mimetype makes this not get decoded
	# 		self.assertEqual(content_2, b'LOLWAT?')
	# 		self.assertEqual(fileN_2, 'lolercoaster.txt')
	# 		self.assertEqual(mType_2, None)


	# def test_get_item_3(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		inurl_3 = "http://localhost:{}/filename/path-only.txt".format(self.mock_server_port)
	# 		content_3, fileN_3, mType_3 = self.wg.getItem(inurl_3)

	# 		self.assertEqual(content_3, b'LOLWAT?')
	# 		self.assertEqual(fileN_3, 'path-only.txt')
	# 		self.assertEqual(mType_3, None)

	# def test_get_cookies_1(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		inurl_1 = "http://localhost:{}/cookie_test".format(self.mock_server_port)
	# 		inurl_2 = "http://localhost:{}/cookie_require".format(self.mock_server_port)

	# 		self.wg.clearCookies()
	# 		cookies = self.wg.getCookies()
	# 		self.assertEqual(list(cookies), [])

	# 		page_resp_nocook = cr.blocking_navigate_and_get_source(inurl_2, timeout=TIMEOUT_SECS)
	# 		self.assertEqual(page_resp_nocook, '<html><body>Cookie is missing</body></html>')


	# 		_ = cr.blocking_navigate_and_get_source(inurl_1, timeout=TIMEOUT_SECS)
	# 		cookies = self.wg.getCookies()
	# 		print(cookies)

	# 		page_resp_cook = cr.blocking_navigate_and_get_source(inurl_2, timeout=TIMEOUT_SECS)
	# 		self.assertEqual(page_resp_cook, '<html><body>Cookie forwarded properly!</body></html>')




	########################################################################################################################
	########################################################################################################################
	########################################################################################################################

	# # So binary downloads are broken ATM
	# # see https://bugs.chromium.org/p/chromium/issues/detail?id=831887.
	# # Siiiiigh.

	# def test_file_and_name_1(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename/path-only.txt".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		# self.assertEqual(fn, 'path-only.txt')


	# def test_file_and_name_2(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename/content-disposition".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'lolercoaster.txt')


	# def test_file_and_name_3(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename_mime/content-disposition-quotes-1".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'lolercoaster.html')


	# def test_file_and_name_4(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename_mime/content-disposition-quotes-2".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'lolercoaster.html')


	# def test_file_and_name_5(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename_mime/content-disposition-quotes-spaces-1".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'loler coaster.html')


	# def test_file_and_name_6(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename_mime/content-disposition-quotes-spaces-2".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'loler coaster.html')


	# def test_file_and_name_7(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source(requestedUrl="http://localhost:{}/filename_mime/content-disposition-quotes-spaces-2".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'loler coaster.html')

	# def test_file_and_name_8(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source(requestedUrl="http://localhost:{}/filename_mime/content-disposition-quotes-spaces-2".format(self.mock_server_port), addlHeaders={"Referer" : 'http://www.example.org'}, timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'loler coaster.html')

	# def test_file_and_name_9(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename_mime/content-disposition-quotes-spaces-2".format(self.mock_server_port), addlHeaders={"Referer" : 'http://www.example.org'}, timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, 'loler coaster.html')

	# def test_file_and_name_10(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source("http://localhost:{}/filename/path-only-trailing-slash/".format(self.mock_server_port), timeout=TIMEOUT_SECS)
	# 		self.assertEqual(resp['content'], b"LOLWAT?\x00\xff\xaa\x55!")
	# 		self.assertEqual(resp['binary'], True)
	# 		# self.assertEqual(fn, '')


	# def test_file_name_mime_1(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source(
	# 						"http://localhost:{}/filename_mime/path-only.txt".format(self.mock_server_port))
	# 		self.assertEqual(resp['content'], 'LOLWAT?')
	# 		self.assertEqual(resp['binary'], False)
	# 		# self.assertEqual(fn, 'path-only.txt')
	# 		self.assertEqual(resp['mimetype'], 'text/plain')

	# def test_file_name_mime_2(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source(
	# 						"http://localhost:{}/filename_mime/content-disposition".format(self.mock_server_port))
	# 		self.assertEqual(resp['content'], 'LOLWAT?')
	# 		self.assertEqual(resp['binary'], False)
	# 		# self.assertEqual(fn, 'lolercoaster.txt')
	# 		self.assertEqual(resp['mimetype'], 'text/plain')

	# def test_file_name_mime_3(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source(
	# 						"http://localhost:{}/filename_mime/content-disposition-html-suffix".format(self.mock_server_port))
	# 		self.assertEqual(resp['content'], 'LOLWAT?')
	# 		self.assertEqual(resp['binary'], False)
	# 		# self.assertEqual(fn, 'lolercoaster.html')
	# 		self.assertEqual(resp['mimetype'], 'text/plain')

	# def test_file_name_mime_5(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source(
	# 						"http://localhost:{}/filename/path-only-trailing-slash/".format(self.mock_server_port))
	# 		self.assertEqual(resp['content'], 'LOLWAT?')
	# 		self.assertEqual(resp['binary'], False)
	# 		# self.assertEqual(fn, '')
	# 		self.assertEqual(resp['mimetype'], 'text/plain')

	# def test_file_name_mime_4(self):
	# 	with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
	# 		resp = cr.blocking_navigate_and_get_source(
	# 						"http://localhost:{}/filename_mime/explicit-html-mime".format(self.mock_server_port))
	# 		self.assertEqual(resp['content'], 'LOLWAT?')
	# 		self.assertEqual(resp['binary'], False)
	# 		# self.assertEqual(fn, 'lolercoaster.html')
	# 		self.assertEqual(resp['mimetype'], 'text/html')
