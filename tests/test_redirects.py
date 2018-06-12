import unittest
import time

from threading import Thread

import ChromeController
from . import testing_server

CHROME_BINARY_NAME = "google-chrome"
WRAPPER_STEP_THROUGH_TIMEOUT = 20
TIMEOUT_SECS       = 5


class TestRedirects(unittest.TestCase):
	def setUp(self):

		# Configure mock server.
		self.mock_server_port, self.mock_server, self.mock_server_thread = testing_server.start_server(self, {})

	def tearDown(self):
		self.mock_server.shutdown()
		self.mock_server_thread.join()


	def test_plain_instantiation_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			self.assertTrue(cr is not None)


	def test_multi_redirect_handling_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			inurl_3 = "http://localhost:{}/redirect_mult/from-1".format(self.mock_server_port)
			outurl_3 = "http://localhost:{}/redirect_mult/to-5".format(self.mock_server_port)

			resp = cr.blocking_navigate_and_get_source(inurl_3)
			_, nurl_3 = cr.get_page_url_title()
			nurl2_3 = cr.get_current_url()

			self.assertEqual(outurl_3, nurl_3)
			self.assertEqual(outurl_3, nurl2_3)

			self.assertEqual(resp['content'], 'Multi-Redirect-end-5')
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	def test_slow_redirect_1(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			inurl_3 = "http://localhost:{}/redirect_slow/from-1".format(self.mock_server_port)
			outurl_3 = "http://localhost:{}/redirect_slow/to-1".format(self.mock_server_port)

			cr.blocking_navigate_and_get_source(inurl_3)

			for x in range(999):
				time.sleep(1)
				current_title, _ = cr.get_page_url_title()
				if x > WRAPPER_STEP_THROUGH_TIMEOUT:
					raise RuntimeError("Timed out!")

				if 'Still at title?' not in current_title:
					break

			resp = cr.handle_page_location_changed()

			_, nurl_3 = cr.get_page_url_title()
			nurl2_3 = cr.get_current_url()

			self.assertEqual(outurl_3, nurl_3)
			self.assertEqual(outurl_3, nurl2_3)

			self.assertEqual(resp['content'], "Slow-Redirect-end-1")
			self.assertEqual(resp['binary'], False)
			self.assertEqual(resp['mimetype'], "text/html")

	def test_cloudflare_auto(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			tgturl = "http://127.0.0.1:{}/cloudflare_under_attack_shit".format(self.mock_server_port)
			cr.blocking_navigate_and_get_source(tgturl)

			for x in range(999):
				time.sleep(1)
				current_title, _ = cr.get_page_url_title()
				if x > WRAPPER_STEP_THROUGH_TIMEOUT:
					raise RuntimeError("Timed out!")

				if 'Just a moment...' not in current_title:
					break

			resp = cr.handle_page_location_changed()

			content = cr.get_rendered_page_source()
			self.assertEqual(content, '<html><head><title>At target CF page!</title></head><body>CF Redirected OK?</body></html>')

			# self.assertEqual(resp['content'], 'Multi-Redirect-end-5')
			# self.assertEqual(resp['binary'], False)
			# self.assertEqual(resp['mimetype'], "text/html")


	def test_sucuri_auto(self):
		with ChromeController.ChromeContext(binary=CHROME_BINARY_NAME) as cr:
			tgturl = "http://127.0.0.1:{}/sucuri_shit".format(self.mock_server_port)
			cr.blocking_navigate_and_get_source(tgturl)

			for x in range(999):
				time.sleep(1)
				current_title, _ = cr.get_page_url_title()
				if x > WRAPPER_STEP_THROUGH_TIMEOUT:
					raise RuntimeError("Timed out!")

				if "You are being redirected..." not in current_title:
					break

			content = cr.get_rendered_page_source()
			self.assertEqual(content, '<html><head><title>At target Sucuri page!</title></head><body>Sucuri Redirected OK?</body></html>')


