
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
import urllib.parse
from http import cookies
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from threading import Thread



def capture_expected_headers(test_context, expected_headers):

	# print("Capturing expected headers:")
	# print(expected_headers)

	if isinstance(expected_headers, list):
		expected_headers = dict(expected_headers)

	assert isinstance(expected_headers, dict), "expected_headers must be a dict. Passed a %s" % type(expected_headers)

	for key, val in expected_headers.items():
		assert isinstance(key, str)
		assert isinstance(val, str)

	cookie_key = uuid.uuid4().hex
	log = logging.getLogger("Main.TestServer")


	counter = 0

	sucuri_reqs_1 = 0
	sucuri_reqs_2 = 0
	sucuri_reqs_3 = 0

	class MockServerRequestHandler(BaseHTTPRequestHandler):


		def log_message(self, format, *args):
			return

		def validate_headers(self):
			try:
				for key, value in expected_headers.items():
					v1 = value.replace(" ", "")
					v2 = self.headers[key]
					if v2 is None:
						v2 = ""
					v2 = v2.replace(" ", "")
					test_context.assertEqual(v1, v2, msg="Mismatch in header parameter '{}' : '{}' -> '{}'".format(key, value, self.headers[key]))
					# print("Header match: ", key, v1, v2)
			except Exception:
				print("Header mismatch!")
				print("Received Headers:")
				for key, value in self.headers.items():
					print("	{} -> {}".format(key, value))
				print("Expected Headers:")
				for key, value in expected_headers.items():
					print("	{} -> {}".format(key, value))

				raise


		def _get_handler(self):

			nonlocal counter
			nonlocal sucuri_reqs_1
			nonlocal sucuri_reqs_2
			nonlocal sucuri_reqs_3


			if self.path != "/ignore-headers":
				try:
					self.validate_headers()
				except Exception:
					self.send_response(500)
					self.send_header('Content-type', "text/html")
					self.end_headers()
					self.wfile.write(b"Headers failed validation!")
					raise


			if self.path == "/":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Root OK?")


			elif self.path == "/ignore-headers":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Root OK?")


			elif self.path == "/favicon.ico":
				self.send_response(404)
				self.end_headers()

			elif self.path == "/raw-txt":
				self.send_response(200)
				self.send_header('Content-type', "text/plain")
				self.end_headers()
				self.wfile.write(b"Root OK?")

			elif self.path == "/html-decode":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Root OK?")

			elif self.path == "/html/real":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"<html><body>Root OK?</body></html>")

			elif self.path == "/compressed/deflate":
				self.send_response(200)
				self.send_header('Content-Encoding', 'deflate')
				self.send_header('Content-type', "text/html")
				self.end_headers()

				inb = b"Root OK?"
				cobj = zlib.compressobj(wbits=-zlib.MAX_WBITS)
				t1 = cobj.compress(inb) + cobj.flush()
				self.wfile.write(t1)

			elif self.path == "/compressed/gzip":
				self.send_response(200)
				self.send_header('Content-Encoding', 'gzip')
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(gzip.compress(b"Root OK?"))

			elif self.path == "/json/invalid":
				self.send_response(200)
				self.send_header('Content-type', "application/json")
				self.end_headers()
				self.wfile.write(b"LOLWAT")

			elif self.path == "/json/valid":
				self.send_response(200)
				self.send_header('Content-type', "application/json")
				self.end_headers()
				self.wfile.write(b'{"oh" : "hai"}')

			elif self.path == "/json/no-coding":
				self.send_response(200)
				self.end_headers()
				self.wfile.write(b'{"oh" : "hai"}')

			elif self.path == "/filename/path-only.txt":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename/path-only-trailing-slash/":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename/content-disposition":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename=lolercoaster.txt")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/path-only.txt":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/content-disposition":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename=lolercoaster.txt")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/content-disposition-html-suffix":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename=lolercoaster.html")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/content-disposition-quotes-1":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename='lolercoaster.html'")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/content-disposition-quotes-2":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename=\'lolercoaster.html\'")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/content-disposition-quotes-spaces-1":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename='loler coaster.html'")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/content-disposition-quotes-spaces-2":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename=\"loler coaster.html\"")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/filename_mime/explicit-html-mime":
				self.send_response(200)
				self.send_header('Content-type', "application/x-binary")
				self.send_header('Content-Disposition', "filename=lolercoaster.html")
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"LOLWAT?\x00\xff\xaa\x55!")

			elif self.path == "/redirect/bad-1":
				self.send_response(302)
				self.end_headers()

			elif self.path == "/redirect/bad-2":
				self.send_response(302)
				self.send_header('location', "bad-2")
				self.end_headers()

			elif self.path == "/redirect/bad-3":
				self.send_response(302)
				self.send_header('location', "gopher://www.google.com")
				self.end_headers()

			elif self.path == "/redirect/from-1":
				self.send_response(302)
				self.send_header('location', "to-1")
				self.end_headers()

			elif self.path == "/redirect/to-1":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Redirect-To-1")

			# I'm not completely sure this is completely a valid way to do redirects?
			elif self.path == "/redirect/from-2":
				self.send_response(302)
				self.send_header('uri', "to-2")
				self.end_headers()

			elif self.path == "/redirect/to-2":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Redirect-To-2")

			elif self.path == "/redirect/from-3":
				self.send_response(302)
				newurl = "http://{}:{}/redirect/to-3".format(self.server.server_address[0], self.server.server_address[1])
				self.send_header('location', newurl)
				self.end_headers()

			elif self.path == "/redirect/to-3":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Redirect-To-3")

			elif self.path == "/redirect/from-4":
				self.send_response(302)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				body = "<html><body><script>window.location.href='/redirect/to-4'</script></body></html>"
				self.wfile.write(body.encode("utf-8"))

			elif self.path == "/redirect/to-4":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Redirect-To-4")

			# This looks like a cross-domain request
			elif self.path == "/redirect/from-5":
				self.send_response(302)
				newurl = "http://{}:{}/".format(self.server.server_address[0], self.server.server_address[1])
				self.send_header('location', newurl)
				self.end_headers()


			##################################################################################################################################
			# Multiple redirects
			##################################################################################################################################

			elif self.path == "/redirect_mult/from-1":
				self.send_response(302)
				self.send_header('location', "from-2")
				self.end_headers()

			elif self.path == "/redirect_mult/from-2":
				self.send_response(302)
				self.send_header('location', "from-3")
				self.end_headers()

			elif self.path == "/redirect_mult/from-3":
				self.send_response(302)
				self.send_header('location', "from-4")
				self.end_headers()

			elif self.path == "/redirect_mult/from-4":
				self.send_response(302)
				self.send_header('location', "to-5")
				self.end_headers()

			elif self.path == "/redirect_mult/to-5":
				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Multi-Redirect-end-5")


			elif self.path == '/redirect_slow/from-1':

				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b'<html><head><title>Still at title?</title></head><body>Slow Redirect</body><script type="text/JavaScript">setTimeout("location.href = \'/redirect_slow/to-1\';", 1500);</script></html>')

			elif self.path == '/redirect_slow/to-1':

				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"Slow-Redirect-end-1")



			##################################################################################################################################
			#
			##################################################################################################################################

			elif self.path == "/password/expect":
				# print("Password")
				# print(self.headers)

				self.send_response(200)
				self.end_headers()

				if not 'Authorization' in self.headers:
					self.wfile.write(b"Password not sent!!")
					return

				val = self.headers['Authorization']
				passval = val.split(" ")[-1]
				passstr = base64.b64decode(passval)

				if passstr == b'lol:wat':
					self.wfile.write(b"Password Ok?")
				else:
					self.wfile.write(b"Password Bad!")

			elif self.path == "/content/have-title":
				self.send_response(200)
				self.end_headers()
				self.wfile.write(b"<html><head><title>I can haz title?</title></head><body>This page has a title!</body></html>")

			elif self.path == "/content/no-title":
				self.send_response(200)
				self.end_headers()
				self.wfile.write(b"<html><head></head><body>This page has no title. Sadface.jpg</body></html>")

			elif self.path == "/binary_ctnt":
				self.send_response(200)
				self.send_header('Content-type', "image/jpeg")
				self.end_headers()
				self.wfile.write(b"Binary!\x00\x01\x02\x03")

			elif self.path == "/binary_ctnt":
				self.send_response(200)
				self.send_header('Content-type', "image/jpeg")
				self.end_headers()
				self.wfile.write(b"Binary!\x00\x01\x02\x03")



			##################################################################################################################################
			# Cookie stuff
			##################################################################################################################################

			elif self.path == '/cookie_test':
				cook = cookies.SimpleCookie()
				cook['cookie_test_key'] = cookie_key
				cook['cookie_test_key']['path'] = "/"
				cook['cookie_test_key']['domain'] = ""
				expiration = datetime.datetime.now() + datetime.timedelta(days=30)
				cook['cookie_test_key']["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
				self.send_response(200)
				self.send_header('Content-type', "text/html")

				self.send_header('Set-Cookie', cook['cookie_test_key'].OutputString())
				self.end_headers()
				self.wfile.write(b"<html><body>CF Cookie Test</body></html>")

			elif self.path == '/cookie_require':
				if self.headers.get_all('Cookie', failobj=[]):
					cook = self.headers.get_all('Cookie', failobj=[])[0]
					cook_key, cook_value = cook.split("=", 1)
					if cook_key == 'cookie_test_key' and cook_value == cookie_key:
						self.send_response(200)
						self.send_header('Content-type', "text/html")
						self.end_headers()
						self.wfile.write(b"<html><body>Cookie forwarded properly!</body></html>")
						return

				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(b"<html><body>Cookie is missing</body></html>")




			##################################################################################################################################
			# Sucuri validation
			##################################################################################################################################





			elif self.path == '/sucuri_shit_3':
				# I'd like to get this down to just 2 requests (cookie bounce, and fetch).
				# Doing that requires pulling html content out of chromium, though.
				# Annoying.
				sucuri_reqs_3 += 1

				if sucuri_reqs_3 > 3:
					raise RuntimeError("Too many requests to sucuri_shit_3 (%s)!" % sucuri_reqs_3)

				if self.headers.get_all('Cookie', failobj=[]):
					cook = self.headers.get_all('Cookie', failobj=[])[0]

					cook_key, cook_value = cook.split("=", 1)

					if cook_key == 'sucuri_cloudproxy_uuid_6293e0004' and cook_value == '04cbb56494ebedbcd19a61b2d728c478':
						# if cook['']
						self.send_response(200)
						self.send_header('Content-type', "text/html")
						self.end_headers()
						self.wfile.write(b"<html><head><title>At target preemptive Sucuri page!</title></head><body>Preemptive waf circumvented OK (p3)?</body></html>")

						return


				container_dir = os.path.dirname(__file__)
				fpath = os.path.join(container_dir, "waf_garbage", 'sucuri_garbage.html')
				with open(fpath, "rb") as fp:
					plain_contents = fp.read()

				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(plain_contents)

			elif self.path == '/sucuri_shit_2':
				# This particular path is the one we should already have a cookie for.
				# As such, we expect one request only
				sucuri_reqs_2 += 1

				if sucuri_reqs_2 > 1:
					raise RuntimeError("Too many requests to sucuri_shit_2 (%s)!" % sucuri_reqs_2)

				if self.headers.get_all('Cookie', failobj=[]):
					cook = self.headers.get_all('Cookie', failobj=[])[0]

					cook_key, cook_value = cook.split("=", 1)

					if cook_key == 'sucuri_cloudproxy_uuid_6293e0004' and cook_value == '04cbb56494ebedbcd19a61b2d728c478':
						# if cook['']
						self.send_response(200)
						self.send_header('Content-type', "text/html")
						self.end_headers()
						self.wfile.write(b"<html><head><title>At target preemptive Sucuri page!</title></head><body>Preemptive waf circumvented OK (p2)?</body></html>")

						return


				container_dir = os.path.dirname(__file__)
				fpath = os.path.join(container_dir, "waf_garbage", 'sucuri_garbage.html')
				with open(fpath, "rb") as fp:
					plain_contents = fp.read()

				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(plain_contents)

			elif self.path == '/sucuri_shit':
				sucuri_reqs_1 += 1

				if sucuri_reqs_1 > 4:
					raise RuntimeError("Too many requests to sucuri_shit (%s)!" % sucuri_reqs_1)

				# print("Fetch for ", self.path)
				# print("Cookies:", self.headers.get_all('Cookie', failobj=[]))

				if self.headers.get_all('Cookie', failobj=[]):
					cook = self.headers.get_all('Cookie', failobj=[])[0]

					cook_key, cook_value = cook.split("=", 1)

					if cook_key == 'sucuri_cloudproxy_uuid_6293e0004' and cook_value == '04cbb56494ebedbcd19a61b2d728c478':
						# if cook['']
						self.send_response(200)
						self.send_header('Content-type', "text/html")
						self.end_headers()
						self.wfile.write(b"<html><head><title>At target Sucuri page!</title></head><body>Sucuri Redirected OK?</body></html>")

						return


				container_dir = os.path.dirname(__file__)
				fpath = os.path.join(container_dir, "waf_garbage", 'sucuri_garbage.html')
				with open(fpath, "rb") as fp:
					plain_contents = fp.read()

				self.send_response(200)
				self.send_header('Content-type', "text/html")
				self.end_headers()
				self.wfile.write(plain_contents)

			##################################################################################################################################
			# Cloudflare validation
			##################################################################################################################################

			elif self.path == '/cloudflare_under_attack_shit_2':
				if self.headers.get_all('Cookie', failobj=[]):
					cook = self.headers.get_all('Cookie', failobj=[])[0]

					cook_key, cook_value = cook.split("=", 1)

					if cook_key == 'cloudflare_validate_key' and cook_value == cookie_key:
						# if cook['']
						self.send_response(200)
						self.send_header('Content-type', "text/html")
						self.end_headers()
						self.wfile.write(b"<html><head><title>At target CF page!</title></head><body>CF Redirected OK?</body></html>")

						return

				container_dir = os.path.dirname(__file__)
				fpath = os.path.join(container_dir, "waf_garbage", 'cloudflare_bullshit.html')
				with open(fpath, "rb") as fp:
					plain_contents = fp.read()

				self.send_response(503)
				self.send_header('Content-type','text/html')
				self.end_headers()
				self.wfile.write(plain_contents)

			elif self.path == '/cloudflare_under_attack_shit':
				if self.headers.get_all('Cookie', failobj=[]):
					cook = self.headers.get_all('Cookie', failobj=[])[0]

					cook_key, cook_value = cook.split("=", 1)

					if cook_key == 'cloudflare_validate_key' and cook_value == cookie_key:
						# if cook['']
						self.send_response(200)
						self.send_header('Content-type', "text/html")
						self.end_headers()
						self.wfile.write(b"<html><head><title>At target CF page!</title></head><body>CF Redirected OK?</body></html>")

						return

				container_dir = os.path.dirname(__file__)
				fpath = os.path.join(container_dir, "waf_garbage", 'cloudflare_bullshit.html')
				with open(fpath, "rb") as fp:
					plain_contents = fp.read()

				self.send_response(503)
				self.send_header('Content-type','text/html')
				self.end_headers()
				self.wfile.write(plain_contents)

			elif (self.path == '/cdn-cgi/l/chk_jschl?jschl_vc=b10392d4929902df66c5d69ff703fde7&pass=1516685611.828-z5pqL%2FrL34&jschl_answer=3161' or
				  self.path == '/cdn-cgi/l/chk_jschl?jschl_vc=b10392d4929902df66c5d69ff703fde7&pass=1516685611.828-z5pqL%2FrL34&jschl_answer=3160'):

				cook = cookies.SimpleCookie()
				cook['cloudflare_validate_key'] = cookie_key
				cook['cloudflare_validate_key']['path'] = "/"
				cook['cloudflare_validate_key']['domain'] = ""
				expiration = datetime.datetime.now() + datetime.timedelta(days=30)
				cook['cloudflare_validate_key']["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
				self.send_response(200)
				self.send_header('Content-type', "text/html")

				self.send_header('Set-Cookie', cook['cloudflare_validate_key'].OutputString())
				self.end_headers()

				body = "<html><body>Setting cookies.<script>window.location.href='/cloudflare_under_attack_shit'</script></body></html>"
				self.wfile.write(body.encode("utf-8"))




			##################################################################################################################################
			# Handle requests for an unknown path
			##################################################################################################################################

			else:
				test_context.assertEqual(self.path, "This shouldn't happen!")

		def _post_handler(self):

			nonlocal counter
			nonlocal sucuri_reqs_1
			nonlocal sucuri_reqs_2
			nonlocal sucuri_reqs_3


			if self.path != "/ignore-headers":
				try:
					self.validate_headers()
				except Exception:
					self.send_response(500)
					self.send_header('Content-type', "text/html")
					self.end_headers()
					self.wfile.write(b"Headers failed validation!")
					raise

			# print("Headers:", self.headers)
			# print("Dir:", dir(self.headers))

			ctype = self.headers.get_content_type()
			if ctype == 'multipart/form-data':
				postvars = urllib.parse.parse_qsl(self.rfile)
			elif ctype == 'application/x-www-form-urlencoded':
				length = int(self.headers.get('content-length'))
				in_str = self.rfile.read(length)
				postvars = urllib.parse.parse_qsl(in_str, keep_blank_values=1)
			else:

				length = int(self.headers.get('content-length', 0))
				if length:
					postvars = self.rfile.read(length)

			# print("Post type: ", ctype)
			# print("PostData: ", postvars)

			##################################################################################################################################
			# POSTing data
			##################################################################################################################################


			if self.path == "/post/json_resp":
				if postvars == b'test_post_1' and ctype == 'application/json':
					self.send_response(200)
					self.send_header('Content-type', "application/json")
					self.end_headers()
					self.wfile.write(b'{"oh" : "hai"}')
				else:
					self.send_response(200)
					self.send_header('Content-type', "application/json")
					self.end_headers()
					self.wfile.write(b'{"not" : "a post?"}')

			elif self.path == "/post/form_urlencoded":
				if postvars == [(b'test', b'1'), (b'moar', b'two')] and ctype == 'application/x-www-form-urlencoded':
					self.send_response(200)
					self.send_header('Content-type', "application/json")
					self.end_headers()
					self.wfile.write(b'{"oh" : "hai"}')
				else:
					self.send_response(200)
					self.send_header('Content-type', "application/json")
					self.end_headers()
					self.wfile.write(b'{"not" : "a post?"}')



			##################################################################################################################################
			# Handle requests for an unknown path
			##################################################################################################################################

			else:
				test_context.assertEqual(self.path, "This shouldn't happen!")



		def do_POST(self):
			log.info("POST for URL path: '%s'", self.path)

			try:
				return self._post_handler()
			except Exception as e:
				log.error("Exception in handler!")
				for line in traceback.format_exc().split("\n"):
					log.error(line)
				raise e


		def do_GET(self):
			# Process an HTTP GET request and return a response with an HTTP 200 status.
			log.info("GET for URL path: '%s'", self.path)
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



	captured_server = capture_expected_headers(expected_headers=expected_headers, test_context=assertion_class)
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

