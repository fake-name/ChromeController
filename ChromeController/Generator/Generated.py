from ChromeController.transport import ChromeExecutionManager
from ChromeController.manager_base import ChromeInterface


class ChromeRemoteDebugInterface(ChromeInterface):
	"""

	"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def Inspector_enable(self):
		"""
		Function path: Inspector.enable
			Domain: Inspector
			Method name: enable
		
			No return value.
		
			Description: Enables inspector domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Inspector.enable')
		return subdom_funcs

	def Inspector_disable(self):
		"""
		Function path: Inspector.disable
			Domain: Inspector
			Method name: disable
		
			No return value.
		
			Description: Disables inspector domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Inspector.disable')
		return subdom_funcs

	def Memory_getDOMCounters(self):
		"""
		Function path: Memory.getDOMCounters
			Domain: Memory
			Method name: getDOMCounters
		
			Returns:
				'documents' (type: integer) -> No description
				'nodes' (type: integer) -> No description
				'jsEventListeners' (type: integer) -> No description
		
		"""
		subdom_funcs = self.synchronous_command('Memory.getDOMCounters')
		return subdom_funcs

	def Memory_prepareForLeakDetection(self):
		"""
		Function path: Memory.prepareForLeakDetection
			Domain: Memory
			Method name: prepareForLeakDetection
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('Memory.prepareForLeakDetection')
		return subdom_funcs

	def Memory_setPressureNotificationsSuppressed(self, suppressed):
		"""
		Function path: Memory.setPressureNotificationsSuppressed
			Domain: Memory
			Method name: setPressureNotificationsSuppressed
		
			Parameters:
				Required arguments:
					'suppressed' (type: boolean) -> If true, memory pressure notifications will be suppressed.
			No return value.
		
			Description: Enable/disable suppressing memory pressure notifications in all processes.
		"""
		assert isinstance(suppressed, (bool,)
		    ), "Argument 'suppressed' must be of type '['bool']'. Received type: '%s'" % type(
		    suppressed)
		subdom_funcs = self.synchronous_command(
		    'Memory.setPressureNotificationsSuppressed', suppressed=suppressed)
		return subdom_funcs

	def Memory_simulatePressureNotification(self, level):
		"""
		Function path: Memory.simulatePressureNotification
			Domain: Memory
			Method name: simulatePressureNotification
		
			Parameters:
				Required arguments:
					'level' (type: PressureLevel) -> Memory pressure level of the notification.
			No return value.
		
			Description: Simulate a memory pressure notification in all processes.
		"""
		subdom_funcs = self.synchronous_command('Memory.simulatePressureNotification'
		    , level=level)
		return subdom_funcs

	def Performance_enable(self):
		"""
		Function path: Performance.enable
			Domain: Performance
			Method name: enable
		
			No return value.
		
			Description: Enable collecting and reporting metrics.
		"""
		subdom_funcs = self.synchronous_command('Performance.enable')
		return subdom_funcs

	def Performance_disable(self):
		"""
		Function path: Performance.disable
			Domain: Performance
			Method name: disable
		
			No return value.
		
			Description: Disable collecting and reporting metrics.
		"""
		subdom_funcs = self.synchronous_command('Performance.disable')
		return subdom_funcs

	def Performance_getMetrics(self):
		"""
		Function path: Performance.getMetrics
			Domain: Performance
			Method name: getMetrics
		
			Returns:
				'metrics' (type: array) -> Current values for run-time metrics.
		
			Description: Retrieve current values of run-time metrics.
		"""
		subdom_funcs = self.synchronous_command('Performance.getMetrics')
		return subdom_funcs

	def Page_enable(self):
		"""
		Function path: Page.enable
			Domain: Page
			Method name: enable
		
			No return value.
		
			Description: Enables page domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Page.enable')
		return subdom_funcs

	def Page_disable(self):
		"""
		Function path: Page.disable
			Domain: Page
			Method name: disable
		
			No return value.
		
			Description: Disables page domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Page.disable')
		return subdom_funcs

	def Page_addScriptToEvaluateOnLoad(self, scriptSource):
		"""
		Function path: Page.addScriptToEvaluateOnLoad
			Domain: Page
			Method name: addScriptToEvaluateOnLoad
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'scriptSource' (type: string) -> No description
			Returns:
				'identifier' (type: ScriptIdentifier) -> Identifier of the added script.
		
			Description: Deprecated, please use addScriptToEvaluateOnNewDocument instead.
		"""
		assert isinstance(scriptSource, (str,)
		    ), "Argument 'scriptSource' must be of type '['str']'. Received type: '%s'" % type(
		    scriptSource)
		subdom_funcs = self.synchronous_command('Page.addScriptToEvaluateOnLoad',
		    scriptSource=scriptSource)
		return subdom_funcs

	def Page_removeScriptToEvaluateOnLoad(self, identifier):
		"""
		Function path: Page.removeScriptToEvaluateOnLoad
			Domain: Page
			Method name: removeScriptToEvaluateOnLoad
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'identifier' (type: ScriptIdentifier) -> No description
			No return value.
		
			Description: Deprecated, please use removeScriptToEvaluateOnNewDocument instead.
		"""
		subdom_funcs = self.synchronous_command('Page.removeScriptToEvaluateOnLoad',
		    identifier=identifier)
		return subdom_funcs

	def Page_addScriptToEvaluateOnNewDocument(self, source):
		"""
		Function path: Page.addScriptToEvaluateOnNewDocument
			Domain: Page
			Method name: addScriptToEvaluateOnNewDocument
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'source' (type: string) -> No description
			Returns:
				'identifier' (type: ScriptIdentifier) -> Identifier of the added script.
		
			Description: Evaluates given script in every frame upon creation (before loading frame's scripts).
		"""
		assert isinstance(source, (str,)
		    ), "Argument 'source' must be of type '['str']'. Received type: '%s'" % type(
		    source)
		subdom_funcs = self.synchronous_command(
		    'Page.addScriptToEvaluateOnNewDocument', source=source)
		return subdom_funcs

	def Page_removeScriptToEvaluateOnNewDocument(self, identifier):
		"""
		Function path: Page.removeScriptToEvaluateOnNewDocument
			Domain: Page
			Method name: removeScriptToEvaluateOnNewDocument
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'identifier' (type: ScriptIdentifier) -> No description
			No return value.
		
			Description: Removes given script from the list.
		"""
		subdom_funcs = self.synchronous_command(
		    'Page.removeScriptToEvaluateOnNewDocument', identifier=identifier)
		return subdom_funcs

	def Page_setAutoAttachToCreatedPages(self, autoAttach):
		"""
		Function path: Page.setAutoAttachToCreatedPages
			Domain: Page
			Method name: setAutoAttachToCreatedPages
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'autoAttach' (type: boolean) -> If true, browser will open a new inspector window for every page created from this one.
			No return value.
		
			Description: Controls whether browser will open a new inspector window for connected pages.
		"""
		assert isinstance(autoAttach, (bool,)
		    ), "Argument 'autoAttach' must be of type '['bool']'. Received type: '%s'" % type(
		    autoAttach)
		subdom_funcs = self.synchronous_command('Page.setAutoAttachToCreatedPages',
		    autoAttach=autoAttach)
		return subdom_funcs

	def Page_reload(self, **kwargs):
		"""
		Function path: Page.reload
			Domain: Page
			Method name: reload
		
			Parameters:
				Optional arguments:
					'ignoreCache' (type: boolean) -> If true, browser cache is ignored (as if the user pressed Shift+refresh).
					'scriptToEvaluateOnLoad' (type: string) -> If set, the script will be injected into all frames of the inspected page after reload.
			No return value.
		
			Description: Reloads given page optionally ignoring the cache.
		"""
		if 'ignoreCache' in kwargs:
			assert isinstance(kwargs['ignoreCache'], (bool,)
			    ), "Optional argument 'ignoreCache' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['ignoreCache'])
		if 'scriptToEvaluateOnLoad' in kwargs:
			assert isinstance(kwargs['scriptToEvaluateOnLoad'], (str,)
			    ), "Optional argument 'scriptToEvaluateOnLoad' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['scriptToEvaluateOnLoad'])
		expected = ['ignoreCache', 'scriptToEvaluateOnLoad']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['ignoreCache', 'scriptToEvaluateOnLoad']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.reload', **kwargs)
		return subdom_funcs

	def Page_setAdBlockingEnabled(self, enabled):
		"""
		Function path: Page.setAdBlockingEnabled
			Domain: Page
			Method name: setAdBlockingEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether to block ads.
			No return value.
		
			Description: Enable Chrome's experimental ad filter on all sites.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Page.setAdBlockingEnabled',
		    enabled=enabled)
		return subdom_funcs

	def Page_navigate(self, url, **kwargs):
		"""
		Function path: Page.navigate
			Domain: Page
			Method name: navigate
		
			Parameters:
				Required arguments:
					'url' (type: string) -> URL to navigate the page to.
				Optional arguments:
					'referrer' (type: string) -> Referrer URL.
					'transitionType' (type: TransitionType) -> Intended transition type.
			Returns:
				'frameId' (type: FrameId) -> Frame id that will be navigated.
		
			Description: Navigates current page to the given URL.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		if 'referrer' in kwargs:
			assert isinstance(kwargs['referrer'], (str,)
			    ), "Optional argument 'referrer' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['referrer'])
		expected = ['referrer', 'transitionType']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['referrer', 'transitionType']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.navigate', url=url, **kwargs)
		return subdom_funcs

	def Page_stopLoading(self):
		"""
		Function path: Page.stopLoading
			Domain: Page
			Method name: stopLoading
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Force the page stop all navigations and pending resource fetches.
		"""
		subdom_funcs = self.synchronous_command('Page.stopLoading')
		return subdom_funcs

	def Page_getNavigationHistory(self):
		"""
		Function path: Page.getNavigationHistory
			Domain: Page
			Method name: getNavigationHistory
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'currentIndex' (type: integer) -> Index of the current navigation history entry.
				'entries' (type: array) -> Array of navigation history entries.
		
			Description: Returns navigation history for the current page.
		"""
		subdom_funcs = self.synchronous_command('Page.getNavigationHistory')
		return subdom_funcs

	def Page_navigateToHistoryEntry(self, entryId):
		"""
		Function path: Page.navigateToHistoryEntry
			Domain: Page
			Method name: navigateToHistoryEntry
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'entryId' (type: integer) -> Unique id of the entry to navigate to.
			No return value.
		
			Description: Navigates current page to the given history entry.
		"""
		assert isinstance(entryId, (int,)
		    ), "Argument 'entryId' must be of type '['int']'. Received type: '%s'" % type(
		    entryId)
		subdom_funcs = self.synchronous_command('Page.navigateToHistoryEntry',
		    entryId=entryId)
		return subdom_funcs

	def Page_getCookies(self):
		"""
		Function path: Page.getCookies
			Domain: Page
			Method name: getCookies
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'cookies' (type: array) -> Array of cookie objects.
		
			Description: Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field.
		"""
		subdom_funcs = self.synchronous_command('Page.getCookies')
		return subdom_funcs

	def Page_deleteCookie(self, cookieName, url):
		"""
		Function path: Page.deleteCookie
			Domain: Page
			Method name: deleteCookie
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'cookieName' (type: string) -> Name of the cookie to remove.
					'url' (type: string) -> URL to match cooke domain and path.
			No return value.
		
			Description: Deletes browser cookie with given name, domain and path.
		"""
		assert isinstance(cookieName, (str,)
		    ), "Argument 'cookieName' must be of type '['str']'. Received type: '%s'" % type(
		    cookieName)
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		subdom_funcs = self.synchronous_command('Page.deleteCookie', cookieName=
		    cookieName, url=url)
		return subdom_funcs

	def Page_getResourceTree(self):
		"""
		Function path: Page.getResourceTree
			Domain: Page
			Method name: getResourceTree
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'frameTree' (type: FrameResourceTree) -> Present frame / resource tree structure.
		
			Description: Returns present frame / resource tree structure.
		"""
		subdom_funcs = self.synchronous_command('Page.getResourceTree')
		return subdom_funcs

	def Page_getResourceContent(self, frameId, url):
		"""
		Function path: Page.getResourceContent
			Domain: Page
			Method name: getResourceContent
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'frameId' (type: FrameId) -> Frame id to get resource for.
					'url' (type: string) -> URL of the resource to get content for.
			Returns:
				'content' (type: string) -> Resource content.
				'base64Encoded' (type: boolean) -> True, if content was served as base64.
		
			Description: Returns content of the given resource.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		subdom_funcs = self.synchronous_command('Page.getResourceContent',
		    frameId=frameId, url=url)
		return subdom_funcs

	def Page_searchInResource(self, frameId, url, query, **kwargs):
		"""
		Function path: Page.searchInResource
			Domain: Page
			Method name: searchInResource
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'frameId' (type: FrameId) -> Frame id for resource to search in.
					'url' (type: string) -> URL of the resource to search in.
					'query' (type: string) -> String to search for.
				Optional arguments:
					'caseSensitive' (type: boolean) -> If true, search is case sensitive.
					'isRegex' (type: boolean) -> If true, treats string parameter as regex.
			Returns:
				'result' (type: array) -> List of search matches.
		
			Description: Searches for given string in resource content.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		assert isinstance(query, (str,)
		    ), "Argument 'query' must be of type '['str']'. Received type: '%s'" % type(
		    query)
		if 'caseSensitive' in kwargs:
			assert isinstance(kwargs['caseSensitive'], (bool,)
			    ), "Optional argument 'caseSensitive' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['caseSensitive'])
		if 'isRegex' in kwargs:
			assert isinstance(kwargs['isRegex'], (bool,)
			    ), "Optional argument 'isRegex' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['isRegex'])
		expected = ['caseSensitive', 'isRegex']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['caseSensitive', 'isRegex']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.searchInResource', frameId=
		    frameId, url=url, query=query, **kwargs)
		return subdom_funcs

	def Page_setDocumentContent(self, frameId, html):
		"""
		Function path: Page.setDocumentContent
			Domain: Page
			Method name: setDocumentContent
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'frameId' (type: FrameId) -> Frame id to set HTML for.
					'html' (type: string) -> HTML content to set.
			No return value.
		
			Description: Sets given markup as the document's HTML.
		"""
		assert isinstance(html, (str,)
		    ), "Argument 'html' must be of type '['str']'. Received type: '%s'" % type(
		    html)
		subdom_funcs = self.synchronous_command('Page.setDocumentContent',
		    frameId=frameId, html=html)
		return subdom_funcs

	def Page_setDeviceMetricsOverride(self, width, height, deviceScaleFactor,
	    mobile, **kwargs):
		"""
		Function path: Page.setDeviceMetricsOverride
			Domain: Page
			Method name: setDeviceMetricsOverride
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'width' (type: integer) -> Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
					'height' (type: integer) -> Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
					'deviceScaleFactor' (type: number) -> Overriding device scale factor value. 0 disables the override.
					'mobile' (type: boolean) -> Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
				Optional arguments:
					'scale' (type: number) -> Scale to apply to resulting view image.
					'screenWidth' (type: integer) -> Overriding screen width value in pixels (minimum 0, maximum 10000000).
					'screenHeight' (type: integer) -> Overriding screen height value in pixels (minimum 0, maximum 10000000).
					'positionX' (type: integer) -> Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
					'positionY' (type: integer) -> Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
					'dontSetVisibleSize' (type: boolean) -> Do not set visible view size, rely upon explicit setVisibleSize call.
					'screenOrientation' (type: Emulation.ScreenOrientation) -> Screen orientation override.
			No return value.
		
			Description: Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results).
		"""
		assert isinstance(width, (int,)
		    ), "Argument 'width' must be of type '['int']'. Received type: '%s'" % type(
		    width)
		assert isinstance(height, (int,)
		    ), "Argument 'height' must be of type '['int']'. Received type: '%s'" % type(
		    height)
		assert isinstance(deviceScaleFactor, (float, int)
		    ), "Argument 'deviceScaleFactor' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    deviceScaleFactor)
		assert isinstance(mobile, (bool,)
		    ), "Argument 'mobile' must be of type '['bool']'. Received type: '%s'" % type(
		    mobile)
		if 'scale' in kwargs:
			assert isinstance(kwargs['scale'], (float, int)
			    ), "Optional argument 'scale' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['scale'])
		if 'screenWidth' in kwargs:
			assert isinstance(kwargs['screenWidth'], (int,)
			    ), "Optional argument 'screenWidth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['screenWidth'])
		if 'screenHeight' in kwargs:
			assert isinstance(kwargs['screenHeight'], (int,)
			    ), "Optional argument 'screenHeight' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['screenHeight'])
		if 'positionX' in kwargs:
			assert isinstance(kwargs['positionX'], (int,)
			    ), "Optional argument 'positionX' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['positionX'])
		if 'positionY' in kwargs:
			assert isinstance(kwargs['positionY'], (int,)
			    ), "Optional argument 'positionY' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['positionY'])
		if 'dontSetVisibleSize' in kwargs:
			assert isinstance(kwargs['dontSetVisibleSize'], (bool,)
			    ), "Optional argument 'dontSetVisibleSize' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['dontSetVisibleSize'])
		expected = ['scale', 'screenWidth', 'screenHeight', 'positionX',
		    'positionY', 'dontSetVisibleSize', 'screenOrientation']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['scale', 'screenWidth', 'screenHeight', 'positionX', 'positionY', 'dontSetVisibleSize', 'screenOrientation']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.setDeviceMetricsOverride',
		    width=width, height=height, deviceScaleFactor=deviceScaleFactor,
		    mobile=mobile, **kwargs)
		return subdom_funcs

	def Page_clearDeviceMetricsOverride(self):
		"""
		Function path: Page.clearDeviceMetricsOverride
			Domain: Page
			Method name: clearDeviceMetricsOverride
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Clears the overriden device metrics.
		"""
		subdom_funcs = self.synchronous_command('Page.clearDeviceMetricsOverride')
		return subdom_funcs

	def Page_setGeolocationOverride(self, **kwargs):
		"""
		Function path: Page.setGeolocationOverride
			Domain: Page
			Method name: setGeolocationOverride
		
			Parameters:
				Optional arguments:
					'latitude' (type: number) -> Mock latitude
					'longitude' (type: number) -> Mock longitude
					'accuracy' (type: number) -> Mock accuracy
			No return value.
		
			Description: Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position unavailable.
		"""
		if 'latitude' in kwargs:
			assert isinstance(kwargs['latitude'], (float, int)
			    ), "Optional argument 'latitude' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['latitude'])
		if 'longitude' in kwargs:
			assert isinstance(kwargs['longitude'], (float, int)
			    ), "Optional argument 'longitude' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['longitude'])
		if 'accuracy' in kwargs:
			assert isinstance(kwargs['accuracy'], (float, int)
			    ), "Optional argument 'accuracy' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['accuracy'])
		expected = ['latitude', 'longitude', 'accuracy']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['latitude', 'longitude', 'accuracy']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.setGeolocationOverride', **
		    kwargs)
		return subdom_funcs

	def Page_clearGeolocationOverride(self):
		"""
		Function path: Page.clearGeolocationOverride
			Domain: Page
			Method name: clearGeolocationOverride
		
			No return value.
		
			Description: Clears the overriden Geolocation Position and Error.
		"""
		subdom_funcs = self.synchronous_command('Page.clearGeolocationOverride')
		return subdom_funcs

	def Page_setDeviceOrientationOverride(self, alpha, beta, gamma):
		"""
		Function path: Page.setDeviceOrientationOverride
			Domain: Page
			Method name: setDeviceOrientationOverride
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'alpha' (type: number) -> Mock alpha
					'beta' (type: number) -> Mock beta
					'gamma' (type: number) -> Mock gamma
			No return value.
		
			Description: Overrides the Device Orientation.
		"""
		assert isinstance(alpha, (float, int)
		    ), "Argument 'alpha' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    alpha)
		assert isinstance(beta, (float, int)
		    ), "Argument 'beta' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    beta)
		assert isinstance(gamma, (float, int)
		    ), "Argument 'gamma' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    gamma)
		subdom_funcs = self.synchronous_command('Page.setDeviceOrientationOverride',
		    alpha=alpha, beta=beta, gamma=gamma)
		return subdom_funcs

	def Page_clearDeviceOrientationOverride(self):
		"""
		Function path: Page.clearDeviceOrientationOverride
			Domain: Page
			Method name: clearDeviceOrientationOverride
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Clears the overridden Device Orientation.
		"""
		subdom_funcs = self.synchronous_command('Page.clearDeviceOrientationOverride'
		    )
		return subdom_funcs

	def Page_setTouchEmulationEnabled(self, enabled, **kwargs):
		"""
		Function path: Page.setTouchEmulationEnabled
			Domain: Page
			Method name: setTouchEmulationEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether the touch event emulation should be enabled.
				Optional arguments:
					'configuration' (type: string) -> Touch/gesture events configuration. Default: current platform.
			No return value.
		
			Description: Toggles mouse event-based touch event emulation.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		if 'configuration' in kwargs:
			assert isinstance(kwargs['configuration'], (str,)
			    ), "Optional argument 'configuration' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['configuration'])
		expected = ['configuration']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['configuration']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.setTouchEmulationEnabled',
		    enabled=enabled, **kwargs)
		return subdom_funcs

	def Page_captureScreenshot(self, **kwargs):
		"""
		Function path: Page.captureScreenshot
			Domain: Page
			Method name: captureScreenshot
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'format' (type: string) -> Image compression format (defaults to png).
					'quality' (type: integer) -> Compression quality from range [0..100] (jpeg only).
					'clip' (type: Viewport) -> Capture the screenshot of a given region only.
					'fromSurface' (type: boolean) -> Capture the screenshot from the surface, rather than the view. Defaults to true.
			Returns:
				'data' (type: string) -> Base64-encoded image data.
		
			Description: Capture page screenshot.
		"""
		if 'format' in kwargs:
			assert isinstance(kwargs['format'], (str,)
			    ), "Optional argument 'format' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['format'])
		if 'quality' in kwargs:
			assert isinstance(kwargs['quality'], (int,)
			    ), "Optional argument 'quality' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['quality'])
		if 'fromSurface' in kwargs:
			assert isinstance(kwargs['fromSurface'], (bool,)
			    ), "Optional argument 'fromSurface' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['fromSurface'])
		expected = ['format', 'quality', 'clip', 'fromSurface']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['format', 'quality', 'clip', 'fromSurface']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.captureScreenshot', **kwargs)
		return subdom_funcs

	def Page_printToPDF(self, **kwargs):
		"""
		Function path: Page.printToPDF
			Domain: Page
			Method name: printToPDF
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'landscape' (type: boolean) -> Paper orientation. Defaults to false.
					'displayHeaderFooter' (type: boolean) -> Display header and footer. Defaults to false.
					'printBackground' (type: boolean) -> Print background graphics. Defaults to false.
					'scale' (type: number) -> Scale of the webpage rendering. Defaults to 1.
					'paperWidth' (type: number) -> Paper width in inches. Defaults to 8.5 inches.
					'paperHeight' (type: number) -> Paper height in inches. Defaults to 11 inches.
					'marginTop' (type: number) -> Top margin in inches. Defaults to 1cm (~0.4 inches).
					'marginBottom' (type: number) -> Bottom margin in inches. Defaults to 1cm (~0.4 inches).
					'marginLeft' (type: number) -> Left margin in inches. Defaults to 1cm (~0.4 inches).
					'marginRight' (type: number) -> Right margin in inches. Defaults to 1cm (~0.4 inches).
					'pageRanges' (type: string) -> Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.
					'ignoreInvalidPageRanges' (type: boolean) -> Whether to silently ignore invalid but successfully parsed page ranges, such as '3-2'. Defaults to false.
			Returns:
				'data' (type: string) -> Base64-encoded pdf data.
		
			Description: Print page as PDF.
		"""
		if 'landscape' in kwargs:
			assert isinstance(kwargs['landscape'], (bool,)
			    ), "Optional argument 'landscape' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['landscape'])
		if 'displayHeaderFooter' in kwargs:
			assert isinstance(kwargs['displayHeaderFooter'], (bool,)
			    ), "Optional argument 'displayHeaderFooter' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['displayHeaderFooter'])
		if 'printBackground' in kwargs:
			assert isinstance(kwargs['printBackground'], (bool,)
			    ), "Optional argument 'printBackground' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['printBackground'])
		if 'scale' in kwargs:
			assert isinstance(kwargs['scale'], (float, int)
			    ), "Optional argument 'scale' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['scale'])
		if 'paperWidth' in kwargs:
			assert isinstance(kwargs['paperWidth'], (float, int)
			    ), "Optional argument 'paperWidth' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['paperWidth'])
		if 'paperHeight' in kwargs:
			assert isinstance(kwargs['paperHeight'], (float, int)
			    ), "Optional argument 'paperHeight' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['paperHeight'])
		if 'marginTop' in kwargs:
			assert isinstance(kwargs['marginTop'], (float, int)
			    ), "Optional argument 'marginTop' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['marginTop'])
		if 'marginBottom' in kwargs:
			assert isinstance(kwargs['marginBottom'], (float, int)
			    ), "Optional argument 'marginBottom' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['marginBottom'])
		if 'marginLeft' in kwargs:
			assert isinstance(kwargs['marginLeft'], (float, int)
			    ), "Optional argument 'marginLeft' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['marginLeft'])
		if 'marginRight' in kwargs:
			assert isinstance(kwargs['marginRight'], (float, int)
			    ), "Optional argument 'marginRight' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['marginRight'])
		if 'pageRanges' in kwargs:
			assert isinstance(kwargs['pageRanges'], (str,)
			    ), "Optional argument 'pageRanges' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['pageRanges'])
		if 'ignoreInvalidPageRanges' in kwargs:
			assert isinstance(kwargs['ignoreInvalidPageRanges'], (bool,)
			    ), "Optional argument 'ignoreInvalidPageRanges' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['ignoreInvalidPageRanges'])
		expected = ['landscape', 'displayHeaderFooter', 'printBackground',
		    'scale', 'paperWidth', 'paperHeight', 'marginTop', 'marginBottom',
		    'marginLeft', 'marginRight', 'pageRanges', 'ignoreInvalidPageRanges']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['landscape', 'displayHeaderFooter', 'printBackground', 'scale', 'paperWidth', 'paperHeight', 'marginTop', 'marginBottom', 'marginLeft', 'marginRight', 'pageRanges', 'ignoreInvalidPageRanges']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.printToPDF', **kwargs)
		return subdom_funcs

	def Page_startScreencast(self, **kwargs):
		"""
		Function path: Page.startScreencast
			Domain: Page
			Method name: startScreencast
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'format' (type: string) -> Image compression format.
					'quality' (type: integer) -> Compression quality from range [0..100].
					'maxWidth' (type: integer) -> Maximum screenshot width.
					'maxHeight' (type: integer) -> Maximum screenshot height.
					'everyNthFrame' (type: integer) -> Send every n-th frame.
			No return value.
		
			Description: Starts sending each frame using the <code>screencastFrame</code> event.
		"""
		if 'format' in kwargs:
			assert isinstance(kwargs['format'], (str,)
			    ), "Optional argument 'format' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['format'])
		if 'quality' in kwargs:
			assert isinstance(kwargs['quality'], (int,)
			    ), "Optional argument 'quality' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['quality'])
		if 'maxWidth' in kwargs:
			assert isinstance(kwargs['maxWidth'], (int,)
			    ), "Optional argument 'maxWidth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['maxWidth'])
		if 'maxHeight' in kwargs:
			assert isinstance(kwargs['maxHeight'], (int,)
			    ), "Optional argument 'maxHeight' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['maxHeight'])
		if 'everyNthFrame' in kwargs:
			assert isinstance(kwargs['everyNthFrame'], (int,)
			    ), "Optional argument 'everyNthFrame' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['everyNthFrame'])
		expected = ['format', 'quality', 'maxWidth', 'maxHeight', 'everyNthFrame']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['format', 'quality', 'maxWidth', 'maxHeight', 'everyNthFrame']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.startScreencast', **kwargs)
		return subdom_funcs

	def Page_stopScreencast(self):
		"""
		Function path: Page.stopScreencast
			Domain: Page
			Method name: stopScreencast
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Stops sending each frame in the <code>screencastFrame</code>.
		"""
		subdom_funcs = self.synchronous_command('Page.stopScreencast')
		return subdom_funcs

	def Page_screencastFrameAck(self, sessionId):
		"""
		Function path: Page.screencastFrameAck
			Domain: Page
			Method name: screencastFrameAck
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'sessionId' (type: integer) -> Frame number.
			No return value.
		
			Description: Acknowledges that a screencast frame has been received by the frontend.
		"""
		assert isinstance(sessionId, (int,)
		    ), "Argument 'sessionId' must be of type '['int']'. Received type: '%s'" % type(
		    sessionId)
		subdom_funcs = self.synchronous_command('Page.screencastFrameAck',
		    sessionId=sessionId)
		return subdom_funcs

	def Page_handleJavaScriptDialog(self, accept, **kwargs):
		"""
		Function path: Page.handleJavaScriptDialog
			Domain: Page
			Method name: handleJavaScriptDialog
		
			Parameters:
				Required arguments:
					'accept' (type: boolean) -> Whether to accept or dismiss the dialog.
				Optional arguments:
					'promptText' (type: string) -> The text to enter into the dialog prompt before accepting. Used only if this is a prompt dialog.
			No return value.
		
			Description: Accepts or dismisses a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload).
		"""
		assert isinstance(accept, (bool,)
		    ), "Argument 'accept' must be of type '['bool']'. Received type: '%s'" % type(
		    accept)
		if 'promptText' in kwargs:
			assert isinstance(kwargs['promptText'], (str,)
			    ), "Optional argument 'promptText' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['promptText'])
		expected = ['promptText']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['promptText']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.handleJavaScriptDialog',
		    accept=accept, **kwargs)
		return subdom_funcs

	def Page_getAppManifest(self):
		"""
		Function path: Page.getAppManifest
			Domain: Page
			Method name: getAppManifest
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'url' (type: string) -> Manifest location.
				'errors' (type: array) -> No description
				'data' (type: string) -> Manifest content.
		
		"""
		subdom_funcs = self.synchronous_command('Page.getAppManifest')
		return subdom_funcs

	def Page_requestAppBanner(self):
		"""
		Function path: Page.requestAppBanner
			Domain: Page
			Method name: requestAppBanner
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('Page.requestAppBanner')
		return subdom_funcs

	def Page_getLayoutMetrics(self):
		"""
		Function path: Page.getLayoutMetrics
			Domain: Page
			Method name: getLayoutMetrics
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'layoutViewport' (type: LayoutViewport) -> Metrics relating to the layout viewport.
				'visualViewport' (type: VisualViewport) -> Metrics relating to the visual viewport.
				'contentSize' (type: DOM.Rect) -> Size of scrollable area.
		
			Description: Returns metrics relating to the layouting of the page, such as viewport bounds/scale.
		"""
		subdom_funcs = self.synchronous_command('Page.getLayoutMetrics')
		return subdom_funcs

	def Page_createIsolatedWorld(self, frameId, **kwargs):
		"""
		Function path: Page.createIsolatedWorld
			Domain: Page
			Method name: createIsolatedWorld
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'frameId' (type: FrameId) -> Id of the frame in which the isolated world should be created.
				Optional arguments:
					'worldName' (type: string) -> An optional name which is reported in the Execution Context.
					'grantUniveralAccess' (type: boolean) -> Whether or not universal access should be granted to the isolated world. This is a powerful option, use with caution.
			Returns:
				'executionContextId' (type: Runtime.ExecutionContextId) -> Execution context of the isolated world.
		
			Description: Creates an isolated world for the given frame.
		"""
		if 'worldName' in kwargs:
			assert isinstance(kwargs['worldName'], (str,)
			    ), "Optional argument 'worldName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['worldName'])
		if 'grantUniveralAccess' in kwargs:
			assert isinstance(kwargs['grantUniveralAccess'], (bool,)
			    ), "Optional argument 'grantUniveralAccess' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['grantUniveralAccess'])
		expected = ['worldName', 'grantUniveralAccess']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['worldName', 'grantUniveralAccess']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.createIsolatedWorld',
		    frameId=frameId, **kwargs)
		return subdom_funcs

	def Page_bringToFront(self):
		"""
		Function path: Page.bringToFront
			Domain: Page
			Method name: bringToFront
		
			No return value.
		
			Description: Brings page to front (activates tab).
		"""
		subdom_funcs = self.synchronous_command('Page.bringToFront')
		return subdom_funcs

	def Page_setDownloadBehavior(self, behavior, **kwargs):
		"""
		Function path: Page.setDownloadBehavior
			Domain: Page
			Method name: setDownloadBehavior
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'behavior' (type: string) -> Whether to allow all or deny all download requests, or use default Chrome behavior if available (otherwise deny).
				Optional arguments:
					'downloadPath' (type: string) -> The default path to save downloaded files to. This is requred if behavior is set to 'allow'
			No return value.
		
			Description: Set the behavior when downloading a file.
		"""
		assert isinstance(behavior, (str,)
		    ), "Argument 'behavior' must be of type '['str']'. Received type: '%s'" % type(
		    behavior)
		if 'downloadPath' in kwargs:
			assert isinstance(kwargs['downloadPath'], (str,)
			    ), "Optional argument 'downloadPath' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['downloadPath'])
		expected = ['downloadPath']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['downloadPath']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.setDownloadBehavior',
		    behavior=behavior, **kwargs)
		return subdom_funcs

	def Overlay_enable(self):
		"""
		Function path: Overlay.enable
			Domain: Overlay
			Method name: enable
		
			No return value.
		
			Description: Enables domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Overlay.enable')
		return subdom_funcs

	def Overlay_disable(self):
		"""
		Function path: Overlay.disable
			Domain: Overlay
			Method name: disable
		
			No return value.
		
			Description: Disables domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Overlay.disable')
		return subdom_funcs

	def Overlay_setShowPaintRects(self, result):
		"""
		Function path: Overlay.setShowPaintRects
			Domain: Overlay
			Method name: setShowPaintRects
		
			Parameters:
				Required arguments:
					'result' (type: boolean) -> True for showing paint rectangles
			No return value.
		
			Description: Requests that backend shows paint rectangles
		"""
		assert isinstance(result, (bool,)
		    ), "Argument 'result' must be of type '['bool']'. Received type: '%s'" % type(
		    result)
		subdom_funcs = self.synchronous_command('Overlay.setShowPaintRects',
		    result=result)
		return subdom_funcs

	def Overlay_setShowDebugBorders(self, show):
		"""
		Function path: Overlay.setShowDebugBorders
			Domain: Overlay
			Method name: setShowDebugBorders
		
			Parameters:
				Required arguments:
					'show' (type: boolean) -> True for showing debug borders
			No return value.
		
			Description: Requests that backend shows debug borders on layers
		"""
		assert isinstance(show, (bool,)
		    ), "Argument 'show' must be of type '['bool']'. Received type: '%s'" % type(
		    show)
		subdom_funcs = self.synchronous_command('Overlay.setShowDebugBorders',
		    show=show)
		return subdom_funcs

	def Overlay_setShowFPSCounter(self, show):
		"""
		Function path: Overlay.setShowFPSCounter
			Domain: Overlay
			Method name: setShowFPSCounter
		
			Parameters:
				Required arguments:
					'show' (type: boolean) -> True for showing the FPS counter
			No return value.
		
			Description: Requests that backend shows the FPS counter
		"""
		assert isinstance(show, (bool,)
		    ), "Argument 'show' must be of type '['bool']'. Received type: '%s'" % type(
		    show)
		subdom_funcs = self.synchronous_command('Overlay.setShowFPSCounter', show
		    =show)
		return subdom_funcs

	def Overlay_setShowScrollBottleneckRects(self, show):
		"""
		Function path: Overlay.setShowScrollBottleneckRects
			Domain: Overlay
			Method name: setShowScrollBottleneckRects
		
			Parameters:
				Required arguments:
					'show' (type: boolean) -> True for showing scroll bottleneck rects
			No return value.
		
			Description: Requests that backend shows scroll bottleneck rects
		"""
		assert isinstance(show, (bool,)
		    ), "Argument 'show' must be of type '['bool']'. Received type: '%s'" % type(
		    show)
		subdom_funcs = self.synchronous_command(
		    'Overlay.setShowScrollBottleneckRects', show=show)
		return subdom_funcs

	def Overlay_setShowViewportSizeOnResize(self, show):
		"""
		Function path: Overlay.setShowViewportSizeOnResize
			Domain: Overlay
			Method name: setShowViewportSizeOnResize
		
			Parameters:
				Required arguments:
					'show' (type: boolean) -> Whether to paint size or not.
			No return value.
		
			Description: Paints viewport size upon main frame resize.
		"""
		assert isinstance(show, (bool,)
		    ), "Argument 'show' must be of type '['bool']'. Received type: '%s'" % type(
		    show)
		subdom_funcs = self.synchronous_command('Overlay.setShowViewportSizeOnResize'
		    , show=show)
		return subdom_funcs

	def Overlay_setPausedInDebuggerMessage(self, **kwargs):
		"""
		Function path: Overlay.setPausedInDebuggerMessage
			Domain: Overlay
			Method name: setPausedInDebuggerMessage
		
			Parameters:
				Optional arguments:
					'message' (type: string) -> The message to display, also triggers resume and step over controls.
			No return value.
		
		"""
		if 'message' in kwargs:
			assert isinstance(kwargs['message'], (str,)
			    ), "Optional argument 'message' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['message'])
		expected = ['message']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['message']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.setPausedInDebuggerMessage',
		    **kwargs)
		return subdom_funcs

	def Overlay_setSuspended(self, suspended):
		"""
		Function path: Overlay.setSuspended
			Domain: Overlay
			Method name: setSuspended
		
			Parameters:
				Required arguments:
					'suspended' (type: boolean) -> Whether overlay should be suspended and not consume any resources until resumed.
			No return value.
		
		"""
		assert isinstance(suspended, (bool,)
		    ), "Argument 'suspended' must be of type '['bool']'. Received type: '%s'" % type(
		    suspended)
		subdom_funcs = self.synchronous_command('Overlay.setSuspended', suspended
		    =suspended)
		return subdom_funcs

	def Overlay_setInspectMode(self, mode, **kwargs):
		"""
		Function path: Overlay.setInspectMode
			Domain: Overlay
			Method name: setInspectMode
		
			Parameters:
				Required arguments:
					'mode' (type: InspectMode) -> Set an inspection mode.
				Optional arguments:
					'highlightConfig' (type: HighlightConfig) -> A descriptor for the highlight appearance of hovered-over nodes. May be omitted if <code>enabled == false</code>.
			No return value.
		
			Description: Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection.
		"""
		expected = ['highlightConfig']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['highlightConfig']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.setInspectMode', mode=
		    mode, **kwargs)
		return subdom_funcs

	def Overlay_highlightRect(self, x, y, width, height, **kwargs):
		"""
		Function path: Overlay.highlightRect
			Domain: Overlay
			Method name: highlightRect
		
			Parameters:
				Required arguments:
					'x' (type: integer) -> X coordinate
					'y' (type: integer) -> Y coordinate
					'width' (type: integer) -> Rectangle width
					'height' (type: integer) -> Rectangle height
				Optional arguments:
					'color' (type: DOM.RGBA) -> The highlight fill color (default: transparent).
					'outlineColor' (type: DOM.RGBA) -> The highlight outline color (default: transparent).
			No return value.
		
			Description: Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport.
		"""
		assert isinstance(x, (int,)
		    ), "Argument 'x' must be of type '['int']'. Received type: '%s'" % type(x
		    )
		assert isinstance(y, (int,)
		    ), "Argument 'y' must be of type '['int']'. Received type: '%s'" % type(y
		    )
		assert isinstance(width, (int,)
		    ), "Argument 'width' must be of type '['int']'. Received type: '%s'" % type(
		    width)
		assert isinstance(height, (int,)
		    ), "Argument 'height' must be of type '['int']'. Received type: '%s'" % type(
		    height)
		expected = ['color', 'outlineColor']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['color', 'outlineColor']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.highlightRect', x=x, y=y,
		    width=width, height=height, **kwargs)
		return subdom_funcs

	def Overlay_highlightQuad(self, quad, **kwargs):
		"""
		Function path: Overlay.highlightQuad
			Domain: Overlay
			Method name: highlightQuad
		
			Parameters:
				Required arguments:
					'quad' (type: DOM.Quad) -> Quad to highlight
				Optional arguments:
					'color' (type: DOM.RGBA) -> The highlight fill color (default: transparent).
					'outlineColor' (type: DOM.RGBA) -> The highlight outline color (default: transparent).
			No return value.
		
			Description: Highlights given quad. Coordinates are absolute with respect to the main frame viewport.
		"""
		expected = ['color', 'outlineColor']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['color', 'outlineColor']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.highlightQuad', quad=
		    quad, **kwargs)
		return subdom_funcs

	def Overlay_highlightNode(self, highlightConfig, **kwargs):
		"""
		Function path: Overlay.highlightNode
			Domain: Overlay
			Method name: highlightNode
		
			Parameters:
				Required arguments:
					'highlightConfig' (type: HighlightConfig) -> A descriptor for the highlight appearance.
				Optional arguments:
					'nodeId' (type: DOM.NodeId) -> Identifier of the node to highlight.
					'backendNodeId' (type: DOM.BackendNodeId) -> Identifier of the backend node to highlight.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node to be highlighted.
			No return value.
		
			Description: Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.highlightNode',
		    highlightConfig=highlightConfig, **kwargs)
		return subdom_funcs

	def Overlay_highlightFrame(self, frameId, **kwargs):
		"""
		Function path: Overlay.highlightFrame
			Domain: Overlay
			Method name: highlightFrame
		
			Parameters:
				Required arguments:
					'frameId' (type: Page.FrameId) -> Identifier of the frame to highlight.
				Optional arguments:
					'contentColor' (type: DOM.RGBA) -> The content box highlight fill color (default: transparent).
					'contentOutlineColor' (type: DOM.RGBA) -> The content box highlight outline color (default: transparent).
			No return value.
		
			Description: Highlights owner element of the frame with given id.
		"""
		expected = ['contentColor', 'contentOutlineColor']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['contentColor', 'contentOutlineColor']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.highlightFrame', frameId
		    =frameId, **kwargs)
		return subdom_funcs

	def Overlay_hideHighlight(self):
		"""
		Function path: Overlay.hideHighlight
			Domain: Overlay
			Method name: hideHighlight
		
			No return value.
		
			Description: Hides any highlight.
		"""
		subdom_funcs = self.synchronous_command('Overlay.hideHighlight')
		return subdom_funcs

	def Overlay_getHighlightObjectForTest(self, nodeId):
		"""
		Function path: Overlay.getHighlightObjectForTest
			Domain: Overlay
			Method name: getHighlightObjectForTest
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> Id of the node to get highlight object for.
			Returns:
				'highlight' (type: object) -> Highlight data for the node.
		
			Description: For testing.
		"""
		subdom_funcs = self.synchronous_command('Overlay.getHighlightObjectForTest',
		    nodeId=nodeId)
		return subdom_funcs

	def Emulation_setDeviceMetricsOverride(self, width, height,
	    deviceScaleFactor, mobile, **kwargs):
		"""
		Function path: Emulation.setDeviceMetricsOverride
			Domain: Emulation
			Method name: setDeviceMetricsOverride
		
			Parameters:
				Required arguments:
					'width' (type: integer) -> Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
					'height' (type: integer) -> Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
					'deviceScaleFactor' (type: number) -> Overriding device scale factor value. 0 disables the override.
					'mobile' (type: boolean) -> Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
				Optional arguments:
					'scale' (type: number) -> Scale to apply to resulting view image.
					'screenWidth' (type: integer) -> Overriding screen width value in pixels (minimum 0, maximum 10000000).
					'screenHeight' (type: integer) -> Overriding screen height value in pixels (minimum 0, maximum 10000000).
					'positionX' (type: integer) -> Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
					'positionY' (type: integer) -> Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
					'dontSetVisibleSize' (type: boolean) -> Do not set visible view size, rely upon explicit setVisibleSize call.
					'screenOrientation' (type: ScreenOrientation) -> Screen orientation override.
			No return value.
		
			Description: Overrides the values of device screen dimensions (window.screen.width, window.screen.height, window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media query results).
		"""
		assert isinstance(width, (int,)
		    ), "Argument 'width' must be of type '['int']'. Received type: '%s'" % type(
		    width)
		assert isinstance(height, (int,)
		    ), "Argument 'height' must be of type '['int']'. Received type: '%s'" % type(
		    height)
		assert isinstance(deviceScaleFactor, (float, int)
		    ), "Argument 'deviceScaleFactor' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    deviceScaleFactor)
		assert isinstance(mobile, (bool,)
		    ), "Argument 'mobile' must be of type '['bool']'. Received type: '%s'" % type(
		    mobile)
		if 'scale' in kwargs:
			assert isinstance(kwargs['scale'], (float, int)
			    ), "Optional argument 'scale' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['scale'])
		if 'screenWidth' in kwargs:
			assert isinstance(kwargs['screenWidth'], (int,)
			    ), "Optional argument 'screenWidth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['screenWidth'])
		if 'screenHeight' in kwargs:
			assert isinstance(kwargs['screenHeight'], (int,)
			    ), "Optional argument 'screenHeight' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['screenHeight'])
		if 'positionX' in kwargs:
			assert isinstance(kwargs['positionX'], (int,)
			    ), "Optional argument 'positionX' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['positionX'])
		if 'positionY' in kwargs:
			assert isinstance(kwargs['positionY'], (int,)
			    ), "Optional argument 'positionY' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['positionY'])
		if 'dontSetVisibleSize' in kwargs:
			assert isinstance(kwargs['dontSetVisibleSize'], (bool,)
			    ), "Optional argument 'dontSetVisibleSize' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['dontSetVisibleSize'])
		expected = ['scale', 'screenWidth', 'screenHeight', 'positionX',
		    'positionY', 'dontSetVisibleSize', 'screenOrientation']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['scale', 'screenWidth', 'screenHeight', 'positionX', 'positionY', 'dontSetVisibleSize', 'screenOrientation']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setDeviceMetricsOverride',
		    width=width, height=height, deviceScaleFactor=deviceScaleFactor,
		    mobile=mobile, **kwargs)
		return subdom_funcs

	def Emulation_clearDeviceMetricsOverride(self):
		"""
		Function path: Emulation.clearDeviceMetricsOverride
			Domain: Emulation
			Method name: clearDeviceMetricsOverride
		
			No return value.
		
			Description: Clears the overriden device metrics.
		"""
		subdom_funcs = self.synchronous_command(
		    'Emulation.clearDeviceMetricsOverride')
		return subdom_funcs

	def Emulation_resetPageScaleFactor(self):
		"""
		Function path: Emulation.resetPageScaleFactor
			Domain: Emulation
			Method name: resetPageScaleFactor
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Requests that page scale factor is reset to initial values.
		"""
		subdom_funcs = self.synchronous_command('Emulation.resetPageScaleFactor')
		return subdom_funcs

	def Emulation_setPageScaleFactor(self, pageScaleFactor):
		"""
		Function path: Emulation.setPageScaleFactor
			Domain: Emulation
			Method name: setPageScaleFactor
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'pageScaleFactor' (type: number) -> Page scale factor.
			No return value.
		
			Description: Sets a specified page scale factor.
		"""
		assert isinstance(pageScaleFactor, (float, int)
		    ), "Argument 'pageScaleFactor' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    pageScaleFactor)
		subdom_funcs = self.synchronous_command('Emulation.setPageScaleFactor',
		    pageScaleFactor=pageScaleFactor)
		return subdom_funcs

	def Emulation_setVisibleSize(self, width, height):
		"""
		Function path: Emulation.setVisibleSize
			Domain: Emulation
			Method name: setVisibleSize
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'width' (type: integer) -> Frame width (DIP).
					'height' (type: integer) -> Frame height (DIP).
			No return value.
		
			Description: Resizes the frame/viewport of the page. Note that this does not affect the frame's container (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported on Android.
		"""
		assert isinstance(width, (int,)
		    ), "Argument 'width' must be of type '['int']'. Received type: '%s'" % type(
		    width)
		assert isinstance(height, (int,)
		    ), "Argument 'height' must be of type '['int']'. Received type: '%s'" % type(
		    height)
		subdom_funcs = self.synchronous_command('Emulation.setVisibleSize', width
		    =width, height=height)
		return subdom_funcs

	def Emulation_setScriptExecutionDisabled(self, value):
		"""
		Function path: Emulation.setScriptExecutionDisabled
			Domain: Emulation
			Method name: setScriptExecutionDisabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'value' (type: boolean) -> Whether script execution should be disabled in the page.
			No return value.
		
			Description: Switches script execution in the page.
		"""
		assert isinstance(value, (bool,)
		    ), "Argument 'value' must be of type '['bool']'. Received type: '%s'" % type(
		    value)
		subdom_funcs = self.synchronous_command(
		    'Emulation.setScriptExecutionDisabled', value=value)
		return subdom_funcs

	def Emulation_setGeolocationOverride(self, **kwargs):
		"""
		Function path: Emulation.setGeolocationOverride
			Domain: Emulation
			Method name: setGeolocationOverride
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'latitude' (type: number) -> Mock latitude
					'longitude' (type: number) -> Mock longitude
					'accuracy' (type: number) -> Mock accuracy
			No return value.
		
			Description: Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position unavailable.
		"""
		if 'latitude' in kwargs:
			assert isinstance(kwargs['latitude'], (float, int)
			    ), "Optional argument 'latitude' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['latitude'])
		if 'longitude' in kwargs:
			assert isinstance(kwargs['longitude'], (float, int)
			    ), "Optional argument 'longitude' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['longitude'])
		if 'accuracy' in kwargs:
			assert isinstance(kwargs['accuracy'], (float, int)
			    ), "Optional argument 'accuracy' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['accuracy'])
		expected = ['latitude', 'longitude', 'accuracy']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['latitude', 'longitude', 'accuracy']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setGeolocationOverride',
		    **kwargs)
		return subdom_funcs

	def Emulation_clearGeolocationOverride(self):
		"""
		Function path: Emulation.clearGeolocationOverride
			Domain: Emulation
			Method name: clearGeolocationOverride
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Clears the overriden Geolocation Position and Error.
		"""
		subdom_funcs = self.synchronous_command('Emulation.clearGeolocationOverride')
		return subdom_funcs

	def Emulation_setTouchEmulationEnabled(self, enabled, **kwargs):
		"""
		Function path: Emulation.setTouchEmulationEnabled
			Domain: Emulation
			Method name: setTouchEmulationEnabled
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether the touch event emulation should be enabled.
				Optional arguments:
					'maxTouchPoints' (type: integer) -> Maximum touch points supported. Defaults to one.
			No return value.
		
			Description: Enables touch on platforms which do not support them.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		if 'maxTouchPoints' in kwargs:
			assert isinstance(kwargs['maxTouchPoints'], (int,)
			    ), "Optional argument 'maxTouchPoints' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['maxTouchPoints'])
		expected = ['maxTouchPoints']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['maxTouchPoints']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setTouchEmulationEnabled',
		    enabled=enabled, **kwargs)
		return subdom_funcs

	def Emulation_setEmitTouchEventsForMouse(self, enabled, **kwargs):
		"""
		Function path: Emulation.setEmitTouchEventsForMouse
			Domain: Emulation
			Method name: setEmitTouchEventsForMouse
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether touch emulation based on mouse input should be enabled.
				Optional arguments:
					'configuration' (type: string) -> Touch/gesture events configuration. Default: current platform.
			No return value.
		
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		if 'configuration' in kwargs:
			assert isinstance(kwargs['configuration'], (str,)
			    ), "Optional argument 'configuration' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['configuration'])
		expected = ['configuration']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['configuration']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'Emulation.setEmitTouchEventsForMouse', enabled=enabled, **kwargs)
		return subdom_funcs

	def Emulation_setEmulatedMedia(self, media):
		"""
		Function path: Emulation.setEmulatedMedia
			Domain: Emulation
			Method name: setEmulatedMedia
		
			Parameters:
				Required arguments:
					'media' (type: string) -> Media type to emulate. Empty string disables the override.
			No return value.
		
			Description: Emulates the given media for CSS media queries.
		"""
		assert isinstance(media, (str,)
		    ), "Argument 'media' must be of type '['str']'. Received type: '%s'" % type(
		    media)
		subdom_funcs = self.synchronous_command('Emulation.setEmulatedMedia',
		    media=media)
		return subdom_funcs

	def Emulation_setCPUThrottlingRate(self, rate):
		"""
		Function path: Emulation.setCPUThrottlingRate
			Domain: Emulation
			Method name: setCPUThrottlingRate
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'rate' (type: number) -> Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
			No return value.
		
			Description: Enables CPU throttling to emulate slow CPUs.
		"""
		assert isinstance(rate, (float, int)
		    ), "Argument 'rate' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    rate)
		subdom_funcs = self.synchronous_command('Emulation.setCPUThrottlingRate',
		    rate=rate)
		return subdom_funcs

	def Emulation_canEmulate(self):
		"""
		Function path: Emulation.canEmulate
			Domain: Emulation
			Method name: canEmulate
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'result' (type: boolean) -> True if emulation is supported.
		
			Description: Tells whether emulation is supported.
		"""
		subdom_funcs = self.synchronous_command('Emulation.canEmulate')
		return subdom_funcs

	def Emulation_setVirtualTimePolicy(self, policy, **kwargs):
		"""
		Function path: Emulation.setVirtualTimePolicy
			Domain: Emulation
			Method name: setVirtualTimePolicy
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'policy' (type: VirtualTimePolicy) -> No description
				Optional arguments:
					'budget' (type: integer) -> If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent.
			No return value.
		
			Description: Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets the current virtual time policy.  Note this supersedes any previous time budget.
		"""
		if 'budget' in kwargs:
			assert isinstance(kwargs['budget'], (int,)
			    ), "Optional argument 'budget' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['budget'])
		expected = ['budget']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['budget']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setVirtualTimePolicy',
		    policy=policy, **kwargs)
		return subdom_funcs

	def Emulation_setNavigatorOverrides(self, platform):
		"""
		Function path: Emulation.setNavigatorOverrides
			Domain: Emulation
			Method name: setNavigatorOverrides
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'platform' (type: string) -> The platform navigator.platform should return.
			No return value.
		
			Description: Overrides value returned by the javascript navigator object.
		"""
		assert isinstance(platform, (str,)
		    ), "Argument 'platform' must be of type '['str']'. Received type: '%s'" % type(
		    platform)
		subdom_funcs = self.synchronous_command('Emulation.setNavigatorOverrides',
		    platform=platform)
		return subdom_funcs

	def Emulation_setDefaultBackgroundColorOverride(self, **kwargs):
		"""
		Function path: Emulation.setDefaultBackgroundColorOverride
			Domain: Emulation
			Method name: setDefaultBackgroundColorOverride
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'color' (type: DOM.RGBA) -> RGBA of the default background color. If not specified, any existing override will be cleared.
			No return value.
		
			Description: Sets or clears an override of the default background color of the frame. This override is used if the content does not specify one.
		"""
		expected = ['color']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['color']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'Emulation.setDefaultBackgroundColorOverride', **kwargs)
		return subdom_funcs

	def Security_enable(self):
		"""
		Function path: Security.enable
			Domain: Security
			Method name: enable
		
			No return value.
		
			Description: Enables tracking security state changes.
		"""
		subdom_funcs = self.synchronous_command('Security.enable')
		return subdom_funcs

	def Security_disable(self):
		"""
		Function path: Security.disable
			Domain: Security
			Method name: disable
		
			No return value.
		
			Description: Disables tracking security state changes.
		"""
		subdom_funcs = self.synchronous_command('Security.disable')
		return subdom_funcs

	def Security_handleCertificateError(self, eventId, action):
		"""
		Function path: Security.handleCertificateError
			Domain: Security
			Method name: handleCertificateError
		
			Parameters:
				Required arguments:
					'eventId' (type: integer) -> The ID of the event.
					'action' (type: CertificateErrorAction) -> The action to take on the certificate error.
			No return value.
		
			Description: Handles a certificate error that fired a certificateError event.
		"""
		assert isinstance(eventId, (int,)
		    ), "Argument 'eventId' must be of type '['int']'. Received type: '%s'" % type(
		    eventId)
		subdom_funcs = self.synchronous_command('Security.handleCertificateError',
		    eventId=eventId, action=action)
		return subdom_funcs

	def Security_setOverrideCertificateErrors(self, override):
		"""
		Function path: Security.setOverrideCertificateErrors
			Domain: Security
			Method name: setOverrideCertificateErrors
		
			Parameters:
				Required arguments:
					'override' (type: boolean) -> If true, certificate errors will be overridden.
			No return value.
		
			Description: Enable/disable overriding certificate errors. If enabled, all certificate error events need to be handled by the DevTools client and should be answered with handleCertificateError commands.
		"""
		assert isinstance(override, (bool,)
		    ), "Argument 'override' must be of type '['bool']'. Received type: '%s'" % type(
		    override)
		subdom_funcs = self.synchronous_command(
		    'Security.setOverrideCertificateErrors', override=override)
		return subdom_funcs

	def Audits_getEncodedResponse(self, requestId, encoding, **kwargs):
		"""
		Function path: Audits.getEncodedResponse
			Domain: Audits
			Method name: getEncodedResponse
		
			Parameters:
				Required arguments:
					'requestId' (type: Network.RequestId) -> Identifier of the network request to get content for.
					'encoding' (type: string) -> The encoding to use.
				Optional arguments:
					'quality' (type: number) -> The quality of the encoding (0-1). (defaults to 1)
					'sizeOnly' (type: boolean) -> Whether to only return the size information (defaults to false).
			Returns:
				'body' (type: string) -> The encoded body as a base64 string. Omitted if sizeOnly is true.
				'originalSize' (type: integer) -> Size before re-encoding.
				'encodedSize' (type: integer) -> Size after re-encoding.
		
			Description: Returns the response body and size if it were re-encoded with the specified settings. Only applies to images.
		"""
		assert isinstance(encoding, (str,)
		    ), "Argument 'encoding' must be of type '['str']'. Received type: '%s'" % type(
		    encoding)
		if 'quality' in kwargs:
			assert isinstance(kwargs['quality'], (float, int)
			    ), "Optional argument 'quality' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['quality'])
		if 'sizeOnly' in kwargs:
			assert isinstance(kwargs['sizeOnly'], (bool,)
			    ), "Optional argument 'sizeOnly' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['sizeOnly'])
		expected = ['quality', 'sizeOnly']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['quality', 'sizeOnly']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Audits.getEncodedResponse',
		    requestId=requestId, encoding=encoding, **kwargs)
		return subdom_funcs

	def Network_enable(self, **kwargs):
		"""
		Function path: Network.enable
			Domain: Network
			Method name: enable
		
			Parameters:
				Optional arguments:
					'maxTotalBufferSize' (type: integer) -> Buffer size in bytes to use when preserving network payloads (XHRs, etc).
					'maxResourceBufferSize' (type: integer) -> Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
			No return value.
		
			Description: Enables network tracking, network events will now be delivered to the client.
		"""
		if 'maxTotalBufferSize' in kwargs:
			assert isinstance(kwargs['maxTotalBufferSize'], (int,)
			    ), "Optional argument 'maxTotalBufferSize' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['maxTotalBufferSize'])
		if 'maxResourceBufferSize' in kwargs:
			assert isinstance(kwargs['maxResourceBufferSize'], (int,)
			    ), "Optional argument 'maxResourceBufferSize' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['maxResourceBufferSize'])
		expected = ['maxTotalBufferSize', 'maxResourceBufferSize']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['maxTotalBufferSize', 'maxResourceBufferSize']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.enable', **kwargs)
		return subdom_funcs

	def Network_disable(self):
		"""
		Function path: Network.disable
			Domain: Network
			Method name: disable
		
			No return value.
		
			Description: Disables network tracking, prevents network events from being sent to the client.
		"""
		subdom_funcs = self.synchronous_command('Network.disable')
		return subdom_funcs

	def Network_setUserAgentOverride(self, userAgent):
		"""
		Function path: Network.setUserAgentOverride
			Domain: Network
			Method name: setUserAgentOverride
		
			Parameters:
				Required arguments:
					'userAgent' (type: string) -> User agent to use.
			No return value.
		
			Description: Allows overriding user agent with the given string.
		"""
		assert isinstance(userAgent, (str,)
		    ), "Argument 'userAgent' must be of type '['str']'. Received type: '%s'" % type(
		    userAgent)
		subdom_funcs = self.synchronous_command('Network.setUserAgentOverride',
		    userAgent=userAgent)
		return subdom_funcs

	def Network_setExtraHTTPHeaders(self, headers):
		"""
		Function path: Network.setExtraHTTPHeaders
			Domain: Network
			Method name: setExtraHTTPHeaders
		
			Parameters:
				Required arguments:
					'headers' (type: Headers) -> Map with extra HTTP headers.
			No return value.
		
			Description: Specifies whether to always send extra HTTP headers with the requests from this page.
		"""
		subdom_funcs = self.synchronous_command('Network.setExtraHTTPHeaders',
		    headers=headers)
		return subdom_funcs

	def Network_getResponseBody(self, requestId):
		"""
		Function path: Network.getResponseBody
			Domain: Network
			Method name: getResponseBody
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> Identifier of the network request to get content for.
			Returns:
				'body' (type: string) -> Response body.
				'base64Encoded' (type: boolean) -> True, if content was sent as base64.
		
			Description: Returns content served for the given request.
		"""
		subdom_funcs = self.synchronous_command('Network.getResponseBody',
		    requestId=requestId)
		return subdom_funcs

	def Network_setBlockedURLs(self, urls):
		"""
		Function path: Network.setBlockedURLs
			Domain: Network
			Method name: setBlockedURLs
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'urls' (type: array) -> URL patterns to block. Wildcards ('*') are allowed.
			No return value.
		
			Description: Blocks URLs from loading.
		"""
		assert isinstance(urls, (list, tuple)
		    ), "Argument 'urls' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    urls)
		subdom_funcs = self.synchronous_command('Network.setBlockedURLs', urls=urls)
		return subdom_funcs

	def Network_replayXHR(self, requestId):
		"""
		Function path: Network.replayXHR
			Domain: Network
			Method name: replayXHR
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> Identifier of XHR to replay.
			No return value.
		
			Description: This method sends a new XMLHttpRequest which is identical to the original one. The following parameters should be identical: method, url, async, request body, extra headers, withCredentials attribute, user, password.
		"""
		subdom_funcs = self.synchronous_command('Network.replayXHR', requestId=
		    requestId)
		return subdom_funcs

	def Network_canClearBrowserCache(self):
		"""
		Function path: Network.canClearBrowserCache
			Domain: Network
			Method name: canClearBrowserCache
		
			Returns:
				'result' (type: boolean) -> True if browser cache can be cleared.
		
			Description: Tells whether clearing browser cache is supported.
		"""
		subdom_funcs = self.synchronous_command('Network.canClearBrowserCache')
		return subdom_funcs

	def Network_clearBrowserCache(self):
		"""
		Function path: Network.clearBrowserCache
			Domain: Network
			Method name: clearBrowserCache
		
			No return value.
		
			Description: Clears browser cache.
		"""
		subdom_funcs = self.synchronous_command('Network.clearBrowserCache')
		return subdom_funcs

	def Network_canClearBrowserCookies(self):
		"""
		Function path: Network.canClearBrowserCookies
			Domain: Network
			Method name: canClearBrowserCookies
		
			Returns:
				'result' (type: boolean) -> True if browser cookies can be cleared.
		
			Description: Tells whether clearing browser cookies is supported.
		"""
		subdom_funcs = self.synchronous_command('Network.canClearBrowserCookies')
		return subdom_funcs

	def Network_clearBrowserCookies(self):
		"""
		Function path: Network.clearBrowserCookies
			Domain: Network
			Method name: clearBrowserCookies
		
			No return value.
		
			Description: Clears browser cookies.
		"""
		subdom_funcs = self.synchronous_command('Network.clearBrowserCookies')
		return subdom_funcs

	def Network_getCookies(self, **kwargs):
		"""
		Function path: Network.getCookies
			Domain: Network
			Method name: getCookies
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'urls' (type: array) -> The list of URLs for which applicable cookies will be fetched
			Returns:
				'cookies' (type: array) -> Array of cookie objects.
		
			Description: Returns all browser cookies for the current URL. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field.
		"""
		if 'urls' in kwargs:
			assert isinstance(kwargs['urls'], (list, tuple)
			    ), "Optional argument 'urls' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['urls'])
		expected = ['urls']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['urls']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.getCookies', **kwargs)
		return subdom_funcs

	def Network_getAllCookies(self):
		"""
		Function path: Network.getAllCookies
			Domain: Network
			Method name: getAllCookies
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'cookies' (type: array) -> Array of cookie objects.
		
			Description: Returns all browser cookies. Depending on the backend support, will return detailed cookie information in the <code>cookies</code> field.
		"""
		subdom_funcs = self.synchronous_command('Network.getAllCookies')
		return subdom_funcs

	def Network_deleteCookies(self, name, **kwargs):
		"""
		Function path: Network.deleteCookies
			Domain: Network
			Method name: deleteCookies
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'name' (type: string) -> Name of the cookies to remove.
				Optional arguments:
					'url' (type: string) -> If specified, deletes all the cookies with the given name where domain and path match provided URL.
					'domain' (type: string) -> If specified, deletes only cookies with the exact domain.
					'path' (type: string) -> If specified, deletes only cookies with the exact path.
			No return value.
		
			Description: Deletes browser cookies with matching name and url or domain/path pair.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		if 'url' in kwargs:
			assert isinstance(kwargs['url'], (str,)
			    ), "Optional argument 'url' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['url'])
		if 'domain' in kwargs:
			assert isinstance(kwargs['domain'], (str,)
			    ), "Optional argument 'domain' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['domain'])
		if 'path' in kwargs:
			assert isinstance(kwargs['path'], (str,)
			    ), "Optional argument 'path' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['path'])
		expected = ['url', 'domain', 'path']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['url', 'domain', 'path']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.deleteCookies', name=
		    name, **kwargs)
		return subdom_funcs

	def Network_setCookie(self, name, value, **kwargs):
		"""
		Function path: Network.setCookie
			Domain: Network
			Method name: setCookie
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'name' (type: string) -> Cookie name.
					'value' (type: string) -> Cookie value.
				Optional arguments:
					'url' (type: string) -> The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie.
					'domain' (type: string) -> Cookie domain.
					'path' (type: string) -> Cookie path.
					'secure' (type: boolean) -> True if cookie is secure.
					'httpOnly' (type: boolean) -> True if cookie is http-only.
					'sameSite' (type: CookieSameSite) -> Cookie SameSite type.
					'expires' (type: TimeSinceEpoch) -> Cookie expiration date, session cookie if not set
			Returns:
				'success' (type: boolean) -> True if successfully set cookie.
		
			Description: Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		assert isinstance(value, (str,)
		    ), "Argument 'value' must be of type '['str']'. Received type: '%s'" % type(
		    value)
		if 'url' in kwargs:
			assert isinstance(kwargs['url'], (str,)
			    ), "Optional argument 'url' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['url'])
		if 'domain' in kwargs:
			assert isinstance(kwargs['domain'], (str,)
			    ), "Optional argument 'domain' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['domain'])
		if 'path' in kwargs:
			assert isinstance(kwargs['path'], (str,)
			    ), "Optional argument 'path' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['path'])
		if 'secure' in kwargs:
			assert isinstance(kwargs['secure'], (bool,)
			    ), "Optional argument 'secure' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['secure'])
		if 'httpOnly' in kwargs:
			assert isinstance(kwargs['httpOnly'], (bool,)
			    ), "Optional argument 'httpOnly' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['httpOnly'])
		expected = ['url', 'domain', 'path', 'secure', 'httpOnly', 'sameSite',
		    'expires']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['url', 'domain', 'path', 'secure', 'httpOnly', 'sameSite', 'expires']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.setCookie', name=name,
		    value=value, **kwargs)
		return subdom_funcs

	def Network_setCookies(self, cookies):
		"""
		Function path: Network.setCookies
			Domain: Network
			Method name: setCookies
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'cookies' (type: array) -> Cookies to be set.
			No return value.
		
			Description: Sets given cookies.
		"""
		assert isinstance(cookies, (list, tuple)
		    ), "Argument 'cookies' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    cookies)
		subdom_funcs = self.synchronous_command('Network.setCookies', cookies=cookies
		    )
		return subdom_funcs

	def Network_canEmulateNetworkConditions(self):
		"""
		Function path: Network.canEmulateNetworkConditions
			Domain: Network
			Method name: canEmulateNetworkConditions
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'result' (type: boolean) -> True if emulation of network conditions is supported.
		
			Description: Tells whether emulation of network conditions is supported.
		"""
		subdom_funcs = self.synchronous_command('Network.canEmulateNetworkConditions'
		    )
		return subdom_funcs

	def Network_emulateNetworkConditions(self, offline, latency,
	    downloadThroughput, uploadThroughput, **kwargs):
		"""
		Function path: Network.emulateNetworkConditions
			Domain: Network
			Method name: emulateNetworkConditions
		
			Parameters:
				Required arguments:
					'offline' (type: boolean) -> True to emulate internet disconnection.
					'latency' (type: number) -> Minimum latency from request sent to response headers received (ms).
					'downloadThroughput' (type: number) -> Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
					'uploadThroughput' (type: number) -> Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
				Optional arguments:
					'connectionType' (type: ConnectionType) -> Connection type if known.
			No return value.
		
			Description: Activates emulation of network conditions.
		"""
		assert isinstance(offline, (bool,)
		    ), "Argument 'offline' must be of type '['bool']'. Received type: '%s'" % type(
		    offline)
		assert isinstance(latency, (float, int)
		    ), "Argument 'latency' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    latency)
		assert isinstance(downloadThroughput, (float, int)
		    ), "Argument 'downloadThroughput' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    downloadThroughput)
		assert isinstance(uploadThroughput, (float, int)
		    ), "Argument 'uploadThroughput' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    uploadThroughput)
		expected = ['connectionType']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['connectionType']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.emulateNetworkConditions',
		    offline=offline, latency=latency, downloadThroughput=
		    downloadThroughput, uploadThroughput=uploadThroughput, **kwargs)
		return subdom_funcs

	def Network_setCacheDisabled(self, cacheDisabled):
		"""
		Function path: Network.setCacheDisabled
			Domain: Network
			Method name: setCacheDisabled
		
			Parameters:
				Required arguments:
					'cacheDisabled' (type: boolean) -> Cache disabled state.
			No return value.
		
			Description: Toggles ignoring cache for each request. If <code>true</code>, cache will not be used.
		"""
		assert isinstance(cacheDisabled, (bool,)
		    ), "Argument 'cacheDisabled' must be of type '['bool']'. Received type: '%s'" % type(
		    cacheDisabled)
		subdom_funcs = self.synchronous_command('Network.setCacheDisabled',
		    cacheDisabled=cacheDisabled)
		return subdom_funcs

	def Network_setBypassServiceWorker(self, bypass):
		"""
		Function path: Network.setBypassServiceWorker
			Domain: Network
			Method name: setBypassServiceWorker
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'bypass' (type: boolean) -> Bypass service worker and load from network.
			No return value.
		
			Description: Toggles ignoring of service worker for each request.
		"""
		assert isinstance(bypass, (bool,)
		    ), "Argument 'bypass' must be of type '['bool']'. Received type: '%s'" % type(
		    bypass)
		subdom_funcs = self.synchronous_command('Network.setBypassServiceWorker',
		    bypass=bypass)
		return subdom_funcs

	def Network_setDataSizeLimitsForTest(self, maxTotalSize, maxResourceSize):
		"""
		Function path: Network.setDataSizeLimitsForTest
			Domain: Network
			Method name: setDataSizeLimitsForTest
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'maxTotalSize' (type: integer) -> Maximum total buffer size.
					'maxResourceSize' (type: integer) -> Maximum per-resource size.
			No return value.
		
			Description: For testing.
		"""
		assert isinstance(maxTotalSize, (int,)
		    ), "Argument 'maxTotalSize' must be of type '['int']'. Received type: '%s'" % type(
		    maxTotalSize)
		assert isinstance(maxResourceSize, (int,)
		    ), "Argument 'maxResourceSize' must be of type '['int']'. Received type: '%s'" % type(
		    maxResourceSize)
		subdom_funcs = self.synchronous_command('Network.setDataSizeLimitsForTest',
		    maxTotalSize=maxTotalSize, maxResourceSize=maxResourceSize)
		return subdom_funcs

	def Network_getCertificate(self, origin):
		"""
		Function path: Network.getCertificate
			Domain: Network
			Method name: getCertificate
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Origin to get certificate for.
			Returns:
				'tableNames' (type: array) -> No description
		
			Description: Returns the DER-encoded certificate.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		subdom_funcs = self.synchronous_command('Network.getCertificate', origin=
		    origin)
		return subdom_funcs

	def Network_setRequestInterceptionEnabled(self, enabled, **kwargs):
		"""
		Function path: Network.setRequestInterceptionEnabled
			Domain: Network
			Method name: setRequestInterceptionEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether requests should be intercepted. If patterns is not set, matches all and resets any previously set patterns. Other parameters are ignored if false.
				Optional arguments:
					'patterns' (type: array) -> URLs matching any of these patterns will be forwarded and wait for the corresponding continueInterceptedRequest call. Wildcards ('*' -> zero or more, '?' -> exactly one) are allowed. Escape character is backslash. If omitted equivalent to ['*'] (intercept all).
			No return value.
		
			Description: Sets the requests to intercept that match a the provided patterns.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		if 'patterns' in kwargs:
			assert isinstance(kwargs['patterns'], (list, tuple)
			    ), "Optional argument 'patterns' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['patterns'])
		expected = ['patterns']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['patterns']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'Network.setRequestInterceptionEnabled', enabled=enabled, **kwargs)
		return subdom_funcs

	def Network_continueInterceptedRequest(self, interceptionId, **kwargs):
		"""
		Function path: Network.continueInterceptedRequest
			Domain: Network
			Method name: continueInterceptedRequest
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'interceptionId' (type: InterceptionId) -> No description
				Optional arguments:
					'errorReason' (type: ErrorReason) -> If set this causes the request to fail with the given reason. Passing <code>Aborted</code> for requests marked with <code>isNavigationRequest</code> also cancels the navigation. Must not be set in response to an authChallenge.
					'rawResponse' (type: string) -> If set the requests completes using with the provided base64 encoded raw response, including HTTP status line and headers etc... Must not be set in response to an authChallenge.
					'url' (type: string) -> If set the request url will be modified in a way that's not observable by page. Must not be set in response to an authChallenge.
					'method' (type: string) -> If set this allows the request method to be overridden. Must not be set in response to an authChallenge.
					'postData' (type: string) -> If set this allows postData to be set. Must not be set in response to an authChallenge.
					'headers' (type: Headers) -> If set this allows the request headers to be changed. Must not be set in response to an authChallenge.
					'authChallengeResponse' (type: AuthChallengeResponse) -> Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
			No return value.
		
			Description: Response to Network.requestIntercepted which either modifies the request to continue with any modifications, or blocks it, or completes it with the provided response bytes. If a network fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted event will be sent with the same InterceptionId.
		"""
		if 'rawResponse' in kwargs:
			assert isinstance(kwargs['rawResponse'], (str,)
			    ), "Optional argument 'rawResponse' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['rawResponse'])
		if 'url' in kwargs:
			assert isinstance(kwargs['url'], (str,)
			    ), "Optional argument 'url' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['url'])
		if 'method' in kwargs:
			assert isinstance(kwargs['method'], (str,)
			    ), "Optional argument 'method' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['method'])
		if 'postData' in kwargs:
			assert isinstance(kwargs['postData'], (str,)
			    ), "Optional argument 'postData' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['postData'])
		expected = ['errorReason', 'rawResponse', 'url', 'method', 'postData',
		    'headers', 'authChallengeResponse']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['errorReason', 'rawResponse', 'url', 'method', 'postData', 'headers', 'authChallengeResponse']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.continueInterceptedRequest',
		    interceptionId=interceptionId, **kwargs)
		return subdom_funcs

	def Database_enable(self):
		"""
		Function path: Database.enable
			Domain: Database
			Method name: enable
		
			No return value.
		
			Description: Enables database tracking, database events will now be delivered to the client.
		"""
		subdom_funcs = self.synchronous_command('Database.enable')
		return subdom_funcs

	def Database_disable(self):
		"""
		Function path: Database.disable
			Domain: Database
			Method name: disable
		
			No return value.
		
			Description: Disables database tracking, prevents database events from being sent to the client.
		"""
		subdom_funcs = self.synchronous_command('Database.disable')
		return subdom_funcs

	def Database_getDatabaseTableNames(self, databaseId):
		"""
		Function path: Database.getDatabaseTableNames
			Domain: Database
			Method name: getDatabaseTableNames
		
			Parameters:
				Required arguments:
					'databaseId' (type: DatabaseId) -> No description
			Returns:
				'tableNames' (type: array) -> No description
		
		"""
		subdom_funcs = self.synchronous_command('Database.getDatabaseTableNames',
		    databaseId=databaseId)
		return subdom_funcs

	def Database_executeSQL(self, databaseId, query):
		"""
		Function path: Database.executeSQL
			Domain: Database
			Method name: executeSQL
		
			Parameters:
				Required arguments:
					'databaseId' (type: DatabaseId) -> No description
					'query' (type: string) -> No description
			Returns:
				'columnNames' (type: array) -> No description
				'values' (type: array) -> No description
				'sqlError' (type: Error) -> No description
		
		"""
		assert isinstance(query, (str,)
		    ), "Argument 'query' must be of type '['str']'. Received type: '%s'" % type(
		    query)
		subdom_funcs = self.synchronous_command('Database.executeSQL', databaseId
		    =databaseId, query=query)
		return subdom_funcs

	def IndexedDB_enable(self):
		"""
		Function path: IndexedDB.enable
			Domain: IndexedDB
			Method name: enable
		
			No return value.
		
			Description: Enables events from backend.
		"""
		subdom_funcs = self.synchronous_command('IndexedDB.enable')
		return subdom_funcs

	def IndexedDB_disable(self):
		"""
		Function path: IndexedDB.disable
			Domain: IndexedDB
			Method name: disable
		
			No return value.
		
			Description: Disables events from backend.
		"""
		subdom_funcs = self.synchronous_command('IndexedDB.disable')
		return subdom_funcs

	def IndexedDB_requestDatabaseNames(self, securityOrigin):
		"""
		Function path: IndexedDB.requestDatabaseNames
			Domain: IndexedDB
			Method name: requestDatabaseNames
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> Security origin.
			Returns:
				'databaseNames' (type: array) -> Database names for origin.
		
			Description: Requests database names for given security origin.
		"""
		assert isinstance(securityOrigin, (str,)
		    ), "Argument 'securityOrigin' must be of type '['str']'. Received type: '%s'" % type(
		    securityOrigin)
		subdom_funcs = self.synchronous_command('IndexedDB.requestDatabaseNames',
		    securityOrigin=securityOrigin)
		return subdom_funcs

	def IndexedDB_requestDatabase(self, securityOrigin, databaseName):
		"""
		Function path: IndexedDB.requestDatabase
			Domain: IndexedDB
			Method name: requestDatabase
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> Security origin.
					'databaseName' (type: string) -> Database name.
			Returns:
				'databaseWithObjectStores' (type: DatabaseWithObjectStores) -> Database with an array of object stores.
		
			Description: Requests database with given name in given frame.
		"""
		assert isinstance(securityOrigin, (str,)
		    ), "Argument 'securityOrigin' must be of type '['str']'. Received type: '%s'" % type(
		    securityOrigin)
		assert isinstance(databaseName, (str,)
		    ), "Argument 'databaseName' must be of type '['str']'. Received type: '%s'" % type(
		    databaseName)
		subdom_funcs = self.synchronous_command('IndexedDB.requestDatabase',
		    securityOrigin=securityOrigin, databaseName=databaseName)
		return subdom_funcs

	def IndexedDB_requestData(self, securityOrigin, databaseName,
	    objectStoreName, indexName, skipCount, pageSize, **kwargs):
		"""
		Function path: IndexedDB.requestData
			Domain: IndexedDB
			Method name: requestData
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> Security origin.
					'databaseName' (type: string) -> Database name.
					'objectStoreName' (type: string) -> Object store name.
					'indexName' (type: string) -> Index name, empty string for object store data requests.
					'skipCount' (type: integer) -> Number of records to skip.
					'pageSize' (type: integer) -> Number of records to fetch.
				Optional arguments:
					'keyRange' (type: KeyRange) -> Key range.
			Returns:
				'objectStoreDataEntries' (type: array) -> Array of object store data entries.
				'hasMore' (type: boolean) -> If true, there are more entries to fetch in the given range.
		
			Description: Requests data from object store or index.
		"""
		assert isinstance(securityOrigin, (str,)
		    ), "Argument 'securityOrigin' must be of type '['str']'. Received type: '%s'" % type(
		    securityOrigin)
		assert isinstance(databaseName, (str,)
		    ), "Argument 'databaseName' must be of type '['str']'. Received type: '%s'" % type(
		    databaseName)
		assert isinstance(objectStoreName, (str,)
		    ), "Argument 'objectStoreName' must be of type '['str']'. Received type: '%s'" % type(
		    objectStoreName)
		assert isinstance(indexName, (str,)
		    ), "Argument 'indexName' must be of type '['str']'. Received type: '%s'" % type(
		    indexName)
		assert isinstance(skipCount, (int,)
		    ), "Argument 'skipCount' must be of type '['int']'. Received type: '%s'" % type(
		    skipCount)
		assert isinstance(pageSize, (int,)
		    ), "Argument 'pageSize' must be of type '['int']'. Received type: '%s'" % type(
		    pageSize)
		expected = ['keyRange']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['keyRange']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('IndexedDB.requestData',
		    securityOrigin=securityOrigin, databaseName=databaseName,
		    objectStoreName=objectStoreName, indexName=indexName, skipCount=
		    skipCount, pageSize=pageSize, **kwargs)
		return subdom_funcs

	def IndexedDB_clearObjectStore(self, securityOrigin, databaseName,
	    objectStoreName):
		"""
		Function path: IndexedDB.clearObjectStore
			Domain: IndexedDB
			Method name: clearObjectStore
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> Security origin.
					'databaseName' (type: string) -> Database name.
					'objectStoreName' (type: string) -> Object store name.
			Returns:
		
			Description: Clears all entries from an object store.
		"""
		assert isinstance(securityOrigin, (str,)
		    ), "Argument 'securityOrigin' must be of type '['str']'. Received type: '%s'" % type(
		    securityOrigin)
		assert isinstance(databaseName, (str,)
		    ), "Argument 'databaseName' must be of type '['str']'. Received type: '%s'" % type(
		    databaseName)
		assert isinstance(objectStoreName, (str,)
		    ), "Argument 'objectStoreName' must be of type '['str']'. Received type: '%s'" % type(
		    objectStoreName)
		subdom_funcs = self.synchronous_command('IndexedDB.clearObjectStore',
		    securityOrigin=securityOrigin, databaseName=databaseName,
		    objectStoreName=objectStoreName)
		return subdom_funcs

	def IndexedDB_deleteDatabase(self, securityOrigin, databaseName):
		"""
		Function path: IndexedDB.deleteDatabase
			Domain: IndexedDB
			Method name: deleteDatabase
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> Security origin.
					'databaseName' (type: string) -> Database name.
			Returns:
		
			Description: Deletes a database.
		"""
		assert isinstance(securityOrigin, (str,)
		    ), "Argument 'securityOrigin' must be of type '['str']'. Received type: '%s'" % type(
		    securityOrigin)
		assert isinstance(databaseName, (str,)
		    ), "Argument 'databaseName' must be of type '['str']'. Received type: '%s'" % type(
		    databaseName)
		subdom_funcs = self.synchronous_command('IndexedDB.deleteDatabase',
		    securityOrigin=securityOrigin, databaseName=databaseName)
		return subdom_funcs

	def CacheStorage_requestCacheNames(self, securityOrigin):
		"""
		Function path: CacheStorage.requestCacheNames
			Domain: CacheStorage
			Method name: requestCacheNames
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> Security origin.
			Returns:
				'caches' (type: array) -> Caches for the security origin.
		
			Description: Requests cache names.
		"""
		assert isinstance(securityOrigin, (str,)
		    ), "Argument 'securityOrigin' must be of type '['str']'. Received type: '%s'" % type(
		    securityOrigin)
		subdom_funcs = self.synchronous_command('CacheStorage.requestCacheNames',
		    securityOrigin=securityOrigin)
		return subdom_funcs

	def CacheStorage_requestEntries(self, cacheId, skipCount, pageSize):
		"""
		Function path: CacheStorage.requestEntries
			Domain: CacheStorage
			Method name: requestEntries
		
			Parameters:
				Required arguments:
					'cacheId' (type: CacheId) -> ID of cache to get entries from.
					'skipCount' (type: integer) -> Number of records to skip.
					'pageSize' (type: integer) -> Number of records to fetch.
			Returns:
				'cacheDataEntries' (type: array) -> Array of object store data entries.
				'hasMore' (type: boolean) -> If true, there are more entries to fetch in the given range.
		
			Description: Requests data from cache.
		"""
		assert isinstance(skipCount, (int,)
		    ), "Argument 'skipCount' must be of type '['int']'. Received type: '%s'" % type(
		    skipCount)
		assert isinstance(pageSize, (int,)
		    ), "Argument 'pageSize' must be of type '['int']'. Received type: '%s'" % type(
		    pageSize)
		subdom_funcs = self.synchronous_command('CacheStorage.requestEntries',
		    cacheId=cacheId, skipCount=skipCount, pageSize=pageSize)
		return subdom_funcs

	def CacheStorage_deleteCache(self, cacheId):
		"""
		Function path: CacheStorage.deleteCache
			Domain: CacheStorage
			Method name: deleteCache
		
			Parameters:
				Required arguments:
					'cacheId' (type: CacheId) -> Id of cache for deletion.
			No return value.
		
			Description: Deletes a cache.
		"""
		subdom_funcs = self.synchronous_command('CacheStorage.deleteCache',
		    cacheId=cacheId)
		return subdom_funcs

	def CacheStorage_deleteEntry(self, cacheId, request):
		"""
		Function path: CacheStorage.deleteEntry
			Domain: CacheStorage
			Method name: deleteEntry
		
			Parameters:
				Required arguments:
					'cacheId' (type: CacheId) -> Id of cache where the entry will be deleted.
					'request' (type: string) -> URL spec of the request.
			No return value.
		
			Description: Deletes a cache entry.
		"""
		assert isinstance(request, (str,)
		    ), "Argument 'request' must be of type '['str']'. Received type: '%s'" % type(
		    request)
		subdom_funcs = self.synchronous_command('CacheStorage.deleteEntry',
		    cacheId=cacheId, request=request)
		return subdom_funcs

	def CacheStorage_requestCachedResponse(self, cacheId, requestURL):
		"""
		Function path: CacheStorage.requestCachedResponse
			Domain: CacheStorage
			Method name: requestCachedResponse
		
			Parameters:
				Required arguments:
					'cacheId' (type: CacheId) -> Id of cache that contains the enty.
					'requestURL' (type: string) -> URL spec of the request.
			Returns:
				'response' (type: CachedResponse) -> Response read from the cache.
		
			Description: Fetches cache entry.
		"""
		assert isinstance(requestURL, (str,)
		    ), "Argument 'requestURL' must be of type '['str']'. Received type: '%s'" % type(
		    requestURL)
		subdom_funcs = self.synchronous_command('CacheStorage.requestCachedResponse',
		    cacheId=cacheId, requestURL=requestURL)
		return subdom_funcs

	def DOMStorage_enable(self):
		"""
		Function path: DOMStorage.enable
			Domain: DOMStorage
			Method name: enable
		
			No return value.
		
			Description: Enables storage tracking, storage events will now be delivered to the client.
		"""
		subdom_funcs = self.synchronous_command('DOMStorage.enable')
		return subdom_funcs

	def DOMStorage_disable(self):
		"""
		Function path: DOMStorage.disable
			Domain: DOMStorage
			Method name: disable
		
			No return value.
		
			Description: Disables storage tracking, prevents storage events from being sent to the client.
		"""
		subdom_funcs = self.synchronous_command('DOMStorage.disable')
		return subdom_funcs

	def DOMStorage_clear(self, storageId):
		"""
		Function path: DOMStorage.clear
			Domain: DOMStorage
			Method name: clear
		
			Parameters:
				Required arguments:
					'storageId' (type: StorageId) -> No description
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('DOMStorage.clear', storageId=
		    storageId)
		return subdom_funcs

	def DOMStorage_getDOMStorageItems(self, storageId):
		"""
		Function path: DOMStorage.getDOMStorageItems
			Domain: DOMStorage
			Method name: getDOMStorageItems
		
			Parameters:
				Required arguments:
					'storageId' (type: StorageId) -> No description
			Returns:
				'entries' (type: array) -> No description
		
		"""
		subdom_funcs = self.synchronous_command('DOMStorage.getDOMStorageItems',
		    storageId=storageId)
		return subdom_funcs

	def DOMStorage_setDOMStorageItem(self, storageId, key, value):
		"""
		Function path: DOMStorage.setDOMStorageItem
			Domain: DOMStorage
			Method name: setDOMStorageItem
		
			Parameters:
				Required arguments:
					'storageId' (type: StorageId) -> No description
					'key' (type: string) -> No description
					'value' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(key, (str,)
		    ), "Argument 'key' must be of type '['str']'. Received type: '%s'" % type(
		    key)
		assert isinstance(value, (str,)
		    ), "Argument 'value' must be of type '['str']'. Received type: '%s'" % type(
		    value)
		subdom_funcs = self.synchronous_command('DOMStorage.setDOMStorageItem',
		    storageId=storageId, key=key, value=value)
		return subdom_funcs

	def DOMStorage_removeDOMStorageItem(self, storageId, key):
		"""
		Function path: DOMStorage.removeDOMStorageItem
			Domain: DOMStorage
			Method name: removeDOMStorageItem
		
			Parameters:
				Required arguments:
					'storageId' (type: StorageId) -> No description
					'key' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(key, (str,)
		    ), "Argument 'key' must be of type '['str']'. Received type: '%s'" % type(
		    key)
		subdom_funcs = self.synchronous_command('DOMStorage.removeDOMStorageItem',
		    storageId=storageId, key=key)
		return subdom_funcs

	def ApplicationCache_getFramesWithManifests(self):
		"""
		Function path: ApplicationCache.getFramesWithManifests
			Domain: ApplicationCache
			Method name: getFramesWithManifests
		
			Returns:
				'frameIds' (type: array) -> Array of frame identifiers with manifest urls for each frame containing a document associated with some application cache.
		
			Description: Returns array of frame identifiers with manifest urls for each frame containing a document associated with some application cache.
		"""
		subdom_funcs = self.synchronous_command(
		    'ApplicationCache.getFramesWithManifests')
		return subdom_funcs

	def ApplicationCache_enable(self):
		"""
		Function path: ApplicationCache.enable
			Domain: ApplicationCache
			Method name: enable
		
			No return value.
		
			Description: Enables application cache domain notifications.
		"""
		subdom_funcs = self.synchronous_command('ApplicationCache.enable')
		return subdom_funcs

	def ApplicationCache_getManifestForFrame(self, frameId):
		"""
		Function path: ApplicationCache.getManifestForFrame
			Domain: ApplicationCache
			Method name: getManifestForFrame
		
			Parameters:
				Required arguments:
					'frameId' (type: Page.FrameId) -> Identifier of the frame containing document whose manifest is retrieved.
			Returns:
				'manifestURL' (type: string) -> Manifest URL for document in the given frame.
		
			Description: Returns manifest URL for document in the given frame.
		"""
		subdom_funcs = self.synchronous_command(
		    'ApplicationCache.getManifestForFrame', frameId=frameId)
		return subdom_funcs

	def ApplicationCache_getApplicationCacheForFrame(self, frameId):
		"""
		Function path: ApplicationCache.getApplicationCacheForFrame
			Domain: ApplicationCache
			Method name: getApplicationCacheForFrame
		
			Parameters:
				Required arguments:
					'frameId' (type: Page.FrameId) -> Identifier of the frame containing document whose application cache is retrieved.
			Returns:
				'applicationCache' (type: ApplicationCache) -> Relevant application cache data for the document in given frame.
		
			Description: Returns relevant application cache data for the document in given frame.
		"""
		subdom_funcs = self.synchronous_command(
		    'ApplicationCache.getApplicationCacheForFrame', frameId=frameId)
		return subdom_funcs

	def DOM_enable(self):
		"""
		Function path: DOM.enable
			Domain: DOM
			Method name: enable
		
			No return value.
		
			Description: Enables DOM agent for the given page.
		"""
		subdom_funcs = self.synchronous_command('DOM.enable')
		return subdom_funcs

	def DOM_disable(self):
		"""
		Function path: DOM.disable
			Domain: DOM
			Method name: disable
		
			No return value.
		
			Description: Disables DOM agent for the given page.
		"""
		subdom_funcs = self.synchronous_command('DOM.disable')
		return subdom_funcs

	def DOM_getDocument(self, **kwargs):
		"""
		Function path: DOM.getDocument
			Domain: DOM
			Method name: getDocument
		
			Parameters:
				Optional arguments:
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
			Returns:
				'root' (type: Node) -> Resulting node.
		
			Description: Returns the root DOM node (and optionally the subtree) to the caller.
		"""
		if 'depth' in kwargs:
			assert isinstance(kwargs['depth'], (int,)
			    ), "Optional argument 'depth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['depth'])
		if 'pierce' in kwargs:
			assert isinstance(kwargs['pierce'], (bool,)
			    ), "Optional argument 'pierce' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['pierce'])
		expected = ['depth', 'pierce']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['depth', 'pierce']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getDocument', **kwargs)
		return subdom_funcs

	def DOM_getFlattenedDocument(self, **kwargs):
		"""
		Function path: DOM.getFlattenedDocument
			Domain: DOM
			Method name: getFlattenedDocument
		
			Parameters:
				Optional arguments:
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
			Returns:
				'nodes' (type: array) -> Resulting node.
		
			Description: Returns the root DOM node (and optionally the subtree) to the caller.
		"""
		if 'depth' in kwargs:
			assert isinstance(kwargs['depth'], (int,)
			    ), "Optional argument 'depth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['depth'])
		if 'pierce' in kwargs:
			assert isinstance(kwargs['pierce'], (bool,)
			    ), "Optional argument 'pierce' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['pierce'])
		expected = ['depth', 'pierce']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['depth', 'pierce']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getFlattenedDocument', **kwargs)
		return subdom_funcs

	def DOM_collectClassNamesFromSubtree(self, nodeId):
		"""
		Function path: DOM.collectClassNamesFromSubtree
			Domain: DOM
			Method name: collectClassNamesFromSubtree
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to collect class names.
			Returns:
				'classNames' (type: array) -> Class name list.
		
			Description: Collects class names for the node with given id and all of it's child nodes.
		"""
		subdom_funcs = self.synchronous_command('DOM.collectClassNamesFromSubtree',
		    nodeId=nodeId)
		return subdom_funcs

	def DOM_requestChildNodes(self, nodeId, **kwargs):
		"""
		Function path: DOM.requestChildNodes
			Domain: DOM
			Method name: requestChildNodes
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to get children for.
				Optional arguments:
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the sub-tree (default is false).
			No return value.
		
			Description: Requests that children of the node with given id are returned to the caller in form of <code>setChildNodes</code> events where not only immediate children are retrieved, but all children down to the specified depth.
		"""
		if 'depth' in kwargs:
			assert isinstance(kwargs['depth'], (int,)
			    ), "Optional argument 'depth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['depth'])
		if 'pierce' in kwargs:
			assert isinstance(kwargs['pierce'], (bool,)
			    ), "Optional argument 'pierce' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['pierce'])
		expected = ['depth', 'pierce']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['depth', 'pierce']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.requestChildNodes', nodeId=
		    nodeId, **kwargs)
		return subdom_funcs

	def DOM_querySelector(self, nodeId, selector):
		"""
		Function path: DOM.querySelector
			Domain: DOM
			Method name: querySelector
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to query upon.
					'selector' (type: string) -> Selector string.
			Returns:
				'nodeId' (type: NodeId) -> Query selector result.
		
			Description: Executes <code>querySelector</code> on a given node.
		"""
		assert isinstance(selector, (str,)
		    ), "Argument 'selector' must be of type '['str']'. Received type: '%s'" % type(
		    selector)
		subdom_funcs = self.synchronous_command('DOM.querySelector', nodeId=
		    nodeId, selector=selector)
		return subdom_funcs

	def DOM_querySelectorAll(self, nodeId, selector):
		"""
		Function path: DOM.querySelectorAll
			Domain: DOM
			Method name: querySelectorAll
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to query upon.
					'selector' (type: string) -> Selector string.
			Returns:
				'nodeIds' (type: array) -> Query selector result.
		
			Description: Executes <code>querySelectorAll</code> on a given node.
		"""
		assert isinstance(selector, (str,)
		    ), "Argument 'selector' must be of type '['str']'. Received type: '%s'" % type(
		    selector)
		subdom_funcs = self.synchronous_command('DOM.querySelectorAll', nodeId=
		    nodeId, selector=selector)
		return subdom_funcs

	def DOM_setNodeName(self, nodeId, name):
		"""
		Function path: DOM.setNodeName
			Domain: DOM
			Method name: setNodeName
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to set name for.
					'name' (type: string) -> New node's name.
			Returns:
				'nodeId' (type: NodeId) -> New node's id.
		
			Description: Sets node name for a node with given id.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		subdom_funcs = self.synchronous_command('DOM.setNodeName', nodeId=nodeId,
		    name=name)
		return subdom_funcs

	def DOM_setNodeValue(self, nodeId, value):
		"""
		Function path: DOM.setNodeValue
			Domain: DOM
			Method name: setNodeValue
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to set value for.
					'value' (type: string) -> New node's value.
			No return value.
		
			Description: Sets node value for a node with given id.
		"""
		assert isinstance(value, (str,)
		    ), "Argument 'value' must be of type '['str']'. Received type: '%s'" % type(
		    value)
		subdom_funcs = self.synchronous_command('DOM.setNodeValue', nodeId=nodeId,
		    value=value)
		return subdom_funcs

	def DOM_removeNode(self, nodeId):
		"""
		Function path: DOM.removeNode
			Domain: DOM
			Method name: removeNode
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to remove.
			No return value.
		
			Description: Removes node with given id.
		"""
		subdom_funcs = self.synchronous_command('DOM.removeNode', nodeId=nodeId)
		return subdom_funcs

	def DOM_setAttributeValue(self, nodeId, name, value):
		"""
		Function path: DOM.setAttributeValue
			Domain: DOM
			Method name: setAttributeValue
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the element to set attribute for.
					'name' (type: string) -> Attribute name.
					'value' (type: string) -> Attribute value.
			No return value.
		
			Description: Sets attribute for an element with given id.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		assert isinstance(value, (str,)
		    ), "Argument 'value' must be of type '['str']'. Received type: '%s'" % type(
		    value)
		subdom_funcs = self.synchronous_command('DOM.setAttributeValue', nodeId=
		    nodeId, name=name, value=value)
		return subdom_funcs

	def DOM_setAttributesAsText(self, nodeId, text, **kwargs):
		"""
		Function path: DOM.setAttributesAsText
			Domain: DOM
			Method name: setAttributesAsText
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the element to set attributes for.
					'text' (type: string) -> Text with a number of attributes. Will parse this text using HTML parser.
				Optional arguments:
					'name' (type: string) -> Attribute name to replace with new attributes derived from text in case text parsed successfully.
			No return value.
		
			Description: Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs.
		"""
		assert isinstance(text, (str,)
		    ), "Argument 'text' must be of type '['str']'. Received type: '%s'" % type(
		    text)
		if 'name' in kwargs:
			assert isinstance(kwargs['name'], (str,)
			    ), "Optional argument 'name' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['name'])
		expected = ['name']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['name']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.setAttributesAsText', nodeId
		    =nodeId, text=text, **kwargs)
		return subdom_funcs

	def DOM_removeAttribute(self, nodeId, name):
		"""
		Function path: DOM.removeAttribute
			Domain: DOM
			Method name: removeAttribute
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the element to remove attribute from.
					'name' (type: string) -> Name of the attribute to remove.
			No return value.
		
			Description: Removes attribute with given name from an element with given id.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		subdom_funcs = self.synchronous_command('DOM.removeAttribute', nodeId=
		    nodeId, name=name)
		return subdom_funcs

	def DOM_getOuterHTML(self, **kwargs):
		"""
		Function path: DOM.getOuterHTML
			Domain: DOM
			Method name: getOuterHTML
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
			Returns:
				'outerHTML' (type: string) -> Outer HTML markup.
		
			Description: Returns node's HTML markup.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getOuterHTML', **kwargs)
		return subdom_funcs

	def DOM_setOuterHTML(self, nodeId, outerHTML):
		"""
		Function path: DOM.setOuterHTML
			Domain: DOM
			Method name: setOuterHTML
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to set markup for.
					'outerHTML' (type: string) -> Outer HTML markup to set.
			No return value.
		
			Description: Sets node HTML markup, returns new node id.
		"""
		assert isinstance(outerHTML, (str,)
		    ), "Argument 'outerHTML' must be of type '['str']'. Received type: '%s'" % type(
		    outerHTML)
		subdom_funcs = self.synchronous_command('DOM.setOuterHTML', nodeId=nodeId,
		    outerHTML=outerHTML)
		return subdom_funcs

	def DOM_performSearch(self, query, **kwargs):
		"""
		Function path: DOM.performSearch
			Domain: DOM
			Method name: performSearch
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'query' (type: string) -> Plain text or query selector or XPath search query.
				Optional arguments:
					'includeUserAgentShadowDOM' (type: boolean) -> True to search in user agent shadow DOM.
			Returns:
				'searchId' (type: string) -> Unique search session identifier.
				'resultCount' (type: integer) -> Number of search results.
		
			Description: Searches for a given string in the DOM tree. Use <code>getSearchResults</code> to access search results or <code>cancelSearch</code> to end this search session.
		"""
		assert isinstance(query, (str,)
		    ), "Argument 'query' must be of type '['str']'. Received type: '%s'" % type(
		    query)
		if 'includeUserAgentShadowDOM' in kwargs:
			assert isinstance(kwargs['includeUserAgentShadowDOM'], (bool,)
			    ), "Optional argument 'includeUserAgentShadowDOM' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeUserAgentShadowDOM'])
		expected = ['includeUserAgentShadowDOM']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['includeUserAgentShadowDOM']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.performSearch', query=query,
		    **kwargs)
		return subdom_funcs

	def DOM_getSearchResults(self, searchId, fromIndex, toIndex):
		"""
		Function path: DOM.getSearchResults
			Domain: DOM
			Method name: getSearchResults
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'searchId' (type: string) -> Unique search session identifier.
					'fromIndex' (type: integer) -> Start index of the search result to be returned.
					'toIndex' (type: integer) -> End index of the search result to be returned.
			Returns:
				'nodeIds' (type: array) -> Ids of the search result nodes.
		
			Description: Returns search results from given <code>fromIndex</code> to given <code>toIndex</code> from the sarch with the given identifier.
		"""
		assert isinstance(searchId, (str,)
		    ), "Argument 'searchId' must be of type '['str']'. Received type: '%s'" % type(
		    searchId)
		assert isinstance(fromIndex, (int,)
		    ), "Argument 'fromIndex' must be of type '['int']'. Received type: '%s'" % type(
		    fromIndex)
		assert isinstance(toIndex, (int,)
		    ), "Argument 'toIndex' must be of type '['int']'. Received type: '%s'" % type(
		    toIndex)
		subdom_funcs = self.synchronous_command('DOM.getSearchResults', searchId=
		    searchId, fromIndex=fromIndex, toIndex=toIndex)
		return subdom_funcs

	def DOM_discardSearchResults(self, searchId):
		"""
		Function path: DOM.discardSearchResults
			Domain: DOM
			Method name: discardSearchResults
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'searchId' (type: string) -> Unique search session identifier.
			No return value.
		
			Description: Discards search results from the session with the given id. <code>getSearchResults</code> should no longer be called for that search.
		"""
		assert isinstance(searchId, (str,)
		    ), "Argument 'searchId' must be of type '['str']'. Received type: '%s'" % type(
		    searchId)
		subdom_funcs = self.synchronous_command('DOM.discardSearchResults',
		    searchId=searchId)
		return subdom_funcs

	def DOM_requestNode(self, objectId):
		"""
		Function path: DOM.requestNode
			Domain: DOM
			Method name: requestNode
		
			Parameters:
				Required arguments:
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id to convert into node.
			Returns:
				'nodeId' (type: NodeId) -> Node id for given object.
		
			Description: Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of <code>setChildNodes</code> notifications.
		"""
		subdom_funcs = self.synchronous_command('DOM.requestNode', objectId=objectId)
		return subdom_funcs

	def DOM_highlightRect(self):
		"""
		Function path: DOM.highlightRect
			Domain: DOM
			Method name: highlightRect
		
			No return value.
		
			Description: Highlights given rectangle.
		"""
		subdom_funcs = self.synchronous_command('DOM.highlightRect')
		return subdom_funcs

	def DOM_highlightNode(self):
		"""
		Function path: DOM.highlightNode
			Domain: DOM
			Method name: highlightNode
		
			No return value.
		
			Description: Highlights DOM node.
		"""
		subdom_funcs = self.synchronous_command('DOM.highlightNode')
		return subdom_funcs

	def DOM_hideHighlight(self):
		"""
		Function path: DOM.hideHighlight
			Domain: DOM
			Method name: hideHighlight
		
			No return value.
		
			Description: Hides any highlight.
		"""
		subdom_funcs = self.synchronous_command('DOM.hideHighlight')
		return subdom_funcs

	def DOM_pushNodeByPathToFrontend(self, path):
		"""
		Function path: DOM.pushNodeByPathToFrontend
			Domain: DOM
			Method name: pushNodeByPathToFrontend
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'path' (type: string) -> Path to node in the proprietary format.
			Returns:
				'nodeId' (type: NodeId) -> Id of the node for given path.
		
			Description: Requests that the node is sent to the caller given its path. // FIXME, use XPath
		"""
		assert isinstance(path, (str,)
		    ), "Argument 'path' must be of type '['str']'. Received type: '%s'" % type(
		    path)
		subdom_funcs = self.synchronous_command('DOM.pushNodeByPathToFrontend',
		    path=path)
		return subdom_funcs

	def DOM_pushNodesByBackendIdsToFrontend(self, backendNodeIds):
		"""
		Function path: DOM.pushNodesByBackendIdsToFrontend
			Domain: DOM
			Method name: pushNodesByBackendIdsToFrontend
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'backendNodeIds' (type: array) -> The array of backend node ids.
			Returns:
				'nodeIds' (type: array) -> The array of ids of pushed nodes that correspond to the backend ids specified in backendNodeIds.
		
			Description: Requests that a batch of nodes is sent to the caller given their backend node ids.
		"""
		assert isinstance(backendNodeIds, (list, tuple)
		    ), "Argument 'backendNodeIds' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    backendNodeIds)
		subdom_funcs = self.synchronous_command('DOM.pushNodesByBackendIdsToFrontend'
		    , backendNodeIds=backendNodeIds)
		return subdom_funcs

	def DOM_setInspectedNode(self, nodeId):
		"""
		Function path: DOM.setInspectedNode
			Domain: DOM
			Method name: setInspectedNode
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> DOM node id to be accessible by means of $x command line API.
			No return value.
		
			Description: Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).
		"""
		subdom_funcs = self.synchronous_command('DOM.setInspectedNode', nodeId=nodeId
		    )
		return subdom_funcs

	def DOM_resolveNode(self, **kwargs):
		"""
		Function path: DOM.resolveNode
			Domain: DOM
			Method name: resolveNode
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Id of the node to resolve.
					'backendNodeId' (type: DOM.BackendNodeId) -> Backend identifier of the node to resolve.
					'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects.
			Returns:
				'object' (type: Runtime.RemoteObject) -> JavaScript object wrapper for given node.
		
			Description: Resolves the JavaScript node object for a given NodeId or BackendNodeId.
		"""
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		expected = ['nodeId', 'backendNodeId', 'objectGroup']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectGroup']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.resolveNode', **kwargs)
		return subdom_funcs

	def DOM_getAttributes(self, nodeId):
		"""
		Function path: DOM.getAttributes
			Domain: DOM
			Method name: getAttributes
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to retrieve attibutes for.
			Returns:
				'attributes' (type: array) -> An interleaved array of node attribute names and values.
		
			Description: Returns attributes for the specified node.
		"""
		subdom_funcs = self.synchronous_command('DOM.getAttributes', nodeId=nodeId)
		return subdom_funcs

	def DOM_copyTo(self, nodeId, targetNodeId, **kwargs):
		"""
		Function path: DOM.copyTo
			Domain: DOM
			Method name: copyTo
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to copy.
					'targetNodeId' (type: NodeId) -> Id of the element to drop the copy into.
				Optional arguments:
					'insertBeforeNodeId' (type: NodeId) -> Drop the copy before this node (if absent, the copy becomes the last child of <code>targetNodeId</code>).
			Returns:
				'nodeId' (type: NodeId) -> Id of the node clone.
		
			Description: Creates a deep copy of the specified node and places it into the target container before the given anchor.
		"""
		expected = ['insertBeforeNodeId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['insertBeforeNodeId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.copyTo', nodeId=nodeId,
		    targetNodeId=targetNodeId, **kwargs)
		return subdom_funcs

	def DOM_moveTo(self, nodeId, targetNodeId, **kwargs):
		"""
		Function path: DOM.moveTo
			Domain: DOM
			Method name: moveTo
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to move.
					'targetNodeId' (type: NodeId) -> Id of the element to drop the moved node into.
				Optional arguments:
					'insertBeforeNodeId' (type: NodeId) -> Drop node before this one (if absent, the moved node becomes the last child of <code>targetNodeId</code>).
			Returns:
				'nodeId' (type: NodeId) -> New id of the moved node.
		
			Description: Moves node into the new container, places it before the given anchor.
		"""
		expected = ['insertBeforeNodeId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['insertBeforeNodeId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.moveTo', nodeId=nodeId,
		    targetNodeId=targetNodeId, **kwargs)
		return subdom_funcs

	def DOM_undo(self):
		"""
		Function path: DOM.undo
			Domain: DOM
			Method name: undo
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Undoes the last performed action.
		"""
		subdom_funcs = self.synchronous_command('DOM.undo')
		return subdom_funcs

	def DOM_redo(self):
		"""
		Function path: DOM.redo
			Domain: DOM
			Method name: redo
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Re-does the last undone action.
		"""
		subdom_funcs = self.synchronous_command('DOM.redo')
		return subdom_funcs

	def DOM_markUndoableState(self):
		"""
		Function path: DOM.markUndoableState
			Domain: DOM
			Method name: markUndoableState
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Marks last undoable state.
		"""
		subdom_funcs = self.synchronous_command('DOM.markUndoableState')
		return subdom_funcs

	def DOM_focus(self, **kwargs):
		"""
		Function path: DOM.focus
			Domain: DOM
			Method name: focus
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
			No return value.
		
			Description: Focuses the given element.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.focus', **kwargs)
		return subdom_funcs

	def DOM_setFileInputFiles(self, files, **kwargs):
		"""
		Function path: DOM.setFileInputFiles
			Domain: DOM
			Method name: setFileInputFiles
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'files' (type: array) -> Array of file paths to set.
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
			No return value.
		
			Description: Sets files for the given file input element.
		"""
		assert isinstance(files, (list, tuple)
		    ), "Argument 'files' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    files)
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.setFileInputFiles', files=
		    files, **kwargs)
		return subdom_funcs

	def DOM_getBoxModel(self, **kwargs):
		"""
		Function path: DOM.getBoxModel
			Domain: DOM
			Method name: getBoxModel
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
			Returns:
				'model' (type: BoxModel) -> Box model for the node.
		
			Description: Returns boxes for the currently selected nodes.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getBoxModel', **kwargs)
		return subdom_funcs

	def DOM_getNodeForLocation(self, x, y, **kwargs):
		"""
		Function path: DOM.getNodeForLocation
			Domain: DOM
			Method name: getNodeForLocation
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'x' (type: integer) -> X coordinate.
					'y' (type: integer) -> Y coordinate.
				Optional arguments:
					'includeUserAgentShadowDOM' (type: boolean) -> False to skip to the nearest non-UA shadow root ancestor (default: false).
			Returns:
				'nodeId' (type: NodeId) -> Id of the node at given coordinates.
		
			Description: Returns node id at given location.
		"""
		assert isinstance(x, (int,)
		    ), "Argument 'x' must be of type '['int']'. Received type: '%s'" % type(x
		    )
		assert isinstance(y, (int,)
		    ), "Argument 'y' must be of type '['int']'. Received type: '%s'" % type(y
		    )
		if 'includeUserAgentShadowDOM' in kwargs:
			assert isinstance(kwargs['includeUserAgentShadowDOM'], (bool,)
			    ), "Optional argument 'includeUserAgentShadowDOM' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeUserAgentShadowDOM'])
		expected = ['includeUserAgentShadowDOM']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['includeUserAgentShadowDOM']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getNodeForLocation', x=x, y=
		    y, **kwargs)
		return subdom_funcs

	def DOM_getRelayoutBoundary(self, nodeId):
		"""
		Function path: DOM.getRelayoutBoundary
			Domain: DOM
			Method name: getRelayoutBoundary
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node.
			Returns:
				'nodeId' (type: NodeId) -> Relayout boundary node id for the given node.
		
			Description: Returns the id of the nearest ancestor that is a relayout boundary.
		"""
		subdom_funcs = self.synchronous_command('DOM.getRelayoutBoundary', nodeId
		    =nodeId)
		return subdom_funcs

	def DOM_describeNode(self, **kwargs):
		"""
		Function path: DOM.describeNode
			Domain: DOM
			Method name: describeNode
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false).
			Returns:
				'node' (type: Node) -> Node description.
		
			Description: Describes node given its id, does not require domain to be enabled. Does not start tracking any objects, can be used for automation.
		"""
		if 'depth' in kwargs:
			assert isinstance(kwargs['depth'], (int,)
			    ), "Optional argument 'depth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['depth'])
		if 'pierce' in kwargs:
			assert isinstance(kwargs['pierce'], (bool,)
			    ), "Optional argument 'pierce' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['pierce'])
		expected = ['nodeId', 'backendNodeId', 'objectId', 'depth', 'pierce']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId', 'depth', 'pierce']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.describeNode', **kwargs)
		return subdom_funcs

	def CSS_enable(self):
		"""
		Function path: CSS.enable
			Domain: CSS
			Method name: enable
		
			No return value.
		
			Description: Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received.
		"""
		subdom_funcs = self.synchronous_command('CSS.enable')
		return subdom_funcs

	def CSS_disable(self):
		"""
		Function path: CSS.disable
			Domain: CSS
			Method name: disable
		
			No return value.
		
			Description: Disables the CSS agent for the given page.
		"""
		subdom_funcs = self.synchronous_command('CSS.disable')
		return subdom_funcs

	def CSS_getMatchedStylesForNode(self, nodeId):
		"""
		Function path: CSS.getMatchedStylesForNode
			Domain: CSS
			Method name: getMatchedStylesForNode
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> No description
			Returns:
				'inlineStyle' (type: CSSStyle) -> Inline style for the specified DOM node.
				'attributesStyle' (type: CSSStyle) -> Attribute-defined element style (e.g. resulting from "width=20 height=100%").
				'matchedCSSRules' (type: array) -> CSS rules matching this node, from all applicable stylesheets.
				'pseudoElements' (type: array) -> Pseudo style matches for this node.
				'inherited' (type: array) -> A chain of inherited styles (from the immediate node parent up to the DOM tree root).
				'cssKeyframesRules' (type: array) -> A list of CSS keyframed animations matching this node.
		
			Description: Returns requested styles for a DOM node identified by <code>nodeId</code>.
		"""
		subdom_funcs = self.synchronous_command('CSS.getMatchedStylesForNode',
		    nodeId=nodeId)
		return subdom_funcs

	def CSS_getInlineStylesForNode(self, nodeId):
		"""
		Function path: CSS.getInlineStylesForNode
			Domain: CSS
			Method name: getInlineStylesForNode
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> No description
			Returns:
				'inlineStyle' (type: CSSStyle) -> Inline style for the specified DOM node.
				'attributesStyle' (type: CSSStyle) -> Attribute-defined element style (e.g. resulting from "width=20 height=100%").
		
			Description: Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by <code>nodeId</code>.
		"""
		subdom_funcs = self.synchronous_command('CSS.getInlineStylesForNode',
		    nodeId=nodeId)
		return subdom_funcs

	def CSS_getComputedStyleForNode(self, nodeId):
		"""
		Function path: CSS.getComputedStyleForNode
			Domain: CSS
			Method name: getComputedStyleForNode
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> No description
			Returns:
				'computedStyle' (type: array) -> Computed style for the specified DOM node.
		
			Description: Returns the computed style for a DOM node identified by <code>nodeId</code>.
		"""
		subdom_funcs = self.synchronous_command('CSS.getComputedStyleForNode',
		    nodeId=nodeId)
		return subdom_funcs

	def CSS_getPlatformFontsForNode(self, nodeId):
		"""
		Function path: CSS.getPlatformFontsForNode
			Domain: CSS
			Method name: getPlatformFontsForNode
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> No description
			Returns:
				'fonts' (type: array) -> Usage statistics for every employed platform font.
		
			Description: Requests information about platform fonts which we used to render child TextNodes in the given node.
		"""
		subdom_funcs = self.synchronous_command('CSS.getPlatformFontsForNode',
		    nodeId=nodeId)
		return subdom_funcs

	def CSS_getStyleSheetText(self, styleSheetId):
		"""
		Function path: CSS.getStyleSheetText
			Domain: CSS
			Method name: getStyleSheetText
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> No description
			Returns:
				'text' (type: string) -> The stylesheet text.
		
			Description: Returns the current textual content and the URL for a stylesheet.
		"""
		subdom_funcs = self.synchronous_command('CSS.getStyleSheetText',
		    styleSheetId=styleSheetId)
		return subdom_funcs

	def CSS_collectClassNames(self, styleSheetId):
		"""
		Function path: CSS.collectClassNames
			Domain: CSS
			Method name: collectClassNames
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> No description
			Returns:
				'classNames' (type: array) -> Class name list.
		
			Description: Returns all class names from specified stylesheet.
		"""
		subdom_funcs = self.synchronous_command('CSS.collectClassNames',
		    styleSheetId=styleSheetId)
		return subdom_funcs

	def CSS_setStyleSheetText(self, styleSheetId, text):
		"""
		Function path: CSS.setStyleSheetText
			Domain: CSS
			Method name: setStyleSheetText
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> No description
					'text' (type: string) -> No description
			Returns:
				'sourceMapURL' (type: string) -> URL of source map associated with script (if any).
		
			Description: Sets the new stylesheet text.
		"""
		assert isinstance(text, (str,)
		    ), "Argument 'text' must be of type '['str']'. Received type: '%s'" % type(
		    text)
		subdom_funcs = self.synchronous_command('CSS.setStyleSheetText',
		    styleSheetId=styleSheetId, text=text)
		return subdom_funcs

	def CSS_setRuleSelector(self, styleSheetId, range, selector):
		"""
		Function path: CSS.setRuleSelector
			Domain: CSS
			Method name: setRuleSelector
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> No description
					'range' (type: SourceRange) -> No description
					'selector' (type: string) -> No description
			Returns:
				'selectorList' (type: SelectorList) -> The resulting selector list after modification.
		
			Description: Modifies the rule selector.
		"""
		assert isinstance(selector, (str,)
		    ), "Argument 'selector' must be of type '['str']'. Received type: '%s'" % type(
		    selector)
		subdom_funcs = self.synchronous_command('CSS.setRuleSelector',
		    styleSheetId=styleSheetId, range=range, selector=selector)
		return subdom_funcs

	def CSS_setKeyframeKey(self, styleSheetId, range, keyText):
		"""
		Function path: CSS.setKeyframeKey
			Domain: CSS
			Method name: setKeyframeKey
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> No description
					'range' (type: SourceRange) -> No description
					'keyText' (type: string) -> No description
			Returns:
				'keyText' (type: Value) -> The resulting key text after modification.
		
			Description: Modifies the keyframe rule key text.
		"""
		assert isinstance(keyText, (str,)
		    ), "Argument 'keyText' must be of type '['str']'. Received type: '%s'" % type(
		    keyText)
		subdom_funcs = self.synchronous_command('CSS.setKeyframeKey',
		    styleSheetId=styleSheetId, range=range, keyText=keyText)
		return subdom_funcs

	def CSS_setStyleTexts(self, edits):
		"""
		Function path: CSS.setStyleTexts
			Domain: CSS
			Method name: setStyleTexts
		
			Parameters:
				Required arguments:
					'edits' (type: array) -> No description
			Returns:
				'styles' (type: array) -> The resulting styles after modification.
		
			Description: Applies specified style edits one after another in the given order.
		"""
		assert isinstance(edits, (list, tuple)
		    ), "Argument 'edits' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    edits)
		subdom_funcs = self.synchronous_command('CSS.setStyleTexts', edits=edits)
		return subdom_funcs

	def CSS_setMediaText(self, styleSheetId, range, text):
		"""
		Function path: CSS.setMediaText
			Domain: CSS
			Method name: setMediaText
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> No description
					'range' (type: SourceRange) -> No description
					'text' (type: string) -> No description
			Returns:
				'media' (type: CSSMedia) -> The resulting CSS media rule after modification.
		
			Description: Modifies the rule selector.
		"""
		assert isinstance(text, (str,)
		    ), "Argument 'text' must be of type '['str']'. Received type: '%s'" % type(
		    text)
		subdom_funcs = self.synchronous_command('CSS.setMediaText', styleSheetId=
		    styleSheetId, range=range, text=text)
		return subdom_funcs

	def CSS_createStyleSheet(self, frameId):
		"""
		Function path: CSS.createStyleSheet
			Domain: CSS
			Method name: createStyleSheet
		
			Parameters:
				Required arguments:
					'frameId' (type: Page.FrameId) -> Identifier of the frame where "via-inspector" stylesheet should be created.
			Returns:
				'styleSheetId' (type: StyleSheetId) -> Identifier of the created "via-inspector" stylesheet.
		
			Description: Creates a new special "via-inspector" stylesheet in the frame with given <code>frameId</code>.
		"""
		subdom_funcs = self.synchronous_command('CSS.createStyleSheet', frameId=
		    frameId)
		return subdom_funcs

	def CSS_addRule(self, styleSheetId, ruleText, location):
		"""
		Function path: CSS.addRule
			Domain: CSS
			Method name: addRule
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> The css style sheet identifier where a new rule should be inserted.
					'ruleText' (type: string) -> The text of a new rule.
					'location' (type: SourceRange) -> Text position of a new rule in the target style sheet.
			Returns:
				'rule' (type: CSSRule) -> The newly created rule.
		
			Description: Inserts a new rule with the given <code>ruleText</code> in a stylesheet with given <code>styleSheetId</code>, at the position specified by <code>location</code>.
		"""
		assert isinstance(ruleText, (str,)
		    ), "Argument 'ruleText' must be of type '['str']'. Received type: '%s'" % type(
		    ruleText)
		subdom_funcs = self.synchronous_command('CSS.addRule', styleSheetId=
		    styleSheetId, ruleText=ruleText, location=location)
		return subdom_funcs

	def CSS_forcePseudoState(self, nodeId, forcedPseudoClasses):
		"""
		Function path: CSS.forcePseudoState
			Domain: CSS
			Method name: forcePseudoState
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> The element id for which to force the pseudo state.
					'forcedPseudoClasses' (type: array) -> Element pseudo classes to force when computing the element's style.
			No return value.
		
			Description: Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser.
		"""
		assert isinstance(forcedPseudoClasses, (list, tuple)
		    ), "Argument 'forcedPseudoClasses' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    forcedPseudoClasses)
		subdom_funcs = self.synchronous_command('CSS.forcePseudoState', nodeId=
		    nodeId, forcedPseudoClasses=forcedPseudoClasses)
		return subdom_funcs

	def CSS_getMediaQueries(self):
		"""
		Function path: CSS.getMediaQueries
			Domain: CSS
			Method name: getMediaQueries
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'medias' (type: array) -> No description
		
			Description: Returns all media queries parsed by the rendering engine.
		"""
		subdom_funcs = self.synchronous_command('CSS.getMediaQueries')
		return subdom_funcs

	def CSS_setEffectivePropertyValueForNode(self, nodeId, propertyName, value):
		"""
		Function path: CSS.setEffectivePropertyValueForNode
			Domain: CSS
			Method name: setEffectivePropertyValueForNode
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> The element id for which to set property.
					'propertyName' (type: string) -> No description
					'value' (type: string) -> No description
			No return value.
		
			Description: Find a rule with the given active property for the given node and set the new value for this property
		"""
		assert isinstance(propertyName, (str,)
		    ), "Argument 'propertyName' must be of type '['str']'. Received type: '%s'" % type(
		    propertyName)
		assert isinstance(value, (str,)
		    ), "Argument 'value' must be of type '['str']'. Received type: '%s'" % type(
		    value)
		subdom_funcs = self.synchronous_command(
		    'CSS.setEffectivePropertyValueForNode', nodeId=nodeId, propertyName=
		    propertyName, value=value)
		return subdom_funcs

	def CSS_getBackgroundColors(self, nodeId):
		"""
		Function path: CSS.getBackgroundColors
			Domain: CSS
			Method name: getBackgroundColors
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> Id of the node to get background colors for.
			Returns:
				'backgroundColors' (type: array) -> The range of background colors behind this element, if it contains any visible text. If no visible text is present, this will be undefined. In the case of a flat background color, this will consist of simply that color. In the case of a gradient, this will consist of each of the color stops. For anything more complicated, this will be an empty array. Images will be ignored (as if the image had failed to load).
				'computedFontSize' (type: string) -> The computed font size for this node, as a CSS computed value string (e.g. '12px').
				'computedFontWeight' (type: string) -> The computed font weight for this node, as a CSS computed value string (e.g. 'normal' or '100').
				'computedBodyFontSize' (type: string) -> The computed font size for the document body, as a computed CSS value string (e.g. '16px').
		
		"""
		subdom_funcs = self.synchronous_command('CSS.getBackgroundColors', nodeId
		    =nodeId)
		return subdom_funcs

	def CSS_startRuleUsageTracking(self):
		"""
		Function path: CSS.startRuleUsageTracking
			Domain: CSS
			Method name: startRuleUsageTracking
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Enables the selector recording.
		"""
		subdom_funcs = self.synchronous_command('CSS.startRuleUsageTracking')
		return subdom_funcs

	def CSS_takeCoverageDelta(self):
		"""
		Function path: CSS.takeCoverageDelta
			Domain: CSS
			Method name: takeCoverageDelta
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'coverage' (type: array) -> No description
		
			Description: Obtain list of rules that became used since last call to this method (or since start of coverage instrumentation)
		"""
		subdom_funcs = self.synchronous_command('CSS.takeCoverageDelta')
		return subdom_funcs

	def CSS_stopRuleUsageTracking(self):
		"""
		Function path: CSS.stopRuleUsageTracking
			Domain: CSS
			Method name: stopRuleUsageTracking
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'ruleUsage' (type: array) -> No description
		
			Description: The list of rules with an indication of whether these were used
		"""
		subdom_funcs = self.synchronous_command('CSS.stopRuleUsageTracking')
		return subdom_funcs

	def DOMSnapshot_getSnapshot(self, computedStyleWhitelist):
		"""
		Function path: DOMSnapshot.getSnapshot
			Domain: DOMSnapshot
			Method name: getSnapshot
		
			Parameters:
				Required arguments:
					'computedStyleWhitelist' (type: array) -> Whitelist of computed styles to return.
			Returns:
				'domNodes' (type: array) -> The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document.
				'layoutTreeNodes' (type: array) -> The nodes in the layout tree.
				'computedStyles' (type: array) -> Whitelisted ComputedStyle properties for each node in the layout tree.
		
			Description: Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened. 
		"""
		assert isinstance(computedStyleWhitelist, (list, tuple)
		    ), "Argument 'computedStyleWhitelist' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    computedStyleWhitelist)
		subdom_funcs = self.synchronous_command('DOMSnapshot.getSnapshot',
		    computedStyleWhitelist=computedStyleWhitelist)
		return subdom_funcs

	def IO_read(self, handle, **kwargs):
		"""
		Function path: IO.read
			Domain: IO
			Method name: read
		
			Parameters:
				Required arguments:
					'handle' (type: StreamHandle) -> Handle of the stream to read.
				Optional arguments:
					'offset' (type: integer) -> Seek to the specified offset before reading (if not specificed, proceed with offset following the last read).
					'size' (type: integer) -> Maximum number of bytes to read (left upon the agent discretion if not specified).
			Returns:
				'base64Encoded' (type: boolean) -> Set if the data is base64-encoded
				'data' (type: string) -> Data that were read.
				'eof' (type: boolean) -> Set if the end-of-file condition occured while reading.
		
			Description: Read a chunk of the stream
		"""
		if 'offset' in kwargs:
			assert isinstance(kwargs['offset'], (int,)
			    ), "Optional argument 'offset' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['offset'])
		if 'size' in kwargs:
			assert isinstance(kwargs['size'], (int,)
			    ), "Optional argument 'size' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['size'])
		expected = ['offset', 'size']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['offset', 'size']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('IO.read', handle=handle, **kwargs)
		return subdom_funcs

	def IO_close(self, handle):
		"""
		Function path: IO.close
			Domain: IO
			Method name: close
		
			Parameters:
				Required arguments:
					'handle' (type: StreamHandle) -> Handle of the stream to close.
			No return value.
		
			Description: Close the stream, discard any temporary backing storage.
		"""
		subdom_funcs = self.synchronous_command('IO.close', handle=handle)
		return subdom_funcs

	def IO_resolveBlob(self, objectId):
		"""
		Function path: IO.resolveBlob
			Domain: IO
			Method name: resolveBlob
		
			Parameters:
				Required arguments:
					'objectId' (type: Runtime.RemoteObjectId) -> Object id of a Blob object wrapper.
			Returns:
				'uuid' (type: string) -> UUID of the specified Blob.
		
			Description: Return UUID of Blob object specified by a remote object id.
		"""
		subdom_funcs = self.synchronous_command('IO.resolveBlob', objectId=objectId)
		return subdom_funcs

	def DOMDebugger_setDOMBreakpoint(self, nodeId, type):
		"""
		Function path: DOMDebugger.setDOMBreakpoint
			Domain: DOMDebugger
			Method name: setDOMBreakpoint
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> Identifier of the node to set breakpoint on.
					'type' (type: DOMBreakpointType) -> Type of the operation to stop upon.
			No return value.
		
			Description: Sets breakpoint on particular operation with DOM.
		"""
		subdom_funcs = self.synchronous_command('DOMDebugger.setDOMBreakpoint',
		    nodeId=nodeId, type=type)
		return subdom_funcs

	def DOMDebugger_removeDOMBreakpoint(self, nodeId, type):
		"""
		Function path: DOMDebugger.removeDOMBreakpoint
			Domain: DOMDebugger
			Method name: removeDOMBreakpoint
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> Identifier of the node to remove breakpoint from.
					'type' (type: DOMBreakpointType) -> Type of the breakpoint to remove.
			No return value.
		
			Description: Removes DOM breakpoint that was set using <code>setDOMBreakpoint</code>.
		"""
		subdom_funcs = self.synchronous_command('DOMDebugger.removeDOMBreakpoint',
		    nodeId=nodeId, type=type)
		return subdom_funcs

	def DOMDebugger_setEventListenerBreakpoint(self, eventName, **kwargs):
		"""
		Function path: DOMDebugger.setEventListenerBreakpoint
			Domain: DOMDebugger
			Method name: setEventListenerBreakpoint
		
			Parameters:
				Required arguments:
					'eventName' (type: string) -> DOM Event name to stop on (any DOM event will do).
				Optional arguments:
					'targetName' (type: string) -> EventTarget interface name to stop on. If equal to <code>"*"</code> or not provided, will stop on any EventTarget.
			No return value.
		
			Description: Sets breakpoint on particular DOM event.
		"""
		assert isinstance(eventName, (str,)
		    ), "Argument 'eventName' must be of type '['str']'. Received type: '%s'" % type(
		    eventName)
		if 'targetName' in kwargs:
			assert isinstance(kwargs['targetName'], (str,)
			    ), "Optional argument 'targetName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['targetName'])
		expected = ['targetName']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['targetName']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'DOMDebugger.setEventListenerBreakpoint', eventName=eventName, **kwargs)
		return subdom_funcs

	def DOMDebugger_removeEventListenerBreakpoint(self, eventName, **kwargs):
		"""
		Function path: DOMDebugger.removeEventListenerBreakpoint
			Domain: DOMDebugger
			Method name: removeEventListenerBreakpoint
		
			Parameters:
				Required arguments:
					'eventName' (type: string) -> Event name.
				Optional arguments:
					'targetName' (type: string) -> EventTarget interface name.
			No return value.
		
			Description: Removes breakpoint on particular DOM event.
		"""
		assert isinstance(eventName, (str,)
		    ), "Argument 'eventName' must be of type '['str']'. Received type: '%s'" % type(
		    eventName)
		if 'targetName' in kwargs:
			assert isinstance(kwargs['targetName'], (str,)
			    ), "Optional argument 'targetName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['targetName'])
		expected = ['targetName']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['targetName']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'DOMDebugger.removeEventListenerBreakpoint', eventName=eventName, **
		    kwargs)
		return subdom_funcs

	def DOMDebugger_setInstrumentationBreakpoint(self, eventName):
		"""
		Function path: DOMDebugger.setInstrumentationBreakpoint
			Domain: DOMDebugger
			Method name: setInstrumentationBreakpoint
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'eventName' (type: string) -> Instrumentation name to stop on.
			No return value.
		
			Description: Sets breakpoint on particular native event.
		"""
		assert isinstance(eventName, (str,)
		    ), "Argument 'eventName' must be of type '['str']'. Received type: '%s'" % type(
		    eventName)
		subdom_funcs = self.synchronous_command(
		    'DOMDebugger.setInstrumentationBreakpoint', eventName=eventName)
		return subdom_funcs

	def DOMDebugger_removeInstrumentationBreakpoint(self, eventName):
		"""
		Function path: DOMDebugger.removeInstrumentationBreakpoint
			Domain: DOMDebugger
			Method name: removeInstrumentationBreakpoint
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'eventName' (type: string) -> Instrumentation name to stop on.
			No return value.
		
			Description: Removes breakpoint on particular native event.
		"""
		assert isinstance(eventName, (str,)
		    ), "Argument 'eventName' must be of type '['str']'. Received type: '%s'" % type(
		    eventName)
		subdom_funcs = self.synchronous_command(
		    'DOMDebugger.removeInstrumentationBreakpoint', eventName=eventName)
		return subdom_funcs

	def DOMDebugger_setXHRBreakpoint(self, url):
		"""
		Function path: DOMDebugger.setXHRBreakpoint
			Domain: DOMDebugger
			Method name: setXHRBreakpoint
		
			Parameters:
				Required arguments:
					'url' (type: string) -> Resource URL substring. All XHRs having this substring in the URL will get stopped upon.
			No return value.
		
			Description: Sets breakpoint on XMLHttpRequest.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		subdom_funcs = self.synchronous_command('DOMDebugger.setXHRBreakpoint',
		    url=url)
		return subdom_funcs

	def DOMDebugger_removeXHRBreakpoint(self, url):
		"""
		Function path: DOMDebugger.removeXHRBreakpoint
			Domain: DOMDebugger
			Method name: removeXHRBreakpoint
		
			Parameters:
				Required arguments:
					'url' (type: string) -> Resource URL substring.
			No return value.
		
			Description: Removes breakpoint from XMLHttpRequest.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		subdom_funcs = self.synchronous_command('DOMDebugger.removeXHRBreakpoint',
		    url=url)
		return subdom_funcs

	def DOMDebugger_getEventListeners(self, objectId, **kwargs):
		"""
		Function path: DOMDebugger.getEventListeners
			Domain: DOMDebugger
			Method name: getEventListeners
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'objectId' (type: Runtime.RemoteObjectId) -> Identifier of the object to return listeners for.
				Optional arguments:
					'depth' (type: integer) -> The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). Reports listeners for all contexts if pierce is enabled.
			Returns:
				'listeners' (type: array) -> Array of relevant listeners.
		
			Description: Returns event listeners of the given object.
		"""
		if 'depth' in kwargs:
			assert isinstance(kwargs['depth'], (int,)
			    ), "Optional argument 'depth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['depth'])
		if 'pierce' in kwargs:
			assert isinstance(kwargs['pierce'], (bool,)
			    ), "Optional argument 'pierce' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['pierce'])
		expected = ['depth', 'pierce']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['depth', 'pierce']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOMDebugger.getEventListeners',
		    objectId=objectId, **kwargs)
		return subdom_funcs

	def Target_setDiscoverTargets(self, discover):
		"""
		Function path: Target.setDiscoverTargets
			Domain: Target
			Method name: setDiscoverTargets
		
			Parameters:
				Required arguments:
					'discover' (type: boolean) -> Whether to discover available targets.
			No return value.
		
			Description: Controls whether to discover available targets and notify via <code>targetCreated/targetInfoChanged/targetDestroyed</code> events.
		"""
		assert isinstance(discover, (bool,)
		    ), "Argument 'discover' must be of type '['bool']'. Received type: '%s'" % type(
		    discover)
		subdom_funcs = self.synchronous_command('Target.setDiscoverTargets',
		    discover=discover)
		return subdom_funcs

	def Target_setAutoAttach(self, autoAttach, waitForDebuggerOnStart):
		"""
		Function path: Target.setAutoAttach
			Domain: Target
			Method name: setAutoAttach
		
			Parameters:
				Required arguments:
					'autoAttach' (type: boolean) -> Whether to auto-attach to related targets.
					'waitForDebuggerOnStart' (type: boolean) -> Whether to pause new targets when attaching to them. Use <code>Runtime.runIfWaitingForDebugger</code> to run paused targets.
			No return value.
		
			Description: Controls whether to automatically attach to new targets which are considered to be related to this one. When turned on, attaches to all existing related targets as well. When turned off, automatically detaches from all currently attached targets.
		"""
		assert isinstance(autoAttach, (bool,)
		    ), "Argument 'autoAttach' must be of type '['bool']'. Received type: '%s'" % type(
		    autoAttach)
		assert isinstance(waitForDebuggerOnStart, (bool,)
		    ), "Argument 'waitForDebuggerOnStart' must be of type '['bool']'. Received type: '%s'" % type(
		    waitForDebuggerOnStart)
		subdom_funcs = self.synchronous_command('Target.setAutoAttach',
		    autoAttach=autoAttach, waitForDebuggerOnStart=waitForDebuggerOnStart)
		return subdom_funcs

	def Target_setAttachToFrames(self, value):
		"""
		Function path: Target.setAttachToFrames
			Domain: Target
			Method name: setAttachToFrames
		
			Parameters:
				Required arguments:
					'value' (type: boolean) -> Whether to attach to frames.
			No return value.
		
		"""
		assert isinstance(value, (bool,)
		    ), "Argument 'value' must be of type '['bool']'. Received type: '%s'" % type(
		    value)
		subdom_funcs = self.synchronous_command('Target.setAttachToFrames', value
		    =value)
		return subdom_funcs

	def Target_setRemoteLocations(self, locations):
		"""
		Function path: Target.setRemoteLocations
			Domain: Target
			Method name: setRemoteLocations
		
			Parameters:
				Required arguments:
					'locations' (type: array) -> List of remote locations.
			No return value.
		
			Description: Enables target discovery for the specified locations, when <code>setDiscoverTargets</code> was set to <code>true</code>.
		"""
		assert isinstance(locations, (list, tuple)
		    ), "Argument 'locations' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    locations)
		subdom_funcs = self.synchronous_command('Target.setRemoteLocations',
		    locations=locations)
		return subdom_funcs

	def Target_sendMessageToTarget(self, message, **kwargs):
		"""
		Function path: Target.sendMessageToTarget
			Domain: Target
			Method name: sendMessageToTarget
		
			Parameters:
				Required arguments:
					'message' (type: string) -> No description
				Optional arguments:
					'sessionId' (type: SessionID) -> Identifier of the session.
					'targetId' (type: TargetID) -> Deprecated.
			No return value.
		
			Description: Sends protocol message over session with given id.
		"""
		assert isinstance(message, (str,)
		    ), "Argument 'message' must be of type '['str']'. Received type: '%s'" % type(
		    message)
		expected = ['sessionId', 'targetId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['sessionId', 'targetId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.sendMessageToTarget',
		    message=message, **kwargs)
		return subdom_funcs

	def Target_getTargetInfo(self, targetId):
		"""
		Function path: Target.getTargetInfo
			Domain: Target
			Method name: getTargetInfo
		
			Parameters:
				Required arguments:
					'targetId' (type: TargetID) -> No description
			Returns:
				'targetInfo' (type: TargetInfo) -> No description
		
			Description: Returns information about a target.
		"""
		subdom_funcs = self.synchronous_command('Target.getTargetInfo', targetId=
		    targetId)
		return subdom_funcs

	def Target_activateTarget(self, targetId):
		"""
		Function path: Target.activateTarget
			Domain: Target
			Method name: activateTarget
		
			Parameters:
				Required arguments:
					'targetId' (type: TargetID) -> No description
			No return value.
		
			Description: Activates (focuses) the target.
		"""
		subdom_funcs = self.synchronous_command('Target.activateTarget', targetId
		    =targetId)
		return subdom_funcs

	def Target_closeTarget(self, targetId):
		"""
		Function path: Target.closeTarget
			Domain: Target
			Method name: closeTarget
		
			Parameters:
				Required arguments:
					'targetId' (type: TargetID) -> No description
			Returns:
				'success' (type: boolean) -> No description
		
			Description: Closes the target. If the target is a page that gets closed too.
		"""
		subdom_funcs = self.synchronous_command('Target.closeTarget', targetId=
		    targetId)
		return subdom_funcs

	def Target_attachToTarget(self, targetId):
		"""
		Function path: Target.attachToTarget
			Domain: Target
			Method name: attachToTarget
		
			Parameters:
				Required arguments:
					'targetId' (type: TargetID) -> No description
			Returns:
				'sessionId' (type: SessionID) -> Id assigned to the session.
		
			Description: Attaches to the target with given id.
		"""
		subdom_funcs = self.synchronous_command('Target.attachToTarget', targetId
		    =targetId)
		return subdom_funcs

	def Target_detachFromTarget(self, **kwargs):
		"""
		Function path: Target.detachFromTarget
			Domain: Target
			Method name: detachFromTarget
		
			Parameters:
				Optional arguments:
					'sessionId' (type: SessionID) -> Session to detach.
					'targetId' (type: TargetID) -> Deprecated.
			No return value.
		
			Description: Detaches session with given id.
		"""
		expected = ['sessionId', 'targetId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['sessionId', 'targetId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.detachFromTarget', **kwargs)
		return subdom_funcs

	def Target_createBrowserContext(self):
		"""
		Function path: Target.createBrowserContext
			Domain: Target
			Method name: createBrowserContext
		
			Returns:
				'browserContextId' (type: BrowserContextID) -> The id of the context created.
		
			Description: Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than one.
		"""
		subdom_funcs = self.synchronous_command('Target.createBrowserContext')
		return subdom_funcs

	def Target_disposeBrowserContext(self, browserContextId):
		"""
		Function path: Target.disposeBrowserContext
			Domain: Target
			Method name: disposeBrowserContext
		
			Parameters:
				Required arguments:
					'browserContextId' (type: BrowserContextID) -> No description
			Returns:
				'success' (type: boolean) -> No description
		
			Description: Deletes a BrowserContext, will fail of any open page uses it.
		"""
		subdom_funcs = self.synchronous_command('Target.disposeBrowserContext',
		    browserContextId=browserContextId)
		return subdom_funcs

	def Target_createTarget(self, url, **kwargs):
		"""
		Function path: Target.createTarget
			Domain: Target
			Method name: createTarget
		
			Parameters:
				Required arguments:
					'url' (type: string) -> The initial URL the page will be navigated to.
				Optional arguments:
					'width' (type: integer) -> Frame width in DIP (headless chrome only).
					'height' (type: integer) -> Frame height in DIP (headless chrome only).
					'browserContextId' (type: BrowserContextID) -> The browser context to create the page in (headless chrome only).
			Returns:
				'targetId' (type: TargetID) -> The id of the page opened.
		
			Description: Creates a new page.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		if 'width' in kwargs:
			assert isinstance(kwargs['width'], (int,)
			    ), "Optional argument 'width' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['width'])
		if 'height' in kwargs:
			assert isinstance(kwargs['height'], (int,)
			    ), "Optional argument 'height' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['height'])
		expected = ['width', 'height', 'browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['width', 'height', 'browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.createTarget', url=url,
		    **kwargs)
		return subdom_funcs

	def Target_getTargets(self):
		"""
		Function path: Target.getTargets
			Domain: Target
			Method name: getTargets
		
			Returns:
				'targetInfos' (type: array) -> The list of targets.
		
			Description: Retrieves a list of available targets.
		"""
		subdom_funcs = self.synchronous_command('Target.getTargets')
		return subdom_funcs

	def ServiceWorker_enable(self):
		"""
		Function path: ServiceWorker.enable
			Domain: ServiceWorker
			Method name: enable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('ServiceWorker.enable')
		return subdom_funcs

	def ServiceWorker_disable(self):
		"""
		Function path: ServiceWorker.disable
			Domain: ServiceWorker
			Method name: disable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('ServiceWorker.disable')
		return subdom_funcs

	def ServiceWorker_unregister(self, scopeURL):
		"""
		Function path: ServiceWorker.unregister
			Domain: ServiceWorker
			Method name: unregister
		
			Parameters:
				Required arguments:
					'scopeURL' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(scopeURL, (str,)
		    ), "Argument 'scopeURL' must be of type '['str']'. Received type: '%s'" % type(
		    scopeURL)
		subdom_funcs = self.synchronous_command('ServiceWorker.unregister',
		    scopeURL=scopeURL)
		return subdom_funcs

	def ServiceWorker_updateRegistration(self, scopeURL):
		"""
		Function path: ServiceWorker.updateRegistration
			Domain: ServiceWorker
			Method name: updateRegistration
		
			Parameters:
				Required arguments:
					'scopeURL' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(scopeURL, (str,)
		    ), "Argument 'scopeURL' must be of type '['str']'. Received type: '%s'" % type(
		    scopeURL)
		subdom_funcs = self.synchronous_command('ServiceWorker.updateRegistration',
		    scopeURL=scopeURL)
		return subdom_funcs

	def ServiceWorker_startWorker(self, scopeURL):
		"""
		Function path: ServiceWorker.startWorker
			Domain: ServiceWorker
			Method name: startWorker
		
			Parameters:
				Required arguments:
					'scopeURL' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(scopeURL, (str,)
		    ), "Argument 'scopeURL' must be of type '['str']'. Received type: '%s'" % type(
		    scopeURL)
		subdom_funcs = self.synchronous_command('ServiceWorker.startWorker',
		    scopeURL=scopeURL)
		return subdom_funcs

	def ServiceWorker_skipWaiting(self, scopeURL):
		"""
		Function path: ServiceWorker.skipWaiting
			Domain: ServiceWorker
			Method name: skipWaiting
		
			Parameters:
				Required arguments:
					'scopeURL' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(scopeURL, (str,)
		    ), "Argument 'scopeURL' must be of type '['str']'. Received type: '%s'" % type(
		    scopeURL)
		subdom_funcs = self.synchronous_command('ServiceWorker.skipWaiting',
		    scopeURL=scopeURL)
		return subdom_funcs

	def ServiceWorker_stopWorker(self, versionId):
		"""
		Function path: ServiceWorker.stopWorker
			Domain: ServiceWorker
			Method name: stopWorker
		
			Parameters:
				Required arguments:
					'versionId' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(versionId, (str,)
		    ), "Argument 'versionId' must be of type '['str']'. Received type: '%s'" % type(
		    versionId)
		subdom_funcs = self.synchronous_command('ServiceWorker.stopWorker',
		    versionId=versionId)
		return subdom_funcs

	def ServiceWorker_stopAllWorkers(self):
		"""
		Function path: ServiceWorker.stopAllWorkers
			Domain: ServiceWorker
			Method name: stopAllWorkers
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('ServiceWorker.stopAllWorkers')
		return subdom_funcs

	def ServiceWorker_inspectWorker(self, versionId):
		"""
		Function path: ServiceWorker.inspectWorker
			Domain: ServiceWorker
			Method name: inspectWorker
		
			Parameters:
				Required arguments:
					'versionId' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(versionId, (str,)
		    ), "Argument 'versionId' must be of type '['str']'. Received type: '%s'" % type(
		    versionId)
		subdom_funcs = self.synchronous_command('ServiceWorker.inspectWorker',
		    versionId=versionId)
		return subdom_funcs

	def ServiceWorker_setForceUpdateOnPageLoad(self, forceUpdateOnPageLoad):
		"""
		Function path: ServiceWorker.setForceUpdateOnPageLoad
			Domain: ServiceWorker
			Method name: setForceUpdateOnPageLoad
		
			Parameters:
				Required arguments:
					'forceUpdateOnPageLoad' (type: boolean) -> No description
			No return value.
		
		"""
		assert isinstance(forceUpdateOnPageLoad, (bool,)
		    ), "Argument 'forceUpdateOnPageLoad' must be of type '['bool']'. Received type: '%s'" % type(
		    forceUpdateOnPageLoad)
		subdom_funcs = self.synchronous_command(
		    'ServiceWorker.setForceUpdateOnPageLoad', forceUpdateOnPageLoad=
		    forceUpdateOnPageLoad)
		return subdom_funcs

	def ServiceWorker_deliverPushMessage(self, origin, registrationId, data):
		"""
		Function path: ServiceWorker.deliverPushMessage
			Domain: ServiceWorker
			Method name: deliverPushMessage
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> No description
					'registrationId' (type: string) -> No description
					'data' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		assert isinstance(registrationId, (str,)
		    ), "Argument 'registrationId' must be of type '['str']'. Received type: '%s'" % type(
		    registrationId)
		assert isinstance(data, (str,)
		    ), "Argument 'data' must be of type '['str']'. Received type: '%s'" % type(
		    data)
		subdom_funcs = self.synchronous_command('ServiceWorker.deliverPushMessage',
		    origin=origin, registrationId=registrationId, data=data)
		return subdom_funcs

	def ServiceWorker_dispatchSyncEvent(self, origin, registrationId, tag,
	    lastChance):
		"""
		Function path: ServiceWorker.dispatchSyncEvent
			Domain: ServiceWorker
			Method name: dispatchSyncEvent
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> No description
					'registrationId' (type: string) -> No description
					'tag' (type: string) -> No description
					'lastChance' (type: boolean) -> No description
			No return value.
		
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		assert isinstance(registrationId, (str,)
		    ), "Argument 'registrationId' must be of type '['str']'. Received type: '%s'" % type(
		    registrationId)
		assert isinstance(tag, (str,)
		    ), "Argument 'tag' must be of type '['str']'. Received type: '%s'" % type(
		    tag)
		assert isinstance(lastChance, (bool,)
		    ), "Argument 'lastChance' must be of type '['bool']'. Received type: '%s'" % type(
		    lastChance)
		subdom_funcs = self.synchronous_command('ServiceWorker.dispatchSyncEvent',
		    origin=origin, registrationId=registrationId, tag=tag, lastChance=
		    lastChance)
		return subdom_funcs

	def Input_setIgnoreInputEvents(self, ignore):
		"""
		Function path: Input.setIgnoreInputEvents
			Domain: Input
			Method name: setIgnoreInputEvents
		
			Parameters:
				Required arguments:
					'ignore' (type: boolean) -> Ignores input events processing when set to true.
			No return value.
		
			Description: Ignores input events (useful while auditing page).
		"""
		assert isinstance(ignore, (bool,)
		    ), "Argument 'ignore' must be of type '['bool']'. Received type: '%s'" % type(
		    ignore)
		subdom_funcs = self.synchronous_command('Input.setIgnoreInputEvents',
		    ignore=ignore)
		return subdom_funcs

	def Input_dispatchKeyEvent(self, type, **kwargs):
		"""
		Function path: Input.dispatchKeyEvent
			Domain: Input
			Method name: dispatchKeyEvent
		
			Parameters:
				Required arguments:
					'type' (type: string) -> Type of the key event.
				Optional arguments:
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
					'timestamp' (type: TimeSinceEpoch) -> Time at which the event occurred.
					'text' (type: string) -> Text as generated by processing a virtual key code with a keyboard layout. Not needed for for <code>keyUp</code> and <code>rawKeyDown</code> events (default: "")
					'unmodifiedText' (type: string) -> Text that would have been generated by the keyboard if no modifiers were pressed (except for shift). Useful for shortcut (accelerator) key handling (default: "").
					'keyIdentifier' (type: string) -> Unique key identifier (e.g., 'U+0041') (default: "").
					'code' (type: string) -> Unique DOM defined string value for each physical key (e.g., 'KeyA') (default: "").
					'key' (type: string) -> Unique DOM defined string value describing the meaning of the key in the context of active modifiers, keyboard layout, etc (e.g., 'AltGr') (default: "").
					'windowsVirtualKeyCode' (type: integer) -> Windows virtual key code (default: 0).
					'nativeVirtualKeyCode' (type: integer) -> Native virtual key code (default: 0).
					'autoRepeat' (type: boolean) -> Whether the event was generated from auto repeat (default: false).
					'isKeypad' (type: boolean) -> Whether the event was generated from the keypad (default: false).
					'isSystemKey' (type: boolean) -> Whether the event was a system key event (default: false).
			No return value.
		
			Description: Dispatches a key event to the page.
		"""
		assert isinstance(type, (str,)
		    ), "Argument 'type' must be of type '['str']'. Received type: '%s'" % type(
		    type)
		if 'modifiers' in kwargs:
			assert isinstance(kwargs['modifiers'], (int,)
			    ), "Optional argument 'modifiers' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['modifiers'])
		if 'text' in kwargs:
			assert isinstance(kwargs['text'], (str,)
			    ), "Optional argument 'text' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['text'])
		if 'unmodifiedText' in kwargs:
			assert isinstance(kwargs['unmodifiedText'], (str,)
			    ), "Optional argument 'unmodifiedText' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['unmodifiedText'])
		if 'keyIdentifier' in kwargs:
			assert isinstance(kwargs['keyIdentifier'], (str,)
			    ), "Optional argument 'keyIdentifier' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['keyIdentifier'])
		if 'code' in kwargs:
			assert isinstance(kwargs['code'], (str,)
			    ), "Optional argument 'code' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['code'])
		if 'key' in kwargs:
			assert isinstance(kwargs['key'], (str,)
			    ), "Optional argument 'key' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['key'])
		if 'windowsVirtualKeyCode' in kwargs:
			assert isinstance(kwargs['windowsVirtualKeyCode'], (int,)
			    ), "Optional argument 'windowsVirtualKeyCode' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['windowsVirtualKeyCode'])
		if 'nativeVirtualKeyCode' in kwargs:
			assert isinstance(kwargs['nativeVirtualKeyCode'], (int,)
			    ), "Optional argument 'nativeVirtualKeyCode' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['nativeVirtualKeyCode'])
		if 'autoRepeat' in kwargs:
			assert isinstance(kwargs['autoRepeat'], (bool,)
			    ), "Optional argument 'autoRepeat' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['autoRepeat'])
		if 'isKeypad' in kwargs:
			assert isinstance(kwargs['isKeypad'], (bool,)
			    ), "Optional argument 'isKeypad' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['isKeypad'])
		if 'isSystemKey' in kwargs:
			assert isinstance(kwargs['isSystemKey'], (bool,)
			    ), "Optional argument 'isSystemKey' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['isSystemKey'])
		expected = ['modifiers', 'timestamp', 'text', 'unmodifiedText',
		    'keyIdentifier', 'code', 'key', 'windowsVirtualKeyCode',
		    'nativeVirtualKeyCode', 'autoRepeat', 'isKeypad', 'isSystemKey']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['modifiers', 'timestamp', 'text', 'unmodifiedText', 'keyIdentifier', 'code', 'key', 'windowsVirtualKeyCode', 'nativeVirtualKeyCode', 'autoRepeat', 'isKeypad', 'isSystemKey']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.dispatchKeyEvent', type=
		    type, **kwargs)
		return subdom_funcs

	def Input_dispatchMouseEvent(self, type, x, y, **kwargs):
		"""
		Function path: Input.dispatchMouseEvent
			Domain: Input
			Method name: dispatchMouseEvent
		
			Parameters:
				Required arguments:
					'type' (type: string) -> Type of the mouse event.
					'x' (type: number) -> X coordinate of the event relative to the main frame's viewport in CSS pixels.
					'y' (type: number) -> Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
				Optional arguments:
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
					'timestamp' (type: TimeSinceEpoch) -> Time at which the event occurred.
					'button' (type: string) -> Mouse button (default: "none").
					'clickCount' (type: integer) -> Number of times the mouse button was clicked (default: 0).
					'deltaX' (type: number) -> X delta in CSS pixels for mouse wheel event (default: 0).
					'deltaY' (type: number) -> Y delta in CSS pixels for mouse wheel event (default: 0).
			No return value.
		
			Description: Dispatches a mouse event to the page.
		"""
		assert isinstance(type, (str,)
		    ), "Argument 'type' must be of type '['str']'. Received type: '%s'" % type(
		    type)
		assert isinstance(x, (float, int)
		    ), "Argument 'x' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    x)
		assert isinstance(y, (float, int)
		    ), "Argument 'y' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    y)
		if 'modifiers' in kwargs:
			assert isinstance(kwargs['modifiers'], (int,)
			    ), "Optional argument 'modifiers' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['modifiers'])
		if 'button' in kwargs:
			assert isinstance(kwargs['button'], (str,)
			    ), "Optional argument 'button' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['button'])
		if 'clickCount' in kwargs:
			assert isinstance(kwargs['clickCount'], (int,)
			    ), "Optional argument 'clickCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['clickCount'])
		if 'deltaX' in kwargs:
			assert isinstance(kwargs['deltaX'], (float, int)
			    ), "Optional argument 'deltaX' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['deltaX'])
		if 'deltaY' in kwargs:
			assert isinstance(kwargs['deltaY'], (float, int)
			    ), "Optional argument 'deltaY' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['deltaY'])
		expected = ['modifiers', 'timestamp', 'button', 'clickCount', 'deltaX',
		    'deltaY']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['modifiers', 'timestamp', 'button', 'clickCount', 'deltaX', 'deltaY']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.dispatchMouseEvent', type=
		    type, x=x, y=y, **kwargs)
		return subdom_funcs

	def Input_dispatchTouchEvent(self, type, touchPoints, **kwargs):
		"""
		Function path: Input.dispatchTouchEvent
			Domain: Input
			Method name: dispatchTouchEvent
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'type' (type: string) -> Type of the touch event. TouchEnd and TouchCancel must not contain any touch points, while TouchStart and TouchMove must contains at least one.
					'touchPoints' (type: array) -> Active touch points on the touch device. One event per any changed point (compared to previous touch event in a sequence) is generated, emulating pressing/moving/releasing points one by one.
				Optional arguments:
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
					'timestamp' (type: TimeSinceEpoch) -> Time at which the event occurred.
			No return value.
		
			Description: Dispatches a touch event to the page.
		"""
		assert isinstance(type, (str,)
		    ), "Argument 'type' must be of type '['str']'. Received type: '%s'" % type(
		    type)
		assert isinstance(touchPoints, (list, tuple)
		    ), "Argument 'touchPoints' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    touchPoints)
		if 'modifiers' in kwargs:
			assert isinstance(kwargs['modifiers'], (int,)
			    ), "Optional argument 'modifiers' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['modifiers'])
		expected = ['modifiers', 'timestamp']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['modifiers', 'timestamp']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.dispatchTouchEvent', type=
		    type, touchPoints=touchPoints, **kwargs)
		return subdom_funcs

	def Input_emulateTouchFromMouseEvent(self, type, x, y, timestamp, button,
	    **kwargs):
		"""
		Function path: Input.emulateTouchFromMouseEvent
			Domain: Input
			Method name: emulateTouchFromMouseEvent
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'type' (type: string) -> Type of the mouse event.
					'x' (type: integer) -> X coordinate of the mouse pointer in DIP.
					'y' (type: integer) -> Y coordinate of the mouse pointer in DIP.
					'timestamp' (type: TimeSinceEpoch) -> Time at which the event occurred.
					'button' (type: string) -> Mouse button.
				Optional arguments:
					'deltaX' (type: number) -> X delta in DIP for mouse wheel event (default: 0).
					'deltaY' (type: number) -> Y delta in DIP for mouse wheel event (default: 0).
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8 (default: 0).
					'clickCount' (type: integer) -> Number of times the mouse button was clicked (default: 0).
			No return value.
		
			Description: Emulates touch event from the mouse event parameters.
		"""
		assert isinstance(type, (str,)
		    ), "Argument 'type' must be of type '['str']'. Received type: '%s'" % type(
		    type)
		assert isinstance(x, (int,)
		    ), "Argument 'x' must be of type '['int']'. Received type: '%s'" % type(x
		    )
		assert isinstance(y, (int,)
		    ), "Argument 'y' must be of type '['int']'. Received type: '%s'" % type(y
		    )
		assert isinstance(button, (str,)
		    ), "Argument 'button' must be of type '['str']'. Received type: '%s'" % type(
		    button)
		if 'deltaX' in kwargs:
			assert isinstance(kwargs['deltaX'], (float, int)
			    ), "Optional argument 'deltaX' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['deltaX'])
		if 'deltaY' in kwargs:
			assert isinstance(kwargs['deltaY'], (float, int)
			    ), "Optional argument 'deltaY' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['deltaY'])
		if 'modifiers' in kwargs:
			assert isinstance(kwargs['modifiers'], (int,)
			    ), "Optional argument 'modifiers' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['modifiers'])
		if 'clickCount' in kwargs:
			assert isinstance(kwargs['clickCount'], (int,)
			    ), "Optional argument 'clickCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['clickCount'])
		expected = ['deltaX', 'deltaY', 'modifiers', 'clickCount']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['deltaX', 'deltaY', 'modifiers', 'clickCount']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.emulateTouchFromMouseEvent',
		    type=type, x=x, y=y, timestamp=timestamp, button=button, **kwargs)
		return subdom_funcs

	def Input_synthesizePinchGesture(self, x, y, scaleFactor, **kwargs):
		"""
		Function path: Input.synthesizePinchGesture
			Domain: Input
			Method name: synthesizePinchGesture
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'x' (type: number) -> X coordinate of the start of the gesture in CSS pixels.
					'y' (type: number) -> Y coordinate of the start of the gesture in CSS pixels.
					'scaleFactor' (type: number) -> Relative scale factor after zooming (>1.0 zooms in, <1.0 zooms out).
				Optional arguments:
					'relativeSpeed' (type: integer) -> Relative pointer speed in pixels per second (default: 800).
					'gestureSourceType' (type: GestureSourceType) -> Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
			No return value.
		
			Description: Synthesizes a pinch gesture over a time period by issuing appropriate touch events.
		"""
		assert isinstance(x, (float, int)
		    ), "Argument 'x' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    x)
		assert isinstance(y, (float, int)
		    ), "Argument 'y' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    y)
		assert isinstance(scaleFactor, (float, int)
		    ), "Argument 'scaleFactor' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    scaleFactor)
		if 'relativeSpeed' in kwargs:
			assert isinstance(kwargs['relativeSpeed'], (int,)
			    ), "Optional argument 'relativeSpeed' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['relativeSpeed'])
		expected = ['relativeSpeed', 'gestureSourceType']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['relativeSpeed', 'gestureSourceType']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.synthesizePinchGesture', x
		    =x, y=y, scaleFactor=scaleFactor, **kwargs)
		return subdom_funcs

	def Input_synthesizeScrollGesture(self, x, y, **kwargs):
		"""
		Function path: Input.synthesizeScrollGesture
			Domain: Input
			Method name: synthesizeScrollGesture
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'x' (type: number) -> X coordinate of the start of the gesture in CSS pixels.
					'y' (type: number) -> Y coordinate of the start of the gesture in CSS pixels.
				Optional arguments:
					'xDistance' (type: number) -> The distance to scroll along the X axis (positive to scroll left).
					'yDistance' (type: number) -> The distance to scroll along the Y axis (positive to scroll up).
					'xOverscroll' (type: number) -> The number of additional pixels to scroll back along the X axis, in addition to the given distance.
					'yOverscroll' (type: number) -> The number of additional pixels to scroll back along the Y axis, in addition to the given distance.
					'preventFling' (type: boolean) -> Prevent fling (default: true).
					'speed' (type: integer) -> Swipe speed in pixels per second (default: 800).
					'gestureSourceType' (type: GestureSourceType) -> Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
					'repeatCount' (type: integer) -> The number of times to repeat the gesture (default: 0).
					'repeatDelayMs' (type: integer) -> The number of milliseconds delay between each repeat. (default: 250).
					'interactionMarkerName' (type: string) -> The name of the interaction markers to generate, if not empty (default: "").
			No return value.
		
			Description: Synthesizes a scroll gesture over a time period by issuing appropriate touch events.
		"""
		assert isinstance(x, (float, int)
		    ), "Argument 'x' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    x)
		assert isinstance(y, (float, int)
		    ), "Argument 'y' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    y)
		if 'xDistance' in kwargs:
			assert isinstance(kwargs['xDistance'], (float, int)
			    ), "Optional argument 'xDistance' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['xDistance'])
		if 'yDistance' in kwargs:
			assert isinstance(kwargs['yDistance'], (float, int)
			    ), "Optional argument 'yDistance' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['yDistance'])
		if 'xOverscroll' in kwargs:
			assert isinstance(kwargs['xOverscroll'], (float, int)
			    ), "Optional argument 'xOverscroll' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['xOverscroll'])
		if 'yOverscroll' in kwargs:
			assert isinstance(kwargs['yOverscroll'], (float, int)
			    ), "Optional argument 'yOverscroll' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['yOverscroll'])
		if 'preventFling' in kwargs:
			assert isinstance(kwargs['preventFling'], (bool,)
			    ), "Optional argument 'preventFling' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['preventFling'])
		if 'speed' in kwargs:
			assert isinstance(kwargs['speed'], (int,)
			    ), "Optional argument 'speed' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['speed'])
		if 'repeatCount' in kwargs:
			assert isinstance(kwargs['repeatCount'], (int,)
			    ), "Optional argument 'repeatCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['repeatCount'])
		if 'repeatDelayMs' in kwargs:
			assert isinstance(kwargs['repeatDelayMs'], (int,)
			    ), "Optional argument 'repeatDelayMs' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['repeatDelayMs'])
		if 'interactionMarkerName' in kwargs:
			assert isinstance(kwargs['interactionMarkerName'], (str,)
			    ), "Optional argument 'interactionMarkerName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['interactionMarkerName'])
		expected = ['xDistance', 'yDistance', 'xOverscroll', 'yOverscroll',
		    'preventFling', 'speed', 'gestureSourceType', 'repeatCount',
		    'repeatDelayMs', 'interactionMarkerName']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['xDistance', 'yDistance', 'xOverscroll', 'yOverscroll', 'preventFling', 'speed', 'gestureSourceType', 'repeatCount', 'repeatDelayMs', 'interactionMarkerName']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.synthesizeScrollGesture',
		    x=x, y=y, **kwargs)
		return subdom_funcs

	def Input_synthesizeTapGesture(self, x, y, **kwargs):
		"""
		Function path: Input.synthesizeTapGesture
			Domain: Input
			Method name: synthesizeTapGesture
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'x' (type: number) -> X coordinate of the start of the gesture in CSS pixels.
					'y' (type: number) -> Y coordinate of the start of the gesture in CSS pixels.
				Optional arguments:
					'duration' (type: integer) -> Duration between touchdown and touchup events in ms (default: 50).
					'tapCount' (type: integer) -> Number of times to perform the tap (e.g. 2 for double tap, default: 1).
					'gestureSourceType' (type: GestureSourceType) -> Which type of input events to be generated (default: 'default', which queries the platform for the preferred input type).
			No return value.
		
			Description: Synthesizes a tap gesture over a time period by issuing appropriate touch events.
		"""
		assert isinstance(x, (float, int)
		    ), "Argument 'x' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    x)
		assert isinstance(y, (float, int)
		    ), "Argument 'y' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    y)
		if 'duration' in kwargs:
			assert isinstance(kwargs['duration'], (int,)
			    ), "Optional argument 'duration' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['duration'])
		if 'tapCount' in kwargs:
			assert isinstance(kwargs['tapCount'], (int,)
			    ), "Optional argument 'tapCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['tapCount'])
		expected = ['duration', 'tapCount', 'gestureSourceType']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['duration', 'tapCount', 'gestureSourceType']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.synthesizeTapGesture', x=x,
		    y=y, **kwargs)
		return subdom_funcs

	def LayerTree_enable(self):
		"""
		Function path: LayerTree.enable
			Domain: LayerTree
			Method name: enable
		
			No return value.
		
			Description: Enables compositing tree inspection.
		"""
		subdom_funcs = self.synchronous_command('LayerTree.enable')
		return subdom_funcs

	def LayerTree_disable(self):
		"""
		Function path: LayerTree.disable
			Domain: LayerTree
			Method name: disable
		
			No return value.
		
			Description: Disables compositing tree inspection.
		"""
		subdom_funcs = self.synchronous_command('LayerTree.disable')
		return subdom_funcs

	def LayerTree_compositingReasons(self, layerId):
		"""
		Function path: LayerTree.compositingReasons
			Domain: LayerTree
			Method name: compositingReasons
		
			Parameters:
				Required arguments:
					'layerId' (type: LayerId) -> The id of the layer for which we want to get the reasons it was composited.
			Returns:
				'compositingReasons' (type: array) -> A list of strings specifying reasons for the given layer to become composited.
		
			Description: Provides the reasons why the given layer was composited.
		"""
		subdom_funcs = self.synchronous_command('LayerTree.compositingReasons',
		    layerId=layerId)
		return subdom_funcs

	def LayerTree_makeSnapshot(self, layerId):
		"""
		Function path: LayerTree.makeSnapshot
			Domain: LayerTree
			Method name: makeSnapshot
		
			Parameters:
				Required arguments:
					'layerId' (type: LayerId) -> The id of the layer.
			Returns:
				'snapshotId' (type: SnapshotId) -> The id of the layer snapshot.
		
			Description: Returns the layer snapshot identifier.
		"""
		subdom_funcs = self.synchronous_command('LayerTree.makeSnapshot', layerId
		    =layerId)
		return subdom_funcs

	def LayerTree_loadSnapshot(self, tiles):
		"""
		Function path: LayerTree.loadSnapshot
			Domain: LayerTree
			Method name: loadSnapshot
		
			Parameters:
				Required arguments:
					'tiles' (type: array) -> An array of tiles composing the snapshot.
			Returns:
				'snapshotId' (type: SnapshotId) -> The id of the snapshot.
		
			Description: Returns the snapshot identifier.
		"""
		assert isinstance(tiles, (list, tuple)
		    ), "Argument 'tiles' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    tiles)
		subdom_funcs = self.synchronous_command('LayerTree.loadSnapshot', tiles=tiles
		    )
		return subdom_funcs

	def LayerTree_releaseSnapshot(self, snapshotId):
		"""
		Function path: LayerTree.releaseSnapshot
			Domain: LayerTree
			Method name: releaseSnapshot
		
			Parameters:
				Required arguments:
					'snapshotId' (type: SnapshotId) -> The id of the layer snapshot.
			No return value.
		
			Description: Releases layer snapshot captured by the back-end.
		"""
		subdom_funcs = self.synchronous_command('LayerTree.releaseSnapshot',
		    snapshotId=snapshotId)
		return subdom_funcs

	def LayerTree_profileSnapshot(self, snapshotId, **kwargs):
		"""
		Function path: LayerTree.profileSnapshot
			Domain: LayerTree
			Method name: profileSnapshot
		
			Parameters:
				Required arguments:
					'snapshotId' (type: SnapshotId) -> The id of the layer snapshot.
				Optional arguments:
					'minRepeatCount' (type: integer) -> The maximum number of times to replay the snapshot (1, if not specified).
					'minDuration' (type: number) -> The minimum duration (in seconds) to replay the snapshot.
					'clipRect' (type: DOM.Rect) -> The clip rectangle to apply when replaying the snapshot.
			Returns:
				'timings' (type: array) -> The array of paint profiles, one per run.
		
		"""
		if 'minRepeatCount' in kwargs:
			assert isinstance(kwargs['minRepeatCount'], (int,)
			    ), "Optional argument 'minRepeatCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['minRepeatCount'])
		if 'minDuration' in kwargs:
			assert isinstance(kwargs['minDuration'], (float, int)
			    ), "Optional argument 'minDuration' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['minDuration'])
		expected = ['minRepeatCount', 'minDuration', 'clipRect']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['minRepeatCount', 'minDuration', 'clipRect']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('LayerTree.profileSnapshot',
		    snapshotId=snapshotId, **kwargs)
		return subdom_funcs

	def LayerTree_replaySnapshot(self, snapshotId, **kwargs):
		"""
		Function path: LayerTree.replaySnapshot
			Domain: LayerTree
			Method name: replaySnapshot
		
			Parameters:
				Required arguments:
					'snapshotId' (type: SnapshotId) -> The id of the layer snapshot.
				Optional arguments:
					'fromStep' (type: integer) -> The first step to replay from (replay from the very start if not specified).
					'toStep' (type: integer) -> The last step to replay to (replay till the end if not specified).
					'scale' (type: number) -> The scale to apply while replaying (defaults to 1).
			Returns:
				'dataURL' (type: string) -> A data: URL for resulting image.
		
			Description: Replays the layer snapshot and returns the resulting bitmap.
		"""
		if 'fromStep' in kwargs:
			assert isinstance(kwargs['fromStep'], (int,)
			    ), "Optional argument 'fromStep' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['fromStep'])
		if 'toStep' in kwargs:
			assert isinstance(kwargs['toStep'], (int,)
			    ), "Optional argument 'toStep' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['toStep'])
		if 'scale' in kwargs:
			assert isinstance(kwargs['scale'], (float, int)
			    ), "Optional argument 'scale' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['scale'])
		expected = ['fromStep', 'toStep', 'scale']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['fromStep', 'toStep', 'scale']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('LayerTree.replaySnapshot',
		    snapshotId=snapshotId, **kwargs)
		return subdom_funcs

	def LayerTree_snapshotCommandLog(self, snapshotId):
		"""
		Function path: LayerTree.snapshotCommandLog
			Domain: LayerTree
			Method name: snapshotCommandLog
		
			Parameters:
				Required arguments:
					'snapshotId' (type: SnapshotId) -> The id of the layer snapshot.
			Returns:
				'commandLog' (type: array) -> The array of canvas function calls.
		
			Description: Replays the layer snapshot and returns canvas log.
		"""
		subdom_funcs = self.synchronous_command('LayerTree.snapshotCommandLog',
		    snapshotId=snapshotId)
		return subdom_funcs

	def DeviceOrientation_setDeviceOrientationOverride(self, alpha, beta, gamma):
		"""
		Function path: DeviceOrientation.setDeviceOrientationOverride
			Domain: DeviceOrientation
			Method name: setDeviceOrientationOverride
		
			Parameters:
				Required arguments:
					'alpha' (type: number) -> Mock alpha
					'beta' (type: number) -> Mock beta
					'gamma' (type: number) -> Mock gamma
			No return value.
		
			Description: Overrides the Device Orientation.
		"""
		assert isinstance(alpha, (float, int)
		    ), "Argument 'alpha' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    alpha)
		assert isinstance(beta, (float, int)
		    ), "Argument 'beta' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    beta)
		assert isinstance(gamma, (float, int)
		    ), "Argument 'gamma' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    gamma)
		subdom_funcs = self.synchronous_command(
		    'DeviceOrientation.setDeviceOrientationOverride', alpha=alpha, beta=
		    beta, gamma=gamma)
		return subdom_funcs

	def DeviceOrientation_clearDeviceOrientationOverride(self):
		"""
		Function path: DeviceOrientation.clearDeviceOrientationOverride
			Domain: DeviceOrientation
			Method name: clearDeviceOrientationOverride
		
			No return value.
		
			Description: Clears the overridden Device Orientation.
		"""
		subdom_funcs = self.synchronous_command(
		    'DeviceOrientation.clearDeviceOrientationOverride')
		return subdom_funcs

	def Tracing_start(self, **kwargs):
		"""
		Function path: Tracing.start
			Domain: Tracing
			Method name: start
		
			Parameters:
				Optional arguments:
					'categories' (type: string) -> Category/tag filter
					'options' (type: string) -> Tracing options
					'bufferUsageReportingInterval' (type: number) -> If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
					'transferMode' (type: string) -> Whether to report trace events as series of dataCollected events or to save trace to a stream (defaults to <code>ReportEvents</code>).
					'traceConfig' (type: TraceConfig) -> 
			No return value.
		
			Description: Start trace events collection.
		"""
		if 'categories' in kwargs:
			assert isinstance(kwargs['categories'], (str,)
			    ), "Optional argument 'categories' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['categories'])
		if 'options' in kwargs:
			assert isinstance(kwargs['options'], (str,)
			    ), "Optional argument 'options' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['options'])
		if 'bufferUsageReportingInterval' in kwargs:
			assert isinstance(kwargs['bufferUsageReportingInterval'], (float, int)
			    ), "Optional argument 'bufferUsageReportingInterval' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['bufferUsageReportingInterval'])
		if 'transferMode' in kwargs:
			assert isinstance(kwargs['transferMode'], (str,)
			    ), "Optional argument 'transferMode' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['transferMode'])
		expected = ['categories', 'options', 'bufferUsageReportingInterval',
		    'transferMode', 'traceConfig']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['categories', 'options', 'bufferUsageReportingInterval', 'transferMode', 'traceConfig']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Tracing.start', **kwargs)
		return subdom_funcs

	def Tracing_end(self):
		"""
		Function path: Tracing.end
			Domain: Tracing
			Method name: end
		
			No return value.
		
			Description: Stop trace events collection.
		"""
		subdom_funcs = self.synchronous_command('Tracing.end')
		return subdom_funcs

	def Tracing_getCategories(self):
		"""
		Function path: Tracing.getCategories
			Domain: Tracing
			Method name: getCategories
		
			Returns:
				'categories' (type: array) -> A list of supported tracing categories.
		
			Description: Gets supported tracing categories.
		"""
		subdom_funcs = self.synchronous_command('Tracing.getCategories')
		return subdom_funcs

	def Tracing_requestMemoryDump(self):
		"""
		Function path: Tracing.requestMemoryDump
			Domain: Tracing
			Method name: requestMemoryDump
		
			Returns:
				'dumpGuid' (type: string) -> GUID of the resulting global memory dump.
				'success' (type: boolean) -> True iff the global memory dump succeeded.
		
			Description: Request a global memory dump.
		"""
		subdom_funcs = self.synchronous_command('Tracing.requestMemoryDump')
		return subdom_funcs

	def Tracing_recordClockSyncMarker(self, syncId):
		"""
		Function path: Tracing.recordClockSyncMarker
			Domain: Tracing
			Method name: recordClockSyncMarker
		
			Parameters:
				Required arguments:
					'syncId' (type: string) -> The ID of this clock sync marker
			No return value.
		
			Description: Record a clock sync marker in the trace.
		"""
		assert isinstance(syncId, (str,)
		    ), "Argument 'syncId' must be of type '['str']'. Received type: '%s'" % type(
		    syncId)
		subdom_funcs = self.synchronous_command('Tracing.recordClockSyncMarker',
		    syncId=syncId)
		return subdom_funcs

	def Animation_enable(self):
		"""
		Function path: Animation.enable
			Domain: Animation
			Method name: enable
		
			No return value.
		
			Description: Enables animation domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Animation.enable')
		return subdom_funcs

	def Animation_disable(self):
		"""
		Function path: Animation.disable
			Domain: Animation
			Method name: disable
		
			No return value.
		
			Description: Disables animation domain notifications.
		"""
		subdom_funcs = self.synchronous_command('Animation.disable')
		return subdom_funcs

	def Animation_getPlaybackRate(self):
		"""
		Function path: Animation.getPlaybackRate
			Domain: Animation
			Method name: getPlaybackRate
		
			Returns:
				'playbackRate' (type: number) -> Playback rate for animations on page.
		
			Description: Gets the playback rate of the document timeline.
		"""
		subdom_funcs = self.synchronous_command('Animation.getPlaybackRate')
		return subdom_funcs

	def Animation_setPlaybackRate(self, playbackRate):
		"""
		Function path: Animation.setPlaybackRate
			Domain: Animation
			Method name: setPlaybackRate
		
			Parameters:
				Required arguments:
					'playbackRate' (type: number) -> Playback rate for animations on page
			No return value.
		
			Description: Sets the playback rate of the document timeline.
		"""
		assert isinstance(playbackRate, (float, int)
		    ), "Argument 'playbackRate' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    playbackRate)
		subdom_funcs = self.synchronous_command('Animation.setPlaybackRate',
		    playbackRate=playbackRate)
		return subdom_funcs

	def Animation_getCurrentTime(self, id):
		"""
		Function path: Animation.getCurrentTime
			Domain: Animation
			Method name: getCurrentTime
		
			Parameters:
				Required arguments:
					'id' (type: string) -> Id of animation.
			Returns:
				'currentTime' (type: number) -> Current time of the page.
		
			Description: Returns the current time of the an animation.
		"""
		assert isinstance(id, (str,)
		    ), "Argument 'id' must be of type '['str']'. Received type: '%s'" % type(
		    id)
		subdom_funcs = self.synchronous_command('Animation.getCurrentTime', id=id)
		return subdom_funcs

	def Animation_setPaused(self, animations, paused):
		"""
		Function path: Animation.setPaused
			Domain: Animation
			Method name: setPaused
		
			Parameters:
				Required arguments:
					'animations' (type: array) -> Animations to set the pause state of.
					'paused' (type: boolean) -> Paused state to set to.
			No return value.
		
			Description: Sets the paused state of a set of animations.
		"""
		assert isinstance(animations, (list, tuple)
		    ), "Argument 'animations' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    animations)
		assert isinstance(paused, (bool,)
		    ), "Argument 'paused' must be of type '['bool']'. Received type: '%s'" % type(
		    paused)
		subdom_funcs = self.synchronous_command('Animation.setPaused', animations
		    =animations, paused=paused)
		return subdom_funcs

	def Animation_setTiming(self, animationId, duration, delay):
		"""
		Function path: Animation.setTiming
			Domain: Animation
			Method name: setTiming
		
			Parameters:
				Required arguments:
					'animationId' (type: string) -> Animation id.
					'duration' (type: number) -> Duration of the animation.
					'delay' (type: number) -> Delay of the animation.
			No return value.
		
			Description: Sets the timing of an animation node.
		"""
		assert isinstance(animationId, (str,)
		    ), "Argument 'animationId' must be of type '['str']'. Received type: '%s'" % type(
		    animationId)
		assert isinstance(duration, (float, int)
		    ), "Argument 'duration' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    duration)
		assert isinstance(delay, (float, int)
		    ), "Argument 'delay' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    delay)
		subdom_funcs = self.synchronous_command('Animation.setTiming',
		    animationId=animationId, duration=duration, delay=delay)
		return subdom_funcs

	def Animation_seekAnimations(self, animations, currentTime):
		"""
		Function path: Animation.seekAnimations
			Domain: Animation
			Method name: seekAnimations
		
			Parameters:
				Required arguments:
					'animations' (type: array) -> List of animation ids to seek.
					'currentTime' (type: number) -> Set the current time of each animation.
			No return value.
		
			Description: Seek a set of animations to a particular time within each animation.
		"""
		assert isinstance(animations, (list, tuple)
		    ), "Argument 'animations' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    animations)
		assert isinstance(currentTime, (float, int)
		    ), "Argument 'currentTime' must be of type '['float', 'int']'. Received type: '%s'" % type(
		    currentTime)
		subdom_funcs = self.synchronous_command('Animation.seekAnimations',
		    animations=animations, currentTime=currentTime)
		return subdom_funcs

	def Animation_releaseAnimations(self, animations):
		"""
		Function path: Animation.releaseAnimations
			Domain: Animation
			Method name: releaseAnimations
		
			Parameters:
				Required arguments:
					'animations' (type: array) -> List of animation ids to seek.
			No return value.
		
			Description: Releases a set of animations to no longer be manipulated.
		"""
		assert isinstance(animations, (list, tuple)
		    ), "Argument 'animations' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    animations)
		subdom_funcs = self.synchronous_command('Animation.releaseAnimations',
		    animations=animations)
		return subdom_funcs

	def Animation_resolveAnimation(self, animationId):
		"""
		Function path: Animation.resolveAnimation
			Domain: Animation
			Method name: resolveAnimation
		
			Parameters:
				Required arguments:
					'animationId' (type: string) -> Animation id.
			Returns:
				'remoteObject' (type: Runtime.RemoteObject) -> Corresponding remote object.
		
			Description: Gets the remote object of the Animation.
		"""
		assert isinstance(animationId, (str,)
		    ), "Argument 'animationId' must be of type '['str']'. Received type: '%s'" % type(
		    animationId)
		subdom_funcs = self.synchronous_command('Animation.resolveAnimation',
		    animationId=animationId)
		return subdom_funcs

	def Accessibility_getPartialAXTree(self, nodeId, **kwargs):
		"""
		Function path: Accessibility.getPartialAXTree
			Domain: Accessibility
			Method name: getPartialAXTree
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> ID of node to get the partial accessibility tree for.
				Optional arguments:
					'fetchRelatives' (type: boolean) -> Whether to fetch this nodes ancestors, siblings and children. Defaults to true.
			Returns:
				'nodes' (type: array) -> The <code>Accessibility.AXNode</code> for this DOM node, if it exists, plus its ancestors, siblings and children, if requested.
		
			Description: Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.
		"""
		if 'fetchRelatives' in kwargs:
			assert isinstance(kwargs['fetchRelatives'], (bool,)
			    ), "Optional argument 'fetchRelatives' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['fetchRelatives'])
		expected = ['fetchRelatives']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['fetchRelatives']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Accessibility.getPartialAXTree',
		    nodeId=nodeId, **kwargs)
		return subdom_funcs

	def Storage_clearDataForOrigin(self, origin, storageTypes):
		"""
		Function path: Storage.clearDataForOrigin
			Domain: Storage
			Method name: clearDataForOrigin
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
					'storageTypes' (type: string) -> Comma separated origin names.
			No return value.
		
			Description: Clears storage for origin.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		assert isinstance(storageTypes, (str,)
		    ), "Argument 'storageTypes' must be of type '['str']'. Received type: '%s'" % type(
		    storageTypes)
		subdom_funcs = self.synchronous_command('Storage.clearDataForOrigin',
		    origin=origin, storageTypes=storageTypes)
		return subdom_funcs

	def Storage_getUsageAndQuota(self, origin):
		"""
		Function path: Storage.getUsageAndQuota
			Domain: Storage
			Method name: getUsageAndQuota
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
			Returns:
				'usage' (type: number) -> Storage usage (bytes).
				'quota' (type: number) -> Storage quota (bytes).
				'usageBreakdown' (type: array) -> Storage usage per type (bytes).
		
			Description: Returns usage and quota in bytes.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		subdom_funcs = self.synchronous_command('Storage.getUsageAndQuota',
		    origin=origin)
		return subdom_funcs

	def Storage_trackCacheStorageForOrigin(self, origin):
		"""
		Function path: Storage.trackCacheStorageForOrigin
			Domain: Storage
			Method name: trackCacheStorageForOrigin
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
			No return value.
		
			Description: Registers origin to be notified when an update occurs to its cache storage list.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		subdom_funcs = self.synchronous_command('Storage.trackCacheStorageForOrigin',
		    origin=origin)
		return subdom_funcs

	def Storage_untrackCacheStorageForOrigin(self, origin):
		"""
		Function path: Storage.untrackCacheStorageForOrigin
			Domain: Storage
			Method name: untrackCacheStorageForOrigin
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
			No return value.
		
			Description: Unregisters origin from receiving notifications for cache storage.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		subdom_funcs = self.synchronous_command(
		    'Storage.untrackCacheStorageForOrigin', origin=origin)
		return subdom_funcs

	def Log_enable(self):
		"""
		Function path: Log.enable
			Domain: Log
			Method name: enable
		
			No return value.
		
			Description: Enables log domain, sends the entries collected so far to the client by means of the <code>entryAdded</code> notification.
		"""
		subdom_funcs = self.synchronous_command('Log.enable')
		return subdom_funcs

	def Log_disable(self):
		"""
		Function path: Log.disable
			Domain: Log
			Method name: disable
		
			No return value.
		
			Description: Disables log domain, prevents further log entries from being reported to the client.
		"""
		subdom_funcs = self.synchronous_command('Log.disable')
		return subdom_funcs

	def Log_clear(self):
		"""
		Function path: Log.clear
			Domain: Log
			Method name: clear
		
			No return value.
		
			Description: Clears the log.
		"""
		subdom_funcs = self.synchronous_command('Log.clear')
		return subdom_funcs

	def Log_startViolationsReport(self, config):
		"""
		Function path: Log.startViolationsReport
			Domain: Log
			Method name: startViolationsReport
		
			Parameters:
				Required arguments:
					'config' (type: array) -> Configuration for violations.
			No return value.
		
			Description: start violation reporting.
		"""
		assert isinstance(config, (list, tuple)
		    ), "Argument 'config' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    config)
		subdom_funcs = self.synchronous_command('Log.startViolationsReport',
		    config=config)
		return subdom_funcs

	def Log_stopViolationsReport(self):
		"""
		Function path: Log.stopViolationsReport
			Domain: Log
			Method name: stopViolationsReport
		
			No return value.
		
			Description: Stop violation reporting.
		"""
		subdom_funcs = self.synchronous_command('Log.stopViolationsReport')
		return subdom_funcs

	def SystemInfo_getInfo(self):
		"""
		Function path: SystemInfo.getInfo
			Domain: SystemInfo
			Method name: getInfo
		
			Returns:
				'gpu' (type: GPUInfo) -> Information about the GPUs on the system.
				'modelName' (type: string) -> A platform-dependent description of the model of the machine. On Mac OS, this is, for example, 'MacBookPro'. Will be the empty string if not supported.
				'modelVersion' (type: string) -> A platform-dependent description of the version of the machine. On Mac OS, this is, for example, '10.1'. Will be the empty string if not supported.
				'commandLine' (type: string) -> The command line string used to launch the browser. Will be the empty string if not supported.
		
			Description: Returns information about the system.
		"""
		subdom_funcs = self.synchronous_command('SystemInfo.getInfo')
		return subdom_funcs

	def Tethering_bind(self, port):
		"""
		Function path: Tethering.bind
			Domain: Tethering
			Method name: bind
		
			Parameters:
				Required arguments:
					'port' (type: integer) -> Port number to bind.
			No return value.
		
			Description: Request browser port binding.
		"""
		assert isinstance(port, (int,)
		    ), "Argument 'port' must be of type '['int']'. Received type: '%s'" % type(
		    port)
		subdom_funcs = self.synchronous_command('Tethering.bind', port=port)
		return subdom_funcs

	def Tethering_unbind(self, port):
		"""
		Function path: Tethering.unbind
			Domain: Tethering
			Method name: unbind
		
			Parameters:
				Required arguments:
					'port' (type: integer) -> Port number to unbind.
			No return value.
		
			Description: Request browser port unbinding.
		"""
		assert isinstance(port, (int,)
		    ), "Argument 'port' must be of type '['int']'. Received type: '%s'" % type(
		    port)
		subdom_funcs = self.synchronous_command('Tethering.unbind', port=port)
		return subdom_funcs

	def Browser_getWindowForTarget(self, targetId):
		"""
		Function path: Browser.getWindowForTarget
			Domain: Browser
			Method name: getWindowForTarget
		
			Parameters:
				Required arguments:
					'targetId' (type: Target.TargetID) -> Devtools agent host id.
			Returns:
				'windowId' (type: WindowID) -> Browser window id.
				'bounds' (type: Bounds) -> Bounds information of the window. When window state is 'minimized', the restored window position and size are returned.
		
			Description: Get the browser window that contains the devtools target.
		"""
		subdom_funcs = self.synchronous_command('Browser.getWindowForTarget',
		    targetId=targetId)
		return subdom_funcs

	def Browser_getVersion(self):
		"""
		Function path: Browser.getVersion
			Domain: Browser
			Method name: getVersion
		
			Returns:
				'protocolVersion' (type: string) -> Protocol version.
				'product' (type: string) -> Product name.
				'revision' (type: string) -> Product revision.
				'userAgent' (type: string) -> User-Agent.
				'jsVersion' (type: string) -> V8 version.
		
			Description: Returns version information.
		"""
		subdom_funcs = self.synchronous_command('Browser.getVersion')
		return subdom_funcs

	def Browser_setWindowBounds(self, windowId, bounds):
		"""
		Function path: Browser.setWindowBounds
			Domain: Browser
			Method name: setWindowBounds
		
			Parameters:
				Required arguments:
					'windowId' (type: WindowID) -> Browser window id.
					'bounds' (type: Bounds) -> New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
			No return value.
		
			Description: Set position and/or size of the browser window.
		"""
		subdom_funcs = self.synchronous_command('Browser.setWindowBounds',
		    windowId=windowId, bounds=bounds)
		return subdom_funcs

	def Browser_getWindowBounds(self, windowId):
		"""
		Function path: Browser.getWindowBounds
			Domain: Browser
			Method name: getWindowBounds
		
			Parameters:
				Required arguments:
					'windowId' (type: WindowID) -> Browser window id.
			Returns:
				'bounds' (type: Bounds) -> Bounds information of the window. When window state is 'minimized', the restored window position and size are returned.
		
			Description: Get position and size of the browser window.
		"""
		subdom_funcs = self.synchronous_command('Browser.getWindowBounds',
		    windowId=windowId)
		return subdom_funcs

	def Schema_getDomains(self):
		"""
		Function path: Schema.getDomains
			Domain: Schema
			Method name: getDomains
		
			Returns:
				'domains' (type: array) -> List of supported domains.
		
			Description: Returns supported domains.
		"""
		subdom_funcs = self.synchronous_command('Schema.getDomains')
		return subdom_funcs

	def Runtime_evaluate(self, expression, **kwargs):
		"""
		Function path: Runtime.evaluate
			Domain: Runtime
			Method name: evaluate
		
			Parameters:
				Required arguments:
					'expression' (type: string) -> Expression to evaluate.
				Optional arguments:
					'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects.
					'includeCommandLineAPI' (type: boolean) -> Determines whether Command Line API should be available during the evaluation.
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
					'contextId' (type: ExecutionContextId) -> Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object that should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'userGesture' (type: boolean) -> Whether execution should be treated as initiated by user in the UI.
					'awaitPromise' (type: boolean) -> Whether execution should <code>await</code> for resulting value and return once awaited promise is resolved.
			Returns:
				'result' (type: RemoteObject) -> Evaluation result.
				'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		
			Description: Evaluates expression on global object.
		"""
		assert isinstance(expression, (str,)
		    ), "Argument 'expression' must be of type '['str']'. Received type: '%s'" % type(
		    expression)
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		if 'includeCommandLineAPI' in kwargs:
			assert isinstance(kwargs['includeCommandLineAPI'], (bool,)
			    ), "Optional argument 'includeCommandLineAPI' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeCommandLineAPI'])
		if 'silent' in kwargs:
			assert isinstance(kwargs['silent'], (bool,)
			    ), "Optional argument 'silent' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['silent'])
		if 'returnByValue' in kwargs:
			assert isinstance(kwargs['returnByValue'], (bool,)
			    ), "Optional argument 'returnByValue' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['returnByValue'])
		if 'generatePreview' in kwargs:
			assert isinstance(kwargs['generatePreview'], (bool,)
			    ), "Optional argument 'generatePreview' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['generatePreview'])
		if 'userGesture' in kwargs:
			assert isinstance(kwargs['userGesture'], (bool,)
			    ), "Optional argument 'userGesture' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['userGesture'])
		if 'awaitPromise' in kwargs:
			assert isinstance(kwargs['awaitPromise'], (bool,)
			    ), "Optional argument 'awaitPromise' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['awaitPromise'])
		expected = ['objectGroup', 'includeCommandLineAPI', 'silent', 'contextId',
		    'returnByValue', 'generatePreview', 'userGesture', 'awaitPromise']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['objectGroup', 'includeCommandLineAPI', 'silent', 'contextId', 'returnByValue', 'generatePreview', 'userGesture', 'awaitPromise']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.evaluate', expression=
		    expression, **kwargs)
		return subdom_funcs

	def Runtime_awaitPromise(self, promiseObjectId, **kwargs):
		"""
		Function path: Runtime.awaitPromise
			Domain: Runtime
			Method name: awaitPromise
		
			Parameters:
				Required arguments:
					'promiseObjectId' (type: RemoteObjectId) -> Identifier of the promise.
				Optional arguments:
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object that should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
			Returns:
				'result' (type: RemoteObject) -> Promise result. Will contain rejected value if promise was rejected.
				'exceptionDetails' (type: ExceptionDetails) -> Exception details if stack strace is available.
		
			Description: Add handler to promise with given promise object id.
		"""
		if 'returnByValue' in kwargs:
			assert isinstance(kwargs['returnByValue'], (bool,)
			    ), "Optional argument 'returnByValue' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['returnByValue'])
		if 'generatePreview' in kwargs:
			assert isinstance(kwargs['generatePreview'], (bool,)
			    ), "Optional argument 'generatePreview' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['generatePreview'])
		expected = ['returnByValue', 'generatePreview']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['returnByValue', 'generatePreview']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.awaitPromise',
		    promiseObjectId=promiseObjectId, **kwargs)
		return subdom_funcs

	def Runtime_callFunctionOn(self, functionDeclaration, **kwargs):
		"""
		Function path: Runtime.callFunctionOn
			Domain: Runtime
			Method name: callFunctionOn
		
			Parameters:
				Required arguments:
					'functionDeclaration' (type: string) -> Declaration of the function to call.
				Optional arguments:
					'objectId' (type: RemoteObjectId) -> Identifier of the object to call function on. Either objectId or executionContextId should be specified.
					'arguments' (type: array) -> Call arguments. All call arguments must belong to the same JavaScript world as the target object.
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object which should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'userGesture' (type: boolean) -> Whether execution should be treated as initiated by user in the UI.
					'awaitPromise' (type: boolean) -> Whether execution should <code>await</code> for resulting value and return once awaited promise is resolved.
					'executionContextId' (type: ExecutionContextId) -> Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified.
					'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object.
			Returns:
				'result' (type: RemoteObject) -> Call result.
				'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		
			Description: Calls function with given declaration on the given object. Object group of the result is inherited from the target object.
		"""
		assert isinstance(functionDeclaration, (str,)
		    ), "Argument 'functionDeclaration' must be of type '['str']'. Received type: '%s'" % type(
		    functionDeclaration)
		if 'arguments' in kwargs:
			assert isinstance(kwargs['arguments'], (list, tuple)
			    ), "Optional argument 'arguments' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['arguments'])
		if 'silent' in kwargs:
			assert isinstance(kwargs['silent'], (bool,)
			    ), "Optional argument 'silent' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['silent'])
		if 'returnByValue' in kwargs:
			assert isinstance(kwargs['returnByValue'], (bool,)
			    ), "Optional argument 'returnByValue' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['returnByValue'])
		if 'generatePreview' in kwargs:
			assert isinstance(kwargs['generatePreview'], (bool,)
			    ), "Optional argument 'generatePreview' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['generatePreview'])
		if 'userGesture' in kwargs:
			assert isinstance(kwargs['userGesture'], (bool,)
			    ), "Optional argument 'userGesture' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['userGesture'])
		if 'awaitPromise' in kwargs:
			assert isinstance(kwargs['awaitPromise'], (bool,)
			    ), "Optional argument 'awaitPromise' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['awaitPromise'])
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		expected = ['objectId', 'arguments', 'silent', 'returnByValue',
		    'generatePreview', 'userGesture', 'awaitPromise',
		    'executionContextId', 'objectGroup']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['objectId', 'arguments', 'silent', 'returnByValue', 'generatePreview', 'userGesture', 'awaitPromise', 'executionContextId', 'objectGroup']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.callFunctionOn',
		    functionDeclaration=functionDeclaration, **kwargs)
		return subdom_funcs

	def Runtime_getProperties(self, objectId, **kwargs):
		"""
		Function path: Runtime.getProperties
			Domain: Runtime
			Method name: getProperties
		
			Parameters:
				Required arguments:
					'objectId' (type: RemoteObjectId) -> Identifier of the object to return properties for.
				Optional arguments:
					'ownProperties' (type: boolean) -> If true, returns properties belonging only to the element itself, not to its prototype chain.
					'accessorPropertiesOnly' (type: boolean) -> If true, returns accessor properties (with getter/setter) only; internal properties are not returned either.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the results.
			Returns:
				'result' (type: array) -> Object properties.
				'internalProperties' (type: array) -> Internal object properties (only of the element itself).
				'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		
			Description: Returns properties of a given object. Object group of the result is inherited from the target object.
		"""
		if 'ownProperties' in kwargs:
			assert isinstance(kwargs['ownProperties'], (bool,)
			    ), "Optional argument 'ownProperties' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['ownProperties'])
		if 'accessorPropertiesOnly' in kwargs:
			assert isinstance(kwargs['accessorPropertiesOnly'], (bool,)
			    ), "Optional argument 'accessorPropertiesOnly' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['accessorPropertiesOnly'])
		if 'generatePreview' in kwargs:
			assert isinstance(kwargs['generatePreview'], (bool,)
			    ), "Optional argument 'generatePreview' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['generatePreview'])
		expected = ['ownProperties', 'accessorPropertiesOnly', 'generatePreview']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['ownProperties', 'accessorPropertiesOnly', 'generatePreview']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.getProperties', objectId
		    =objectId, **kwargs)
		return subdom_funcs

	def Runtime_releaseObject(self, objectId):
		"""
		Function path: Runtime.releaseObject
			Domain: Runtime
			Method name: releaseObject
		
			Parameters:
				Required arguments:
					'objectId' (type: RemoteObjectId) -> Identifier of the object to release.
			No return value.
		
			Description: Releases remote object with given id.
		"""
		subdom_funcs = self.synchronous_command('Runtime.releaseObject', objectId
		    =objectId)
		return subdom_funcs

	def Runtime_releaseObjectGroup(self, objectGroup):
		"""
		Function path: Runtime.releaseObjectGroup
			Domain: Runtime
			Method name: releaseObjectGroup
		
			Parameters:
				Required arguments:
					'objectGroup' (type: string) -> Symbolic object group name.
			No return value.
		
			Description: Releases all remote objects that belong to a given group.
		"""
		assert isinstance(objectGroup, (str,)
		    ), "Argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
		    objectGroup)
		subdom_funcs = self.synchronous_command('Runtime.releaseObjectGroup',
		    objectGroup=objectGroup)
		return subdom_funcs

	def Runtime_runIfWaitingForDebugger(self):
		"""
		Function path: Runtime.runIfWaitingForDebugger
			Domain: Runtime
			Method name: runIfWaitingForDebugger
		
			No return value.
		
			Description: Tells inspected instance to run if it was waiting for debugger to attach.
		"""
		subdom_funcs = self.synchronous_command('Runtime.runIfWaitingForDebugger')
		return subdom_funcs

	def Runtime_enable(self):
		"""
		Function path: Runtime.enable
			Domain: Runtime
			Method name: enable
		
			No return value.
		
			Description: Enables reporting of execution contexts creation by means of <code>executionContextCreated</code> event. When the reporting gets enabled the event will be sent immediately for each existing execution context.
		"""
		subdom_funcs = self.synchronous_command('Runtime.enable')
		return subdom_funcs

	def Runtime_disable(self):
		"""
		Function path: Runtime.disable
			Domain: Runtime
			Method name: disable
		
			No return value.
		
			Description: Disables reporting of execution contexts creation.
		"""
		subdom_funcs = self.synchronous_command('Runtime.disable')
		return subdom_funcs

	def Runtime_discardConsoleEntries(self):
		"""
		Function path: Runtime.discardConsoleEntries
			Domain: Runtime
			Method name: discardConsoleEntries
		
			No return value.
		
			Description: Discards collected exceptions and console API calls.
		"""
		subdom_funcs = self.synchronous_command('Runtime.discardConsoleEntries')
		return subdom_funcs

	def Runtime_setCustomObjectFormatterEnabled(self, enabled):
		"""
		Function path: Runtime.setCustomObjectFormatterEnabled
			Domain: Runtime
			Method name: setCustomObjectFormatterEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> No description
			No return value.
		
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command(
		    'Runtime.setCustomObjectFormatterEnabled', enabled=enabled)
		return subdom_funcs

	def Runtime_compileScript(self, expression, sourceURL, persistScript, **kwargs
	    ):
		"""
		Function path: Runtime.compileScript
			Domain: Runtime
			Method name: compileScript
		
			Parameters:
				Required arguments:
					'expression' (type: string) -> Expression to compile.
					'sourceURL' (type: string) -> Source url to be set for the script.
					'persistScript' (type: boolean) -> Specifies whether the compiled script should be persisted.
				Optional arguments:
					'executionContextId' (type: ExecutionContextId) -> Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
			Returns:
				'scriptId' (type: ScriptId) -> Id of the script.
				'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		
			Description: Compiles expression.
		"""
		assert isinstance(expression, (str,)
		    ), "Argument 'expression' must be of type '['str']'. Received type: '%s'" % type(
		    expression)
		assert isinstance(sourceURL, (str,)
		    ), "Argument 'sourceURL' must be of type '['str']'. Received type: '%s'" % type(
		    sourceURL)
		assert isinstance(persistScript, (bool,)
		    ), "Argument 'persistScript' must be of type '['bool']'. Received type: '%s'" % type(
		    persistScript)
		expected = ['executionContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['executionContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.compileScript',
		    expression=expression, sourceURL=sourceURL, persistScript=
		    persistScript, **kwargs)
		return subdom_funcs

	def Runtime_runScript(self, scriptId, **kwargs):
		"""
		Function path: Runtime.runScript
			Domain: Runtime
			Method name: runScript
		
			Parameters:
				Required arguments:
					'scriptId' (type: ScriptId) -> Id of the script to run.
				Optional arguments:
					'executionContextId' (type: ExecutionContextId) -> Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
					'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects.
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
					'includeCommandLineAPI' (type: boolean) -> Determines whether Command Line API should be available during the evaluation.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object which should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'awaitPromise' (type: boolean) -> Whether execution should <code>await</code> for resulting value and return once awaited promise is resolved.
			Returns:
				'result' (type: RemoteObject) -> Run result.
				'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		
			Description: Runs script with given id in a given context.
		"""
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		if 'silent' in kwargs:
			assert isinstance(kwargs['silent'], (bool,)
			    ), "Optional argument 'silent' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['silent'])
		if 'includeCommandLineAPI' in kwargs:
			assert isinstance(kwargs['includeCommandLineAPI'], (bool,)
			    ), "Optional argument 'includeCommandLineAPI' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeCommandLineAPI'])
		if 'returnByValue' in kwargs:
			assert isinstance(kwargs['returnByValue'], (bool,)
			    ), "Optional argument 'returnByValue' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['returnByValue'])
		if 'generatePreview' in kwargs:
			assert isinstance(kwargs['generatePreview'], (bool,)
			    ), "Optional argument 'generatePreview' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['generatePreview'])
		if 'awaitPromise' in kwargs:
			assert isinstance(kwargs['awaitPromise'], (bool,)
			    ), "Optional argument 'awaitPromise' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['awaitPromise'])
		expected = ['executionContextId', 'objectGroup', 'silent',
		    'includeCommandLineAPI', 'returnByValue', 'generatePreview',
		    'awaitPromise']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['executionContextId', 'objectGroup', 'silent', 'includeCommandLineAPI', 'returnByValue', 'generatePreview', 'awaitPromise']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.runScript', scriptId=
		    scriptId, **kwargs)
		return subdom_funcs

	def Runtime_queryObjects(self, prototypeObjectId):
		"""
		Function path: Runtime.queryObjects
			Domain: Runtime
			Method name: queryObjects
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'prototypeObjectId' (type: RemoteObjectId) -> Identifier of the prototype to return objects for.
			Returns:
				'objects' (type: RemoteObject) -> Array with objects.
		
		"""
		subdom_funcs = self.synchronous_command('Runtime.queryObjects',
		    prototypeObjectId=prototypeObjectId)
		return subdom_funcs

	def Debugger_enable(self):
		"""
		Function path: Debugger.enable
			Domain: Debugger
			Method name: enable
		
			No return value.
		
			Description: Enables debugger for the given page. Clients should not assume that the debugging has been enabled until the result for this command is received.
		"""
		subdom_funcs = self.synchronous_command('Debugger.enable')
		return subdom_funcs

	def Debugger_disable(self):
		"""
		Function path: Debugger.disable
			Domain: Debugger
			Method name: disable
		
			No return value.
		
			Description: Disables debugger for given page.
		"""
		subdom_funcs = self.synchronous_command('Debugger.disable')
		return subdom_funcs

	def Debugger_setBreakpointsActive(self, active):
		"""
		Function path: Debugger.setBreakpointsActive
			Domain: Debugger
			Method name: setBreakpointsActive
		
			Parameters:
				Required arguments:
					'active' (type: boolean) -> New value for breakpoints active state.
			No return value.
		
			Description: Activates / deactivates all breakpoints on the page.
		"""
		assert isinstance(active, (bool,)
		    ), "Argument 'active' must be of type '['bool']'. Received type: '%s'" % type(
		    active)
		subdom_funcs = self.synchronous_command('Debugger.setBreakpointsActive',
		    active=active)
		return subdom_funcs

	def Debugger_setSkipAllPauses(self, skip):
		"""
		Function path: Debugger.setSkipAllPauses
			Domain: Debugger
			Method name: setSkipAllPauses
		
			Parameters:
				Required arguments:
					'skip' (type: boolean) -> New value for skip pauses state.
			No return value.
		
			Description: Makes page not interrupt on any pauses (breakpoint, exception, dom exception etc).
		"""
		assert isinstance(skip, (bool,)
		    ), "Argument 'skip' must be of type '['bool']'. Received type: '%s'" % type(
		    skip)
		subdom_funcs = self.synchronous_command('Debugger.setSkipAllPauses', skip
		    =skip)
		return subdom_funcs

	def Debugger_setBreakpointByUrl(self, lineNumber, **kwargs):
		"""
		Function path: Debugger.setBreakpointByUrl
			Domain: Debugger
			Method name: setBreakpointByUrl
		
			Parameters:
				Required arguments:
					'lineNumber' (type: integer) -> Line number to set breakpoint at.
				Optional arguments:
					'url' (type: string) -> URL of the resources to set breakpoint on.
					'urlRegex' (type: string) -> Regex pattern for the URLs of the resources to set breakpoints on. Either <code>url</code> or <code>urlRegex</code> must be specified.
					'columnNumber' (type: integer) -> Offset in the line to set breakpoint at.
					'condition' (type: string) -> Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
			Returns:
				'breakpointId' (type: BreakpointId) -> Id of the created breakpoint for further reference.
				'locations' (type: array) -> List of the locations this breakpoint resolved into upon addition.
		
			Description: Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this command is issued, all existing parsed scripts will have breakpoints resolved and returned in <code>locations</code> property. Further matching script parsing will result in subsequent <code>breakpointResolved</code> events issued. This logical breakpoint will survive page reloads.
		"""
		assert isinstance(lineNumber, (int,)
		    ), "Argument 'lineNumber' must be of type '['int']'. Received type: '%s'" % type(
		    lineNumber)
		if 'url' in kwargs:
			assert isinstance(kwargs['url'], (str,)
			    ), "Optional argument 'url' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['url'])
		if 'urlRegex' in kwargs:
			assert isinstance(kwargs['urlRegex'], (str,)
			    ), "Optional argument 'urlRegex' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['urlRegex'])
		if 'columnNumber' in kwargs:
			assert isinstance(kwargs['columnNumber'], (int,)
			    ), "Optional argument 'columnNumber' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['columnNumber'])
		if 'condition' in kwargs:
			assert isinstance(kwargs['condition'], (str,)
			    ), "Optional argument 'condition' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['condition'])
		expected = ['url', 'urlRegex', 'columnNumber', 'condition']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['url', 'urlRegex', 'columnNumber', 'condition']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.setBreakpointByUrl',
		    lineNumber=lineNumber, **kwargs)
		return subdom_funcs

	def Debugger_setBreakpoint(self, location, **kwargs):
		"""
		Function path: Debugger.setBreakpoint
			Domain: Debugger
			Method name: setBreakpoint
		
			Parameters:
				Required arguments:
					'location' (type: Location) -> Location to set breakpoint in.
				Optional arguments:
					'condition' (type: string) -> Expression to use as a breakpoint condition. When specified, debugger will only stop on the breakpoint if this expression evaluates to true.
			Returns:
				'breakpointId' (type: BreakpointId) -> Id of the created breakpoint for further reference.
				'actualLocation' (type: Location) -> Location this breakpoint resolved into.
		
			Description: Sets JavaScript breakpoint at a given location.
		"""
		if 'condition' in kwargs:
			assert isinstance(kwargs['condition'], (str,)
			    ), "Optional argument 'condition' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['condition'])
		expected = ['condition']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['condition']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.setBreakpoint',
		    location=location, **kwargs)
		return subdom_funcs

	def Debugger_removeBreakpoint(self, breakpointId):
		"""
		Function path: Debugger.removeBreakpoint
			Domain: Debugger
			Method name: removeBreakpoint
		
			Parameters:
				Required arguments:
					'breakpointId' (type: BreakpointId) -> No description
			No return value.
		
			Description: Removes JavaScript breakpoint.
		"""
		subdom_funcs = self.synchronous_command('Debugger.removeBreakpoint',
		    breakpointId=breakpointId)
		return subdom_funcs

	def Debugger_getPossibleBreakpoints(self, start, **kwargs):
		"""
		Function path: Debugger.getPossibleBreakpoints
			Domain: Debugger
			Method name: getPossibleBreakpoints
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'start' (type: Location) -> Start of range to search possible breakpoint locations in.
				Optional arguments:
					'end' (type: Location) -> End of range to search possible breakpoint locations in (excluding). When not specified, end of scripts is used as end of range.
					'restrictToFunction' (type: boolean) -> Only consider locations which are in the same (non-nested) function as start.
			Returns:
				'locations' (type: array) -> List of the possible breakpoint locations.
		
			Description: Returns possible locations for breakpoint. scriptId in start and end range locations should be the same.
		"""
		if 'restrictToFunction' in kwargs:
			assert isinstance(kwargs['restrictToFunction'], (bool,)
			    ), "Optional argument 'restrictToFunction' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['restrictToFunction'])
		expected = ['end', 'restrictToFunction']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['end', 'restrictToFunction']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.getPossibleBreakpoints',
		    start=start, **kwargs)
		return subdom_funcs

	def Debugger_continueToLocation(self, location, **kwargs):
		"""
		Function path: Debugger.continueToLocation
			Domain: Debugger
			Method name: continueToLocation
		
			Parameters:
				Required arguments:
					'location' (type: Location) -> Location to continue to.
				Optional arguments:
					'targetCallFrames' (type: string) -> No description
			No return value.
		
			Description: Continues execution until specific location is reached.
		"""
		if 'targetCallFrames' in kwargs:
			assert isinstance(kwargs['targetCallFrames'], (str,)
			    ), "Optional argument 'targetCallFrames' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['targetCallFrames'])
		expected = ['targetCallFrames']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['targetCallFrames']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.continueToLocation',
		    location=location, **kwargs)
		return subdom_funcs

	def Debugger_stepOver(self):
		"""
		Function path: Debugger.stepOver
			Domain: Debugger
			Method name: stepOver
		
			No return value.
		
			Description: Steps over the statement.
		"""
		subdom_funcs = self.synchronous_command('Debugger.stepOver')
		return subdom_funcs

	def Debugger_stepInto(self):
		"""
		Function path: Debugger.stepInto
			Domain: Debugger
			Method name: stepInto
		
			No return value.
		
			Description: Steps into the function call.
		"""
		subdom_funcs = self.synchronous_command('Debugger.stepInto')
		return subdom_funcs

	def Debugger_stepOut(self):
		"""
		Function path: Debugger.stepOut
			Domain: Debugger
			Method name: stepOut
		
			No return value.
		
			Description: Steps out of the function call.
		"""
		subdom_funcs = self.synchronous_command('Debugger.stepOut')
		return subdom_funcs

	def Debugger_pause(self):
		"""
		Function path: Debugger.pause
			Domain: Debugger
			Method name: pause
		
			No return value.
		
			Description: Stops on the next JavaScript statement.
		"""
		subdom_funcs = self.synchronous_command('Debugger.pause')
		return subdom_funcs

	def Debugger_scheduleStepIntoAsync(self):
		"""
		Function path: Debugger.scheduleStepIntoAsync
			Domain: Debugger
			Method name: scheduleStepIntoAsync
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Steps into next scheduled async task if any is scheduled before next pause. Returns success when async task is actually scheduled, returns error if no task were scheduled or another scheduleStepIntoAsync was called.
		"""
		subdom_funcs = self.synchronous_command('Debugger.scheduleStepIntoAsync')
		return subdom_funcs

	def Debugger_resume(self):
		"""
		Function path: Debugger.resume
			Domain: Debugger
			Method name: resume
		
			No return value.
		
			Description: Resumes JavaScript execution.
		"""
		subdom_funcs = self.synchronous_command('Debugger.resume')
		return subdom_funcs

	def Debugger_searchInContent(self, scriptId, query, **kwargs):
		"""
		Function path: Debugger.searchInContent
			Domain: Debugger
			Method name: searchInContent
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'scriptId' (type: Runtime.ScriptId) -> Id of the script to search in.
					'query' (type: string) -> String to search for.
				Optional arguments:
					'caseSensitive' (type: boolean) -> If true, search is case sensitive.
					'isRegex' (type: boolean) -> If true, treats string parameter as regex.
			Returns:
				'result' (type: array) -> List of search matches.
		
			Description: Searches for given string in script content.
		"""
		assert isinstance(query, (str,)
		    ), "Argument 'query' must be of type '['str']'. Received type: '%s'" % type(
		    query)
		if 'caseSensitive' in kwargs:
			assert isinstance(kwargs['caseSensitive'], (bool,)
			    ), "Optional argument 'caseSensitive' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['caseSensitive'])
		if 'isRegex' in kwargs:
			assert isinstance(kwargs['isRegex'], (bool,)
			    ), "Optional argument 'isRegex' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['isRegex'])
		expected = ['caseSensitive', 'isRegex']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['caseSensitive', 'isRegex']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.searchInContent',
		    scriptId=scriptId, query=query, **kwargs)
		return subdom_funcs

	def Debugger_setScriptSource(self, scriptId, scriptSource, **kwargs):
		"""
		Function path: Debugger.setScriptSource
			Domain: Debugger
			Method name: setScriptSource
		
			Parameters:
				Required arguments:
					'scriptId' (type: Runtime.ScriptId) -> Id of the script to edit.
					'scriptSource' (type: string) -> New content of the script.
				Optional arguments:
					'dryRun' (type: boolean) ->  If true the change will not actually be applied. Dry run may be used to get result description without actually modifying the code.
			Returns:
				'callFrames' (type: array) -> New stack trace in case editing has happened while VM was stopped.
				'stackChanged' (type: boolean) -> Whether current call stack  was modified after applying the changes.
				'asyncStackTrace' (type: Runtime.StackTrace) -> Async stack trace, if any.
				'exceptionDetails' (type: Runtime.ExceptionDetails) -> Exception details if any.
		
			Description: Edits JavaScript source live.
		"""
		assert isinstance(scriptSource, (str,)
		    ), "Argument 'scriptSource' must be of type '['str']'. Received type: '%s'" % type(
		    scriptSource)
		if 'dryRun' in kwargs:
			assert isinstance(kwargs['dryRun'], (bool,)
			    ), "Optional argument 'dryRun' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['dryRun'])
		expected = ['dryRun']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['dryRun']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.setScriptSource',
		    scriptId=scriptId, scriptSource=scriptSource, **kwargs)
		return subdom_funcs

	def Debugger_restartFrame(self, callFrameId):
		"""
		Function path: Debugger.restartFrame
			Domain: Debugger
			Method name: restartFrame
		
			Parameters:
				Required arguments:
					'callFrameId' (type: CallFrameId) -> Call frame identifier to evaluate on.
			Returns:
				'callFrames' (type: array) -> New stack trace.
				'asyncStackTrace' (type: Runtime.StackTrace) -> Async stack trace, if any.
		
			Description: Restarts particular call frame from the beginning.
		"""
		subdom_funcs = self.synchronous_command('Debugger.restartFrame',
		    callFrameId=callFrameId)
		return subdom_funcs

	def Debugger_getScriptSource(self, scriptId):
		"""
		Function path: Debugger.getScriptSource
			Domain: Debugger
			Method name: getScriptSource
		
			Parameters:
				Required arguments:
					'scriptId' (type: Runtime.ScriptId) -> Id of the script to get source for.
			Returns:
				'scriptSource' (type: string) -> Script source.
		
			Description: Returns source for the script with given id.
		"""
		subdom_funcs = self.synchronous_command('Debugger.getScriptSource',
		    scriptId=scriptId)
		return subdom_funcs

	def Debugger_setPauseOnExceptions(self, state):
		"""
		Function path: Debugger.setPauseOnExceptions
			Domain: Debugger
			Method name: setPauseOnExceptions
		
			Parameters:
				Required arguments:
					'state' (type: string) -> Pause on exceptions mode.
			No return value.
		
			Description: Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions or no exceptions. Initial pause on exceptions state is <code>none</code>.
		"""
		assert isinstance(state, (str,)
		    ), "Argument 'state' must be of type '['str']'. Received type: '%s'" % type(
		    state)
		subdom_funcs = self.synchronous_command('Debugger.setPauseOnExceptions',
		    state=state)
		return subdom_funcs

	def Debugger_evaluateOnCallFrame(self, callFrameId, expression, **kwargs):
		"""
		Function path: Debugger.evaluateOnCallFrame
			Domain: Debugger
			Method name: evaluateOnCallFrame
		
			Parameters:
				Required arguments:
					'callFrameId' (type: CallFrameId) -> Call frame identifier to evaluate on.
					'expression' (type: string) -> Expression to evaluate.
				Optional arguments:
					'objectGroup' (type: string) -> String object group name to put result into (allows rapid releasing resulting object handles using <code>releaseObjectGroup</code>).
					'includeCommandLineAPI' (type: boolean) -> Specifies whether command line API should be available to the evaluated expression, defaults to false.
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object that should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'throwOnSideEffect' (type: boolean) -> Whether to throw an exception if side effect cannot be ruled out during evaluation.
			Returns:
				'result' (type: Runtime.RemoteObject) -> Object wrapper for the evaluation result.
				'exceptionDetails' (type: Runtime.ExceptionDetails) -> Exception details.
		
			Description: Evaluates expression on a given call frame.
		"""
		assert isinstance(expression, (str,)
		    ), "Argument 'expression' must be of type '['str']'. Received type: '%s'" % type(
		    expression)
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		if 'includeCommandLineAPI' in kwargs:
			assert isinstance(kwargs['includeCommandLineAPI'], (bool,)
			    ), "Optional argument 'includeCommandLineAPI' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeCommandLineAPI'])
		if 'silent' in kwargs:
			assert isinstance(kwargs['silent'], (bool,)
			    ), "Optional argument 'silent' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['silent'])
		if 'returnByValue' in kwargs:
			assert isinstance(kwargs['returnByValue'], (bool,)
			    ), "Optional argument 'returnByValue' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['returnByValue'])
		if 'generatePreview' in kwargs:
			assert isinstance(kwargs['generatePreview'], (bool,)
			    ), "Optional argument 'generatePreview' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['generatePreview'])
		if 'throwOnSideEffect' in kwargs:
			assert isinstance(kwargs['throwOnSideEffect'], (bool,)
			    ), "Optional argument 'throwOnSideEffect' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['throwOnSideEffect'])
		expected = ['objectGroup', 'includeCommandLineAPI', 'silent',
		    'returnByValue', 'generatePreview', 'throwOnSideEffect']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['objectGroup', 'includeCommandLineAPI', 'silent', 'returnByValue', 'generatePreview', 'throwOnSideEffect']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.evaluateOnCallFrame',
		    callFrameId=callFrameId, expression=expression, **kwargs)
		return subdom_funcs

	def Debugger_setVariableValue(self, scopeNumber, variableName, newValue,
	    callFrameId):
		"""
		Function path: Debugger.setVariableValue
			Domain: Debugger
			Method name: setVariableValue
		
			Parameters:
				Required arguments:
					'scopeNumber' (type: integer) -> 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch' scope types are allowed. Other scopes could be manipulated manually.
					'variableName' (type: string) -> Variable name.
					'newValue' (type: Runtime.CallArgument) -> New variable value.
					'callFrameId' (type: CallFrameId) -> Id of callframe that holds variable.
			No return value.
		
			Description: Changes value of variable in a callframe. Object-based scopes are not supported and must be mutated manually.
		"""
		assert isinstance(scopeNumber, (int,)
		    ), "Argument 'scopeNumber' must be of type '['int']'. Received type: '%s'" % type(
		    scopeNumber)
		assert isinstance(variableName, (str,)
		    ), "Argument 'variableName' must be of type '['str']'. Received type: '%s'" % type(
		    variableName)
		subdom_funcs = self.synchronous_command('Debugger.setVariableValue',
		    scopeNumber=scopeNumber, variableName=variableName, newValue=newValue,
		    callFrameId=callFrameId)
		return subdom_funcs

	def Debugger_setAsyncCallStackDepth(self, maxDepth):
		"""
		Function path: Debugger.setAsyncCallStackDepth
			Domain: Debugger
			Method name: setAsyncCallStackDepth
		
			Parameters:
				Required arguments:
					'maxDepth' (type: integer) -> Maximum depth of async call stacks. Setting to <code>0</code> will effectively disable collecting async call stacks (default).
			No return value.
		
			Description: Enables or disables async call stacks tracking.
		"""
		assert isinstance(maxDepth, (int,)
		    ), "Argument 'maxDepth' must be of type '['int']'. Received type: '%s'" % type(
		    maxDepth)
		subdom_funcs = self.synchronous_command('Debugger.setAsyncCallStackDepth',
		    maxDepth=maxDepth)
		return subdom_funcs

	def Debugger_setBlackboxPatterns(self, patterns):
		"""
		Function path: Debugger.setBlackboxPatterns
			Domain: Debugger
			Method name: setBlackboxPatterns
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'patterns' (type: array) -> Array of regexps that will be used to check script url for blackbox state.
			No return value.
		
			Description: Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in scripts with url matching one of the patterns. VM will try to leave blackboxed script by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
		"""
		assert isinstance(patterns, (list, tuple)
		    ), "Argument 'patterns' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    patterns)
		subdom_funcs = self.synchronous_command('Debugger.setBlackboxPatterns',
		    patterns=patterns)
		return subdom_funcs

	def Debugger_setBlackboxedRanges(self, scriptId, positions):
		"""
		Function path: Debugger.setBlackboxedRanges
			Domain: Debugger
			Method name: setBlackboxedRanges
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'scriptId' (type: Runtime.ScriptId) -> Id of the script.
					'positions' (type: array) -> No description
			No return value.
		
			Description: Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful. Positions array contains positions where blackbox state is changed. First interval isn't blackboxed. Array should be sorted.
		"""
		assert isinstance(positions, (list, tuple)
		    ), "Argument 'positions' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    positions)
		subdom_funcs = self.synchronous_command('Debugger.setBlackboxedRanges',
		    scriptId=scriptId, positions=positions)
		return subdom_funcs

	def Console_enable(self):
		"""
		Function path: Console.enable
			Domain: Console
			Method name: enable
		
			No return value.
		
			Description: Enables console domain, sends the messages collected so far to the client by means of the <code>messageAdded</code> notification.
		"""
		subdom_funcs = self.synchronous_command('Console.enable')
		return subdom_funcs

	def Console_disable(self):
		"""
		Function path: Console.disable
			Domain: Console
			Method name: disable
		
			No return value.
		
			Description: Disables console domain, prevents further console messages from being reported to the client.
		"""
		subdom_funcs = self.synchronous_command('Console.disable')
		return subdom_funcs

	def Console_clearMessages(self):
		"""
		Function path: Console.clearMessages
			Domain: Console
			Method name: clearMessages
		
			No return value.
		
			Description: Does nothing.
		"""
		subdom_funcs = self.synchronous_command('Console.clearMessages')
		return subdom_funcs

	def Profiler_enable(self):
		"""
		Function path: Profiler.enable
			Domain: Profiler
			Method name: enable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('Profiler.enable')
		return subdom_funcs

	def Profiler_disable(self):
		"""
		Function path: Profiler.disable
			Domain: Profiler
			Method name: disable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('Profiler.disable')
		return subdom_funcs

	def Profiler_setSamplingInterval(self, interval):
		"""
		Function path: Profiler.setSamplingInterval
			Domain: Profiler
			Method name: setSamplingInterval
		
			Parameters:
				Required arguments:
					'interval' (type: integer) -> New sampling interval in microseconds.
			No return value.
		
			Description: Changes CPU profiler sampling interval. Must be called before CPU profiles recording started.
		"""
		assert isinstance(interval, (int,)
		    ), "Argument 'interval' must be of type '['int']'. Received type: '%s'" % type(
		    interval)
		subdom_funcs = self.synchronous_command('Profiler.setSamplingInterval',
		    interval=interval)
		return subdom_funcs

	def Profiler_start(self):
		"""
		Function path: Profiler.start
			Domain: Profiler
			Method name: start
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('Profiler.start')
		return subdom_funcs

	def Profiler_stop(self):
		"""
		Function path: Profiler.stop
			Domain: Profiler
			Method name: stop
		
			Returns:
				'profile' (type: Profile) -> Recorded profile.
		
		"""
		subdom_funcs = self.synchronous_command('Profiler.stop')
		return subdom_funcs

	def Profiler_startPreciseCoverage(self, **kwargs):
		"""
		Function path: Profiler.startPreciseCoverage
			Domain: Profiler
			Method name: startPreciseCoverage
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'callCount' (type: boolean) -> Collect accurate call counts beyond simple 'covered' or 'not covered'.
					'detailed' (type: boolean) -> Collect block-based coverage.
			No return value.
		
			Description: Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code coverage may be incomplete. Enabling prevents running optimized code and resets execution counters.
		"""
		if 'callCount' in kwargs:
			assert isinstance(kwargs['callCount'], (bool,)
			    ), "Optional argument 'callCount' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['callCount'])
		if 'detailed' in kwargs:
			assert isinstance(kwargs['detailed'], (bool,)
			    ), "Optional argument 'detailed' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['detailed'])
		expected = ['callCount', 'detailed']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['callCount', 'detailed']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Profiler.startPreciseCoverage',
		    **kwargs)
		return subdom_funcs

	def Profiler_stopPreciseCoverage(self):
		"""
		Function path: Profiler.stopPreciseCoverage
			Domain: Profiler
			Method name: stopPreciseCoverage
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Disable precise code coverage. Disabling releases unnecessary execution count records and allows executing optimized code.
		"""
		subdom_funcs = self.synchronous_command('Profiler.stopPreciseCoverage')
		return subdom_funcs

	def Profiler_takePreciseCoverage(self):
		"""
		Function path: Profiler.takePreciseCoverage
			Domain: Profiler
			Method name: takePreciseCoverage
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'result' (type: array) -> Coverage data for the current isolate.
		
			Description: Collect coverage data for the current isolate, and resets execution counters. Precise code coverage needs to have started.
		"""
		subdom_funcs = self.synchronous_command('Profiler.takePreciseCoverage')
		return subdom_funcs

	def Profiler_getBestEffortCoverage(self):
		"""
		Function path: Profiler.getBestEffortCoverage
			Domain: Profiler
			Method name: getBestEffortCoverage
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'result' (type: array) -> Coverage data for the current isolate.
		
			Description: Collect coverage data for the current isolate. The coverage data may be incomplete due to garbage collection.
		"""
		subdom_funcs = self.synchronous_command('Profiler.getBestEffortCoverage')
		return subdom_funcs

	def Profiler_startTypeProfile(self):
		"""
		Function path: Profiler.startTypeProfile
			Domain: Profiler
			Method name: startTypeProfile
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Enable type profile.
		"""
		subdom_funcs = self.synchronous_command('Profiler.startTypeProfile')
		return subdom_funcs

	def Profiler_stopTypeProfile(self):
		"""
		Function path: Profiler.stopTypeProfile
			Domain: Profiler
			Method name: stopTypeProfile
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Disable type profile. Disabling releases type profile data collected so far.
		"""
		subdom_funcs = self.synchronous_command('Profiler.stopTypeProfile')
		return subdom_funcs

	def Profiler_takeTypeProfile(self):
		"""
		Function path: Profiler.takeTypeProfile
			Domain: Profiler
			Method name: takeTypeProfile
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'result' (type: array) -> Type profile for all scripts since startTypeProfile() was turned on.
		
			Description: Collect type profile.
		"""
		subdom_funcs = self.synchronous_command('Profiler.takeTypeProfile')
		return subdom_funcs

	def HeapProfiler_enable(self):
		"""
		Function path: HeapProfiler.enable
			Domain: HeapProfiler
			Method name: enable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.enable')
		return subdom_funcs

	def HeapProfiler_disable(self):
		"""
		Function path: HeapProfiler.disable
			Domain: HeapProfiler
			Method name: disable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.disable')
		return subdom_funcs

	def HeapProfiler_startTrackingHeapObjects(self, **kwargs):
		"""
		Function path: HeapProfiler.startTrackingHeapObjects
			Domain: HeapProfiler
			Method name: startTrackingHeapObjects
		
			Parameters:
				Optional arguments:
					'trackAllocations' (type: boolean) -> No description
			No return value.
		
		"""
		if 'trackAllocations' in kwargs:
			assert isinstance(kwargs['trackAllocations'], (bool,)
			    ), "Optional argument 'trackAllocations' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['trackAllocations'])
		expected = ['trackAllocations']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['trackAllocations']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'HeapProfiler.startTrackingHeapObjects', **kwargs)
		return subdom_funcs

	def HeapProfiler_stopTrackingHeapObjects(self, **kwargs):
		"""
		Function path: HeapProfiler.stopTrackingHeapObjects
			Domain: HeapProfiler
			Method name: stopTrackingHeapObjects
		
			Parameters:
				Optional arguments:
					'reportProgress' (type: boolean) -> If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken when the tracking is stopped.
			No return value.
		
		"""
		if 'reportProgress' in kwargs:
			assert isinstance(kwargs['reportProgress'], (bool,)
			    ), "Optional argument 'reportProgress' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['reportProgress'])
		expected = ['reportProgress']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['reportProgress']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'HeapProfiler.stopTrackingHeapObjects', **kwargs)
		return subdom_funcs

	def HeapProfiler_takeHeapSnapshot(self, **kwargs):
		"""
		Function path: HeapProfiler.takeHeapSnapshot
			Domain: HeapProfiler
			Method name: takeHeapSnapshot
		
			Parameters:
				Optional arguments:
					'reportProgress' (type: boolean) -> If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken.
			No return value.
		
		"""
		if 'reportProgress' in kwargs:
			assert isinstance(kwargs['reportProgress'], (bool,)
			    ), "Optional argument 'reportProgress' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['reportProgress'])
		expected = ['reportProgress']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['reportProgress']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('HeapProfiler.takeHeapSnapshot',
		    **kwargs)
		return subdom_funcs

	def HeapProfiler_collectGarbage(self):
		"""
		Function path: HeapProfiler.collectGarbage
			Domain: HeapProfiler
			Method name: collectGarbage
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.collectGarbage')
		return subdom_funcs

	def HeapProfiler_getObjectByHeapObjectId(self, objectId, **kwargs):
		"""
		Function path: HeapProfiler.getObjectByHeapObjectId
			Domain: HeapProfiler
			Method name: getObjectByHeapObjectId
		
			Parameters:
				Required arguments:
					'objectId' (type: HeapSnapshotObjectId) -> No description
				Optional arguments:
					'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects.
			Returns:
				'result' (type: Runtime.RemoteObject) -> Evaluation result.
		
		"""
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		expected = ['objectGroup']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['objectGroup']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'HeapProfiler.getObjectByHeapObjectId', objectId=objectId, **kwargs)
		return subdom_funcs

	def HeapProfiler_addInspectedHeapObject(self, heapObjectId):
		"""
		Function path: HeapProfiler.addInspectedHeapObject
			Domain: HeapProfiler
			Method name: addInspectedHeapObject
		
			Parameters:
				Required arguments:
					'heapObjectId' (type: HeapSnapshotObjectId) -> Heap snapshot object id to be accessible by means of $x command line API.
			No return value.
		
			Description: Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.addInspectedHeapObject'
		    , heapObjectId=heapObjectId)
		return subdom_funcs

	def HeapProfiler_getHeapObjectId(self, objectId):
		"""
		Function path: HeapProfiler.getHeapObjectId
			Domain: HeapProfiler
			Method name: getHeapObjectId
		
			Parameters:
				Required arguments:
					'objectId' (type: Runtime.RemoteObjectId) -> Identifier of the object to get heap object id for.
			Returns:
				'heapSnapshotObjectId' (type: HeapSnapshotObjectId) -> Id of the heap snapshot object corresponding to the passed remote object id.
		
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.getHeapObjectId',
		    objectId=objectId)
		return subdom_funcs

	def HeapProfiler_startSampling(self, **kwargs):
		"""
		Function path: HeapProfiler.startSampling
			Domain: HeapProfiler
			Method name: startSampling
		
			Parameters:
				Optional arguments:
					'samplingInterval' (type: number) -> Average sample interval in bytes. Poisson distribution is used for the intervals. The default value is 32768 bytes.
			No return value.
		
		"""
		if 'samplingInterval' in kwargs:
			assert isinstance(kwargs['samplingInterval'], (float, int)
			    ), "Optional argument 'samplingInterval' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['samplingInterval'])
		expected = ['samplingInterval']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['samplingInterval']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('HeapProfiler.startSampling', **
		    kwargs)
		return subdom_funcs

	def HeapProfiler_stopSampling(self):
		"""
		Function path: HeapProfiler.stopSampling
			Domain: HeapProfiler
			Method name: stopSampling
		
			Returns:
				'profile' (type: SamplingHeapProfile) -> Recorded sampling heap profile.
		
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.stopSampling')
		return subdom_funcs
