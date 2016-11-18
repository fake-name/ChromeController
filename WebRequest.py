#!/usr/bin/python3
import sys
import codecs

try:
	import cchardet as chardet
except ImportError:
	import chardet as chardet

import http.client
import email.parser

def parse_headers(fp, _class=http.client.HTTPMessage):
	"""Parses only RFC2822 headers from a file pointer.

	email Parser wants to see strings rather than bytes.
	But a TextIOWrapper around self.rfile would buffer too many bytes
	from the stream, bytes which we later need to read as bytes.
	So we read the correct bytes here, as bytes, for email Parser
	to parse.

	Note: Monkey-patched version to try to more intelligently determine
	header encoding

	"""
	headers = []
	while True:
		line = fp.readline(http.client._MAXLINE + 1)
		if len(line) > http.client._MAXLINE:
			raise http.client.LineTooLong("header line")
		headers.append(line)
		if len(headers) > http.client._MAXHEADERS:
			raise HTTPException("got more than %d headers" % http.client._MAXHEADERS)
		if line in (b'\r\n', b'\n', b''):
			break


	hstring = b''.join(headers)
	inferred = chardet.detect(hstring)
	if inferred and inferred['confidence'] > 0.8:
		print("Parsing headers!", hstring)
		hstring = hstring.decode(inferred['encoding'])
	else:
		hstring = hstring.decode('iso-8859-1')

	return email.parser.Parser(_class=_class).parsestr(hstring)

http.client.parse_headers = parse_headers

import urllib.request
import urllib.parse
import urllib.error
import os.path

import time
import http.cookiejar

import traceback

import logging
import zlib
import bs4
import re
import string
import gzip
import io
import socket
import json
import base64

import random
random.seed()


import selenium.webdriver.chrome.service
import selenium.webdriver.chrome.options
import selenium.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




def as_soup(str):
	return bs4.BeautifulSoup(str, "lxml")


def determine_json_encoding(json_bytes):
	'''
	Given the fact that the first 2 characters in json are guaranteed to be ASCII, we can use
	these to determine the encoding.
	See: http://tools.ietf.org/html/rfc4627#section-3

	Copied here:
	   Since the first two characters of a JSON text will always be ASCII
	   characters [RFC0020], it is possible to determine whether an octet
	   stream is UTF-8, UTF-16 (BE or LE), or UTF-32 (BE or LE) by looking
	   at the pattern of nulls in the first four octets.

			   00 00 00 xx  UTF-32BE
			   00 xx 00 xx  UTF-16BE
			   xx 00 00 00  UTF-32LE
			   xx 00 xx 00  UTF-16LE
			   xx xx xx xx  UTF-8
	'''
	assert(isinstance(json_bytes, bytes))
	if len(json_bytes) > 4:
		b1, b2, b3, b4 = json_bytes[0], json_bytes[1], json_bytes[2], json_bytes[3]
		if   b1 == 0 and b2 == 0 and b3 == 0 and b4 != 0:
			return "UTF-32BE"
		elif b1 == 0 and b2 != 0 and b3 == 0 and b4 != 0:
			return "UTF-16BE"
		elif b1 != 0 and b2 == 0 and b3 == 0 and b4 == 0:
			return "UTF-32LE"
		elif b1 != 0 and b2 == 0 and b3 != 0 and b4 == 0:
			return "UTF-16LE"
		elif b1 != 0 and b2 != 0 and b3 != 0 and b4 != 0:
			return "UTF-8"
		else:
			raise ValueError("Unknown encoding!")
	elif len(json_bytes) > 2:
		b1, b2 = json_bytes[0], json_bytes[1]
		if   b1 == 0 and b2 == 0:
			return "UTF-32BE"
		elif b1 == 0 and b2 != 0:
			return "UTF-16BE"
		elif b1 != 0 and b2 == 0:
			raise ValueError("Json string too short to definitively infer encoding.")
		elif b1 != 0 and b2 != 0:
			return "UTF-8"
		else:
			raise ValueError("Unknown encoding!")

	raise ValueError("Input string too short to guess encoding!")


class title_not_contains(object):
	""" An expectation for checking that the title *does not* contain a case-sensitive
	substring. title is the fragment of title expected
	returns True when the title matches, False otherwise
	"""
	def __init__(self, title):
		self.title = title


	def __call__(self, driver):
		return self.title not in driver.title

#pylint: disable-msg=E1101, C0325, R0201, W0702, W0703

def wait_for(condition_function):
	start_time = time.time()
	while time.time() < start_time + 3:
		if condition_function():
			return True
		else:
			time.sleep(0.1)
	raise Exception(
		'Timeout waiting for {}'.format(condition_function.__name__)
	)

class load_delay_context_manager(object):

	def __init__(self, browser):
		self.browser = browser

	def __enter__(self):
		self.old_page = self.browser.find_element_by_tag_name('html')

	def page_has_loaded(self):
		new_page = self.browser.find_element_by_tag_name('html')
		return new_page.id != self.old_page.id

	def __exit__(self, *_):
		wait_for(self.page_has_loaded)


class HeadRequest(urllib.request.Request):
	def get_method(self):
		# Apparently HEAD is now being blocked. Because douche.
		return "GET"
		# return "HEAD"

class HTTPRedirectBlockerErrorHandler(urllib.request.HTTPErrorProcessor):

	def http_response(self, request, response):
		code, msg, hdrs = response.code, response.msg, response.info()

		# only add this line to stop 302 redirection.
		if code == 302:
			print("Code!", 302)
			return response
		if code == 301:
			print("Code!", 301)
			return response

		print("[HTTPRedirectBlockerErrorHandler] http_response! code:", code)
		print(hdrs)
		print(msg)
		if not (200 <= code < 300):
			response = self.parent.error('http', request, response, code, msg, hdrs)
		return response

	https_response = http_response

# Custom redirect handler to work around
# issue https://bugs.python.org/issue17214
class HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
	# Implementation note: To avoid the server sending us into an
	# infinite loop, the request object needs to track what URLs we
	# have already seen.  Do this by adding a handler-specific
	# attribute to the Request object.
	def http_error_302(self, req, fp, code, msg, headers):
		# Some servers (incorrectly) return multiple Location headers
		# (so probably same goes for URI).  Use first header.
		if "location" in headers:
			newurl = headers["location"]
		elif "uri" in headers:
			newurl = headers["uri"]
		else:
			return

		# fix a possible malformed URL
		urlparts = urllib.parse.urlparse(newurl)

		# For security reasons we don't allow redirection to anything other
		# than http, https or ftp.

		if urlparts.scheme not in ('http', 'https', 'ftp', ''):
			raise urllib.error.HTTPError(
				newurl, code,
				"%s - Redirection to url '%s' is not allowed" % (msg, newurl),
				headers, fp)

		if not urlparts.path:
			urlparts = list(urlparts)
			urlparts[2] = "/"
		newurl = urllib.parse.urlunparse(urlparts)

		# http.client.parse_headers() decodes as ISO-8859-1.  Recover the
		# original bytes and percent-encode non-ASCII bytes, and any special
		# characters such as the space.
		newurl = urllib.parse.quote(
			newurl, encoding="iso-8859-1", safe=string.punctuation)
		newurl = urllib.parse.urljoin(req.full_url, newurl)

		# XXX Probably want to forget about the state of the current
		# request, although that might interact poorly with other
		# handlers that also use handler-specific request attributes
		new = self.redirect_request(req, fp, code, msg, headers, newurl)
		if new is None:
			return

		# loop detection
		# .redirect_dict has a key url if url was previously visited.
		if hasattr(req, 'redirect_dict'):
			visited = new.redirect_dict = req.redirect_dict
			if (visited.get(newurl, 0) >= self.max_repeats or
				len(visited) >= self.max_redirections):
				raise urllib.error.HTTPError(req.full_url, code,
								self.inf_msg + msg, headers, fp)
		else:
			visited = new.redirect_dict = req.redirect_dict = {}
		visited[newurl] = visited.get(newurl, 0) + 1

		# Don't close the fp until we are sure that we won't use it
		# with HTTPError.
		fp.read()
		fp.close()

		return self.parent.open(new, timeout=req.timeout)

# A urllib2 wrapper that provides error handling and logging, as well as cookie management. It's a bit crude, but it works.
# Also supports transport compresion.
# OOOOLLLLLLDDDDD, has lots of creaky internals. Needs some cleanup desperately, but lots of crap depends on almost everything.
# Arrrgh.

from threading import Lock
COOKIEWRITELOCK = Lock()

GLOBAL_COOKIE_FILE = None

class PreemptiveBasicAuthHandler(urllib.request.HTTPBasicAuthHandler):
	'''Preemptive basic auth.

	Instead of waiting for a 403 to then retry with the credentials,
	send the credentials if the url is handled by the password manager.
	Note: please use realm=None when calling add_password.'''
	def http_request(self, req):
		url = req.get_full_url()
		realm = None
		# this is very similar to the code from retry_http_basic_auth()
		# but returns a request object.
		user, pw = self.passwd.find_user_password(realm, url)
		if pw:
			raw = "%s:%s" % (user, pw)
			raw = raw.encode("ascii")
			auth = b'Basic ' + base64.standard_b64encode(raw).strip()
			req.add_unredirected_header(self.auth_header, auth)
		return req

	https_request = http_request

class WebGetRobust:
	COOKIEFILE = 'cookies.lwp'				# the path and filename to save your cookies in
	cj = None
	cookielib = None
	opener = None

	errorOutCount = 2
	# retryDelay = 0.1
	retryDelay = 0.0


	data = None

	# if test=true, no resources are actually fetched (for testing)
	# creds is a list of 3-tuples that gets inserted into the password manager.
	# it is structured [(top_level_url1, username1, password1), (top_level_url2, username2, password2)]
	def __init__(self, test=False, creds=None, logPath="Main.Web", cookie_lock=None, cloudflare=False):

		self.rules = {}
		self.rules['cloudflare'] = cloudflare
		if cookie_lock:
			self.cookie_lock = cookie_lock
		else:
			self.cookie_lock = COOKIEWRITELOCK

		self.pjs_driver = None
		self.cr_driver = None

		# Override the global default socket timeout, so hung connections will actually time out properly.
		socket.setdefaulttimeout(15)

		self.log = logging.getLogger(logPath)
		# print("Webget init! Logpath = ", logPath)
		if creds:
			print("Have creds for a domain")
		if test:
			self.log.warning("-----------------------------------------------------------------------------------------------")
			self.log.warning("WARNING: WebGet in testing mode!")
			self.log.warning("-----------------------------------------------------------------------------------------------")

		# Due to general internet people douchebaggyness, I've basically said to hell with it and decided to spoof a whole assortment of browsers
		# It should keep people from blocking this scraper *too* easily
		self.browserHeaders = getUserAgent()

		self.testMode = test		# if we don't want to actually contact the remote server, you pass a string containing
									# pagecontent for testing purposes as test. It will get returned for any calls of getpage()

		self.data = urllib.parse.urlencode(self.browserHeaders)


		if creds:
			print("Have credentials, installing password manager into urllib handler.")
			passManager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
			for url, username, password in creds:
				passManager.add_password(None, url, username, password)
			self.credHandler = PreemptiveBasicAuthHandler(passManager)
		else:
			self.credHandler = None

		self.loadCookies()

	def loadCookies(self):

		self.cj = http.cookiejar.LWPCookieJar()		# This is a subclass of FileCookieJar
												# that has useful load and save methods
		if self.cj is not None:
			if os.path.isfile(self.COOKIEFILE):
				try:
					self.cj.load(self.COOKIEFILE)
					# self.log.info("Loading CookieJar")
				except:
					self.log.critical("Cookie file is corrupt/damaged?")
					try:
						os.remove(self.COOKIEFILE)
					except FileNotFoundError:
						pass
			if http.cookiejar is not None:
				# self.log.info("Installing CookieJar")
				self.log.debug(self.cj)
				cookieHandler = urllib.request.HTTPCookieProcessor(self.cj)
				if self.credHandler:
					print("Have cred handler. Building opener using it")
					self.opener = urllib.request.build_opener(cookieHandler, self.credHandler, HTTPRedirectHandler())
				else:
					# print("No cred handler")
					self.opener = urllib.request.build_opener(cookieHandler, HTTPRedirectHandler())
				#self.opener.addheaders = [('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')]
				self.opener.addheaders = self.browserHeaders
				#urllib2.install_opener(self.opener)

		for cookie in self.cj:
			self.log.debug(cookie)
			#print cookie


	def chunkReport(self, bytesSoFar, totalSize):
		if totalSize:
			percent = float(bytesSoFar) / totalSize
			percent = round(percent * 100, 2)
			self.log.info("Downloaded %d of %d bytes (%0.2f%%)" % (bytesSoFar, totalSize, percent))
		else:
			self.log.info("Downloaded %d bytes" % (bytesSoFar))


	def chunkRead(self, response, chunkSize=2 ** 18, reportHook=None):
		contentLengthHeader = response.info().getheader('Content-Length')
		if contentLengthHeader:
			totalSize = contentLengthHeader.strip()
			totalSize = int(totalSize)
		else:
			totalSize = None
		bytesSoFar = 0
		pgContent = ""
		while 1:
			chunk = response.read(chunkSize)
			pgContent += chunk
			bytesSoFar += len(chunk)

			if not chunk:
				break

			if reportHook:
				reportHook(bytesSoFar, chunkSize, totalSize)

		return pgContent



	def getSoup(self, *args, **kwargs):
		if 'returnMultiple' in kwargs and kwargs['returnMultiple']:
			raise ValueError("getSoup cannot be called with 'returnMultiple' being true")

		if 'soup' in kwargs and kwargs['soup']:
			raise ValueError("getSoup contradicts the 'soup' directive!")

		page = self.getpage(*args, **kwargs)
		if isinstance(page, bytes):
			raise ValueError("Received content not decoded! Cannot parse!")

		soup = bs4.BeautifulSoup(page, "lxml")
		return soup

	def getJson(self, *args, **kwargs):
		if 'returnMultiple' in kwargs and kwargs['returnMultiple']:
			raise ValueError("getSoup cannot be called with 'returnMultiple' being true")

		attempts = 0
		while 1:
			try:
				page = self.getpage(*args, **kwargs)
				if isinstance(page, bytes):
					page = page.decode(determine_json_encoding(page))
					# raise ValueError("Received content not decoded! Cannot parse!")

				page = page.strip()
				ret = json.loads(page)
				return ret
			except ValueError:
				if attempts < 1:
					attempts += 1
					self.log.error("JSON Parsing issue retreiving content from page!")
					for line in traceback.format_exc().split("\n"):
						self.log.error("%s", line.rstrip())
					self.log.error("Retrying!")

					# Scramble our current UA
					self.browserHeaders = getUserAgent()
					time.sleep(self.retryDelay)
				else:
					self.log.error("JSON Parsing issue, and retries exhausted!")
					# self.log.error("Page content:")
					# self.log.error(page)
					# with open("Error-ctnt-{}.json".format(time.time()), "w") as tmp_err_fp:
					# 	tmp_err_fp.write(page)
					raise


	def getFileAndName(self, *args, **kwargs):
		if 'returnMultiple' in kwargs:
			raise ValueError("getFileAndName cannot be called with 'returnMultiple'")

		if 'soup' in kwargs and kwargs['soup']:
			raise ValueError("getFileAndName contradicts the 'soup' directive!")

		kwargs["returnMultiple"] = True

		pgctnt, pghandle = self.getpage(*args, **kwargs)

		info = pghandle.info()
		if not 'Content-Disposition' in info:
			hName = ''
		elif not 'filename=' in info['Content-Disposition']:
			hName = ''
		else:
			hName = info['Content-Disposition'].split('filename=')[1]
		return pgctnt, hName

	def buildRequest(self, pgreq, postData, addlHeaders, binaryForm, req_class = urllib.request.Request):
		# Encode Unicode URL's properly

		try:
			tmp = pgreq.encode("ascii")
		except UnicodeEncodeError:
			print("Wat?")
			print("pgreq: '%s'", pgreq)

		try:
			params = {}
			headers = {}
			if postData != None:
				self.log.info("Making a post-request! Params: '%s'", postData)
				params['data'] = urllib.parse.urlencode(postData).encode("utf-8")
			if addlHeaders != None:
				self.log.info("Have additional GET parameters!")
				for key, parameter in addlHeaders.items():
					self.log.info("	Item: '%s' -> '%s'", key, parameter)
				headers = addlHeaders
			if binaryForm:
				self.log.info("Binary form submission!")
				if 'data' in params:
					raise ValueError("You cannot make a binary form post and a plain post request at the same time!")

				params['data']            = binaryForm.make_result()
				headers['Content-type']   =  binaryForm.get_content_type()
				headers['Content-length'] =  len(params['data'])

			return req_class(pgreq, headers=headers, **params)

		except:
			self.log.critical("Invalid header or url")
			raise


	def decodeHtml(self, pageContent, cType):

		# this *should* probably be done using a parser.
		# However, it seems to be grossly overkill to shove the whole page (which can be quite large) through a parser just to pull out a tag that
		# should be right near the page beginning anyways.
		# As such, it's a regular expression for the moment

		# Regex is of bytes type, since we can't convert a string to unicode until we know the encoding the
		# bytes string is using, and we need the regex to get that encoding
		coding = re.search(rb"charset=[\'\"]?([a-zA-Z0-9\-]*)[\'\"]?", pageContent, flags=re.IGNORECASE)

		cType = b""
		charset = None
		try:
			if coding:
				cType = coding.group(1)
				codecs.lookup(cType.decode("ascii"))
				charset = cType.decode("ascii")

		except LookupError:

			# I'm actually not sure what I was thinking when I wrote this if statement. I don't think it'll ever trigger.
			if (b";" in cType) and (b"=" in cType): 		# the server is reporting an encoding. Now we use it to decode the

				dummy_docType, charset = cType.split(b";")
				charset = charset.split(b"=")[-1]

		if not charset:
			self.log.warning("Could not find encoding information on page - Using default charset. Shit may break!")
			charset = "iso-8859-1"

		try:
			pageContent = str(pageContent, charset)

		except UnicodeDecodeError:
			self.log.error("Encoding Error! Stripping invalid chars.")
			pageContent = pageContent.decode('utf-8', errors='ignore')

		return pageContent

	def decompressContent(self, coding, pgctnt):
		#preLen = len(pgctnt)
		if coding == 'deflate':
			compType = "deflate"

			pgctnt = zlib.decompress(pgctnt, -zlib.MAX_WBITS)

		elif coding == 'gzip':
			compType = "gzip"

			buf = io.BytesIO(pgctnt)
			f = gzip.GzipFile(fileobj=buf)
			pgctnt = f.read()

		elif coding == "sdch":
			raise ValueError("Wait, someone other then google actually supports SDCH compression?")

		else:
			compType = "none"

		return compType, pgctnt


	def getItem(self, itemUrl):

		try:
			content, handle = self.getpage(itemUrl, returnMultiple=True)
		except:
			print("Failure?")
			if self.rules['cloudflare']:
				if not self.stepThroughCloudFlare(itemUrl, titleNotContains='Just a moment...'):
					raise ValueError("Could not step through cloudflare!")
				# Cloudflare cookie set, retrieve again
				content, handle = self.getpage(itemUrl, returnMultiple=True)
			else:
				raise

		if not content or not handle:
			raise urllib.error.URLError("Failed to retreive file from page '%s'!" % itemUrl)

		fileN = urllib.parse.unquote(urllib.parse.urlparse(handle.geturl())[2].split("/")[-1])
		fileN = bs4.UnicodeDammit(fileN).unicode_markup
		mType = handle.info()['Content-Type']

		# If there is an encoding in the content-type (or any other info), strip it out.
		# We don't care about the encoding, since WebFunctions will already have handled that,
		# and returned a decoded unicode object.
		if mType and ";" in mType:
			mType = mType.split(";")[0].strip()

		# *sigh*. So minus.com is fucking up their http headers, and apparently urlencoding the
		# mime type, because apparently they're shit at things.
		# Anyways, fix that.
		if '%2F' in  mType:
			mType = mType.replace('%2F', '/')

		self.log.info("Retreived file of type '%s', name of '%s' with a size of %0.3f K", mType, fileN, len(content)/1000.0)
		return content, fileN, mType


	def _initPjsWebDriver(self):
		if self.pjs_driver:
			self.pjs_driver.quit()
		dcap = dict(DesiredCapabilities.PHANTOMJS)
		wgSettings = dict(self.browserHeaders)
		# Install the headers from the WebGet class into phantomjs
		dcap["phantomjs.page.settings.userAgent"] = wgSettings.pop('User-Agent')
		for headerName in wgSettings:
			if headerName != 'Accept-Encoding':
				dcap['phantomjs.page.customHeaders.{header}'.format(header=headerName)] = wgSettings[headerName]

		self.pjs_driver = selenium.webdriver.PhantomJS(desired_capabilities=dcap)
		self.pjs_driver.set_window_size(1024, 768)

	def _initCrWebDriver(self):
		if self.cr_driver:
			self.cr_driver.quit()
		dcap = dict(DesiredCapabilities.CHROME)
		wgSettings = dict(self.browserHeaders)
		# Install the headers from the WebGet class into phantomjs
		user_agent = wgSettings.pop('User-Agent')
		dcap["chrome.page.settings.userAgent"] = user_agent
		for headerName in wgSettings:
			if headerName != 'Accept-Encoding':
				dcap['chrome.page.customHeaders.{header}'.format(header=headerName)] = wgSettings[headerName]

		dcap["chrome.switches"] = ["--user-agent="+user_agent]


		chromedriver = r'./venv/bin/chromedriver'
		chrome       = r'./Headless/headless_shell'

		chrome_options = selenium.webdriver.chrome.options.Options()
		chrome_options.binary_location = chrome
		chrome_options.add_argument('--load-component-extension')
		chrome_options.add_argument("--user-agent=\"{}\"".format(user_agent))
		chrome_options.add_argument('--verbose')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-extension')

		self.cr_driver = selenium.webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=dcap)
		# We can't set the chrome desired capabilities, since headless chrome
		# doesn't allow extensions.

		self.cr_driver.set_page_load_timeout(30)

	def _syncIntoPjsWebDriver(self):
		# TODO
		pass

	def _syncOutOfPjsWebDriver(self):
		for cookie in self.pjs_driver.get_cookies():
			self.addSeleniumCookie(cookie)


	def getItemPhantomJS(self, itemUrl):
		self.log.info("Fetching page for URL: '%s' with PhantomJS" % itemUrl)

		if not self.pjs_driver:
			self._initPjsWebDriver()
		self._syncIntoPjsWebDriver()

		with load_delay_context_manager(self.pjs_driver):
			self.pjs_driver.get(itemUrl)
		time.sleep(3)

		fileN = urllib.parse.unquote(urllib.parse.urlparse(self.pjs_driver.current_url)[2].split("/")[-1])
		fileN = bs4.UnicodeDammit(fileN).unicode_markup

		self._syncOutOfPjsWebDriver()

		# Probably a bad assumption
		mType = "text/html"

		# So, self.pjs_driver.page_source appears to be the *compressed* page source as-rendered. Because reasons.
		source = self.pjs_driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

		assert source != '<head></head><body></body>'

		source = "<html>"+source+"</html>"
		return source, fileN, mType


	def decodeTextContent(self, pgctnt, cType):

		if cType:
			if (";" in cType) and ("=" in cType):
				# the server is reporting an encoding. Now we use it to decode the content
				# Some wierdos put two charsets in their headers:
				# `text/html;Charset=UTF-8;charset=UTF-8`
				# Split, and take the first two entries.
				docType, charset = cType.split(";")[:2]
				charset = charset.split("=")[-1]

				# Only decode content marked as text (yeah, google is serving zip files
				# with the content-disposition charset header specifying "UTF-8") or
				# specifically allowed other content types I know are really text.
				decode = ['application/atom+xml', 'application/xml', "application/json", 'text']
				if any([item in docType for item in decode]):
					try:
						pgctnt = str(pgctnt, charset)
					except UnicodeDecodeError:
						self.log.error("Encoding Error! Stripping invalid chars.")
						pgctnt = pgctnt.decode('utf-8', errors='ignore')

			else:
				# The server is not reporting an encoding in the headers.
				# Use content-aware mechanisms for determing the content encoding.


				if "text/html" in cType or \
					'text/javascript' in cType or    \
					'application/xml' in cType or    \
					'application/atom+xml' in cType:				# If this is a html/text page, we want to decode it using the local encoding

					pgctnt = self.decodeHtml(pgctnt, cType)

				elif "text/plain" in cType or "text/xml" in cType:
					pgctnt = bs4.UnicodeDammit(pgctnt).unicode_markup

				# Assume JSON is utf-8. Probably a bad idea?
				elif "application/json" in cType:
					pgctnt = pgctnt.decode('utf-8')

				elif "text" in cType:
					self.log.critical("Unknown content type!")
					self.log.critical(cType)

		else:
			self.log.critical("No content disposition header!")
			self.log.critical("Cannot guess content type!")

		return pgctnt

	def retreiveContent(self, pgreq, pghandle, callBack):
		try:
			# If we have a progress callback, call it for chunked read.
			# Otherwise, just read in the entire content.
			if callBack:
				pgctnt = self.chunkRead(pghandle, 2 ** 17, reportHook=callBack)
			else:
				pgctnt = pghandle.read()


			if pgctnt == None:
				return False

			self.log.info("URL fully retrieved.")

			preDecompSize = len(pgctnt)/1000.0

			encoded = pghandle.headers.get('Content-Encoding')
			compType, pgctnt = self.decompressContent(encoded, pgctnt)


			decompSize = len(pgctnt)/1000.0
			# self.log.info("Page content type = %s", type(pgctnt))
			cType = pghandle.headers.get("Content-Type")
			if compType == 'none':
				self.log.info("Compression type = %s. Content Size = %0.3fK. File type: %s.", compType, decompSize, cType)
			else:
				self.log.info("Compression type = %s. Content Size compressed = %0.3fK. Decompressed = %0.3fK. File type: %s.", compType, preDecompSize, decompSize, cType)

			pgctnt = self.decodeTextContent(pgctnt, cType)

			return pgctnt

		except:
			print("pghandle = ", pghandle)

			self.log.error(sys.exc_info())
			traceback.print_exc()
			self.log.error("Error Retrieving Page! - Transfer failed. Waiting %s seconds before retrying", self.retryDelay)

			try:
				self.log.critical("Critical Failure to retrieve page! %s at %s", pgreq.get_full_url(), time.ctime(time.time()))
				self.log.critical("Exiting")
			except:
				self.log.critical("And the URL could not be printed due to an encoding error")
			print()
			self.log.error(pghandle)
			time.sleep(self.retryDelay)

		return False


		# HUGE GOD-FUNCTION.
		# OH GOD FIXME.

		# postData expects a dict
		# addlHeaders also expects a dict
	def getpage(self, requestedUrl, **kwargs):
		# pgreq = fixurl(pgreq)

		# strip trailing and leading spaces.
		requestedUrl = requestedUrl.strip()

		# addlHeaders = None, returnMultiple = False, callBack=None, postData=None, soup=False, retryQuantity=None, nativeError=False, binaryForm=False

		# If we have 'soup' as a param, just pop it, and call `getSoup()`.
		if 'soup' in kwargs and kwargs['soup']:
			self.log.warn("'soup' kwarg is depreciated. Please use the `getSoup()` call instead.")
			kwargs.pop('soup')

			return self.getSoup(requestedUrl, **kwargs)

		# Decode the kwargs values
		addlHeaders    = kwargs.setdefault("addlHeaders",     None)
		returnMultiple = kwargs.setdefault("returnMultiple",  False)
		callBack       = kwargs.setdefault("callBack",        None)
		postData       = kwargs.setdefault("postData",        None)
		retryQuantity  = kwargs.setdefault("retryQuantity",   None)
		nativeError    = kwargs.setdefault("nativeError",     False)
		binaryForm     = kwargs.setdefault("binaryForm",      False)

		# Conditionally encode the referrer if needed, because otherwise
		# urllib will barf on unicode referrer values.
		if addlHeaders and 'Referer' in addlHeaders:
			addlHeaders['Referer'] = iri2uri(addlHeaders['Referer'])

		requestedUrl = iri2uri(requestedUrl)


		if not self.testMode:
			retryCount = 0
			while 1:

				pgctnt = None
				pghandle = None

				pgreq = self.buildRequest(requestedUrl, postData, addlHeaders, binaryForm)

				errored = False
				lastErr = ""

				retryCount = retryCount + 1

				if (retryQuantity and retryCount > retryQuantity) or (not retryQuantity and retryCount > self.errorOutCount):
					self.log.error("Failed to retrieve Website : %s at %s All Attempts Exhausted", pgreq.get_full_url(), time.ctime(time.time()))
					pgctnt = None
					try:
						self.log.critical("Critical Failure to retrieve page! %s at %s, attempt %s", pgreq.get_full_url(), time.ctime(time.time()), retryCount)
						self.log.critical("Error: %s", lastErr)
						self.log.critical("Exiting")
					except:
						self.log.critical("And the URL could not be printed due to an encoding error")
					break

				#print "execution", retryCount
				try:
					# print("Getpage!", requestedUrl, kwargs)
					pghandle = self.opener.open(pgreq, timeout=30)					# Get Webpage
					# print("Gotpage")

				except urllib.error.HTTPError as e:								# Lotta logging
					self.log.warning("Error opening page: %s at %s On Attempt %s.", pgreq.get_full_url(), time.ctime(time.time()), retryCount)
					self.log.warning("Error Code: %s", e)

					#traceback.print_exc()
					lastErr = e
					try:

						self.log.warning("Original URL: %s", requestedUrl)
						errored = True
					except:
						self.log.warning("And the URL could not be printed due to an encoding error")

					if e.code == 404:
						#print "Unrecoverable - Page not found. Breaking"
						self.log.critical("Unrecoverable - Page not found. Breaking")
						break

					time.sleep(self.retryDelay)
					if e.code == 503:
						errcontent = e.read()
						if b'This process is automatic. Your browser will redirect to your requested content shortly.' in errcontent:
							self.log.warn("Cloudflare failure! Doing automatic step-through.")
							self.stepThroughCloudFlare(requestedUrl, titleNotContains="Just a moment...")
				except UnicodeEncodeError:
					self.log.critical("Unrecoverable Unicode issue retreiving page - %s", requestedUrl)
					for line in traceback.format_exc().split("\n"):
						self.log.critical("%s", line.rstrip())
					self.log.critical("Parameters:")
					self.log.critical("	requestedUrl: '%s'", requestedUrl)
					self.log.critical("	postData:     '%s'", postData)
					self.log.critical("	addlHeaders:  '%s'", addlHeaders)
					self.log.critical("	binaryForm:   '%s'", binaryForm)


					break





				except Exception:
					errored = True
					#traceback.print_exc()
					lastErr = sys.exc_info()
					self.log.warning("Retreival failed. Traceback:")
					self.log.warning(lastErr)
					self.log.warning(traceback.format_exc())

					self.log.warning("Error Retrieving Page! - Trying again - Waiting %s seconds", self.retryDelay)

					try:
						self.log.critical("Error on page - %s", requestedUrl)
					except:
						self.log.critical("And the URL could not be printed due to an encoding error")

					time.sleep(self.retryDelay)


					continue

				if pghandle != None:
					self.log.info("Request for URL: %s succeeded at %s On Attempt %s. Recieving...", pgreq.get_full_url(), time.ctime(time.time()), retryCount)
					pgctnt = self.retreiveContent(pgreq, pghandle, callBack)

					# if retreiveContent did not return false, it managed to fetch valid results, so break
					if pgctnt != False:
						break

		if errored and pghandle != None:
			print(("Later attempt succeeded %s" % pgreq.get_full_url()))
			#print len(pgctnt)
		elif errored and pghandle == None:

			if lastErr and nativeError:
				raise lastErr
			raise urllib.error.URLError("Failed to retreive page '%s'!" % (requestedUrl, ))

		if returnMultiple:
			return pgctnt, pghandle
		else:
			if pghandle:
				pghandle.close()
			return pgctnt

	def getHead(self, url, addlHeaders):
		for x in range(9999):
			try:
				self.log.info("Doing HTTP HEAD request for '%s'", url)
				pgreq = self.buildRequest(url, None, addlHeaders, None, req_class=HeadRequest)
				pghandle = self.opener.open(pgreq, timeout=30)
				returl = pghandle.geturl()
				if returl != url:
					self.log.info("HEAD request returned a different URL '%s'", returl)

				return returl
			except socket.timeout as e:
				self.log.info("Timeout, retrying....")
				if x >= 3:
					self.log.error("Failure fetching: %s", url)
					raise e
			except urllib.error.URLError as e:
				# Continue even in the face of cloudflare crapping it's pants
				if e.code == 500 and e.geturl():
					return e.geturl()
				self.log.info("URLError, retrying....")
				if x >= 3:
					self.log.error("Failure fetching: %s", url)
					raise e

	def getHeadPhantomJS(self, url, referrer):
		self.log.info("Getting HEAD with PhantomJS")

		if not self.pjs_driver:
			self._initPjsWebDriver()
		self._syncIntoPjsWebDriver()

		def try_get(loc_url):
			tries = 3
			for x in range(9999):
				try:
					self.pjs_driver.get(loc_url)
					time.sleep(random.uniform(2, 6))
					return
				except socket.timeout as e:
					if x > tries:
						raise e

		try_get(referrer)
		try_get(url)

		self._syncOutOfPjsWebDriver()

		return self.pjs_driver.current_url

	def syncCookiesFromFile(self):
		# self.log.info("Synchronizing cookies with cookieFile.")
		if os.path.isfile(self.COOKIEFILE):
			self.cj.save("cookietemp.lwp")
			self.cj.load(self.COOKIEFILE)
			self.cj.load("cookietemp.lwp")
		# First, load any changed cookies so we don't overwrite them
		# However, we want to persist any cookies that we have that are more recent then the saved cookies, so we temporarily save
		# the cookies in memory to a temp-file, then load the cookiefile, and finally overwrite the loaded cookies with the ones from the
		# temp file

	def updateCookiesFromFile(self):
		if os.path.exists(self.COOKIEFILE):
			# self.log.info("Synchronizing cookies with cookieFile.")
			self.cj.load(self.COOKIEFILE)
		# Update cookies from cookiefile

	def addCookie(self, inCookie):
		self.log.info("Updating cookie!")
		self.cj.set_cookie(inCookie)

	def addSeleniumCookie(self, cookieDict):
		'''
		Install a cookie exported from a selenium webdriver into
		the active opener
		'''
		# print cookieDict
		cookie = http.cookiejar.Cookie(
				version            = 0,
				name               = cookieDict['name'],
				value              = cookieDict['value'],
				port               = None,
				port_specified     = False,
				domain             = cookieDict['domain'],
				domain_specified   = True,
				domain_initial_dot = False,
				path               = cookieDict['path'],
				path_specified     = False,
				secure             = cookieDict['secure'],
				expires            = cookieDict['expiry'] if 'expiry' in cookieDict else None,
				discard            = False,
				comment            = None,
				comment_url        = None,
				rest               = {"httponly":"%s" % cookieDict['httponly']},
				rfc2109            = False
			)

		self.cj.set_cookie(cookie)

	def initLogging(self):
		print("WARNING - Webget logging re-initialized?")
		mainLogger = logging.getLogger("Main")			# Main logger
		mainLogger.setLevel(logging.DEBUG)

		ch = logging.StreamHandler(sys.stdout)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		ch.setFormatter(formatter)
		mainLogger.addHandler(ch)

	def saveCookies(self, halting=False):

		locked = self.cookie_lock.acquire(timeout=5)
		if not locked:
			self.log.error("Failed to acquire cookie-lock!")
			return

		# print("Have %d cookies before saving cookiejar" % len(self.cj))
		try:
			# self.log.info("Trying to save cookies!")
			if self.cj is not None:							# If cookies were used

				self.syncCookiesFromFile()

				# self.log.info("Have cookies to save")
				for cookie in self.cj:
					# print(cookie)
					# print(cookie.expires)

					if isinstance(cookie.expires, int) and cookie.expires > 30000000000:		# Clamp cookies that expire stupidly far in the future because people are assholes
						cookie.expires = 30000000000

				# self.log.info("Calling save function")
				self.cj.save(self.COOKIEFILE)					# save the cookies again


				# self.log.info("Cookies Saved")
			else:
				self.log.info("No cookies to save?")
		except Exception as e:
			pass
			# The destructor call order is too incoherent, and shit fails
			# during the teardown with null-references. The error printout is
			# not informative, so just silence it.
			# print("Possible error on exit (or just the destructor): '%s'." % e)
		finally:
			self.cookie_lock.release()

		# print("Have %d cookies after saving cookiejar" % len(self.cj))
		if not halting:
			self.syncCookiesFromFile()
		# print "Have %d cookies after reloading cookiejar" % len(self.cj)

	def __del__(self):
		# print "WGH Destructor called!"
		self.saveCookies(halting=True)

		if self.pjs_driver != None:
			self.pjs_driver.quit()



	def stepThroughCloudFlare(self, url, titleContains='', titleNotContains=''):
		'''
		Use Selenium+PhantomJS to access a resource behind cloudflare protection.

		Params:
			``url`` - The URL to access that is protected by cloudflare
			``titleContains`` - A string that is in the title of the protected page, and NOT the
				cloudflare intermediate page. The presence of this string in the page title
				is used to determine whether the cloudflare protection has been successfully
				penetrated.

		The current WebGetRobust headers are installed into the selenium browser, which
		is then used to access the protected resource.

		Once the protected page has properly loaded, the cloudflare access cookie is
		then extracted from the selenium browser, and installed back into the WebGetRobust
		instance, so it can continue to use the cloudflare auth in normal requests.

		'''

		if (not titleContains) and (not titleNotContains):
			raise ValueError("You must pass either a string the title should contain, or a string the title shouldn't contain!")

		if titleContains and titleNotContains:
			raise ValueError("You can only pass a single conditional statement!")


		self.log.info("Attempting to access page through cloudflare browser verification.")

		dcap = dict(DesiredCapabilities.PHANTOMJS)
		wgSettings = dict(self.browserHeaders)

		# Install the headers from the WebGet class into phantomjs
		dcap["phantomjs.page.settings.userAgent"] = wgSettings.pop('User-Agent')
		for headerName in wgSettings:
			dcap['phantomjs.page.customHeaders.{header}'.format(header=headerName)] = wgSettings[headerName]

		driver = selenium.webdriver.PhantomJS(desired_capabilities=dcap)
		driver.set_window_size(1024, 768)

		driver.get(url)

		if titleContains:
			condition = EC.title_contains(titleContains)
		elif titleNotContains:
			condition = title_not_contains(titleNotContains)
		else:
			raise ValueError("Wat?")


		try:
			WebDriverWait(driver, 20).until(condition)
			success = True
			self.log.info("Successfully accessed main page!")
		except TimeoutException:
			self.log.error("Could not pass through cloudflare blocking!")
			success = False
		# Add cookies to cookiejar

		for cookie in driver.get_cookies():
			self.addSeleniumCookie(cookie)
			#print cookie[u"value"]

		self.syncCookiesFromFile()

		return success




# Convert an IRI to a URI following the rules in RFC 3987
#
# The characters we need to enocde and escape are defined in the spec:
#
# iprivate =  %xE000-F8FF / %xF0000-FFFFD / %x100000-10FFFD
# ucschar = %xA0-D7FF / %xF900-FDCF / %xFDF0-FFEF
#         / %x10000-1FFFD / %x20000-2FFFD / %x30000-3FFFD
#         / %x40000-4FFFD / %x50000-5FFFD / %x60000-6FFFD
#         / %x70000-7FFFD / %x80000-8FFFD / %x90000-9FFFD
#         / %xA0000-AFFFD / %xB0000-BFFFD / %xC0000-CFFFD
#         / %xD0000-DFFFD / %xE1000-EFFFD

escape_range = [
	(0xA0, 0xD7FF),
	(0xE000, 0xF8FF),
	(0xF900, 0xFDCF),
	(0xFDF0, 0xFFEF),
	(0x10000, 0x1FFFD),
	(0x20000, 0x2FFFD),
	(0x30000, 0x3FFFD),
	(0x40000, 0x4FFFD),
	(0x50000, 0x5FFFD),
	(0x60000, 0x6FFFD),
	(0x70000, 0x7FFFD),
	(0x80000, 0x8FFFD),
	(0x90000, 0x9FFFD),
	(0xA0000, 0xAFFFD),
	(0xB0000, 0xBFFFD),
	(0xC0000, 0xCFFFD),
	(0xD0000, 0xDFFFD),
	(0xE1000, 0xEFFFD),
	(0xF0000, 0xFFFFD),
	(0x100000, 0x10FFFD),
]

def encode(c):
	retval = c
	i = ord(c)
	for low, high in escape_range:
		if i < low:
			break
		if i >= low and i <= high:
			retval = "".join(["%%%2X" % o for o in c.encode('utf-8')])
			break
	return retval


def iri2uri(uri):
	"""Convert an IRI to a URI. Note that IRIs must be
	passed in a unicode strings. That is, do not utf-8 encode
	the IRI before passing it into the function."""

	assert uri != None, 'iri2uri must be passed a non-none string!'

	original = uri
	if isinstance(uri ,str):
		(scheme, authority, path, query, fragment) = urllib.parse.urlsplit(uri)
		authority = authority.encode('idna').decode('utf-8')
		# For each character in 'ucschar' or 'iprivate'
		#  1. encode as utf-8
		#  2. then %-encode each octet of that utf-8
		path = urllib.parse.quote(path)
		uri = urllib.parse.urlunsplit((scheme, authority, path, query, fragment))
		uri = "".join([encode(c) for c in uri])

	# urllib.parse.urlunsplit(urllib.parse.urlsplit({something})
	# strips any trailing "?" chars. While this may be legal according to the
	# spec, it breaks some services. Therefore, we patch
	# the "?" back in if it has been removed.
	if original.endswith("?") and not uri.endswith("?"):
		uri = uri+"?"
	return uri


class DummyLog:									# For testing WebGetRobust (mostly)
	logText = ""

	def __init__(self):
		pass

	def __repr__(self):
		return self.logText

	def write(self, string):
		self.logText = "%s\n%s" % (self.logText, string)

	def close(self):
		pass




# Due to general internet people douchebaggyness, I've basically said to hell with it and decided to spoof a whole assortment of browsers
# It should keep people from blocking this scraper *too* easily

# This file generates a random browser user-agent, It should have an extremely large set of possible UA structures.
USER_AGENTS = [
	"Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2) ",
	"Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2)",
	"Mozilla/4.0 (compatible; Dillo 3.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Maxthon 2.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; Trident/7.0; .NET4.0E; .NET4.0C)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
	"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
	"Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 (like Gecko)",
	"Mozilla/5.0 (compatible; Konqueror/4.1; OpenBSD) KHTML/4.1.4 (like Gecko)",
	"Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.4 (like Gecko) Slackware/13.0",
	"Mozilla/5.0 (compatible; Konqueror/4.3; Linux) KHTML/4.3.1 (like Gecko) Fedora/4.3.1-3.fc11",
	"Mozilla/5.0 (compatible; Konqueror/4.4; Linux 2.6.32-22-generic; X11; en_US) KHTML/4.4.3 (like Gecko) Kubuntu",
	"Mozilla/5.0 (compatible; Konqueror/4.4; Linux) KHTML/4.4.1 (like Gecko) Fedora/4.4.1-1.fc12",
	"Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)",
	"Mozilla/5.0 (compatible; Konqueror/4.5; NetBSD 5.0.2; X11; amd64; en_US) KHTML/4.5.4 (like Gecko)",
	"Mozilla/5.0 (compatible; Konqueror/4.5; Windows) KHTML/4.5.4 (like Gecko)",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
	"Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0)",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:20.0) Gecko/20100101 Firefox/20.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:35.0) Gecko/20100101 Firefox/35.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 1083) AppleWebKit/537.36 (KHTML like Gecko) Chrome/28.0.1469.0 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML like Gecko) Version/6.0.2 Safari/536.26.17",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.31 (KHTML like Gecko) Chrome/26.0.1410.63 Safari/537.31",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.1 (KHTML like Gecko) Version/7.0.6 Safari/537.78.1",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.0.13.81_10003810) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15  (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7; en-us) AppleWebKit/534.20.8 (KHTML, like Gecko) Version/5.1 Safari/534.20.8",
	"Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941",
	"Mozilla/5.0 (Unknown; U; UNIX BSD/SYSV system; C -) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.2",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
	"Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
	"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	"Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.29 Safari/537.36 OPR/15.0.1147.24 (Edition Next)",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.71 (KHTML like Gecko) WebVideo/1.0.1.10 Version/7.0 Safari/537.71",
	"Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:35.0) Gecko/20100101 Firefox/35.0",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML like Gecko) Maxthon/4.0.0.2000 Chrome/22.0.1229.79 Safari/537.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/28.0.1469.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36 OPR/19.0.1326.56",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36 OPR/20.0.1387.91",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20120422 Firefox/12.0 SeaMonkey/2.9",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
	"Mozilla/5.0 (Windows NT 6.2; rv:19.0) Gecko/20121129 Firefox/19.0",
	"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/28.0.1469.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
	"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34",
	"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.33",
	"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.35",
	"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.36",
	"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.37",
	"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.38",
	"Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/533.34",
	"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36 OPR/18.0.1284.49",
	"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
	"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
	"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
	"Mozilla/5.0 (Windows; U; Windows NT 6.2; es-US ) AppleWebKit/540.0 (KHTML like Gecko) Version/6.0 Safari/8900.00",
	"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	"Mozilla/5.0 (X11; CrOS x86_64 5841.83.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.138 Safari/537.36",
	"Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/536.5",
	"Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.79 Safari/537.4",
	"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
	"Mozilla/5.0 (X11; FreeBSD i386; rv:28.0) Gecko/20100101 Firefox/28.0 SeaMonkey/2.25",
	"Mozilla/5.0 (X11; Linux 3.8-6.dmz.1-liquorix-686) KHTML/4.8.4 (like Gecko) Konqueror/4.8",
	"Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
	"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.22 (KHTML like Gecko) Ubuntu Chromium/25.0.1364.160 Chrome/25.0.1364.160 Safari/537.22",
	"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1478.0 Safari/537.36",
	"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2166.2 Safari/537.36",
	"Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20120502 Firefox/12.0 SeaMonkey/2.9.1",
	"Mozilla/5.0 (X11; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1 Iceweasel/14.0.1",
	"Mozilla/5.0 (X11; Linux i686; rv:16.0) Gecko/20100101 Firefox/16.0",
	"Mozilla/5.0 (X11; Linux i686; rv:20.0) Gecko/20100101 Firefox/20.0",
	"Mozilla/5.0 (X11; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0",
	"Mozilla/5.0 (X11; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0",
	"Mozilla/5.0 (X11; Linux i686; rv:32.0) Gecko/20100101 Firefox/32.0",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/36.0.1985.125 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.166 Safari/537.36 OPR/20.0.1396.73172",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.56 Safari/537.4",
	"Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.02",
	"Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0 Iceweasel/19.0.2",
	"Mozilla/5.0 (X11; Linux) KHTML/4.9.1 (like Gecko) Konqueror/4.9",
	"Mozilla/5.0 (X11; NetBSD amd64; rv:16.0) Gecko/20121102 Firefox/16.0",
	"Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
	"Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
	"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
	"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
	"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
	"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
	"Mozilla/5.0 (X11; U; Linux i686; rv:19.0) Gecko/20100101 Slackware/13 Firefox/19.0",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
	"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
	"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
	"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
	"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
	"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
	"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
	"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
	"NetSurf/1.2 (NetBSD; amd64)",
	"Opera/9.20 (Macintosh; Intel Mac OS X; U; en)",
	"Opera/9.64 (Macintosh; PPC Mac OS X; U; en) Presto/2.1.1",
	"Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
	"Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
	"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.16",
	"Opera/9.80 (X11; FreeBSD 8.1-RELEASE i386; Edition Next) Presto/2.12.388 Version/12.10",
	"Opera/9.80 (X11; Linux i686) Presto/2.12.388 Version/12.16",
	"Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.10",
	"Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
	"Uzbl (Webkit 1.3) (Linux i686 [i686])",

]

ACCEPT_LANGUAGE =[

	"en-gb,en-us;q=0.7,de-ch;q=0.3",
	"en-GB,en-US;q=0.8,en;q=0.6",
	"en-GB,en-US;q=0.8,en;q=0.6",
	"en-US",
	"en-us, en;q=1.0,fr-ca, fr;q=0.5,pt-br, pt;q=0.5,es;q=0.5",
	"en-US,de-DE;q=0.5",
	"en-us,en;q=0.5",
	"en-US,en;q=0.8",
	"en-US,en;q=0.8,en-GB;q=0.6,fr-CA;q=0.4,fr;q=0.2",
	"en-US,en;q=0.8,es-419;q=0.6",
	"en-us,en;q=0.8,es;q=0.5,es-mx;q=0.3",
	"en-US,en;q=0.8,es;q=0.6",
	"en-US,en;q=0.8,pl;q=0.6",
	"en-US,en;q=0.8,pl;q=0.6",
	"en-US,en;q=0.9",
	"en-US,en;q=0.9,fr;q=0.8,de;q=0.7,id;q=0.6",
	"en-US,en;q=0.9,ja;q=0.8,fr;q=0.7,de;q=0.6,es;q=0.5,it;q=0.4,nl;q=0.3,sv;q=0.2,nb;q=0.1",

]

ACCEPT = [
		["text/html","application/xhtml+xml","application/xml;q=0.9"],
		["application/xml","application/xhtml+xml","text/html;q=0.9"," text/plain;q=0.8","image/png"],
		["text/html","application/xhtml+xml","application/xml;q=0.9"],
		["image/jpeg","application/x-ms-application","image/gif","application/xaml+xml","image/pjpeg","application/x-ms-xbap","application/x-shockwave-flash","application/msword"],
		["text/html","application/xml;q=0.9","application/xhtml+xml","image/png","image/webp","image/jpeg","image/gif","image/x-xbitmap"]
]

ACCEPT_POSTFIX = ["*/*;q=0.8", "*/*;q=0.5", "*/*;q=0.8", "*/*", "*/*;q=0.1"]

ENCODINGS = [['gzip'], ['gzip', 'deflate'], ['gzip', 'deflate', 'sdch']]


def getUserAgent():
	'''
	Generate a randomized user agent by permuting a large set of possible values.
	The returned user agent should look like a valid, in-use brower, with a specified preferred language of english.

	Return value is a list of tuples, where each tuple is one of the user-agent headers.

	Currently can provide approximately 147 * 17 * 5 * 5 * 2 * 3 * 2 values, or ~749K possible
	unique user-agents.
	'''
	coding = random.choice(ENCODINGS)
	random.shuffle(coding)
	coding = ",".join(coding)

	accept = random.choice(ACCEPT)
	random.shuffle(accept)
	accept.append(random.choice(ACCEPT_POSTFIX))
	accept = random.choice((", ", ",")).join(accept)

	user_agent = [
				('User-Agent'		,	random.choice(USER_AGENTS)),
				('Accept-Language'	,	random.choice(ACCEPT_LANGUAGE)),
				('Accept'			,	accept),
				('Accept-Encoding'	,	coding)
				]
	return user_agent




# This file based heavily on the UA List, Copyright (c) 2014, Harald Hope
# This list was released under the BSD 2 clause.

# Home page: techpatterns.com/forums/about304.html

# Special thanks to the following:
# User-Agent Switcher: www.chrispederick.com/work/user-agent-switcher
# Firefox history: www.zytrax.com/tech/web/firefox-history.html
# Mobile data: wikipedia.org/wiki/List_of_user_agents_for_mobile_phones
# Mobile data: www.zytrax.com/tech/web/mobile_ids.html
# Current User-Agents: http://myip.ms/browse/comp_browsers
# User-agent data: www.zytrax.com/tech/web/browser_ids.htm
# User-agent strings: www.useragentstring.com
# User-agent strings: www.webapps-online.com/online-tools/user-agent-strings/dv/

# License: BSD 2 Clause
# All rights reserved. Redistribution and use in source and binary forms,
# with or without modification, are permitted provided that the following
# conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this
# list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.




if __name__ == "__main__":
	import logSetup
	import sys
	logSetup.initLogging()
	print("Oh HAI")
	wg = WebGetRobust()

	if len(sys.argv) == 3:
		getUrl = sys.argv[1]
		fName  = sys.argv[2]
		print(getUrl, fName)

		content = wg.getpage(getUrl)

		try:
			out = content.encode("utf-8")
		except:
			out = content

		with open(fName, 'wb') as fp:
			fp.write(out)



	wg.getHead("http://www.novelupdates.com/extnu/125399/", addlHeaders={"Referer" : "http://www.novelupdates.com/series/limitless-sword-god/"})

	# # content, handle = wg.getpage("http://japtem.com/wp-content/uploads/2014/07/Arifureta.png", returnMultiple = True)
	# # print((handle.headers.get('Content-Encoding')))
	# # print(len(content))
	# # content, handle = wg.getpage("http://japtem.com/wp-content/uploads/2014/03/knm.png", returnMultiple = True)
	# # print((handle.headers.get('Content-Encoding')))
	# # content, handle = wg.getpage("https://www.google.com/images/srpr/logo11w.png", returnMultiple = True)
	# # print((handle.headers.get('Content-Encoding')))
	# # content, handle = wg.getpage("http://www.doujin-moe.us/ajax/newest.php", returnMultiple = True)
	# # print((handle.headers.get('Content-Encoding')))

	# # print("SoupGet")
	# # content_1 = wg.getpage("http://www.lighttpd.net", soup = True)

	# # content_2 = wg.getSoup("http://www.lighttpd.net")
	# # assert(content_1 == content_2)

	# gTest = wg.getpage('https://drive.google.com/folderview?id=0B2lnOX3NF2LOeW55WlpYQWIxYnM')
	# print(type(gTest))

	# gTest = wg.getpage('https://www.google.com/search?q=Gödel')
	# gTest = wg.getpage('https://www.google.com/search?q=禁断の愛')
	# gTest = wg.getpage('http://www.fanfiction.net/s/6711282/1/Jag-%C3%A4lskar-dig')
	# print(type(gTest))



# if __name__ == "__main__":
# 	print("User agent", getUserAgent())
