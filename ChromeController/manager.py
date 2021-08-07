
import distutils.spawn
import os.path
import sys
import subprocess
import pprint
import types
import json
import base64
import signal
import pprint
import time
import http.cookiejar
import urllib.parse
import ChromeController.filter_funcs as filter_funcs

from ChromeController.cr_exceptions import ChromeResponseNotReceived
from ChromeController.cr_exceptions import ChromeNavigateTimedOut
from ChromeController.cr_exceptions import ChromeError
from ChromeController.resources import js


# We use the generated wrapper. If you want a different version, use the CLI interface to update.
from ChromeController.Generator.Generated import ChromeRemoteDebugInterface as ChromeRemoteDebugInterface_base

DEFAULT_TIMEOUT_SECS = 10

class RemoteObject():
	def __init__(self, object_meta):
		self.object_meta = object_meta

		# TODO: Allow retreiving/interacting with these.
	def __repr__(self):
		return "<(Unimplemented) RemoteObject for JS object: '%s'>" % (self.object_meta, )

class ChromeRemoteDebugInterface(ChromeRemoteDebugInterface_base):
	'''
	Remote control class for Chromium.
	'''

	def __init__(self,
		binary                = None,
		dbg_port              = None,
		use_execution_manager = None,
		additional_options    = [],
		visible_size          = None,
		disable_page          = False,
		disable_dom           = False,
		disable_network       = False,
		*args,
		**kwargs):
		super().__init__(
			binary                = binary,
			dbg_port              = dbg_port,
			use_execution_manager = use_execution_manager,
			additional_options    = additional_options,
			*args, **kwargs)

		if disable_page:
			self.log.debug("Not enabling page debug interface")
		else:
			self.Page_enable()

		if disable_dom:
			self.log.debug("Not enabling DOM debug interface")
		else:
			self.DOM_enable()

		if disable_network:
			self.log.debug("Not enabling Network debug interface")
		else:
			self.Network_enable()

		if visible_size:
			assert isinstance(visible_size, tuple), "visible_size must be a 2-tuple containing 2 integers"
			assert len(visible_size) == 2, "visible_size must be a 2-tuple containing 2 integers"
			assert all([isinstance(val, int) for val in visible_size]), "visible_size must be a 2-tuple containing 2 integers"
			self.log.debug("Visible size overridden to %sx%s" % visible_size)
			self.Emulation_setVisibleSize(*visible_size)
		else:
			self.Emulation_setVisibleSize(1024, 1366)

		self.__new_tab_scripts = []

		# cr_ver = self.Browser_getVersion()
		# self.log.debug("Remote browser version info:")
		# self.log.debug(str(cr_ver))
		# 'protocolVersion'
		# 'product'
		# 'revision'
		# 'userAgent'
		# 'jsVersion'


	def update_headers(self, header_args):
		'''
		Given a set of headers, update both the user-agent
		and additional headers for the remote browser.

		header_args must be a dict. Keys are the names of
		the corresponding HTTP header.

		return value is a 2-tuple of the results of the user-agent
		update, as well as the extra headers update.
		If no 'User-Agent' key is present in the new headers,
		the first item in the tuple will be None

		'''
		assert isinstance(header_args, dict), "header_args must be a dict, passed type was %s" \
			% (type(header_args), )

		ua = header_args.pop('User-Agent', None)
		ret_1 = None
		if ua:
			ret_1 = self.Network_setUserAgentOverride(userAgent=ua)


		ret_2 = self.Network_setExtraHTTPHeaders(headers = header_args)
		return (ret_1, ret_2)


	def __remove_default_members(self, js_object):

		ret = []

		# This is kind of horrible
		for item in js_object:
			if 'name' in item:
				if item['name'] == '__defineGetter__':
					continue
				if item['name'] == '__defineSetter__':
					continue
				if item['name'] == '__lookupGetter__':
					continue
				if item['name'] == '__lookupSetter__':
					continue
				if item['name'] == '__proto__':
					continue
				if item['name'] == 'constructor':
					continue
				if item['name'] == 'hasOwnProperty':
					continue
				if item['name'] == 'isPrototypeOf':
					continue
				if item['name'] == 'propertyIsEnumerable':
					continue
				if item['name'] == 'toLocaleString':
					continue
				if item['name'] == 'toString':
					continue
				if item['name'] == 'valueOf':
					continue
				if item['name'] == 'ABORT_ERR':
					continue
				if item['name'] == 'DATA_CLONE_ERR':
					continue
				if item['name'] == 'INUSE_ATTRIBUTE_ERR':
					continue
				if item['name'] == 'INVALID_ACCESS_ERR':
					continue
				if item['name'] == 'INVALID_CHARACTER_ERR':
					continue
				if item['name'] == 'INVALID_MODIFICATION_ERR':
					continue
				if item['name'] == 'INVALID_NODE_TYPE_ERR':
					continue
				if item['name'] == 'INVALID_STATE_ERR':
					continue
				if item['name'] == 'NAMESPACE_ERR':
					continue
				if item['name'] == 'NETWORK_ERR':
					continue
				if item['name'] == 'NO_DATA_ALLOWED_ERR':
					continue
				if item['name'] == 'NO_MODIFICATION_ALLOWED_ERR':
					continue
				if item['name'] == 'NOT_FOUND_ERR':
					continue
				if item['name'] == 'NOT_SUPPORTED_ERR':
					continue
				if item['name'] == 'QUOTA_EXCEEDED_ERR':
					continue
				if item['name'] == 'SECURITY_ERR':
					continue
				if item['name'] == 'SYNTAX_ERR':
					continue
				if item['name'] == 'TIMEOUT_ERR':
					continue
				if item['name'] == 'TYPE_MISMATCH_ERR':
					continue
				if item['name'] == 'URL_MISMATCH_ERR':
					continue
				if item['name'] == 'VALIDATION_ERR':
					continue
				if item['name'] == 'WRONG_DOCUMENT_ERR':
					continue
				if item['name'] ==  'DOMSTRING_SIZE_ERR':
					continue
				if item['name'] ==  'HIERARCHY_REQUEST_ERR':
					continue
				if item['name'] ==  'INDEX_SIZE_ERR':
					continue

			ret.append(item)

		return ret

	def __unpack_object(self, object):
		assert isinstance(object, dict), "Object values must be a dict! Passed %s (%s)" % (type(object), object)
		ret = {}
		for key, value in object.items():
			assert isinstance(key, str)

			if isinstance(value, str):
				ret[key] = value
			elif isinstance(value, int):
				ret[key] = value
			elif isinstance(value, float):
				ret[key] = value
			elif value is None:   # Dammit, NoneType isn't exposed
				ret[key] = value
			elif value in (True, False):
				ret[key] = value
			elif isinstance(value, dict):
				ret[key] = self.__unpack_object(value)
			else:
				raise ValueError("Unknown type in object: %s (%s)" % (type(value), value))

		return ret

	def __decode_serialized_value(self, value):
		assert 'type' in value,  "Missing 'type' key from value: '%s'" % (value, )

		if 'get' in value and 'set' in value:
			self.log.debug("Unserializable remote script object")
			return RemoteObject(value['objectId'])

		if value['type'] == 'object' and 'objectId' in value:
			self.log.debug("Unserializable remote script object")
			return RemoteObject(value['objectId'])

		assert 'value' in value, "Missing 'value' key from value: '%s'" % (value, )

		if value['type'] == 'number':
			return float(value['value'])
		if value['type'] == 'string':
			return value['value']


		if value['type'] == 'object':
			return self.__unpack_object(value['value'])

		# Special case for null/none objects
		if (
				    'subtype' in value
				and
				    value['subtype'] == 'null'
				and
				    value['type'] == 'object'
				and
				    value['value'] is None):
			return None

		self.log.warning("Unknown serialized javascript value of type %s", value['type'])
		self.log.warning("Complete value: %s", value)

		return value

	def _unpack_xhr_resp(self, values):
		ret = {}

		# Handle single objects without all the XHR stuff.
		# This seems to be a chrome 84 change.
		if set(values.keys()) == set(['type', 'value']):
			if values['type'] == 'object':
				return self.__decode_serialized_value(values)

		for entry in values:
			# assert 'configurable' in entry, "'configurable' missing from entry (%s, %s)" % (entry, values)
			# assert 'enumerable'   in entry, "'enumerable' missing from entry (%s, %s)"   % (entry, values)
			# assert 'isOwn'        in entry, "'isOwn' missing from entry (%s, %s)"        % (entry, values)
			assert 'name'         in entry, "'name' missing from entry (%s, %s)"         % (entry, values)
			assert 'value'        in entry, "'value' missing from entry (%s, %s)"        % (entry, values)
			# assert 'writable'     in entry, "'writable' missing from entry (%s, %s)"     % (entry, values)

			if 'isOwn' in entry and entry['isOwn'] is False:
				continue

			assert entry['name'] not in ret
			ret[entry['name']] = self.__decode_serialized_value(entry['value'])

		return ret

	def xhr_fetch(self, url, headers=None, post_data=None, post_type=None):
		'''
		Execute a XMLHttpRequest() for content at `url`. If
		`headers` are specified, they must be a dict of string:string
		keader:values. post_data must also be pre-encoded.

		Note that this will be affected by the same-origin policy of the current
		page, so it can fail if you are requesting content from another domain and
		the current site has restrictive same-origin policies (which is very common).
		'''

		'''
		If you're thinking this is kind of a hack, well, it is.

		We also cheat a bunch and use synchronous XMLHttpRequest()s, because it
		SO much easier.
		'''
		js_script = '''
		function (url, headers, post_data, post_type){

			var req = new XMLHttpRequest();

			// We use sync calls, since we want to wait until the call completes
			// This will probably be depreciated at some point.
			if (post_data)
			{
				req.open("POST", url, false);
				if (post_type)
					req.setRequestHeader("Content-Type", post_type);
			}
			else
				req.open("GET", url, false);

			if (headers)
			{
				let entries = Object.entries(headers);
				for (let idx = 0; idx < entries.length; idx += 1)
				{
					req.setRequestHeader(entries[idx][0], entries[idx][1]);

				}
			}

			if (post_data)
				req.send(post_data);
			else
				req.send();

			return {
					url          : url,
					headers      : headers,
					resp_headers : req.getAllResponseHeaders(),
					post         : post_data,
					response     : req.responseText,
					mimetype     : req.getResponseHeader("Content-Type"),
					code         : req.status
				};
		}

		'''


		ret = self.execute_javascript_function(js_script, [url, headers, post_data, post_type])

		# print()
		# print()
		# print("XHR Response")
		# pprint.pprint(ret)
		# print()
		# print()

		ret = self._unpack_xhr_resp(ret)
		return ret
		# if


	def __unwrap_object_return(self, ret):
		if "result" in ret and 'result' in ret['result']:
			res = ret['result']['result']
			if 'objectId' in res:
				resp4 = self.Runtime_getProperties(res['objectId'])

				if "result" in resp4 and 'result' in resp4['result']:
					res_full = resp4['result']['result']

					return self.__remove_default_members(res_full)

			# Direct POD type return, just use it directly.
			if "type" in res and "value" in res:
				return res

		self.log.error("Failed fetching results from call!")
		return ret

	def __exec_js(self, script, should_call=False, args=None):
		'''

		Execute the passed javascript function/statement, optionally with passed
		arguments.

		Note that if args is not False, or should_call is True the passed script
		will be treated as a function definition and called via
		`(script).apply(null, args)`. Otherwise, the passed script will simply
		be evaluated.

		Note that if `script` is not a function, it must be a single statement.
		The presence of semicolons not enclosed in a bracket scope will produce
		an error.

		'''


		if args is None:
			args = {}

		# How chromedriver does this:

		#  std::unique_ptr<base::Value>* result) {
		#   std::string json;
		#   base::JSONWriter::Write(args, &json);
		#   // TODO(zachconrad): Second null should be array of shadow host ids.
		#   std::string expression = base::StringPrintf(
		#       "(%s).apply(null, [null, %s, %s])",
		#       kCallFunctionScript,
		#       function.c_str(),
		#       json.c_str());

		if args or should_call:
			expression = "({script}).apply(null, JSON.parse({args}))".format(
					script=script,
					args=repr(json.dumps(args))
				)
		else:
			expression = "({script})".format(
					script=script,
				)

		resp3 = self.Runtime_evaluate(expression=expression, returnByValue=True)

		resp4 = self.__unwrap_object_return(resp3)

		return resp4



	# Interact with http.cookiejar.Cookie() instances
	def get_cookies(self):
		'''
		Retreive the cookies from the remote browser.

		Return value is a list of http.cookiejar.Cookie() instances.
		These can be directly used with the various http.cookiejar.XXXCookieJar
		cookie management classes.
		'''
		ret = self.Network_getAllCookies()

		assert 'result' in ret, "No return value in function response!"
		assert 'cookies' in ret['result'], "No 'cookies' key in function response"

		cookies = []
		for raw_cookie in ret['result']['cookies']:

			# Chromium seems to support the following key values for the cookie dict:
			# 	"name"
			# 	"value"
			# 	"domain"
			# 	"path"
			# 	"expires"
			# 	"httpOnly"
			# 	"session"
			# 	"secure"
			#
			#  This seems supported by the fact that the underlying chromium cookie implementation has
			#  the following members:
			#        std::string name_;
			#        std::string value_;
			#        std::string domain_;
			#        std::string path_;
			#        base::Time creation_date_;
			#        base::Time expiry_date_;
			#        base::Time last_access_date_;
			#        bool secure_;
			#        bool httponly_;
			#        CookieSameSite same_site_;
			#        CookiePriority priority_;
			#
			# See chromium/net/cookies/canonical_cookie.h for more.
			#
			# I suspect the python cookie implementation is derived exactly from the standard, while the
			# chromium implementation is more of a practically derived structure.

			# Network.setCookie

			baked_cookie = http.cookiejar.Cookie(
					# We assume V0 cookies, principally because I don't think I've /ever/ actually encountered a V1 cookie.
					# Chromium doesn't seem to specify it.
					version            = 0,

					name               = raw_cookie['name'],
					value              = raw_cookie['value'],
					port               = None,
					port_specified     = False,
					domain             = raw_cookie['domain'],
					domain_specified   = True,
					domain_initial_dot = False,
					path               = raw_cookie['path'],
					path_specified     = False,
					secure             = raw_cookie['secure'],
					expires            = raw_cookie['expires'],
					discard            = raw_cookie['session'],
					comment            = None,
					comment_url        = None,
					rest               = {"httponly":"%s" % raw_cookie['httpOnly']},
					rfc2109            = False
				)
			cookies.append(baked_cookie)

		return cookies

	def set_cookie(self, cookie):
		'''
		Add a cookie to the remote chromium instance.

		Passed value `cookie` must be an instance of `http.cookiejar.Cookie()`.
		'''

		# Function path: Network.setCookie
		# Domain: Network
		# Method name: setCookie
		# WARNING: This function is marked 'Experimental'!
		# Parameters:
		#         Required arguments:
		#                 'url' (type: string) -> The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie.
		#                 'name' (type: string) -> The name of the cookie.
		#                 'value' (type: string) -> The value of the cookie.
		#         Optional arguments:
		#                 'domain' (type: string) -> If omitted, the cookie becomes a host-only cookie.
		#                 'path' (type: string) -> Defaults to the path portion of the url parameter.
		#                 'secure' (type: boolean) -> Defaults ot false.
		#                 'httpOnly' (type: boolean) -> Defaults to false.
		#                 'sameSite' (type: CookieSameSite) -> Defaults to browser default behavior.
		#                 'expirationDate' (type: Timestamp) -> If omitted, the cookie becomes a session cookie.
		# Returns:
		#         'success' (type: boolean) -> True if successfully set cookie.

		# Description: Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

		assert isinstance(cookie, http.cookiejar.Cookie), 'The value passed to `set_cookie` must be an instance of http.cookiejar.Cookie().' + \
			' Passed: %s ("%s").' % (type(cookie), cookie)

		# Yeah, the cookielib stores this attribute as a string, despite it containing a
		# boolean value. No idea why.
		is_http_only = str(cookie.get_nonstandard_attr('httponly', 'False')).lower() == "true"


		# I'm unclear what the "url" field is actually for. A cookie only needs the domain and
		# path component to be fully defined. Considering the API apparently allows the domain and
		# path parameters to be unset, I think it forms a partially redundant, with some
		# strange interactions with mode-changing between host-only and more general
		# cookies depending on what's set where.
		# Anyways, given we need a URL for the API to work properly, we produce a fake
		# host url by building it out of the relevant cookie properties.
		fake_url = urllib.parse.urlunsplit((
				"http" if is_http_only else "https",  # Scheme
				cookie.domain,                        # netloc
				cookie.path,                          # path
				'',                                   # query
				'',                                   # fragment
			))

		params = {
				'url'      : fake_url,

				'name'     : cookie.name,
				'value'    : cookie.value if cookie.value else "",
				'domain'   : cookie.domain,
				'path'     : cookie.path,
				'secure'   : cookie.secure,
				'expires'  : float(cookie.expires) if cookie.expires else float(2**32),

				'httpOnly' : is_http_only,

				# The "sameSite" flag appears to be a chromium-only extension for controlling
				# cookie sending in non-first-party contexts. See:
				# https://bugs.chromium.org/p/chromium/issues/detail?id=459154
				# Anyways, we just use the default here, whatever that is.
				# sameSite       = cookie.xxx
			}

		ret = self.Network_setCookie(**params)

		return ret

	def clear_cookies(self):
		'''
		At this point, this is just a thin shim around the Network_clearBrowserCookies() operation.

		That function postdates the clear_cookies() call here.
		'''
		self.Network_clearBrowserCookies()



	def navigate_to(self, url):
		'''
		Trigger a page navigation to url `url`.

		Note that this is done via javascript injection, and as such results in
		the `referer` header being sent with the url of the network location.

		This is useful when a page's navigation is stateful, or for simple
		cases of referrer spoofing.

		'''

		assert "'" not in url
		return self.__exec_js("window.location.href = '{}'".format(url))

	def get_current_url(self):
		'''
		Probe the remote session for the current window URL.

		This is primarily used to do things like unwrap redirects,
		or circumvent outbound url wrappers.

		'''
		res = self.Page_getNavigationHistory()
		assert 'result' in res
		assert 'currentIndex' in res['result']
		assert 'entries' in res['result']

		return res['result']['entries'][res['result']['currentIndex']]['url']

	def get_page_url_title(self):
		'''
		Get the title and current url from the remote session.

		Return is a 2-tuple: (page_title, page_url).

		'''

		cr_tab_id = self.transport._get_cr_tab_meta_for_key(self.tab_id)['id']
		targets = self.Target_getTargets()

		assert 'result' in targets
		assert 'targetInfos' in targets['result']

		for tgt in targets['result']['targetInfos']:
			if tgt['targetId'] == cr_tab_id:
				# {
				# 	'title': 'Page Title 1',
				# 	'targetId': '9d2c503c-e39e-42cc-b950-96db073918ee',
				# 	'attached': True,
				# 	'url': 'http://localhost:47181/with_title_1',
				# 	'type': 'page'
				# }

				title   = tgt['title']
				cur_url = tgt['url']
				return title, cur_url




	def click_link_containing_url(self, url):
		'''
		TODO

		'''

		# exec_func =

		self.__exec_js("window.location.href = '/test'")

		# js.kCallFunctionScript

		# "window.history.back();"

		# elem = self.find_element("//a".format(url))
		# print(elem)

	def execute_javascript_statement(self, script):
		'''
		Execute a javascript string in the context of the browser tab.
		This only works for simple JS statements. More complex usage should
		be via execute_javascript_function().

		This can also be used to interrogate the JS interpreter, as simply passing
		variable names of interest will return the variable value.
		'''

		ret = self.__exec_js(script=script)
		return ret

	def execute_javascript_function(self, script, args=None):
		'''
		Execute a javascript function in the context of the browser tab.

		The passed script must be a single function definition, which will
		be called via ({script}).apply(null, {args}).
		'''

		ret = self.__exec_js(script=script, should_call=True, args=args)
		return ret

	def find_element(self, search):

		'''
		DOM_performSearch(self, query, includeUserAgentShadowDOM)
		Python Function: DOM_performSearch
		        Domain: DOM
		        Method name: performSearch

		        WARNING: This function is marked 'Experimental'!

		        Parameters:
		                'query' (type: string) -> Plain text or query selector or XPath search query.
		                'includeUserAgentShadowDOM' (type: boolean) -> True to search in user agent shadow DOM.
		        Returns:
		                'searchId' (type: string) -> Unique search session identifier.
		                'resultCount' (type: integer) -> Number of search results.
		        Description: Searches for a given string in the DOM tree. Use <code>getSearchResults</code> to access search results or <code>cancelSearch</code> to end this search session.

		Python Function: DOM_getSearchResults
		        Domain: DOM
		        Method name: getSearchResults

		        WARNING: This function is marked 'Experimental'!

		        Parameters:
		                'searchId' (type: string) -> Unique search session identifier.
		                'fromIndex' (type: integer) -> Start index of the search result to be returned.
		                'toIndex' (type: integer) -> End index of the search result to be returned.
		        Returns:
		                'nodeIds' (type: array) -> Ids of the search result nodes.
		        Description: Returns search results from given <code>fromIndex</code> to given <code>toIndex</code> from the sarch with the given identifier.

		DOM_discardSearchResults(self, searchId)
		Python Function: DOM_discardSearchResults
		        Domain: DOM
		        Method name: discardSearchResults

		        WARNING: This function is marked 'Experimental'!

		        Parameters:
		                'searchId' (type: string) -> Unique search session identifier.
		        No return value.
		        Description: Discards search results from the session with the given id. <code>getSearchResults</code> should no longer be called for that search.
		'''

		res = self.DOM_performSearch(search, includeUserAgentShadowDOM=False)
		assert 'result' in res
		assert 'searchId' in res['result']
		searchid = res['result']['searchId']
		res_cnt  = res['result']['resultCount']
		self.log.info("res -> %s", res)
		self.log.info("searchid -> %s", searchid)

		if res_cnt == 0:
			return []

		items = self.DOM_getSearchResults(searchId=searchid, fromIndex=0, toIndex=res_cnt)

		self.log.info("Results:")
		self.log.info("items -> %s", items)

		assert 'result' in items
		assert 'nodeIds' in items['result']
		node_ids  = items['result']['nodeIds']

		return node_ids


	def click_element(self, contains_url):
		'''

		TODO


		ChromeDriver source for how to click an element:

		Status ExecuteClickElement(Session* session,
		                           WebView* web_view,
		                           const std::string& element_id,
		                           const base::DictionaryValue& params,
		                           std::unique_ptr<base::Value>* value) {
		  std::string tag_name;
		  Status status = GetElementTagName(session, web_view, element_id, &tag_name);
		  if (status.IsError())
		    return status;
		  if (tag_name == "option") {
		    bool is_toggleable;
		    status = IsOptionElementTogglable(
		        session, web_view, element_id, &is_toggleable);
		    if (status.IsError())
		      return status;
		    if (is_toggleable)
		      return ToggleOptionElement(session, web_view, element_id);
		    else
		      return SetOptionElementSelected(session, web_view, element_id, true);
		  } else {
		    WebPoint location;
		    status = GetElementClickableLocation(
		        session, web_view, element_id, &location);
		    if (status.IsError())
		      return status;

		    std::list<MouseEvent> events;
		    events.push_back(
		        MouseEvent(kMovedMouseEventType, kNoneMouseButton,
		                   location.x, location.y, session->sticky_modifiers, 0));
		    events.push_back(
		        MouseEvent(kPressedMouseEventType, kLeftMouseButton,
		                   location.x, location.y, session->sticky_modifiers, 1));
		    events.push_back(
		        MouseEvent(kReleasedMouseEventType, kLeftMouseButton,
		                   location.x, location.y, session->sticky_modifiers, 1));
		    status =
		        web_view->DispatchMouseEvents(events, session->GetCurrentFrameId());
		    if (status.IsOk())
		      session->mouse_position = location;
		    return status;
		  }
		}
		'''

		pass

	def get_unpacked_response_body(self, requestId, mimetype="application/unknown"):
		'''
		Return a unpacked, decoded resposne body from Network_getResponseBody()
		'''
		content = self.Network_getResponseBody(requestId)

		assert 'result' in content
		result = content['result']

		assert 'base64Encoded' in result
		assert 'body' in result

		if result['base64Encoded']:
			content = base64.b64decode(result['body'])
		else:
			content = result['body']

		self.log.info("Navigate complete. Received %s byte response with type %s.", len(content), mimetype)

		return {'binary' : result['base64Encoded'],  'mimetype' : mimetype, 'content' : content}


	def handle_page_location_changed(self, timeout=None):
		'''
		If the chrome tab has internally redirected (generally because jerberscript), this
		will walk the page navigation responses and attempt to fetch the response body for
		the tab's latest location.
		'''

		# In general, this is often called after other mechanisms have confirmed
		# that the tab has already navigated. As such, we want to not wait a while
		# to discover something went wrong, so use a timeout that basically just
		# results in checking the available buffer, and nothing else.
		if not timeout:
			timeout = 0.1

		self.log.debug("We may have redirected. Checking.")

		messages = self.transport.recv_all_filtered(filter_funcs.capture_loading_events, tab_key=self.tab_id)
		if not messages:
			raise ChromeError("Couldn't track redirect! No idea what to do!")

		last_message = messages[-1]
		self.log.info("Probably a redirect! New content url: '%s'", last_message['params']['documentURL'])

		resp = self.transport.recv_filtered(filter_funcs.network_response_recieved_for_url(last_message['params']['documentURL'], last_message['params']['frameId']), tab_key=self.tab_id)
		resp = resp['params']

		ctype = 'application/unknown'

		resp_response = resp['response']

		if 'mimeType' in resp_response:
			ctype = resp_response['mimeType']
		if 'headers' in resp_response and 'content-type' in resp_response['headers']:
			ctype = resp_response['headers']['content-type'].split(";")[0]

		# We assume the last document request was the redirect.
		# This is /probably/ kind of a poor practice, but what the hell.
		# I have no idea what this would do if there are non-html documents (or if that can even happen.)
		return self.get_unpacked_response_body(last_message['params']['requestId'], mimetype=ctype)

	def blocking_navigate_and_get_source(self, url, timeout=DEFAULT_TIMEOUT_SECS):
		'''
		Do a blocking navigate to url `url`, and then extract the
		response body and return that.

		This effectively returns the *unrendered* page content that's sent over the wire. As such,
		if the page does any modification of the contained markup during rendering (via javascript), this
		function will not reflect the changes made by the javascript.

		The rendered page content can be retreived by calling `get_rendered_page_source()`.

		Due to the remote api structure, accessing the raw content after the content has been loaded
		is not possible, so any task requiring the raw content must be careful to request it
		before it actually navigates to said content.

		Return value is a dictionary with two keys:
		{
			'binary' : (boolean, true if content is binary, false if not)
			'content' : (string of bytestring, depending on whether `binary` is true or not)
		}

		'''


		resp = self.blocking_navigate(url, timeout)
		assert 'requestId' in resp
		assert 'response' in resp
		# self.log.debug('blocking_navigate Response %s', pprint.pformat(resp))

		ctype = 'application/unknown'

		resp_response = resp['response']

		if 'mimeType' in resp_response:
			ctype = resp_response['mimeType']
		if 'headers' in resp_response and 'content-type' in resp_response['headers']:
			ctype = resp_response['headers']['content-type'].split(";")[0]

		self.log.debug("Trying to get response body")
		try:
			ret = self.get_unpacked_response_body(resp['requestId'], mimetype=ctype)
		except ChromeError:
			ret = self.handle_page_location_changed(timeout)

		return ret


	def get_rendered_page_source(self, dom_idle_requirement_secs=3, max_wait_timeout=30):
		'''
		Get the HTML markup for the current page.

		This is done by looking up the root DOM node, and then requesting the outer HTML
		for that node ID.

		This calls return will reflect any modifications made by javascript to the
		page. For unmodified content, use `blocking_navigate_and_get_source()`

		dom_idle_requirement_secs specifies the period of time for which there must have been no
		DOM modifications before treating the rendered output as "final". This call will therefore block for
		at least dom_idle_requirement_secs seconds.
		'''

		# There are a bunch of events which generally indicate a page is still doing *things*.
		# I have some concern about how this will handle things like advertisements, which
		# basically load crap forever. That's why we have the max_wait_timeout.
		target_events = [
			"Page.frameResized",
			"Page.frameStartedLoading",
			"Page.frameNavigated",
			"Page.frameAttached",
			"Page.frameStoppedLoading",
			"Page.frameScheduledNavigation",
			"Page.domContentEventFired",
			"Page.frameClearedScheduledNavigation",
			"Page.loadEventFired",
			"DOM.documentUpdated",
			"DOM.childNodeInserted",
			"DOM.childNodeRemoved",
			"DOM.childNodeCountUpdated",
		]

		start_time = time.time()
		try:
			while 1:
				if time.time() - start_time > max_wait_timeout:
					self.log.debug("Page was not idle after waiting %s seconds. Giving up and extracting content now.", max_wait_timeout)
				self.transport.recv_filtered(
						filter_funcs.wait_for_methods(target_events),
						tab_key = self.tab_id,
						timeout = dom_idle_requirement_secs
					)

		except ChromeResponseNotReceived:
			# We timed out, the DOM is probably idle.
			pass

		root_node_id = self.get_dom_root_id()

		# Use that to get the HTML for the specified node
		response = self.DOM_getOuterHTML(nodeId=root_node_id)

		assert 'result' in response
		assert 'outerHTML' in response['result']
		return response['result']['outerHTML']


	def take_screeshot(self):
		'''
		Take a screenshot of the virtual viewport content.

		Return value is a png image as a bytestring.
		'''
		resp = self.Page_captureScreenshot()
		assert 'result' in resp
		assert 'data' in resp['result']
		imgdat = base64.b64decode(resp['result']['data'])
		return imgdat


	def blocking_navigate(self, url, timeout=DEFAULT_TIMEOUT_SECS):
		'''
		Do a blocking navigate to url `url`.

		This function triggers a navigation, and then waits for the browser
		to claim the page has finished loading.

		Roughly, this corresponds to the javascript `DOMContentLoaded` event,
		meaning the dom for the page is ready.

		Internals:

		A navigation command results in a sequence of events:

		 - Page.frameStartedLoading" (with frameid)
		 - Page.frameStoppedLoading" (with frameid)
		 - Page.loadEventFired" (not attached to an ID)

		Therefore, this call triggers a navigation option,
		and then waits for the expected set of response event messages.

		'''

		self.transport.flush(tab_key=self.tab_id)

		self.log.debug("Blocking navigate to URL: '%s'", url)
		ret = self.Page_navigate(url = url)

		assert("result"   in ret),           "Missing return content"
		assert("frameId"  in ret['result']), "Missing 'frameId' in return content"
		assert("loaderId" in ret['result']), "Missing 'loaderId' in return content"

		expected_id = ret['result']['frameId']
		loader_id   = ret['result']['loaderId']

		try:
			self.log.debug("Waiting for frame navigated command response.")
			self.transport.recv_filtered(filter_funcs.check_frame_navigated_command(expected_id), tab_key=self.tab_id, timeout=timeout)
			self.log.debug("Waiting for frameStartedLoading response.")
			self.transport.recv_filtered(filter_funcs.check_frame_load_command("Page.frameStartedLoading"), tab_key=self.tab_id, timeout=timeout)
			self.log.debug("Waiting for frameStoppedLoading response.")
			self.transport.recv_filtered(filter_funcs.check_frame_load_command("Page.frameStoppedLoading"), tab_key=self.tab_id, timeout=timeout)
			# self.transport.recv_filtered(check_load_event_fired, tab_key=self.tab_id, timeout=timeout)

			self.log.debug("Waiting for responseReceived response.")
			resp = self.transport.recv_filtered(filter_funcs.network_response_recieved_for_url(url=None, expected_id=expected_id), tab_key=self.tab_id, timeout=timeout)

			if resp is None:
				raise ChromeNavigateTimedOut("Blocking navigate timed out!")

			return resp['params']
		# The `Page.frameNavigated ` event does not get fired for non-markup responses.
		# Therefore, if we timeout on waiting for that, check to see if we received a binary response.
		except ChromeResponseNotReceived:
			# So this is basically broken, fix is https://bugs.chromium.org/p/chromium/issues/detail?id=831887
			# but that bug report isn't fixed yet.
			# Siiiigh.
			self.log.warning("Failed to receive expected response to navigate command. Checking if response is a binary object.")
			resp = self.transport.recv_filtered(
				keycheck = filter_funcs.check_frame_loader_command(
						method_name = "Network.responseReceived",
						loader_id   = loader_id
					),
				tab_key  = self.tab_id,
				timeout  = timeout)

			return resp['params']

	def new_tab(self, *args, **kwargs):

		tab = super().new_tab(*args, **kwargs)

		for script in self.__new_tab_scripts:
			tab.Page_addScriptToEvaluateOnNewDocument(script)
		return tab


	def install_evasions(self):
		'''
		Load headless detection evasions from the puppeteer-extra repository (
		https://github.com/berstend/puppeteer-extra/tree/master/packages/puppeteer-extra-plugin-stealth/evasions).

		'''
		from ChromeController.resources import evasions

		scripts = evasions.load_evasions()


		self.__new_tab_scripts.extend(scripts.values())

		for script, contents in scripts.items():

			print("Loading '%s'" % script)
			ret = self.Page_addScriptToEvaluateOnNewDocument(contents)
			pprint.pprint(ret)

			ret2 = self.execute_javascript_function("function()" + contents)
			pprint.pprint(ret2)

			# ret3 = self.execute_javascript_statement(contents)
			# pprint.pprint(ret3)






	def scroll_page(self, scroll_y_delta, scroll_x_delta=0, mouse_pos_x=10, mouse_pos_y=10):
		'''
		Inject a synthezised mouse scroll event into the page.

		Positive Y scroll means "down" on the page. The mouse position is where the
		virtual mouse pointer is placed when it emits the scroll event.

		Note that this returns immediately, and the browser takes a short period of time
		to actually perform the scroll (and for any onscroll() events to be triggered.)

		Additionally, scroll events are delta relatve to the current viewport. Repeated
		calls with the same scroll delta will incrementally move the viewport in the
		chosen direction.
		'''

		self.Input_dispatchMouseEvent(
				type        = 'mouseWheel',
				x           = mouse_pos_x,
				y           = mouse_pos_y,
				deltaX      = scroll_x_delta,
				deltaY      = scroll_y_delta,
				pointerType = 'mouse',
			)


	def get_dom_root_id(self):
		'''
		Get the NodeID for the DOM Root.

		This assumes the page has fully loaded.
		'''



		# We have to find the DOM root node ID
		dom_attr = self.DOM_getDocument(depth=-1, pierce=False)
		assert 'result' in dom_attr
		assert 'root' in dom_attr['result']
		assert 'nodeId' in dom_attr['result']['root']

		# Now, we have the root node ID.
		root_node_id = dom_attr['result']['root']['nodeId']

		return root_node_id

	def get_dom_item_center_coords(self, dom_object_id):
		'''
		Given a DOM object ID, scroll it into view (if needed), and
		return it's center point coordinates.
		'''

		# Scroll the dom object into view
		self.DOM_scrollIntoViewIfNeeded(nodeId=dom_object_id)


		res = self.DOM_getContentQuads(nodeId=dom_object_id)

		assert 'result' in res
		assert 'quads' in res['result']

		quads = res['result']['quads']

		if not quads:
			return []

		p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y = quads[0]


		max_x = max([p1_x, p2_x, p3_x, p4_x])
		max_y = max([p1_y, p2_y, p3_y, p4_y])

		min_x = min([p1_x, p2_x, p3_x, p4_x])
		min_y = min([p1_y, p2_y, p3_y, p4_y])

		half_x = (max_x - min_x) / 2
		half_y = (max_y - min_y) / 2

		return min_x + half_x, min_y + half_y


	def click_item_at_coords(self, x_pos, y_pos):
		'''
		Use the input api to generate a mouse click event at the specified coordinates.

		Note that if this generates a navigation event, it will not wait for that navigation
		to complete before returning.

		'''

		self.Input_dispatchMouseEvent(
			type='mousePressed',
			x = x_pos,
			y = y_pos,
			button = 'left',
			clickCount=1,
		)
		self.Input_dispatchMouseEvent(
			type='mouseReleased',
			x = x_pos,
			y = y_pos,
			button = 'left',
			clickCount=1,
		)

