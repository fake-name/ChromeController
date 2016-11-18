
import distutils.spawn
import os.path
import sys
import subprocess
import pprint
import base64
import signal
import pprint
import time
import requests.exceptions

from .Generator import gen

CromeRemoteDebugInterfaceBase = gen.get_class_def()


# [
# 	'Accessibility_getPartialAXTree',
# 	'Animation_disable',
# 	'Animation_enable',
# 	'Animation_getCurrentTime',
# 	'Animation_getPlaybackRate',
# 	'Animation_releaseAnimations',
# 	'Animation_resolveAnimation',
# 	'Animation_seekAnimations',
# 	'Animation_setPaused',
# 	'Animation_setPlaybackRate',
# 	'Animation_setTiming',
# 	'ApplicationCache_enable',
# 	'ApplicationCache_getApplicationCacheForFrame',
# 	'ApplicationCache_getFramesWithManifests',
# 	'ApplicationCache_getManifestForFrame',
# 	'CSS_addRule',
# 	'CSS_collectClassNames',
# 	'CSS_createStyleSheet',
# 	'CSS_disable',
# 	'CSS_enable',
# 	'CSS_forcePseudoState',
# 	'CSS_getBackgroundColors',
# 	'CSS_getComputedStyleForNode',
# 	'CSS_getInlineStylesForNode',
# 	'CSS_getLayoutTreeAndStyles',
# 	'CSS_getMatchedStylesForNode',
# 	'CSS_getMediaQueries',
# 	'CSS_getPlatformFontsForNode',
# 	'CSS_getStyleSheetText',
# 	'CSS_setEffectivePropertyValueForNode',
# 	'CSS_setKeyframeKey',
# 	'CSS_setMediaText',
# 	'CSS_setRuleSelector',
# 	'CSS_setStyleSheetText',
# 	'CSS_setStyleTexts',
# 	'CSS_startRuleUsageTracking',
# 	'CSS_stopRuleUsageTracking',
# 	'CacheStorage_deleteCache',
# 	'CacheStorage_deleteEntry',
# 	'CacheStorage_requestCacheNames',
# 	'CacheStorage_requestEntries',
# 	'DOMDebugger_getEventListeners',
# 	'DOMDebugger_removeDOMBreakpoint',
# 	'DOMDebugger_removeEventListenerBreakpoint',
# 	'DOMDebugger_removeInstrumentationBreakpoint',
# 	'DOMDebugger_removeXHRBreakpoint',
# 	'DOMDebugger_setDOMBreakpoint',
# 	'DOMDebugger_setEventListenerBreakpoint',
# 	'DOMDebugger_setInstrumentationBreakpoint',
# 	'DOMDebugger_setXHRBreakpoint',
# 	'DOMStorage_disable',
# 	'DOMStorage_enable',
# 	'DOMStorage_getDOMStorageItems',
# 	'DOMStorage_removeDOMStorageItem',
# 	'DOMStorage_setDOMStorageItem',
# 	'DOM_collectClassNamesFromSubtree',
# 	'DOM_copyTo',
# 	'DOM_disable',
# 	'DOM_discardSearchResults',
# 	'DOM_enable',
# 	'DOM_focus',
# 	'DOM_getAttributes',
# 	'DOM_getBoxModel',
# 	'DOM_getDocument',
# 	'DOM_getHighlightObjectForTest',
# 	'DOM_getNodeForLocation',
# 	'DOM_getOuterHTML',
# 	'DOM_getRelayoutBoundary',
# 	'DOM_getSearchResults',
# 	'DOM_hideHighlight',
# 	'DOM_highlightFrame',
# 	'DOM_highlightNode',
# 	'DOM_highlightQuad',
# 	'DOM_highlightRect',
# 	'DOM_markUndoableState',
# 	'DOM_moveTo',
# 	'DOM_performSearch',
# 	'DOM_pushNodeByPathToFrontend',
# 	'DOM_pushNodesByBackendIdsToFrontend',
# 	'DOM_querySelector',
# 	'DOM_querySelectorAll',
# 	'DOM_redo',
# 	'DOM_removeAttribute',
# 	'DOM_removeNode',
# 	'DOM_requestChildNodes',
# 	'DOM_requestNode',
# 	'DOM_resolveNode',
# 	'DOM_setAttributeValue',
# 	'DOM_setAttributesAsText',
# 	'DOM_setFileInputFiles',
# 	'DOM_setInspectMode',
# 	'DOM_setInspectedNode',
# 	'DOM_setNodeName',
# 	'DOM_setNodeValue',
# 	'DOM_setOuterHTML',
# 	'DOM_undo',
# 	'Database_disable',
# 	'Database_enable',
# 	'Database_executeSQL',
# 	'Database_getDatabaseTableNames',
# 	'DeviceOrientation_clearDeviceOrientationOverride',
# 	'DeviceOrientation_setDeviceOrientationOverride',
# 	'Emulation_canEmulate',
# 	'Emulation_clearDeviceMetricsOverride',
# 	'Emulation_clearGeolocationOverride',
# 	'Emulation_forceViewport',
# 	'Emulation_resetPageScaleFactor',
# 	'Emulation_resetViewport',
# 	'Emulation_setCPUThrottlingRate',
# 	'Emulation_setDeviceMetricsOverride',
# 	'Emulation_setEmulatedMedia',
# 	'Emulation_setGeolocationOverride',
# 	'Emulation_setPageScaleFactor',
# 	'Emulation_setScriptExecutionDisabled',
# 	'Emulation_setTouchEmulationEnabled',
# 	'Emulation_setVirtualTimePolicy',
# 	'Emulation_setVisibleSize',
# 	'IO_close',
# 	'IO_read',
# 	'IndexedDB_clearObjectStore',
# 	'IndexedDB_disable',
# 	'IndexedDB_enable',
# 	'IndexedDB_requestData',
# 	'IndexedDB_requestDatabase',
# 	'IndexedDB_requestDatabaseNames',
# 	'Input_dispatchKeyEvent',
# 	'Input_dispatchMouseEvent',
# 	'Input_dispatchTouchEvent',
# 	'Input_emulateTouchFromMouseEvent',
# 	'Input_synthesizePinchGesture',
# 	'Input_synthesizeScrollGesture',
# 	'Input_synthesizeTapGesture',
# 	'Inspector_disable',
# 	'Inspector_enable',
# 	'LayerTree_compositingReasons',
# 	'LayerTree_disable',
# 	'LayerTree_enable',
# 	'LayerTree_loadSnapshot',
# 	'LayerTree_makeSnapshot',
# 	'LayerTree_profileSnapshot',
# 	'LayerTree_releaseSnapshot',
# 	'LayerTree_replaySnapshot',
# 	'LayerTree_snapshotCommandLog',
# 	'Log_clear',
# 	'Log_disable',
# 	'Log_enable',
# 	'Log_startViolationsReport',
# 	'Log_stopViolationsReport',
# 	'Memory_getDOMCounters',
# 	'Memory_setPressureNotificationsSuppressed',
# 	'Memory_simulatePressureNotification',
# 	'Network_addBlockedURL',
# 	'Network_canClearBrowserCache',
# 	'Network_canClearBrowserCookies',
# 	'Network_canEmulateNetworkConditions',
# 	'Network_clearBrowserCache',
# 	'Network_clearBrowserCookies',
# 	'Network_deleteCookie',
# 	'Network_disable',
# 	'Network_emulateNetworkConditions',
# 	'Network_enable',
# 	'Network_getCertificate',
# 	'Network_getCookies',
# 	'Network_getResponseBody',
# 	'Network_removeBlockedURL',
# 	'Network_replayXHR',
# 	'Network_setBypassServiceWorker',
# 	'Network_setCacheDisabled',
# 	'Network_setCookie',
# 	'Network_setDataSizeLimitsForTest',
# 	'Network_setExtraHTTPHeaders',
# 	'Network_setMonitoringXHREnabled',
# 	'Network_setUserAgentOverride',
# 	'Page_addScriptToEvaluateOnLoad',
# 	'Page_captureScreenshot',
# 	'Page_clearDeviceMetricsOverride',
# 	'Page_clearDeviceOrientationOverride',
# 	'Page_clearGeolocationOverride',
# 	'Page_configureOverlay',
# 	'Page_deleteCookie',
# 	'Page_disable',
# 	'Page_enable',
# 	'Page_getAppManifest',
# 	'Page_getCookies',
# 	'Page_getLayoutMetrics',
# 	'Page_getNavigationHistory',
# 	'Page_getResourceContent',
# 	'Page_getResourceTree',
# 	'Page_handleJavaScriptDialog',
# 	'Page_navigate',
# 	'Page_navigateToHistoryEntry',
# 	'Page_processNavigation',
# 	'Page_reload',
# 	'Page_removeScriptToEvaluateOnLoad',
# 	'Page_requestAppBanner',
# 	'Page_screencastFrameAck',
# 	'Page_searchInResource',
# 	'Page_setAutoAttachToCreatedPages',
# 	'Page_setColorPickerEnabled',
# 	'Page_setControlNavigations',
# 	'Page_setDeviceMetricsOverride',
# 	'Page_setDeviceOrientationOverride',
# 	'Page_setDocumentContent',
# 	'Page_setGeolocationOverride',
# 	'Page_setTouchEmulationEnabled',
# 	'Page_startScreencast',
# 	'Page_stopScreencast',
# 	'Rendering_setShowDebugBorders',
# 	'Rendering_setShowFPSCounter',
# 	'Rendering_setShowPaintRects',
# 	'Rendering_setShowScrollBottleneckRects',
# 	'Rendering_setShowViewportSizeOnResize',
# 	'Security_disable',
# 	'Security_enable',
# 	'Security_showCertificateViewer',
# 	'ServiceWorker_deliverPushMessage',
# 	'ServiceWorker_disable',
# 	'ServiceWorker_dispatchSyncEvent',
# 	'ServiceWorker_enable',
# 	'ServiceWorker_inspectWorker',
# 	'ServiceWorker_setForceUpdateOnPageLoad',
# 	'ServiceWorker_skipWaiting',
# 	'ServiceWorker_startWorker',
# 	'ServiceWorker_stopWorker',
# 	'ServiceWorker_unregister',
# 	'ServiceWorker_updateRegistration',
# 	'Storage_clearDataForOrigin',
# 	'SystemInfo_getInfo',
# 	'Target_activateTarget',
# 	'Target_attachToTarget',
# 	'Target_closeTarget',
# 	'Target_createBrowserContext',
# 	'Target_createTarget',
# 	'Target_detachFromTarget',
# 	'Target_disposeBrowserContext',
# 	'Target_getTargetInfo',
# 	'Target_getTargets',
# 	'Target_sendMessageToTarget',
# 	'Target_setAttachToFrames',
# 	'Target_setAutoAttach',
# 	'Target_setDiscoverTargets',
# 	'Target_setRemoteLocations',
# 	'Tethering_bind',
# 	'Tethering_unbind',
# 	'Tracing_end',
# 	'Tracing_getCategories',
# 	'Tracing_recordClockSyncMarker',
# 	'Tracing_requestMemoryDump',
# 	'Tracing_start',
# 	'_ChromeInterface__check_ret',
# 	'__class__',
# 	'__del__',
# 	'__delattr__',
# 	'__dict__',
# 	'__dir__',
# 	'__doc__',
# 	'__eq__',
# 	'__format__',
# 	'__ge__',
# 	'__getattribute__',
# 	'__gt__',
# 	'__hash__',
# 	'__init__',
# 	'__le__',
# 	'__lt__',
# 	'__module__',
# 	'__ne__',
# 	'__new__',
# 	'__reduce__',
# 	'__reduce_ex__',
# 	'__repr__',
# 	'__setattr__',
# 	'__sizeof__',
# 	'__str__',
# 	'__subclasshook__',
# 	'__weakref__',
# 	'blocking_navigate',
# 	'close',
# 	'cr_proc',
# 	'drain_transport',
# 	'set_headers',
# 	'set_user_agent_string',
# 	'set_viewport_size',
# 	'synchronous_command',
# 	'take_screeshot',
# 	'transport'
# ]


class CromeRemoteDebugInterface(CromeRemoteDebugInterfaceBase):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		resp1 = self.Page_enable()
		resp2 = self.DOM_enable()

		# I haven't worked out optionally ignorable arguments for this, yet
		resp3 = self.synchronous_command("Network.enable")


	def set_viewport_size(self, x_pix, y_pix):
		'''
		Set the emulated viewport size to `x_pix` by `y_pix`

		'''
		ret = self.Emulation_setVisibleSize(width = int(x_pix), height = int(y_pix))

		# Command has an empty return
		return ret


	def set_user_agent_string(self, ua_string):
		'''
		Override the user-agent string for the remote browser, setting it to `ua_string`.
		'''
		# "name": "setUserAgentOverride",
		# "description": "Allows overriding user agent with the given string.",
		# "parameters": [
		#     { "name": "userAgent", "type": "string", "description": "User agent to use." }

		ret = self.Network_setUserAgentOverride(userAgent = ua_string)

		# Command has an empty return
		return ret

	def set_headers(self, header_dict):
		'''
		Update or add a set of headers to the remote browser.

		Passed headers should be a dictionary of key-value items, where the key is the name
		of the header, and value is the header content.

		'''
		# {
		#     "name": "setExtraHTTPHeaders",
		#     "description": "Specifies whether to always send extra HTTP headers with the requests from this page.",
		#     "parameters": [
		#         { "name": "headers", "$ref": "Headers", "description": "Map with extra HTTP headers." }
		#     ]
		# },

		ret = self.Network_setExtraHTTPHeaders(headers = header_dict)
		# Command has an empty return

		return ret

	# Interact with httplib.cookie instances
	def set_cookie(self, cookie):
		'''
		TODO
		'''
		pass

	def get_cookie(self):
		'''
		TODO
		'''
		pass

	def click_link_containing_url(self, url):
		elem = self.find_element("//a".format(url))
		print(elem)

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

		res = self.DOM_performSearch(search, False)
		assert 'result' in res
		assert 'searchId' in res['result']
		searchid = res['result']['searchId']
		res_cnt  = res['result']['resultCount']
		print(res)
		print(searchid)

		if res_cnt == 0:
			return None

		items = self.DOM_getSearchResults(searchId=searchid, fromIndex=0, toIndex=res_cnt)

		print("Results:")
		print(items)

		# DOM_getSearchResults


	def click_element(self, contains_url):
		'''
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







	def blocking_navigate_and_get_source(self, url):
		'''
		Do a blocking navigate to url `url`, and then extract the
		response body and return that.

		This effectively returns the *unrendered* page content that's sent over the wire. As such,
		if the page does any modification of the contained markup during rendering (via javascript), this
		function will not reflect the changes made by the javascript.

		The rendered page content can be retreived by calling `get_rendered_page_source()`.

		Return value is a dictionary with two keys:
		{
			'binary' : (boolean, true if content is binary, false if not)
			'content' : (string of bytestring, depending on whether `binary` is true or not)
		}

		'''

		resp = self.blocking_navigate(url)
		assert 'requestId' in resp
		print('resp', resp)

		content = self.Network_getResponseBody(resp['requestId'])
		assert 'result' in content
		result = content['result']

		assert 'base64Encoded' in result
		assert 'body' in result

		if result['base64Encoded']:
			return {'binary' : True,  'content' : base64.b64decode(result['body'])}
		else:
			return {'binary' : False, 'content' : result['body']}


	def get_rendered_page_source(self):
		'''
		Get the HTML markup for the current page.

		This is done by looking up the root DOM node, and then requesting the outer HTML
		for that node ID.
		'''

		dom_attr = self.DOM_getDocument(depth=1, traverseFrames=False)
		assert 'result' in dom_attr
		assert 'root' in dom_attr['result']
		assert 'nodeId' in dom_attr['result']['root']

		# Now, we have the root node ID.
		root_node_id = dom_attr['result']['root']['nodeId']

		ret = self.DOM_getOuterHTML(nodeId=root_node_id)
		return ret


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


	def blocking_navigate(self, url, timeout=30):
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

		Therefore, we trigger a navigation option, and then wait for the expected set of results.


		'''
		ret = self.Page_navigate(url = url)

		assert("result" in ret), "Missing return content"
		assert("frameId" in ret['result']), "Missing 'frameId' in return content"

		expected_id = ret['result']['frameId']

		def check_frame_navigated(message):
			if "method" not in message:
				return False
			if message['method'] != "Page.frameNavigated":
				return False
			if 'params' not in message:
				return False
			params = message['params']
			if 'frame' not in params:
				return False
			frame = params['frame']
			if 'id' in frame:
				ret = frame['id'] == expected_id
				# print('check_frame_navigated', message)
				return ret
			return False

		def check_frame_load_command(method_name):
			def frame_loading_tracker(message):
				if "method" not in message:
					return False
				if message['method'] != method_name:
					return False
				if 'params' not in message:
					return False
				params = message['params']
				if 'frameId' not in params:
					return False
				if 'frameId' in params:
					ret = params['frameId'] == expected_id
					# print("frame_loading_tracker", message)
					return ret
				return False
			return frame_loading_tracker

		def check_load_event_fired(message):
				if "method" not in message:
					return False
				if message['method'] == 'Page.loadEventFired':
					# print("check_load_event_fired", message)
					return True
				return False


		def network_response_recieved_for_url(url):
			def network_response_recieved_tracker(message):
				if "method" not in message:
					return False
				if message['method'] != 'Network.responseReceived':
					return False
				if 'params' not in message:
					return False
				params = message['params']
				if 'frameId' not in params:
					return False
				if 'frameId' in params:
					if params['frameId'] == expected_id and 'response' in params:
						response = params['response']
						if 'url' in response:
							return url in response['url']
				return False
			return network_response_recieved_tracker


		self.transport.recv_filtered(check_frame_navigated)

		self.transport.recv_filtered(check_frame_load_command("Page.frameStartedLoading"))
		self.transport.recv_filtered(check_frame_load_command("Page.frameStoppedLoading"))
		self.transport.recv_filtered(check_load_event_fired)

		resp = self.transport.recv_filtered(network_response_recieved_for_url(url))

		return resp['params']

