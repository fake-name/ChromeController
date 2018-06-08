
import traceback
import uuid
import socket
import logging
import os
import base64
import zlib
import gzip
import time
import datetime
from http import cookies
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from threading import Thread

import WebRequest


def capture_expected_headers(expected_headers, test_context, is_chromium=False, is_selenium_garbage_chromium=False, is_annoying_pjs=False, skip_header_checks=False):

	# print("Capturing expected headers:")
	# print(expected_headers)

	assert isinstance(expected_headers, dict)

	for key, val in expected_headers.items():
		assert isinstance(key, str)
		assert isinstance(val, str)

	cookie_key = uuid.uuid4().hex
	log = logging.getLogger("Main.TestServer")


	counter = 0

	class MockServerRequestHandler(BaseHTTPRequestHandler):


		def log_message(self, format, *args):
			return

		def validate_headers(self):
			for key, value in expected_headers.items():
				if not skip_header_checks:
					v1 = value.replace(" ", "")
					v2 = self.headers[key]
					if v2 is None:
						v2 = ""
					v2 = v2.replace(" ", "")
					test_context.assertEqual(v1, v2, msg="Mismatch in header parameter '{}' : '{}' -> '{}'".format(key, value, self.headers[key]))


		def _get_handler(self):
			nonlocal counter

			try:
				self.validate_headers()
			except Exception:
				self.send_response(500)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Headers failed validation!")
				raise

			trimmed_path = self.path.split("?")[0]

			if trimmed_path == "/":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Root OK?")
			elif trimmed_path == "/counter":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				ret = "Counter: %s" % counter
				self.wfile.write(ret.encode("utf-8"))
				counter += 1

			elif trimmed_path == "/counter_big":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				ret = "Counter: %s" % counter
				ret = ret * 50000
				self.wfile.write(ret.encode("utf-8"))
				counter += 1

			##################################################################################################################################
			# Handle requests for an unknown path
			##################################################################################################################################
			else:
				test_context.assertEqual(self.path, "This shouldn't happen!")

		def do_GET(self):
			# Process an HTTP GET request and return a response with an HTTP 200 status.
			log.info("Request for URL path: '%s'", self.path)
			# print("Headers: ", self.headers)
			# print("Cookie(s): ", self.headers.get_all('Cookie', failobj=[]))

			try:
				return self._get_handler()
			except Exception as e:
				log.error("Exception in handler!")
				for line in traceback.format_exc().split("\n"):
					log.error(line)
				raise e

	return MockServerRequestHandler

def get_free_port():
	s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
	s.bind(('localhost', 0))
	address, port = s.getsockname()
	s.close()
	return port


def start_server(assertion_class,
			expected_headers,
			port_override                = None,
			skip_header_checks           = False
		):

	# Configure mock server.
	if port_override:
		mock_server_port = port_override
	else:
		mock_server_port = get_free_port()

	captured_server = capture_expected_headers(expected_headers,
			assertion_class,
			skip_header_checks           = skip_header_checks
		)
	retries = 4

	for x in range(retries + 1):
		try:
			mock_server = HTTPServer(('localhost', mock_server_port), captured_server)
			break
		except OSError:
			time.sleep(0.2)
			if x >= retries:
				raise

	# Start running mock server in a separate thread.
	# Daemon threads automatically shut down when the main process exits.
	mock_server_thread = Thread(target=mock_server.serve_forever)
	mock_server_thread.setDaemon(True)
	mock_server_thread.start()

	return mock_server_port, mock_server, mock_server_thread



if __name__ == '__main__':

	wg = WebRequest.WebGetRobust()
	srv = start_server(None, wg, skip_header_checks=True)

	print("running server on port: ", srv)
	while 1:
		time.sleep(1)
