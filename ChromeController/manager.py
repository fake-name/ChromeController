
import distutils.spawn
import os.path
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
	pass
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		resp1 = self.Page_enable()
		resp2 = self.DOM_enable()
		# I haven't worked out optionally ignorable arguments for this, yet
		resp3 = self.synchronous_command("Network.enable", {})

		print(resp1)
		print(resp2)
		print(resp3)



	def set_viewport_size(self, x_pix, y_pix):
		ret = self.Emulation_setVisibleSize(width = int(x_pix), height = int(y_pix))

		# Command has an empty return
		return ret


	def set_user_agent_string(self, ua_string):
		# "name": "setUserAgentOverride",
		# "description": "Allows overriding user agent with the given string.",
		# "parameters": [
		#     { "name": "userAgent", "type": "string", "description": "User agent to use." }

		ret = self.Network_setUserAgentOverride(userAgent = ua_string)

		# Command has an empty return
		return ret

	def set_headers(self, header_dict):
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
		pass

	def get_cookie(self):
		pass

	def take_screeshot(self):
		resp = self.Page_captureScreenshot()
		assert 'result' in resp
		assert 'data' in resp['result']
		imgdat = base64.b64decode(resp['result']['data'])
		return imgdat


	def blocking_navigate(self, url, timeout=30):
		'''
		A navigation command results in a sequence of events:

		 - Page.frameStartedLoading" (with frameid)
		 - Page.frameStoppedLoading" (with frameid)
		 - Page.frameStoppedLoading" (not attached to an ID)

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
				return frame['id'] == expected_id
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
					return params['frameId'] == expected_id
				return False
			return frame_loading_tracker

		def check_load_event_fired(message):
				if "method" not in message:
					return False
				if message['method'] == 'Page.loadEventFired':
					return True
				return False

		frame_navigated = self.transport.recv_filtered(check_frame_navigated)

		frame_mav_1 = self.transport.recv_filtered(check_frame_load_command("Page.frameStartedLoading"))
		frame_mav_2 = self.transport.recv_filtered(check_frame_load_command("Page.frameStoppedLoading"))
		frame_mav_2 = self.transport.recv_filtered(check_load_event_fired)

		print(frame_navigated)
		print(frame_mav_1)
		print(frame_mav_2)

		print("Navigation completed!")


		pass
