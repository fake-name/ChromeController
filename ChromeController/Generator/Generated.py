from ChromeController.transport import ChromeExecutionManager
from ChromeController.manager_base import ChromeInterface


class ChromeRemoteDebugInterface(ChromeInterface):
	"""

	"""

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def Accessibility_disable(self):
		"""
		Function path: Accessibility.disable
			Domain: Accessibility
			Method name: disable
		
			No return value.
		
			Description: Disables the accessibility domain.
		"""
		subdom_funcs = self.synchronous_command('Accessibility.disable')
		return subdom_funcs

	def Accessibility_enable(self):
		"""
		Function path: Accessibility.enable
			Domain: Accessibility
			Method name: enable
		
			No return value.
		
			Description: Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls.
This turns on accessibility for the page, which can impact performance until accessibility is disabled.
		"""
		subdom_funcs = self.synchronous_command('Accessibility.enable')
		return subdom_funcs

	def Accessibility_getPartialAXTree(self, **kwargs):
		"""
		Function path: Accessibility.getPartialAXTree
			Domain: Accessibility
			Method name: getPartialAXTree
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'nodeId' (type: DOM.NodeId) -> Identifier of the node to get the partial accessibility tree for.
					'backendNodeId' (type: DOM.BackendNodeId) -> Identifier of the backend node to get the partial accessibility tree for.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper to get the partial accessibility tree for.
					'fetchRelatives' (type: boolean) -> Whether to fetch this nodes ancestors, siblings and children. Defaults to true.
			Returns:
				'nodes' (type: array) -> The `Accessibility.AXNode` for this DOM node, if it exists, plus its ancestors, siblings and
children, if requested.
		
			Description: Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.
		"""
		if 'fetchRelatives' in kwargs:
			assert isinstance(kwargs['fetchRelatives'], (bool,)
			    ), "Optional argument 'fetchRelatives' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['fetchRelatives'])
		expected = ['nodeId', 'backendNodeId', 'objectId', 'fetchRelatives']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId', 'fetchRelatives']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Accessibility.getPartialAXTree',
		    **kwargs)
		return subdom_funcs

	def Accessibility_getFullAXTree(self, **kwargs):
		"""
		Function path: Accessibility.getFullAXTree
			Domain: Accessibility
			Method name: getFullAXTree
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'max_depth' (type: integer) -> The maximum depth at which descendants of the root node should be retrieved.
If omitted, the full tree is returned.
			Returns:
				'nodes' (type: array) -> No description
		
			Description: Fetches the entire accessibility tree for the root Document
		"""
		if 'max_depth' in kwargs:
			assert isinstance(kwargs['max_depth'], (int,)
			    ), "Optional argument 'max_depth' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['max_depth'])
		expected = ['max_depth']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['max_depth']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Accessibility.getFullAXTree', **
		    kwargs)
		return subdom_funcs

	def Accessibility_getChildAXNodes(self, id):
		"""
		Function path: Accessibility.getChildAXNodes
			Domain: Accessibility
			Method name: getChildAXNodes
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'id' (type: AXNodeId) -> No description
			Returns:
				'nodes' (type: array) -> No description
		
			Description: Fetches a particular accessibility node by AXNodeId.
Requires `enable()` to have been called previously.
		"""
		subdom_funcs = self.synchronous_command('Accessibility.getChildAXNodes',
		    id=id)
		return subdom_funcs

	def Accessibility_queryAXTree(self, **kwargs):
		"""
		Function path: Accessibility.queryAXTree
			Domain: Accessibility
			Method name: queryAXTree
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'nodeId' (type: DOM.NodeId) -> Identifier of the node for the root to query.
					'backendNodeId' (type: DOM.BackendNodeId) -> Identifier of the backend node for the root to query.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper for the root to query.
					'accessibleName' (type: string) -> Find nodes with this computed name.
					'role' (type: string) -> Find nodes with this computed role.
			Returns:
				'nodes' (type: array) -> A list of `Accessibility.AXNode` matching the specified attributes,
including nodes that are ignored for accessibility.
		
			Description: Query a DOM node's accessibility subtree for accessible name and role.
This command computes the name and role for all nodes in the subtree, including those that are
ignored for accessibility, and returns those that mactch the specified name and role. If no DOM
node is specified, or the DOM node does not exist, the command returns an error. If neither
`accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree.
		"""
		if 'accessibleName' in kwargs:
			assert isinstance(kwargs['accessibleName'], (str,)
			    ), "Optional argument 'accessibleName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['accessibleName'])
		if 'role' in kwargs:
			assert isinstance(kwargs['role'], (str,)
			    ), "Optional argument 'role' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['role'])
		expected = ['nodeId', 'backendNodeId', 'objectId', 'accessibleName', 'role']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId', 'accessibleName', 'role']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Accessibility.queryAXTree', **kwargs
		    )
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

	def ApplicationCache_getFramesWithManifests(self):
		"""
		Function path: ApplicationCache.getFramesWithManifests
			Domain: ApplicationCache
			Method name: getFramesWithManifests
		
			Returns:
				'frameIds' (type: array) -> Array of frame identifiers with manifest urls for each frame containing a document
associated with some application cache.
		
			Description: Returns array of frame identifiers with manifest urls for each frame containing a document
associated with some application cache.
		"""
		subdom_funcs = self.synchronous_command(
		    'ApplicationCache.getFramesWithManifests')
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
				'body' (type: string) -> The encoded body as a base64 string. Omitted if sizeOnly is true. (Encoded as a base64 string when passed over JSON)
				'originalSize' (type: integer) -> Size before re-encoding.
				'encodedSize' (type: integer) -> Size after re-encoding.
		
			Description: Returns the response body and size if it were re-encoded with the specified settings. Only
applies to images.
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

	def Audits_disable(self):
		"""
		Function path: Audits.disable
			Domain: Audits
			Method name: disable
		
			No return value.
		
			Description: Disables issues domain, prevents further issues from being reported to the client.
		"""
		subdom_funcs = self.synchronous_command('Audits.disable')
		return subdom_funcs

	def Audits_enable(self):
		"""
		Function path: Audits.enable
			Domain: Audits
			Method name: enable
		
			No return value.
		
			Description: Enables issues domain, sends the issues collected so far to the client by means of the
`issueAdded` event.
		"""
		subdom_funcs = self.synchronous_command('Audits.enable')
		return subdom_funcs

	def Audits_checkContrast(self, **kwargs):
		"""
		Function path: Audits.checkContrast
			Domain: Audits
			Method name: checkContrast
		
			Parameters:
				Optional arguments:
					'reportAAA' (type: boolean) -> Whether to report WCAG AAA level issues. Default is false.
			No return value.
		
			Description: Runs the contrast check for the target page. Found issues are reported
using Audits.issueAdded event.
		"""
		if 'reportAAA' in kwargs:
			assert isinstance(kwargs['reportAAA'], (bool,)
			    ), "Optional argument 'reportAAA' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['reportAAA'])
		expected = ['reportAAA']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['reportAAA']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Audits.checkContrast', **kwargs)
		return subdom_funcs

	def BackgroundService_startObserving(self, service):
		"""
		Function path: BackgroundService.startObserving
			Domain: BackgroundService
			Method name: startObserving
		
			Parameters:
				Required arguments:
					'service' (type: ServiceName) -> No description
			No return value.
		
			Description: Enables event updates for the service.
		"""
		subdom_funcs = self.synchronous_command('BackgroundService.startObserving',
		    service=service)
		return subdom_funcs

	def BackgroundService_stopObserving(self, service):
		"""
		Function path: BackgroundService.stopObserving
			Domain: BackgroundService
			Method name: stopObserving
		
			Parameters:
				Required arguments:
					'service' (type: ServiceName) -> No description
			No return value.
		
			Description: Disables event updates for the service.
		"""
		subdom_funcs = self.synchronous_command('BackgroundService.stopObserving',
		    service=service)
		return subdom_funcs

	def BackgroundService_setRecording(self, shouldRecord, service):
		"""
		Function path: BackgroundService.setRecording
			Domain: BackgroundService
			Method name: setRecording
		
			Parameters:
				Required arguments:
					'shouldRecord' (type: boolean) -> No description
					'service' (type: ServiceName) -> No description
			No return value.
		
			Description: Set the recording state for the service.
		"""
		assert isinstance(shouldRecord, (bool,)
		    ), "Argument 'shouldRecord' must be of type '['bool']'. Received type: '%s'" % type(
		    shouldRecord)
		subdom_funcs = self.synchronous_command('BackgroundService.setRecording',
		    shouldRecord=shouldRecord, service=service)
		return subdom_funcs

	def BackgroundService_clearEvents(self, service):
		"""
		Function path: BackgroundService.clearEvents
			Domain: BackgroundService
			Method name: clearEvents
		
			Parameters:
				Required arguments:
					'service' (type: ServiceName) -> No description
			No return value.
		
			Description: Clears all stored data for the service.
		"""
		subdom_funcs = self.synchronous_command('BackgroundService.clearEvents',
		    service=service)
		return subdom_funcs

	def Browser_setPermission(self, permission, setting, **kwargs):
		"""
		Function path: Browser.setPermission
			Domain: Browser
			Method name: setPermission
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'permission' (type: PermissionDescriptor) -> Descriptor of permission to override.
					'setting' (type: PermissionSetting) -> Setting of the permission.
				Optional arguments:
					'origin' (type: string) -> Origin the permission applies to, all origins if not specified.
					'browserContextId' (type: BrowserContextID) -> Context to override. When omitted, default browser context is used.
			No return value.
		
			Description: Set permission settings for given origin.
		"""
		if 'origin' in kwargs:
			assert isinstance(kwargs['origin'], (str,)
			    ), "Optional argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['origin'])
		expected = ['origin', 'browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['origin', 'browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.setPermission',
		    permission=permission, setting=setting, **kwargs)
		return subdom_funcs

	def Browser_grantPermissions(self, permissions, **kwargs):
		"""
		Function path: Browser.grantPermissions
			Domain: Browser
			Method name: grantPermissions
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'permissions' (type: array) -> No description
				Optional arguments:
					'origin' (type: string) -> Origin the permission applies to, all origins if not specified.
					'browserContextId' (type: BrowserContextID) -> BrowserContext to override permissions. When omitted, default browser context is used.
			No return value.
		
			Description: Grant specific permissions to the given origin and reject all others.
		"""
		assert isinstance(permissions, (list, tuple)
		    ), "Argument 'permissions' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    permissions)
		if 'origin' in kwargs:
			assert isinstance(kwargs['origin'], (str,)
			    ), "Optional argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['origin'])
		expected = ['origin', 'browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['origin', 'browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.grantPermissions',
		    permissions=permissions, **kwargs)
		return subdom_funcs

	def Browser_resetPermissions(self, **kwargs):
		"""
		Function path: Browser.resetPermissions
			Domain: Browser
			Method name: resetPermissions
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'browserContextId' (type: BrowserContextID) -> BrowserContext to reset permissions. When omitted, default browser context is used.
			No return value.
		
			Description: Reset all permission management for all origins.
		"""
		expected = ['browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.resetPermissions', **kwargs)
		return subdom_funcs

	def Browser_setDownloadBehavior(self, behavior, **kwargs):
		"""
		Function path: Browser.setDownloadBehavior
			Domain: Browser
			Method name: setDownloadBehavior
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'behavior' (type: string) -> Whether to allow all or deny all download requests, or use default Chrome behavior if
available (otherwise deny). |allowAndName| allows download and names files according to
their dowmload guids.
				Optional arguments:
					'browserContextId' (type: BrowserContextID) -> BrowserContext to set download behavior. When omitted, default browser context is used.
					'downloadPath' (type: string) -> The default path to save downloaded files to. This is required if behavior is set to 'allow'
or 'allowAndName'.
					'eventsEnabled' (type: boolean) -> Whether to emit download events (defaults to false).
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
		if 'eventsEnabled' in kwargs:
			assert isinstance(kwargs['eventsEnabled'], (bool,)
			    ), "Optional argument 'eventsEnabled' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['eventsEnabled'])
		expected = ['browserContextId', 'downloadPath', 'eventsEnabled']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['browserContextId', 'downloadPath', 'eventsEnabled']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.setDownloadBehavior',
		    behavior=behavior, **kwargs)
		return subdom_funcs

	def Browser_cancelDownload(self, guid, **kwargs):
		"""
		Function path: Browser.cancelDownload
			Domain: Browser
			Method name: cancelDownload
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'guid' (type: string) -> Global unique identifier of the download.
				Optional arguments:
					'browserContextId' (type: BrowserContextID) -> BrowserContext to perform the action in. When omitted, default browser context is used.
			No return value.
		
			Description: Cancel a download if in progress
		"""
		assert isinstance(guid, (str,)
		    ), "Argument 'guid' must be of type '['str']'. Received type: '%s'" % type(
		    guid)
		expected = ['browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.cancelDownload', guid=
		    guid, **kwargs)
		return subdom_funcs

	def Browser_close(self):
		"""
		Function path: Browser.close
			Domain: Browser
			Method name: close
		
			No return value.
		
			Description: Close browser gracefully.
		"""
		subdom_funcs = self.synchronous_command('Browser.close')
		return subdom_funcs

	def Browser_crash(self):
		"""
		Function path: Browser.crash
			Domain: Browser
			Method name: crash
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Crashes browser on the main thread.
		"""
		subdom_funcs = self.synchronous_command('Browser.crash')
		return subdom_funcs

	def Browser_crashGpuProcess(self):
		"""
		Function path: Browser.crashGpuProcess
			Domain: Browser
			Method name: crashGpuProcess
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Crashes GPU process.
		"""
		subdom_funcs = self.synchronous_command('Browser.crashGpuProcess')
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

	def Browser_getBrowserCommandLine(self):
		"""
		Function path: Browser.getBrowserCommandLine
			Domain: Browser
			Method name: getBrowserCommandLine
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'arguments' (type: array) -> Commandline parameters
		
			Description: Returns the command line switches for the browser process if, and only if
--enable-automation is on the commandline.
		"""
		subdom_funcs = self.synchronous_command('Browser.getBrowserCommandLine')
		return subdom_funcs

	def Browser_getHistograms(self, **kwargs):
		"""
		Function path: Browser.getHistograms
			Domain: Browser
			Method name: getHistograms
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'query' (type: string) -> Requested substring in name. Only histograms which have query as a
substring in their name are extracted. An empty or absent query returns
all histograms.
					'delta' (type: boolean) -> If true, retrieve delta since last call.
			Returns:
				'histograms' (type: array) -> Histograms.
		
			Description: Get Chrome histograms.
		"""
		if 'query' in kwargs:
			assert isinstance(kwargs['query'], (str,)
			    ), "Optional argument 'query' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['query'])
		if 'delta' in kwargs:
			assert isinstance(kwargs['delta'], (bool,)
			    ), "Optional argument 'delta' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['delta'])
		expected = ['query', 'delta']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['query', 'delta']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.getHistograms', **kwargs)
		return subdom_funcs

	def Browser_getHistogram(self, name, **kwargs):
		"""
		Function path: Browser.getHistogram
			Domain: Browser
			Method name: getHistogram
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'name' (type: string) -> Requested histogram name.
				Optional arguments:
					'delta' (type: boolean) -> If true, retrieve delta since last call.
			Returns:
				'histogram' (type: Histogram) -> Histogram.
		
			Description: Get a Chrome histogram by name.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		if 'delta' in kwargs:
			assert isinstance(kwargs['delta'], (bool,)
			    ), "Optional argument 'delta' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['delta'])
		expected = ['delta']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['delta']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.getHistogram', name=name,
		    **kwargs)
		return subdom_funcs

	def Browser_getWindowBounds(self, windowId):
		"""
		Function path: Browser.getWindowBounds
			Domain: Browser
			Method name: getWindowBounds
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'windowId' (type: WindowID) -> Browser window id.
			Returns:
				'bounds' (type: Bounds) -> Bounds information of the window. When window state is 'minimized', the restored window
position and size are returned.
		
			Description: Get position and size of the browser window.
		"""
		subdom_funcs = self.synchronous_command('Browser.getWindowBounds',
		    windowId=windowId)
		return subdom_funcs

	def Browser_getWindowForTarget(self, **kwargs):
		"""
		Function path: Browser.getWindowForTarget
			Domain: Browser
			Method name: getWindowForTarget
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'targetId' (type: Target.TargetID) -> Devtools agent host id. If called as a part of the session, associated targetId is used.
			Returns:
				'windowId' (type: WindowID) -> Browser window id.
				'bounds' (type: Bounds) -> Bounds information of the window. When window state is 'minimized', the restored window
position and size are returned.
		
			Description: Get the browser window that contains the devtools target.
		"""
		expected = ['targetId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['targetId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.getWindowForTarget', **
		    kwargs)
		return subdom_funcs

	def Browser_setWindowBounds(self, windowId, bounds):
		"""
		Function path: Browser.setWindowBounds
			Domain: Browser
			Method name: setWindowBounds
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'windowId' (type: WindowID) -> Browser window id.
					'bounds' (type: Bounds) -> New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined
with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
			No return value.
		
			Description: Set position and/or size of the browser window.
		"""
		subdom_funcs = self.synchronous_command('Browser.setWindowBounds',
		    windowId=windowId, bounds=bounds)
		return subdom_funcs

	def Browser_setDockTile(self, **kwargs):
		"""
		Function path: Browser.setDockTile
			Domain: Browser
			Method name: setDockTile
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'badgeLabel' (type: string) -> No description
					'image' (type: string) -> Png encoded image. (Encoded as a base64 string when passed over JSON)
			No return value.
		
			Description: Set dock tile details, platform-specific.
		"""
		if 'badgeLabel' in kwargs:
			assert isinstance(kwargs['badgeLabel'], (str,)
			    ), "Optional argument 'badgeLabel' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['badgeLabel'])
		if 'image' in kwargs:
			assert isinstance(kwargs['image'], (str,)
			    ), "Optional argument 'image' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['image'])
		expected = ['badgeLabel', 'image']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['badgeLabel', 'image']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Browser.setDockTile', **kwargs)
		return subdom_funcs

	def Browser_executeBrowserCommand(self, commandId):
		"""
		Function path: Browser.executeBrowserCommand
			Domain: Browser
			Method name: executeBrowserCommand
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'commandId' (type: BrowserCommandId) -> No description
			No return value.
		
			Description: Invoke custom browser commands used by telemetry.
		"""
		subdom_funcs = self.synchronous_command('Browser.executeBrowserCommand',
		    commandId=commandId)
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
		
			Description: Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
position specified by `location`.
		"""
		assert isinstance(ruleText, (str,)
		    ), "Argument 'ruleText' must be of type '['str']'. Received type: '%s'" % type(
		    ruleText)
		subdom_funcs = self.synchronous_command('CSS.addRule', styleSheetId=
		    styleSheetId, ruleText=ruleText, location=location)
		return subdom_funcs

	def CSS_collectClassNames(self, styleSheetId):
		"""
		Function path: CSS.collectClassNames
			Domain: CSS
			Method name: collectClassNames
		
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
		
			Description: Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.
		"""
		subdom_funcs = self.synchronous_command('CSS.createStyleSheet', frameId=
		    frameId)
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

	def CSS_enable(self):
		"""
		Function path: CSS.enable
			Domain: CSS
			Method name: enable
		
			No return value.
		
			Description: Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
enabled until the result of this command is received.
		"""
		subdom_funcs = self.synchronous_command('CSS.enable')
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
		
			Description: Ensures that the given node will have specified pseudo-classes whenever its style is computed by
the browser.
		"""
		assert isinstance(forcedPseudoClasses, (list, tuple)
		    ), "Argument 'forcedPseudoClasses' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    forcedPseudoClasses)
		subdom_funcs = self.synchronous_command('CSS.forcePseudoState', nodeId=
		    nodeId, forcedPseudoClasses=forcedPseudoClasses)
		return subdom_funcs

	def CSS_getBackgroundColors(self, nodeId):
		"""
		Function path: CSS.getBackgroundColors
			Domain: CSS
			Method name: getBackgroundColors
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> Id of the node to get background colors for.
			Returns:
				'backgroundColors' (type: array) -> The range of background colors behind this element, if it contains any visible text. If no
visible text is present, this will be undefined. In the case of a flat background color,
this will consist of simply that color. In the case of a gradient, this will consist of each
of the color stops. For anything more complicated, this will be an empty array. Images will
be ignored (as if the image had failed to load).
				'computedFontSize' (type: string) -> The computed font size for this node, as a CSS computed value string (e.g. '12px').
				'computedFontWeight' (type: string) -> The computed font weight for this node, as a CSS computed value string (e.g. 'normal' or
'100').
		
		"""
		subdom_funcs = self.synchronous_command('CSS.getBackgroundColors', nodeId
		    =nodeId)
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
		
			Description: Returns the computed style for a DOM node identified by `nodeId`.
		"""
		subdom_funcs = self.synchronous_command('CSS.getComputedStyleForNode',
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
		
			Description: Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
attributes) for a DOM node identified by `nodeId`.
		"""
		subdom_funcs = self.synchronous_command('CSS.getInlineStylesForNode',
		    nodeId=nodeId)
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
		
			Description: Returns requested styles for a DOM node identified by `nodeId`.
		"""
		subdom_funcs = self.synchronous_command('CSS.getMatchedStylesForNode',
		    nodeId=nodeId)
		return subdom_funcs

	def CSS_getMediaQueries(self):
		"""
		Function path: CSS.getMediaQueries
			Domain: CSS
			Method name: getMediaQueries
		
			Returns:
				'medias' (type: array) -> No description
		
			Description: Returns all media queries parsed by the rendering engine.
		"""
		subdom_funcs = self.synchronous_command('CSS.getMediaQueries')
		return subdom_funcs

	def CSS_getPlatformFontsForNode(self, nodeId):
		"""
		Function path: CSS.getPlatformFontsForNode
			Domain: CSS
			Method name: getPlatformFontsForNode
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> No description
			Returns:
				'fonts' (type: array) -> Usage statistics for every employed platform font.
		
			Description: Requests information about platform fonts which we used to render child TextNodes in the given
node.
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
		
			Description: Returns the current textual content for a stylesheet.
		"""
		subdom_funcs = self.synchronous_command('CSS.getStyleSheetText',
		    styleSheetId=styleSheetId)
		return subdom_funcs

	def CSS_trackComputedStyleUpdates(self, propertiesToTrack):
		"""
		Function path: CSS.trackComputedStyleUpdates
			Domain: CSS
			Method name: trackComputedStyleUpdates
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'propertiesToTrack' (type: array) -> No description
			No return value.
		
			Description: Starts tracking the given computed styles for updates. The specified array of properties
replaces the one previously specified. Pass empty array to disable tracking.
Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
The changes to computed style properties are only tracked for nodes pushed to the front-end
by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
to the front-end, no updates will be issued for the node.
		"""
		assert isinstance(propertiesToTrack, (list, tuple)
		    ), "Argument 'propertiesToTrack' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    propertiesToTrack)
		subdom_funcs = self.synchronous_command('CSS.trackComputedStyleUpdates',
		    propertiesToTrack=propertiesToTrack)
		return subdom_funcs

	def CSS_takeComputedStyleUpdates(self):
		"""
		Function path: CSS.takeComputedStyleUpdates
			Domain: CSS
			Method name: takeComputedStyleUpdates
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'nodeIds' (type: array) -> The list of node Ids that have their tracked computed styles updated
		
			Description: Polls the next batch of computed style updates.
		"""
		subdom_funcs = self.synchronous_command('CSS.takeComputedStyleUpdates')
		return subdom_funcs

	def CSS_setEffectivePropertyValueForNode(self, nodeId, propertyName, value):
		"""
		Function path: CSS.setEffectivePropertyValueForNode
			Domain: CSS
			Method name: setEffectivePropertyValueForNode
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> The element id for which to set property.
					'propertyName' (type: string) -> No description
					'value' (type: string) -> No description
			No return value.
		
			Description: Find a rule with the given active property for the given node and set the new value for this
property
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

	def CSS_setContainerQueryText(self, styleSheetId, range, text):
		"""
		Function path: CSS.setContainerQueryText
			Domain: CSS
			Method name: setContainerQueryText
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'styleSheetId' (type: StyleSheetId) -> No description
					'range' (type: SourceRange) -> No description
					'text' (type: string) -> No description
			Returns:
				'containerQuery' (type: CSSContainerQuery) -> The resulting CSS container query rule after modification.
		
			Description: Modifies the expression of a container query.
		"""
		assert isinstance(text, (str,)
		    ), "Argument 'text' must be of type '['str']'. Received type: '%s'" % type(
		    text)
		subdom_funcs = self.synchronous_command('CSS.setContainerQueryText',
		    styleSheetId=styleSheetId, range=range, text=text)
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

	def CSS_startRuleUsageTracking(self):
		"""
		Function path: CSS.startRuleUsageTracking
			Domain: CSS
			Method name: startRuleUsageTracking
		
			No return value.
		
			Description: Enables the selector recording.
		"""
		subdom_funcs = self.synchronous_command('CSS.startRuleUsageTracking')
		return subdom_funcs

	def CSS_stopRuleUsageTracking(self):
		"""
		Function path: CSS.stopRuleUsageTracking
			Domain: CSS
			Method name: stopRuleUsageTracking
		
			Returns:
				'ruleUsage' (type: array) -> No description
		
			Description: Stop tracking rule usage and return the list of rules that were used since last call to
`takeCoverageDelta` (or since start of coverage instrumentation)
		"""
		subdom_funcs = self.synchronous_command('CSS.stopRuleUsageTracking')
		return subdom_funcs

	def CSS_takeCoverageDelta(self):
		"""
		Function path: CSS.takeCoverageDelta
			Domain: CSS
			Method name: takeCoverageDelta
		
			Returns:
				'coverage' (type: array) -> No description
				'timestamp' (type: number) -> Monotonically increasing time, in seconds.
		
			Description: Obtain list of rules that became used since last call to this method (or since start of coverage
instrumentation)
		"""
		subdom_funcs = self.synchronous_command('CSS.takeCoverageDelta')
		return subdom_funcs

	def CSS_setLocalFontsEnabled(self, enabled):
		"""
		Function path: CSS.setLocalFontsEnabled
			Domain: CSS
			Method name: setLocalFontsEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether rendering of local fonts is enabled.
			No return value.
		
			Description: Enables/disables rendering of local CSS fonts (enabled by default).
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('CSS.setLocalFontsEnabled',
		    enabled=enabled)
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

	def CacheStorage_requestCachedResponse(self, cacheId, requestURL,
	    requestHeaders):
		"""
		Function path: CacheStorage.requestCachedResponse
			Domain: CacheStorage
			Method name: requestCachedResponse
		
			Parameters:
				Required arguments:
					'cacheId' (type: CacheId) -> Id of cache that contains the entry.
					'requestURL' (type: string) -> URL spec of the request.
					'requestHeaders' (type: array) -> headers of the request.
			Returns:
				'response' (type: CachedResponse) -> Response read from the cache.
		
			Description: Fetches cache entry.
		"""
		assert isinstance(requestURL, (str,)
		    ), "Argument 'requestURL' must be of type '['str']'. Received type: '%s'" % type(
		    requestURL)
		assert isinstance(requestHeaders, (list, tuple)
		    ), "Argument 'requestHeaders' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    requestHeaders)
		subdom_funcs = self.synchronous_command('CacheStorage.requestCachedResponse',
		    cacheId=cacheId, requestURL=requestURL, requestHeaders=requestHeaders)
		return subdom_funcs

	def CacheStorage_requestEntries(self, cacheId, **kwargs):
		"""
		Function path: CacheStorage.requestEntries
			Domain: CacheStorage
			Method name: requestEntries
		
			Parameters:
				Required arguments:
					'cacheId' (type: CacheId) -> ID of cache to get entries from.
				Optional arguments:
					'skipCount' (type: integer) -> Number of records to skip.
					'pageSize' (type: integer) -> Number of records to fetch.
					'pathFilter' (type: string) -> If present, only return the entries containing this substring in the path
			Returns:
				'cacheDataEntries' (type: array) -> Array of object store data entries.
				'returnCount' (type: number) -> Count of returned entries from this storage. If pathFilter is empty, it
is the count of all entries from this storage.
		
			Description: Requests data from cache.
		"""
		if 'skipCount' in kwargs:
			assert isinstance(kwargs['skipCount'], (int,)
			    ), "Optional argument 'skipCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['skipCount'])
		if 'pageSize' in kwargs:
			assert isinstance(kwargs['pageSize'], (int,)
			    ), "Optional argument 'pageSize' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['pageSize'])
		if 'pathFilter' in kwargs:
			assert isinstance(kwargs['pathFilter'], (str,)
			    ), "Optional argument 'pathFilter' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['pathFilter'])
		expected = ['skipCount', 'pageSize', 'pathFilter']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['skipCount', 'pageSize', 'pathFilter']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('CacheStorage.requestEntries',
		    cacheId=cacheId, **kwargs)
		return subdom_funcs

	def Cast_enable(self, **kwargs):
		"""
		Function path: Cast.enable
			Domain: Cast
			Method name: enable
		
			Parameters:
				Optional arguments:
					'presentationUrl' (type: string) -> No description
			No return value.
		
			Description: Starts observing for sinks that can be used for tab mirroring, and if set,
sinks compatible with |presentationUrl| as well. When sinks are found, a
|sinksUpdated| event is fired.
Also starts observing for issue messages. When an issue is added or removed,
an |issueUpdated| event is fired.
		"""
		if 'presentationUrl' in kwargs:
			assert isinstance(kwargs['presentationUrl'], (str,)
			    ), "Optional argument 'presentationUrl' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['presentationUrl'])
		expected = ['presentationUrl']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['presentationUrl']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Cast.enable', **kwargs)
		return subdom_funcs

	def Cast_disable(self):
		"""
		Function path: Cast.disable
			Domain: Cast
			Method name: disable
		
			No return value.
		
			Description: Stops observing for sinks and issues.
		"""
		subdom_funcs = self.synchronous_command('Cast.disable')
		return subdom_funcs

	def Cast_setSinkToUse(self, sinkName):
		"""
		Function path: Cast.setSinkToUse
			Domain: Cast
			Method name: setSinkToUse
		
			Parameters:
				Required arguments:
					'sinkName' (type: string) -> No description
			No return value.
		
			Description: Sets a sink to be used when the web page requests the browser to choose a
sink via Presentation API, Remote Playback API, or Cast SDK.
		"""
		assert isinstance(sinkName, (str,)
		    ), "Argument 'sinkName' must be of type '['str']'. Received type: '%s'" % type(
		    sinkName)
		subdom_funcs = self.synchronous_command('Cast.setSinkToUse', sinkName=
		    sinkName)
		return subdom_funcs

	def Cast_startTabMirroring(self, sinkName):
		"""
		Function path: Cast.startTabMirroring
			Domain: Cast
			Method name: startTabMirroring
		
			Parameters:
				Required arguments:
					'sinkName' (type: string) -> No description
			No return value.
		
			Description: Starts mirroring the tab to the sink.
		"""
		assert isinstance(sinkName, (str,)
		    ), "Argument 'sinkName' must be of type '['str']'. Received type: '%s'" % type(
		    sinkName)
		subdom_funcs = self.synchronous_command('Cast.startTabMirroring',
		    sinkName=sinkName)
		return subdom_funcs

	def Cast_stopCasting(self, sinkName):
		"""
		Function path: Cast.stopCasting
			Domain: Cast
			Method name: stopCasting
		
			Parameters:
				Required arguments:
					'sinkName' (type: string) -> No description
			No return value.
		
			Description: Stops the active Cast session on the sink.
		"""
		assert isinstance(sinkName, (str,)
		    ), "Argument 'sinkName' must be of type '['str']'. Received type: '%s'" % type(
		    sinkName)
		subdom_funcs = self.synchronous_command('Cast.stopCasting', sinkName=sinkName
		    )
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
					'insertBeforeNodeId' (type: NodeId) -> Drop the copy before this node (if absent, the copy becomes the last child of
`targetNodeId`).
			Returns:
				'nodeId' (type: NodeId) -> Id of the node clone.
		
			Description: Creates a deep copy of the specified node and places it into the target container before the
given anchor.
		"""
		expected = ['insertBeforeNodeId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['insertBeforeNodeId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.copyTo', nodeId=nodeId,
		    targetNodeId=targetNodeId, **kwargs)
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
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false).
			Returns:
				'node' (type: Node) -> Node description.
		
			Description: Describes node given its id, does not require domain to be enabled. Does not start tracking any
objects, can be used for automation.
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

	def DOM_scrollIntoViewIfNeeded(self, **kwargs):
		"""
		Function path: DOM.scrollIntoViewIfNeeded
			Domain: DOM
			Method name: scrollIntoViewIfNeeded
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
					'rect' (type: Rect) -> The rect to be scrolled into view, relative to the node's border box, in CSS pixels.
When omitted, center of the node will be used, similar to Element.scrollIntoView.
			No return value.
		
			Description: Scrolls the specified rect of the given node into view if not already visible.
Note: exactly one between nodeId, backendNodeId and objectId should be passed
to identify the node.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId', 'rect']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId', 'rect']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.scrollIntoViewIfNeeded', **
		    kwargs)
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
		
			Description: Discards search results from the session with the given id. `getSearchResults` should no longer
be called for that search.
		"""
		assert isinstance(searchId, (str,)
		    ), "Argument 'searchId' must be of type '['str']'. Received type: '%s'" % type(
		    searchId)
		subdom_funcs = self.synchronous_command('DOM.discardSearchResults',
		    searchId=searchId)
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

	def DOM_focus(self, **kwargs):
		"""
		Function path: DOM.focus
			Domain: DOM
			Method name: focus
		
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

	def DOM_getBoxModel(self, **kwargs):
		"""
		Function path: DOM.getBoxModel
			Domain: DOM
			Method name: getBoxModel
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
			Returns:
				'model' (type: BoxModel) -> Box model for the node.
		
			Description: Returns boxes for the given node.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getBoxModel', **kwargs)
		return subdom_funcs

	def DOM_getContentQuads(self, **kwargs):
		"""
		Function path: DOM.getContentQuads
			Domain: DOM
			Method name: getContentQuads
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'nodeId' (type: NodeId) -> Identifier of the node.
					'backendNodeId' (type: BackendNodeId) -> Identifier of the backend node.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
			Returns:
				'quads' (type: array) -> Quads that describe node layout relative to viewport.
		
			Description: Returns quads that describe node position on the page. This method
might return multiple quads for inline nodes.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getContentQuads', **kwargs)
		return subdom_funcs

	def DOM_getDocument(self, **kwargs):
		"""
		Function path: DOM.getDocument
			Domain: DOM
			Method name: getDocument
		
			Parameters:
				Optional arguments:
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false).
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
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false).
			Returns:
				'nodes' (type: array) -> Resulting node.
		
			Description: Returns the root DOM node (and optionally the subtree) to the caller.
Deprecated, as it is not designed to work well with the rest of the DOM agent.
Use DOMSnapshot.captureSnapshot instead.
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

	def DOM_getNodesForSubtreeByStyle(self, nodeId, computedStyles, **kwargs):
		"""
		Function path: DOM.getNodesForSubtreeByStyle
			Domain: DOM
			Method name: getNodesForSubtreeByStyle
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Node ID pointing to the root of a subtree.
					'computedStyles' (type: array) -> The style to filter nodes by (includes nodes if any of properties matches).
				Optional arguments:
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots in the same target should be traversed when returning the
results (default is false).
			Returns:
				'nodeIds' (type: array) -> Resulting nodes.
		
			Description: Finds nodes with a given computed style in a subtree.
		"""
		assert isinstance(computedStyles, (list, tuple)
		    ), "Argument 'computedStyles' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    computedStyles)
		if 'pierce' in kwargs:
			assert isinstance(kwargs['pierce'], (bool,)
			    ), "Optional argument 'pierce' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['pierce'])
		expected = ['pierce']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['pierce']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getNodesForSubtreeByStyle',
		    nodeId=nodeId, computedStyles=computedStyles, **kwargs)
		return subdom_funcs

	def DOM_getNodeForLocation(self, x, y, **kwargs):
		"""
		Function path: DOM.getNodeForLocation
			Domain: DOM
			Method name: getNodeForLocation
		
			Parameters:
				Required arguments:
					'x' (type: integer) -> X coordinate.
					'y' (type: integer) -> Y coordinate.
				Optional arguments:
					'includeUserAgentShadowDOM' (type: boolean) -> False to skip to the nearest non-UA shadow root ancestor (default: false).
					'ignorePointerEventsNone' (type: boolean) -> Whether to ignore pointer-events: none on elements and hit test them.
			Returns:
				'backendNodeId' (type: BackendNodeId) -> Resulting node.
				'frameId' (type: Page.FrameId) -> Frame this node belongs to.
				'nodeId' (type: NodeId) -> Id of the node at given coordinates, only when enabled and requested document.
		
			Description: Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
either returned or not.
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
		if 'ignorePointerEventsNone' in kwargs:
			assert isinstance(kwargs['ignorePointerEventsNone'], (bool,)
			    ), "Optional argument 'ignorePointerEventsNone' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['ignorePointerEventsNone'])
		expected = ['includeUserAgentShadowDOM', 'ignorePointerEventsNone']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['includeUserAgentShadowDOM', 'ignorePointerEventsNone']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getNodeForLocation', x=x, y=
		    y, **kwargs)
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
		
			Description: Returns search results from given `fromIndex` to given `toIndex` from the search with the given
identifier.
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
					'insertBeforeNodeId' (type: NodeId) -> Drop node before this one (if absent, the moved node becomes the last child of
`targetNodeId`).
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
		
			Description: Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
`cancelSearch` to end this search session.
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
				'nodeIds' (type: array) -> The array of ids of pushed nodes that correspond to the backend ids specified in
backendNodeIds.
		
			Description: Requests that a batch of nodes is sent to the caller given their backend node ids.
		"""
		assert isinstance(backendNodeIds, (list, tuple)
		    ), "Argument 'backendNodeIds' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    backendNodeIds)
		subdom_funcs = self.synchronous_command('DOM.pushNodesByBackendIdsToFrontend'
		    , backendNodeIds=backendNodeIds)
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
		
			Description: Executes `querySelector` on a given node.
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
		
			Description: Executes `querySelectorAll` on a given node.
		"""
		assert isinstance(selector, (str,)
		    ), "Argument 'selector' must be of type '['str']'. Received type: '%s'" % type(
		    selector)
		subdom_funcs = self.synchronous_command('DOM.querySelectorAll', nodeId=
		    nodeId, selector=selector)
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

	def DOM_requestChildNodes(self, nodeId, **kwargs):
		"""
		Function path: DOM.requestChildNodes
			Domain: DOM
			Method name: requestChildNodes
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to get children for.
				Optional arguments:
					'depth' (type: integer) -> The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the sub-tree
(default is false).
			No return value.
		
			Description: Requests that children of the node with given id are returned to the caller in form of
`setChildNodes` events where not only immediate children are retrieved, but all children down to
the specified depth.
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
		
			Description: Requests that the node is sent to the caller given the JavaScript node object reference. All
nodes that form the path from the node to the root are also sent to the client as a series of
`setChildNodes` notifications.
		"""
		subdom_funcs = self.synchronous_command('DOM.requestNode', objectId=objectId)
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
					'executionContextId' (type: Runtime.ExecutionContextId) -> Execution context in which to resolve the node.
			Returns:
				'object' (type: Runtime.RemoteObject) -> JavaScript object wrapper for given node.
		
			Description: Resolves the JavaScript node object for a given NodeId or BackendNodeId.
		"""
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		expected = ['nodeId', 'backendNodeId', 'objectGroup', 'executionContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectGroup', 'executionContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.resolveNode', **kwargs)
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
					'name' (type: string) -> Attribute name to replace with new attributes derived from text in case text parsed
successfully.
			No return value.
		
			Description: Sets attributes on element with given id. This method is useful when user edits some existing
attribute value and types in several attribute name/value pairs.
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

	def DOM_setFileInputFiles(self, files, **kwargs):
		"""
		Function path: DOM.setFileInputFiles
			Domain: DOM
			Method name: setFileInputFiles
		
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

	def DOM_setNodeStackTracesEnabled(self, enable):
		"""
		Function path: DOM.setNodeStackTracesEnabled
			Domain: DOM
			Method name: setNodeStackTracesEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enable' (type: boolean) -> Enable or disable.
			No return value.
		
			Description: Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled.
		"""
		assert isinstance(enable, (bool,)
		    ), "Argument 'enable' must be of type '['bool']'. Received type: '%s'" % type(
		    enable)
		subdom_funcs = self.synchronous_command('DOM.setNodeStackTracesEnabled',
		    enable=enable)
		return subdom_funcs

	def DOM_getNodeStackTraces(self, nodeId):
		"""
		Function path: DOM.getNodeStackTraces
			Domain: DOM
			Method name: getNodeStackTraces
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> Id of the node to get stack traces for.
			Returns:
				'creation' (type: Runtime.StackTrace) -> Creation stack trace, if available.
		
			Description: Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation.
		"""
		subdom_funcs = self.synchronous_command('DOM.getNodeStackTraces', nodeId=
		    nodeId)
		return subdom_funcs

	def DOM_getFileInfo(self, objectId):
		"""
		Function path: DOM.getFileInfo
			Domain: DOM
			Method name: getFileInfo
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node wrapper.
			Returns:
				'path' (type: string) -> No description
		
			Description: Returns file information for the given
File wrapper.
		"""
		subdom_funcs = self.synchronous_command('DOM.getFileInfo', objectId=objectId)
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
		
			Description: Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).
		"""
		subdom_funcs = self.synchronous_command('DOM.setInspectedNode', nodeId=nodeId
		    )
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

	def DOM_getFrameOwner(self, frameId):
		"""
		Function path: DOM.getFrameOwner
			Domain: DOM
			Method name: getFrameOwner
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'frameId' (type: Page.FrameId) -> No description
			Returns:
				'backendNodeId' (type: BackendNodeId) -> Resulting node.
				'nodeId' (type: NodeId) -> Id of the node at given coordinates, only when enabled and requested document.
		
			Description: Returns iframe node that owns iframe with the given domain.
		"""
		subdom_funcs = self.synchronous_command('DOM.getFrameOwner', frameId=frameId)
		return subdom_funcs

	def DOM_getContainerForNode(self, nodeId, **kwargs):
		"""
		Function path: DOM.getContainerForNode
			Domain: DOM
			Method name: getContainerForNode
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'nodeId' (type: NodeId) -> No description
				Optional arguments:
					'containerName' (type: string) -> No description
			Returns:
				'nodeId' (type: NodeId) -> The container node for the given node, or null if not found.
		
			Description: Returns the container of the given node based on container query conditions.
If containerName is given, it will find the nearest container with a matching name;
otherwise it will find the nearest container regardless of its container name.
		"""
		if 'containerName' in kwargs:
			assert isinstance(kwargs['containerName'], (str,)
			    ), "Optional argument 'containerName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['containerName'])
		expected = ['containerName']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['containerName']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOM.getContainerForNode', nodeId
		    =nodeId, **kwargs)
		return subdom_funcs

	def DOMDebugger_getEventListeners(self, objectId, **kwargs):
		"""
		Function path: DOMDebugger.getEventListeners
			Domain: DOMDebugger
			Method name: getEventListeners
		
			Parameters:
				Required arguments:
					'objectId' (type: Runtime.RemoteObjectId) -> Identifier of the object to return listeners for.
				Optional arguments:
					'depth' (type: integer) -> The maximum depth at which Node children should be retrieved, defaults to 1. Use -1 for the
entire subtree or provide an integer larger than 0.
					'pierce' (type: boolean) -> Whether or not iframes and shadow roots should be traversed when returning the subtree
(default is false). Reports listeners for all contexts if pierce is enabled.
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
		
			Description: Removes DOM breakpoint that was set using `setDOMBreakpoint`.
		"""
		subdom_funcs = self.synchronous_command('DOMDebugger.removeDOMBreakpoint',
		    nodeId=nodeId, type=type)
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

	def DOMDebugger_setBreakOnCSPViolation(self, violationTypes):
		"""
		Function path: DOMDebugger.setBreakOnCSPViolation
			Domain: DOMDebugger
			Method name: setBreakOnCSPViolation
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'violationTypes' (type: array) -> CSP Violations to stop upon.
			No return value.
		
			Description: Sets breakpoint on particular CSP violations.
		"""
		assert isinstance(violationTypes, (list, tuple)
		    ), "Argument 'violationTypes' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    violationTypes)
		subdom_funcs = self.synchronous_command('DOMDebugger.setBreakOnCSPViolation',
		    violationTypes=violationTypes)
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

	def DOMDebugger_setEventListenerBreakpoint(self, eventName, **kwargs):
		"""
		Function path: DOMDebugger.setEventListenerBreakpoint
			Domain: DOMDebugger
			Method name: setEventListenerBreakpoint
		
			Parameters:
				Required arguments:
					'eventName' (type: string) -> DOM Event name to stop on (any DOM event will do).
				Optional arguments:
					'targetName' (type: string) -> EventTarget interface name to stop on. If equal to `"*"` or not provided, will stop on any
EventTarget.
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

	def DOMSnapshot_disable(self):
		"""
		Function path: DOMSnapshot.disable
			Domain: DOMSnapshot
			Method name: disable
		
			No return value.
		
			Description: Disables DOM snapshot agent for the given page.
		"""
		subdom_funcs = self.synchronous_command('DOMSnapshot.disable')
		return subdom_funcs

	def DOMSnapshot_enable(self):
		"""
		Function path: DOMSnapshot.enable
			Domain: DOMSnapshot
			Method name: enable
		
			No return value.
		
			Description: Enables DOM snapshot agent for the given page.
		"""
		subdom_funcs = self.synchronous_command('DOMSnapshot.enable')
		return subdom_funcs

	def DOMSnapshot_getSnapshot(self, computedStyleWhitelist, **kwargs):
		"""
		Function path: DOMSnapshot.getSnapshot
			Domain: DOMSnapshot
			Method name: getSnapshot
		
			Parameters:
				Required arguments:
					'computedStyleWhitelist' (type: array) -> Whitelist of computed styles to return.
				Optional arguments:
					'includeEventListeners' (type: boolean) -> Whether or not to retrieve details of DOM listeners (default false).
					'includePaintOrder' (type: boolean) -> Whether to determine and include the paint order index of LayoutTreeNodes (default false).
					'includeUserAgentShadowTree' (type: boolean) -> Whether to include UA shadow tree in the snapshot (default false).
			Returns:
				'domNodes' (type: array) -> The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document.
				'layoutTreeNodes' (type: array) -> The nodes in the layout tree.
				'computedStyles' (type: array) -> Whitelisted ComputedStyle properties for each node in the layout tree.
		
			Description: Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.
		"""
		assert isinstance(computedStyleWhitelist, (list, tuple)
		    ), "Argument 'computedStyleWhitelist' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    computedStyleWhitelist)
		if 'includeEventListeners' in kwargs:
			assert isinstance(kwargs['includeEventListeners'], (bool,)
			    ), "Optional argument 'includeEventListeners' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeEventListeners'])
		if 'includePaintOrder' in kwargs:
			assert isinstance(kwargs['includePaintOrder'], (bool,)
			    ), "Optional argument 'includePaintOrder' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includePaintOrder'])
		if 'includeUserAgentShadowTree' in kwargs:
			assert isinstance(kwargs['includeUserAgentShadowTree'], (bool,)
			    ), "Optional argument 'includeUserAgentShadowTree' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeUserAgentShadowTree'])
		expected = ['includeEventListeners', 'includePaintOrder',
		    'includeUserAgentShadowTree']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['includeEventListeners', 'includePaintOrder', 'includeUserAgentShadowTree']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOMSnapshot.getSnapshot',
		    computedStyleWhitelist=computedStyleWhitelist, **kwargs)
		return subdom_funcs

	def DOMSnapshot_captureSnapshot(self, computedStyles, **kwargs):
		"""
		Function path: DOMSnapshot.captureSnapshot
			Domain: DOMSnapshot
			Method name: captureSnapshot
		
			Parameters:
				Required arguments:
					'computedStyles' (type: array) -> Whitelist of computed styles to return.
				Optional arguments:
					'includePaintOrder' (type: boolean) -> Whether to include layout object paint orders into the snapshot.
					'includeDOMRects' (type: boolean) -> Whether to include DOM rectangles (offsetRects, clientRects, scrollRects) into the snapshot
					'includeBlendedBackgroundColors' (type: boolean) -> Whether to include blended background colors in the snapshot (default: false).
Blended background color is achieved by blending background colors of all elements
that overlap with the current element.
					'includeTextColorOpacities' (type: boolean) -> Whether to include text color opacity in the snapshot (default: false).
An element might have the opacity property set that affects the text color of the element.
The final text color opacity is computed based on the opacity of all overlapping elements.
			Returns:
				'documents' (type: array) -> The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document.
				'strings' (type: array) -> Shared string table that all string properties refer to with indexes.
		
			Description: Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.
		"""
		assert isinstance(computedStyles, (list, tuple)
		    ), "Argument 'computedStyles' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    computedStyles)
		if 'includePaintOrder' in kwargs:
			assert isinstance(kwargs['includePaintOrder'], (bool,)
			    ), "Optional argument 'includePaintOrder' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includePaintOrder'])
		if 'includeDOMRects' in kwargs:
			assert isinstance(kwargs['includeDOMRects'], (bool,)
			    ), "Optional argument 'includeDOMRects' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeDOMRects'])
		if 'includeBlendedBackgroundColors' in kwargs:
			assert isinstance(kwargs['includeBlendedBackgroundColors'], (bool,)
			    ), "Optional argument 'includeBlendedBackgroundColors' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeBlendedBackgroundColors'])
		if 'includeTextColorOpacities' in kwargs:
			assert isinstance(kwargs['includeTextColorOpacities'], (bool,)
			    ), "Optional argument 'includeTextColorOpacities' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeTextColorOpacities'])
		expected = ['includePaintOrder', 'includeDOMRects',
		    'includeBlendedBackgroundColors', 'includeTextColorOpacities']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['includePaintOrder', 'includeDOMRects', 'includeBlendedBackgroundColors', 'includeTextColorOpacities']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('DOMSnapshot.captureSnapshot',
		    computedStyles=computedStyles, **kwargs)
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

	def Emulation_canEmulate(self):
		"""
		Function path: Emulation.canEmulate
			Domain: Emulation
			Method name: canEmulate
		
			Returns:
				'result' (type: boolean) -> True if emulation is supported.
		
			Description: Tells whether emulation is supported.
		"""
		subdom_funcs = self.synchronous_command('Emulation.canEmulate')
		return subdom_funcs

	def Emulation_clearDeviceMetricsOverride(self):
		"""
		Function path: Emulation.clearDeviceMetricsOverride
			Domain: Emulation
			Method name: clearDeviceMetricsOverride
		
			No return value.
		
			Description: Clears the overridden device metrics.
		"""
		subdom_funcs = self.synchronous_command(
		    'Emulation.clearDeviceMetricsOverride')
		return subdom_funcs

	def Emulation_clearGeolocationOverride(self):
		"""
		Function path: Emulation.clearGeolocationOverride
			Domain: Emulation
			Method name: clearGeolocationOverride
		
			No return value.
		
			Description: Clears the overridden Geolocation Position and Error.
		"""
		subdom_funcs = self.synchronous_command('Emulation.clearGeolocationOverride')
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

	def Emulation_setFocusEmulationEnabled(self, enabled):
		"""
		Function path: Emulation.setFocusEmulationEnabled
			Domain: Emulation
			Method name: setFocusEmulationEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether to enable to disable focus emulation.
			No return value.
		
			Description: Enables or disables simulating a focused and active page.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Emulation.setFocusEmulationEnabled',
		    enabled=enabled)
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

	def Emulation_setDefaultBackgroundColorOverride(self, **kwargs):
		"""
		Function path: Emulation.setDefaultBackgroundColorOverride
			Domain: Emulation
			Method name: setDefaultBackgroundColorOverride
		
			Parameters:
				Optional arguments:
					'color' (type: DOM.RGBA) -> RGBA of the default background color. If not specified, any existing override will be
cleared.
			No return value.
		
			Description: Sets or clears an override of the default background color of the frame. This override is used
if the content does not specify one.
		"""
		expected = ['color']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['color']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'Emulation.setDefaultBackgroundColorOverride', **kwargs)
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
					'mobile' (type: boolean) -> Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
autosizing and more.
				Optional arguments:
					'scale' (type: number) -> Scale to apply to resulting view image.
					'screenWidth' (type: integer) -> Overriding screen width value in pixels (minimum 0, maximum 10000000).
					'screenHeight' (type: integer) -> Overriding screen height value in pixels (minimum 0, maximum 10000000).
					'positionX' (type: integer) -> Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
					'positionY' (type: integer) -> Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
					'dontSetVisibleSize' (type: boolean) -> Do not set visible view size, rely upon explicit setVisibleSize call.
					'screenOrientation' (type: ScreenOrientation) -> Screen orientation override.
					'viewport' (type: Page.Viewport) -> If set, the visible area of the page will be overridden to this viewport. This viewport
change is not observed by the page, e.g. viewport-relative elements do not change positions.
					'displayFeature' (type: DisplayFeature) -> If set, the display feature of a multi-segment screen. If not set, multi-segment support
is turned-off.
			No return value.
		
			Description: Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
query results).
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
		    'positionY', 'dontSetVisibleSize', 'screenOrientation', 'viewport',
		    'displayFeature']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['scale', 'screenWidth', 'screenHeight', 'positionX', 'positionY', 'dontSetVisibleSize', 'screenOrientation', 'viewport', 'displayFeature']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setDeviceMetricsOverride',
		    width=width, height=height, deviceScaleFactor=deviceScaleFactor,
		    mobile=mobile, **kwargs)
		return subdom_funcs

	def Emulation_setScrollbarsHidden(self, hidden):
		"""
		Function path: Emulation.setScrollbarsHidden
			Domain: Emulation
			Method name: setScrollbarsHidden
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'hidden' (type: boolean) -> Whether scrollbars should be always hidden.
			No return value.
		
		"""
		assert isinstance(hidden, (bool,)
		    ), "Argument 'hidden' must be of type '['bool']'. Received type: '%s'" % type(
		    hidden)
		subdom_funcs = self.synchronous_command('Emulation.setScrollbarsHidden',
		    hidden=hidden)
		return subdom_funcs

	def Emulation_setDocumentCookieDisabled(self, disabled):
		"""
		Function path: Emulation.setDocumentCookieDisabled
			Domain: Emulation
			Method name: setDocumentCookieDisabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'disabled' (type: boolean) -> Whether document.coookie API should be disabled.
			No return value.
		
		"""
		assert isinstance(disabled, (bool,)
		    ), "Argument 'disabled' must be of type '['bool']'. Received type: '%s'" % type(
		    disabled)
		subdom_funcs = self.synchronous_command('Emulation.setDocumentCookieDisabled'
		    , disabled=disabled)
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

	def Emulation_setEmulatedMedia(self, **kwargs):
		"""
		Function path: Emulation.setEmulatedMedia
			Domain: Emulation
			Method name: setEmulatedMedia
		
			Parameters:
				Optional arguments:
					'media' (type: string) -> Media type to emulate. Empty string disables the override.
					'features' (type: array) -> Media features to emulate.
			No return value.
		
			Description: Emulates the given media type or media feature for CSS media queries.
		"""
		if 'media' in kwargs:
			assert isinstance(kwargs['media'], (str,)
			    ), "Optional argument 'media' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['media'])
		if 'features' in kwargs:
			assert isinstance(kwargs['features'], (list, tuple)
			    ), "Optional argument 'features' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['features'])
		expected = ['media', 'features']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['media', 'features']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setEmulatedMedia', **
		    kwargs)
		return subdom_funcs

	def Emulation_setEmulatedVisionDeficiency(self, type):
		"""
		Function path: Emulation.setEmulatedVisionDeficiency
			Domain: Emulation
			Method name: setEmulatedVisionDeficiency
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'type' (type: string) -> Vision deficiency to emulate.
			No return value.
		
			Description: Emulates the given vision deficiency.
		"""
		assert isinstance(type, (str,)
		    ), "Argument 'type' must be of type '['str']'. Received type: '%s'" % type(
		    type)
		subdom_funcs = self.synchronous_command(
		    'Emulation.setEmulatedVisionDeficiency', type=type)
		return subdom_funcs

	def Emulation_setGeolocationOverride(self, **kwargs):
		"""
		Function path: Emulation.setGeolocationOverride
			Domain: Emulation
			Method name: setGeolocationOverride
		
			Parameters:
				Optional arguments:
					'latitude' (type: number) -> Mock latitude
					'longitude' (type: number) -> Mock longitude
					'accuracy' (type: number) -> Mock accuracy
			No return value.
		
			Description: Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
unavailable.
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

	def Emulation_setIdleOverride(self, isUserActive, isScreenUnlocked):
		"""
		Function path: Emulation.setIdleOverride
			Domain: Emulation
			Method name: setIdleOverride
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'isUserActive' (type: boolean) -> Mock isUserActive
					'isScreenUnlocked' (type: boolean) -> Mock isScreenUnlocked
			No return value.
		
			Description: Overrides the Idle state.
		"""
		assert isinstance(isUserActive, (bool,)
		    ), "Argument 'isUserActive' must be of type '['bool']'. Received type: '%s'" % type(
		    isUserActive)
		assert isinstance(isScreenUnlocked, (bool,)
		    ), "Argument 'isScreenUnlocked' must be of type '['bool']'. Received type: '%s'" % type(
		    isScreenUnlocked)
		subdom_funcs = self.synchronous_command('Emulation.setIdleOverride',
		    isUserActive=isUserActive, isScreenUnlocked=isScreenUnlocked)
		return subdom_funcs

	def Emulation_clearIdleOverride(self):
		"""
		Function path: Emulation.clearIdleOverride
			Domain: Emulation
			Method name: clearIdleOverride
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Clears Idle state overrides.
		"""
		subdom_funcs = self.synchronous_command('Emulation.clearIdleOverride')
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

	def Emulation_setScriptExecutionDisabled(self, value):
		"""
		Function path: Emulation.setScriptExecutionDisabled
			Domain: Emulation
			Method name: setScriptExecutionDisabled
		
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
					'budget' (type: number) -> If set, after this many virtual milliseconds have elapsed virtual time will be paused and a
virtualTimeBudgetExpired event is sent.
					'maxVirtualTimeTaskStarvationCount' (type: integer) -> If set this specifies the maximum number of tasks that can be run before virtual is forced
forwards to prevent deadlock.
					'waitForNavigation' (type: boolean) -> If set the virtual time policy change should be deferred until any frame starts navigating.
Note any previous deferred policy change is superseded.
					'initialVirtualTime' (type: Network.TimeSinceEpoch) -> If set, base::Time::Now will be overridden to initially return this value.
			Returns:
				'virtualTimeTicksBase' (type: number) -> Absolute timestamp at which virtual time was first enabled (up time in milliseconds).
		
			Description: Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
the current virtual time policy.  Note this supersedes any previous time budget.
		"""
		if 'budget' in kwargs:
			assert isinstance(kwargs['budget'], (float, int)
			    ), "Optional argument 'budget' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['budget'])
		if 'maxVirtualTimeTaskStarvationCount' in kwargs:
			assert isinstance(kwargs['maxVirtualTimeTaskStarvationCount'], (int,)
			    ), "Optional argument 'maxVirtualTimeTaskStarvationCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['maxVirtualTimeTaskStarvationCount'])
		if 'waitForNavigation' in kwargs:
			assert isinstance(kwargs['waitForNavigation'], (bool,)
			    ), "Optional argument 'waitForNavigation' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['waitForNavigation'])
		expected = ['budget', 'maxVirtualTimeTaskStarvationCount',
		    'waitForNavigation', 'initialVirtualTime']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['budget', 'maxVirtualTimeTaskStarvationCount', 'waitForNavigation', 'initialVirtualTime']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setVirtualTimePolicy',
		    policy=policy, **kwargs)
		return subdom_funcs

	def Emulation_setLocaleOverride(self, **kwargs):
		"""
		Function path: Emulation.setLocaleOverride
			Domain: Emulation
			Method name: setLocaleOverride
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'locale' (type: string) -> ICU style C locale (e.g. "en_US"). If not specified or empty, disables the override and
restores default host system locale.
			No return value.
		
			Description: Overrides default host system locale with the specified one.
		"""
		if 'locale' in kwargs:
			assert isinstance(kwargs['locale'], (str,)
			    ), "Optional argument 'locale' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['locale'])
		expected = ['locale']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['locale']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setLocaleOverride', **
		    kwargs)
		return subdom_funcs

	def Emulation_setTimezoneOverride(self, timezoneId):
		"""
		Function path: Emulation.setTimezoneOverride
			Domain: Emulation
			Method name: setTimezoneOverride
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'timezoneId' (type: string) -> The timezone identifier. If empty, disables the override and
restores default host system timezone.
			No return value.
		
			Description: Overrides default host system timezone with the specified one.
		"""
		assert isinstance(timezoneId, (str,)
		    ), "Argument 'timezoneId' must be of type '['str']'. Received type: '%s'" % type(
		    timezoneId)
		subdom_funcs = self.synchronous_command('Emulation.setTimezoneOverride',
		    timezoneId=timezoneId)
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
		
			Description: Resizes the frame/viewport of the page. Note that this does not affect the frame's container
(e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
on Android.
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

	def Emulation_setDisabledImageTypes(self, imageTypes):
		"""
		Function path: Emulation.setDisabledImageTypes
			Domain: Emulation
			Method name: setDisabledImageTypes
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'imageTypes' (type: array) -> Image types to disable.
			No return value.
		
		"""
		assert isinstance(imageTypes, (list, tuple)
		    ), "Argument 'imageTypes' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    imageTypes)
		subdom_funcs = self.synchronous_command('Emulation.setDisabledImageTypes',
		    imageTypes=imageTypes)
		return subdom_funcs

	def Emulation_setUserAgentOverride(self, userAgent, **kwargs):
		"""
		Function path: Emulation.setUserAgentOverride
			Domain: Emulation
			Method name: setUserAgentOverride
		
			Parameters:
				Required arguments:
					'userAgent' (type: string) -> User agent to use.
				Optional arguments:
					'acceptLanguage' (type: string) -> Browser langugage to emulate.
					'platform' (type: string) -> The platform navigator.platform should return.
					'userAgentMetadata' (type: UserAgentMetadata) -> To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
			No return value.
		
			Description: Allows overriding user agent with the given string.
		"""
		assert isinstance(userAgent, (str,)
		    ), "Argument 'userAgent' must be of type '['str']'. Received type: '%s'" % type(
		    userAgent)
		if 'acceptLanguage' in kwargs:
			assert isinstance(kwargs['acceptLanguage'], (str,)
			    ), "Optional argument 'acceptLanguage' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['acceptLanguage'])
		if 'platform' in kwargs:
			assert isinstance(kwargs['platform'], (str,)
			    ), "Optional argument 'platform' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['platform'])
		expected = ['acceptLanguage', 'platform', 'userAgentMetadata']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['acceptLanguage', 'platform', 'userAgentMetadata']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Emulation.setUserAgentOverride',
		    userAgent=userAgent, **kwargs)
		return subdom_funcs

	def HeadlessExperimental_beginFrame(self, **kwargs):
		"""
		Function path: HeadlessExperimental.beginFrame
			Domain: HeadlessExperimental
			Method name: beginFrame
		
			Parameters:
				Optional arguments:
					'frameTimeTicks' (type: number) -> Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set,
the current time will be used.
					'interval' (type: number) -> The interval between BeginFrames that is reported to the compositor, in milliseconds.
Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
					'noDisplayUpdates' (type: boolean) -> Whether updates should not be committed and drawn onto the display. False by default. If
true, only side effects of the BeginFrame will be run, such as layout and animations, but
any visual updates may not be visible on the display or in screenshots.
					'screenshot' (type: ScreenshotParams) -> If set, a screenshot of the frame will be captured and returned in the response. Otherwise,
no screenshot will be captured. Note that capturing a screenshot can fail, for example,
during renderer initialization. In such a case, no screenshot data will be returned.
			Returns:
				'hasDamage' (type: boolean) -> Whether the BeginFrame resulted in damage and, thus, a new frame was committed to the
display. Reported for diagnostic uses, may be removed in the future.
				'screenshotData' (type: string) -> Base64-encoded image data of the screenshot, if one was requested and successfully taken. (Encoded as a base64 string when passed over JSON)
		
			Description: Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
screenshot from the resulting frame. Requires that the target was created with enabled
BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
https://goo.gl/3zHXhB for more background.
		"""
		if 'frameTimeTicks' in kwargs:
			assert isinstance(kwargs['frameTimeTicks'], (float, int)
			    ), "Optional argument 'frameTimeTicks' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['frameTimeTicks'])
		if 'interval' in kwargs:
			assert isinstance(kwargs['interval'], (float, int)
			    ), "Optional argument 'interval' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['interval'])
		if 'noDisplayUpdates' in kwargs:
			assert isinstance(kwargs['noDisplayUpdates'], (bool,)
			    ), "Optional argument 'noDisplayUpdates' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['noDisplayUpdates'])
		expected = ['frameTimeTicks', 'interval', 'noDisplayUpdates', 'screenshot']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['frameTimeTicks', 'interval', 'noDisplayUpdates', 'screenshot']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('HeadlessExperimental.beginFrame',
		    **kwargs)
		return subdom_funcs

	def HeadlessExperimental_disable(self):
		"""
		Function path: HeadlessExperimental.disable
			Domain: HeadlessExperimental
			Method name: disable
		
			No return value.
		
			Description: Disables headless events for the target.
		"""
		subdom_funcs = self.synchronous_command('HeadlessExperimental.disable')
		return subdom_funcs

	def HeadlessExperimental_enable(self):
		"""
		Function path: HeadlessExperimental.enable
			Domain: HeadlessExperimental
			Method name: enable
		
			No return value.
		
			Description: Enables headless events for the target.
		"""
		subdom_funcs = self.synchronous_command('HeadlessExperimental.enable')
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

	def IO_read(self, handle, **kwargs):
		"""
		Function path: IO.read
			Domain: IO
			Method name: read
		
			Parameters:
				Required arguments:
					'handle' (type: StreamHandle) -> Handle of the stream to read.
				Optional arguments:
					'offset' (type: integer) -> Seek to the specified offset before reading (if not specificed, proceed with offset
following the last read). Some types of streams may only support sequential reads.
					'size' (type: integer) -> Maximum number of bytes to read (left upon the agent discretion if not specified).
			Returns:
				'base64Encoded' (type: boolean) -> Set if the data is base64-encoded
				'data' (type: string) -> Data that were read.
				'eof' (type: boolean) -> Set if the end-of-file condition occurred while reading.
		
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
			No return value.
		
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
			No return value.
		
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

	def IndexedDB_deleteObjectStoreEntries(self, securityOrigin, databaseName,
	    objectStoreName, keyRange):
		"""
		Function path: IndexedDB.deleteObjectStoreEntries
			Domain: IndexedDB
			Method name: deleteObjectStoreEntries
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> No description
					'databaseName' (type: string) -> No description
					'objectStoreName' (type: string) -> No description
					'keyRange' (type: KeyRange) -> Range of entry keys to delete
			No return value.
		
			Description: Delete a range of entries from an object store
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
		subdom_funcs = self.synchronous_command('IndexedDB.deleteObjectStoreEntries',
		    securityOrigin=securityOrigin, databaseName=databaseName,
		    objectStoreName=objectStoreName, keyRange=keyRange)
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

	def IndexedDB_getMetadata(self, securityOrigin, databaseName, objectStoreName
	    ):
		"""
		Function path: IndexedDB.getMetadata
			Domain: IndexedDB
			Method name: getMetadata
		
			Parameters:
				Required arguments:
					'securityOrigin' (type: string) -> Security origin.
					'databaseName' (type: string) -> Database name.
					'objectStoreName' (type: string) -> Object store name.
			Returns:
				'entriesCount' (type: number) -> the entries count
				'keyGeneratorValue' (type: number) -> the current value of key generator, to become the next inserted
key into the object store. Valid if objectStore.autoIncrement
is true.
		
			Description: Gets metadata of an object store
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
		subdom_funcs = self.synchronous_command('IndexedDB.getMetadata',
		    securityOrigin=securityOrigin, databaseName=databaseName,
		    objectStoreName=objectStoreName)
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

	def Input_dispatchDragEvent(self, type, x, y, data, **kwargs):
		"""
		Function path: Input.dispatchDragEvent
			Domain: Input
			Method name: dispatchDragEvent
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'type' (type: string) -> Type of the drag event.
					'x' (type: number) -> X coordinate of the event relative to the main frame's viewport in CSS pixels.
					'y' (type: number) -> Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to
the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
					'data' (type: DragData) -> No description
				Optional arguments:
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8
(default: 0).
			No return value.
		
			Description: Dispatches a drag event into the page.
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
		expected = ['modifiers']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['modifiers']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.dispatchDragEvent', type=
		    type, x=x, y=y, data=data, **kwargs)
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
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8
(default: 0).
					'timestamp' (type: TimeSinceEpoch) -> Time at which the event occurred.
					'text' (type: string) -> Text as generated by processing a virtual key code with a keyboard layout. Not needed for
for `keyUp` and `rawKeyDown` events (default: "")
					'unmodifiedText' (type: string) -> Text that would have been generated by the keyboard if no modifiers were pressed (except for
shift). Useful for shortcut (accelerator) key handling (default: "").
					'keyIdentifier' (type: string) -> Unique key identifier (e.g., 'U+0041') (default: "").
					'code' (type: string) -> Unique DOM defined string value for each physical key (e.g., 'KeyA') (default: "").
					'key' (type: string) -> Unique DOM defined string value describing the meaning of the key in the context of active
modifiers, keyboard layout, etc (e.g., 'AltGr') (default: "").
					'windowsVirtualKeyCode' (type: integer) -> Windows virtual key code (default: 0).
					'nativeVirtualKeyCode' (type: integer) -> Native virtual key code (default: 0).
					'autoRepeat' (type: boolean) -> Whether the event was generated from auto repeat (default: false).
					'isKeypad' (type: boolean) -> Whether the event was generated from the keypad (default: false).
					'isSystemKey' (type: boolean) -> Whether the event was a system key event (default: false).
					'location' (type: integer) -> Whether the event was from the left or right side of the keyboard. 1=Left, 2=Right (default:
0).
					'commands' (type: array) -> Editing commands to send with the key event (e.g., 'selectAll') (default: []).
These are related to but not equal the command names used in `document.execCommand` and NSStandardKeyBindingResponding.
See https://source.chromium.org/chromium/chromium/src/+/master:third_party/blink/renderer/core/editing/commands/editor_command_names.h for valid command names.
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
		if 'location' in kwargs:
			assert isinstance(kwargs['location'], (int,)
			    ), "Optional argument 'location' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['location'])
		if 'commands' in kwargs:
			assert isinstance(kwargs['commands'], (list, tuple)
			    ), "Optional argument 'commands' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['commands'])
		expected = ['modifiers', 'timestamp', 'text', 'unmodifiedText',
		    'keyIdentifier', 'code', 'key', 'windowsVirtualKeyCode',
		    'nativeVirtualKeyCode', 'autoRepeat', 'isKeypad', 'isSystemKey',
		    'location', 'commands']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['modifiers', 'timestamp', 'text', 'unmodifiedText', 'keyIdentifier', 'code', 'key', 'windowsVirtualKeyCode', 'nativeVirtualKeyCode', 'autoRepeat', 'isKeypad', 'isSystemKey', 'location', 'commands']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.dispatchKeyEvent', type=
		    type, **kwargs)
		return subdom_funcs

	def Input_insertText(self, text):
		"""
		Function path: Input.insertText
			Domain: Input
			Method name: insertText
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'text' (type: string) -> The text to insert.
			No return value.
		
			Description: This method emulates inserting text that doesn't come from a key press,
for example an emoji keyboard or an IME.
		"""
		assert isinstance(text, (str,)
		    ), "Argument 'text' must be of type '['str']'. Received type: '%s'" % type(
		    text)
		subdom_funcs = self.synchronous_command('Input.insertText', text=text)
		return subdom_funcs

	def Input_imeSetComposition(self, text, selectionStart, selectionEnd, **kwargs
	    ):
		"""
		Function path: Input.imeSetComposition
			Domain: Input
			Method name: imeSetComposition
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'text' (type: string) -> The text to insert
					'selectionStart' (type: integer) -> selection start
					'selectionEnd' (type: integer) -> selection end
				Optional arguments:
					'replacementStart' (type: integer) -> replacement start
					'replacementEnd' (type: integer) -> replacement end
			No return value.
		
			Description: This method sets the current candidate text for ime.
Use imeCommitComposition to commit the final text.
Use imeSetComposition with empty string as text to cancel composition.
		"""
		assert isinstance(text, (str,)
		    ), "Argument 'text' must be of type '['str']'. Received type: '%s'" % type(
		    text)
		assert isinstance(selectionStart, (int,)
		    ), "Argument 'selectionStart' must be of type '['int']'. Received type: '%s'" % type(
		    selectionStart)
		assert isinstance(selectionEnd, (int,)
		    ), "Argument 'selectionEnd' must be of type '['int']'. Received type: '%s'" % type(
		    selectionEnd)
		if 'replacementStart' in kwargs:
			assert isinstance(kwargs['replacementStart'], (int,)
			    ), "Optional argument 'replacementStart' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['replacementStart'])
		if 'replacementEnd' in kwargs:
			assert isinstance(kwargs['replacementEnd'], (int,)
			    ), "Optional argument 'replacementEnd' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['replacementEnd'])
		expected = ['replacementStart', 'replacementEnd']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['replacementStart', 'replacementEnd']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.imeSetComposition', text=
		    text, selectionStart=selectionStart, selectionEnd=selectionEnd, **kwargs)
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
					'y' (type: number) -> Y coordinate of the event relative to the main frame's viewport in CSS pixels. 0 refers to
the top of the viewport and Y increases as it proceeds towards the bottom of the viewport.
				Optional arguments:
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8
(default: 0).
					'timestamp' (type: TimeSinceEpoch) -> Time at which the event occurred.
					'button' (type: MouseButton) -> Mouse button (default: "none").
					'buttons' (type: integer) -> A number indicating which buttons are pressed on the mouse when a mouse event is triggered.
Left=1, Right=2, Middle=4, Back=8, Forward=16, None=0.
					'clickCount' (type: integer) -> Number of times the mouse button was clicked (default: 0).
					'force' (type: number) -> The normalized pressure, which has a range of [0,1] (default: 0).
					'tangentialPressure' (type: number) -> The normalized tangential pressure, which has a range of [-1,1] (default: 0).
					'tiltX' (type: integer) -> The plane angle between the Y-Z plane and the plane containing both the stylus axis and the Y axis, in degrees of the range [-90,90], a positive tiltX is to the right (default: 0).
					'tiltY' (type: integer) -> The plane angle between the X-Z plane and the plane containing both the stylus axis and the X axis, in degrees of the range [-90,90], a positive tiltY is towards the user (default: 0).
					'twist' (type: integer) -> The clockwise rotation of a pen stylus around its own major axis, in degrees in the range [0,359] (default: 0).
					'deltaX' (type: number) -> X delta in CSS pixels for mouse wheel event (default: 0).
					'deltaY' (type: number) -> Y delta in CSS pixels for mouse wheel event (default: 0).
					'pointerType' (type: string) -> Pointer type (default: "mouse").
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
		if 'buttons' in kwargs:
			assert isinstance(kwargs['buttons'], (int,)
			    ), "Optional argument 'buttons' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['buttons'])
		if 'clickCount' in kwargs:
			assert isinstance(kwargs['clickCount'], (int,)
			    ), "Optional argument 'clickCount' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['clickCount'])
		if 'force' in kwargs:
			assert isinstance(kwargs['force'], (float, int)
			    ), "Optional argument 'force' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['force'])
		if 'tangentialPressure' in kwargs:
			assert isinstance(kwargs['tangentialPressure'], (float, int)
			    ), "Optional argument 'tangentialPressure' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['tangentialPressure'])
		if 'tiltX' in kwargs:
			assert isinstance(kwargs['tiltX'], (int,)
			    ), "Optional argument 'tiltX' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['tiltX'])
		if 'tiltY' in kwargs:
			assert isinstance(kwargs['tiltY'], (int,)
			    ), "Optional argument 'tiltY' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['tiltY'])
		if 'twist' in kwargs:
			assert isinstance(kwargs['twist'], (int,)
			    ), "Optional argument 'twist' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['twist'])
		if 'deltaX' in kwargs:
			assert isinstance(kwargs['deltaX'], (float, int)
			    ), "Optional argument 'deltaX' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['deltaX'])
		if 'deltaY' in kwargs:
			assert isinstance(kwargs['deltaY'], (float, int)
			    ), "Optional argument 'deltaY' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['deltaY'])
		if 'pointerType' in kwargs:
			assert isinstance(kwargs['pointerType'], (str,)
			    ), "Optional argument 'pointerType' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['pointerType'])
		expected = ['modifiers', 'timestamp', 'button', 'buttons', 'clickCount',
		    'force', 'tangentialPressure', 'tiltX', 'tiltY', 'twist', 'deltaX',
		    'deltaY', 'pointerType']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['modifiers', 'timestamp', 'button', 'buttons', 'clickCount', 'force', 'tangentialPressure', 'tiltX', 'tiltY', 'twist', 'deltaX', 'deltaY', 'pointerType']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.dispatchMouseEvent', type=
		    type, x=x, y=y, **kwargs)
		return subdom_funcs

	def Input_dispatchTouchEvent(self, type, touchPoints, **kwargs):
		"""
		Function path: Input.dispatchTouchEvent
			Domain: Input
			Method name: dispatchTouchEvent
		
			Parameters:
				Required arguments:
					'type' (type: string) -> Type of the touch event. TouchEnd and TouchCancel must not contain any touch points, while
TouchStart and TouchMove must contains at least one.
					'touchPoints' (type: array) -> Active touch points on the touch device. One event per any changed point (compared to
previous touch event in a sequence) is generated, emulating pressing/moving/releasing points
one by one.
				Optional arguments:
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8
(default: 0).
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

	def Input_emulateTouchFromMouseEvent(self, type, x, y, button, **kwargs):
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
					'button' (type: MouseButton) -> Mouse button. Only "none", "left", "right" are supported.
				Optional arguments:
					'timestamp' (type: TimeSinceEpoch) -> Time at which the event occurred (default: current time).
					'deltaX' (type: number) -> X delta in DIP for mouse wheel event (default: 0).
					'deltaY' (type: number) -> Y delta in DIP for mouse wheel event (default: 0).
					'modifiers' (type: integer) -> Bit field representing pressed modifier keys. Alt=1, Ctrl=2, Meta/Command=4, Shift=8
(default: 0).
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
		expected = ['timestamp', 'deltaX', 'deltaY', 'modifiers', 'clickCount']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['timestamp', 'deltaX', 'deltaY', 'modifiers', 'clickCount']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Input.emulateTouchFromMouseEvent',
		    type=type, x=x, y=y, button=button, **kwargs)
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

	def Input_setInterceptDrags(self, enabled):
		"""
		Function path: Input.setInterceptDrags
			Domain: Input
			Method name: setInterceptDrags
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> No description
			No return value.
		
			Description: Prevents default drag and drop behavior and instead emits `Input.dragIntercepted` events.
Drag and drop behavior can be directly controlled via `Input.dispatchDragEvent`.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Input.setInterceptDrags',
		    enabled=enabled)
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
					'gestureSourceType' (type: GestureSourceType) -> Which type of input events to be generated (default: 'default', which queries the platform
for the preferred input type).
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
					'xOverscroll' (type: number) -> The number of additional pixels to scroll back along the X axis, in addition to the given
distance.
					'yOverscroll' (type: number) -> The number of additional pixels to scroll back along the Y axis, in addition to the given
distance.
					'preventFling' (type: boolean) -> Prevent fling (default: true).
					'speed' (type: integer) -> Swipe speed in pixels per second (default: 800).
					'gestureSourceType' (type: GestureSourceType) -> Which type of input events to be generated (default: 'default', which queries the platform
for the preferred input type).
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
					'gestureSourceType' (type: GestureSourceType) -> Which type of input events to be generated (default: 'default', which queries the platform
for the preferred input type).
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
				'compositingReasonIds' (type: array) -> A list of strings specifying reason IDs for the given layer to become composited.
		
			Description: Provides the reasons why the given layer was composited.
		"""
		subdom_funcs = self.synchronous_command('LayerTree.compositingReasons',
		    layerId=layerId)
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

	def Log_enable(self):
		"""
		Function path: Log.enable
			Domain: Log
			Method name: enable
		
			No return value.
		
			Description: Enables log domain, sends the entries collected so far to the client by means of the
`entryAdded` notification.
		"""
		subdom_funcs = self.synchronous_command('Log.enable')
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

	def Memory_forciblyPurgeJavaScriptMemory(self):
		"""
		Function path: Memory.forciblyPurgeJavaScriptMemory
			Domain: Memory
			Method name: forciblyPurgeJavaScriptMemory
		
			No return value.
		
			Description: Simulate OomIntervention by purging V8 memory.
		"""
		subdom_funcs = self.synchronous_command(
		    'Memory.forciblyPurgeJavaScriptMemory')
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

	def Memory_startSampling(self, **kwargs):
		"""
		Function path: Memory.startSampling
			Domain: Memory
			Method name: startSampling
		
			Parameters:
				Optional arguments:
					'samplingInterval' (type: integer) -> Average number of bytes between samples.
					'suppressRandomness' (type: boolean) -> Do not randomize intervals between samples.
			No return value.
		
			Description: Start collecting native memory profile.
		"""
		if 'samplingInterval' in kwargs:
			assert isinstance(kwargs['samplingInterval'], (int,)
			    ), "Optional argument 'samplingInterval' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['samplingInterval'])
		if 'suppressRandomness' in kwargs:
			assert isinstance(kwargs['suppressRandomness'], (bool,)
			    ), "Optional argument 'suppressRandomness' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['suppressRandomness'])
		expected = ['samplingInterval', 'suppressRandomness']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['samplingInterval', 'suppressRandomness']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Memory.startSampling', **kwargs)
		return subdom_funcs

	def Memory_stopSampling(self):
		"""
		Function path: Memory.stopSampling
			Domain: Memory
			Method name: stopSampling
		
			No return value.
		
			Description: Stop collecting native memory profile.
		"""
		subdom_funcs = self.synchronous_command('Memory.stopSampling')
		return subdom_funcs

	def Memory_getAllTimeSamplingProfile(self):
		"""
		Function path: Memory.getAllTimeSamplingProfile
			Domain: Memory
			Method name: getAllTimeSamplingProfile
		
			Returns:
				'profile' (type: SamplingProfile) -> No description
		
			Description: Retrieve native memory allocations profile
collected since renderer process startup.
		"""
		subdom_funcs = self.synchronous_command('Memory.getAllTimeSamplingProfile')
		return subdom_funcs

	def Memory_getBrowserSamplingProfile(self):
		"""
		Function path: Memory.getBrowserSamplingProfile
			Domain: Memory
			Method name: getBrowserSamplingProfile
		
			Returns:
				'profile' (type: SamplingProfile) -> No description
		
			Description: Retrieve native memory allocations profile
collected since browser process startup.
		"""
		subdom_funcs = self.synchronous_command('Memory.getBrowserSamplingProfile')
		return subdom_funcs

	def Memory_getSamplingProfile(self):
		"""
		Function path: Memory.getSamplingProfile
			Domain: Memory
			Method name: getSamplingProfile
		
			Returns:
				'profile' (type: SamplingProfile) -> No description
		
			Description: Retrieve native memory allocations profile collected since last
`startSampling` call.
		"""
		subdom_funcs = self.synchronous_command('Memory.getSamplingProfile')
		return subdom_funcs

	def Network_setAcceptedEncodings(self, encodings):
		"""
		Function path: Network.setAcceptedEncodings
			Domain: Network
			Method name: setAcceptedEncodings
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'encodings' (type: array) -> List of accepted content encodings.
			No return value.
		
			Description: Sets a list of content encodings that will be accepted. Empty list means no encoding is accepted.
		"""
		assert isinstance(encodings, (list, tuple)
		    ), "Argument 'encodings' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    encodings)
		subdom_funcs = self.synchronous_command('Network.setAcceptedEncodings',
		    encodings=encodings)
		return subdom_funcs

	def Network_clearAcceptedEncodingsOverride(self):
		"""
		Function path: Network.clearAcceptedEncodingsOverride
			Domain: Network
			Method name: clearAcceptedEncodingsOverride
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Clears accepted encodings set by setAcceptedEncodings
		"""
		subdom_funcs = self.synchronous_command(
		    'Network.clearAcceptedEncodingsOverride')
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

	def Network_canEmulateNetworkConditions(self):
		"""
		Function path: Network.canEmulateNetworkConditions
			Domain: Network
			Method name: canEmulateNetworkConditions
		
			Returns:
				'result' (type: boolean) -> True if emulation of network conditions is supported.
		
			Description: Tells whether emulation of network conditions is supported.
		"""
		subdom_funcs = self.synchronous_command('Network.canEmulateNetworkConditions'
		    )
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
					'errorReason' (type: ErrorReason) -> If set this causes the request to fail with the given reason. Passing `Aborted` for requests
marked with `isNavigationRequest` also cancels the navigation. Must not be set in response
to an authChallenge.
					'rawResponse' (type: string) -> If set the requests completes using with the provided base64 encoded raw response, including
HTTP status line and headers etc... Must not be set in response to an authChallenge. (Encoded as a base64 string when passed over JSON)
					'url' (type: string) -> If set the request url will be modified in a way that's not observable by page. Must not be
set in response to an authChallenge.
					'method' (type: string) -> If set this allows the request method to be overridden. Must not be set in response to an
authChallenge.
					'postData' (type: string) -> If set this allows postData to be set. Must not be set in response to an authChallenge.
					'headers' (type: Headers) -> If set this allows the request headers to be changed. Must not be set in response to an
authChallenge.
					'authChallengeResponse' (type: AuthChallengeResponse) -> Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
			No return value.
		
			Description: Response to Network.requestIntercepted which either modifies the request to continue with any
modifications, or blocks it, or completes it with the provided response bytes. If a network
fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
event will be sent with the same InterceptionId.
Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead.
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

	def Network_deleteCookies(self, name, **kwargs):
		"""
		Function path: Network.deleteCookies
			Domain: Network
			Method name: deleteCookies
		
			Parameters:
				Required arguments:
					'name' (type: string) -> Name of the cookies to remove.
				Optional arguments:
					'url' (type: string) -> If specified, deletes all the cookies with the given name where domain and path match
provided URL.
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

	def Network_enable(self, **kwargs):
		"""
		Function path: Network.enable
			Domain: Network
			Method name: enable
		
			Parameters:
				Optional arguments:
					'maxTotalBufferSize' (type: integer) -> Buffer size in bytes to use when preserving network payloads (XHRs, etc).
					'maxResourceBufferSize' (type: integer) -> Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
					'maxPostDataSize' (type: integer) -> Longest post body size (in bytes) that would be included in requestWillBeSent notification
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
		if 'maxPostDataSize' in kwargs:
			assert isinstance(kwargs['maxPostDataSize'], (int,)
			    ), "Optional argument 'maxPostDataSize' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['maxPostDataSize'])
		expected = ['maxTotalBufferSize', 'maxResourceBufferSize', 'maxPostDataSize']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['maxTotalBufferSize', 'maxResourceBufferSize', 'maxPostDataSize']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.enable', **kwargs)
		return subdom_funcs

	def Network_getAllCookies(self):
		"""
		Function path: Network.getAllCookies
			Domain: Network
			Method name: getAllCookies
		
			Returns:
				'cookies' (type: array) -> Array of cookie objects.
		
			Description: Returns all browser cookies. Depending on the backend support, will return detailed cookie
information in the `cookies` field.
		"""
		subdom_funcs = self.synchronous_command('Network.getAllCookies')
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

	def Network_getCookies(self, **kwargs):
		"""
		Function path: Network.getCookies
			Domain: Network
			Method name: getCookies
		
			Parameters:
				Optional arguments:
					'urls' (type: array) -> The list of URLs for which applicable cookies will be fetched.
If not specified, it's assumed to be set to the list containing
the URLs of the page and all of its subframes.
			Returns:
				'cookies' (type: array) -> Array of cookie objects.
		
			Description: Returns all browser cookies for the current URL. Depending on the backend support, will return
detailed cookie information in the `cookies` field.
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

	def Network_getRequestPostData(self, requestId):
		"""
		Function path: Network.getRequestPostData
			Domain: Network
			Method name: getRequestPostData
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> Identifier of the network request to get content for.
			Returns:
				'postData' (type: string) -> Request body string, omitting files from multipart requests
		
			Description: Returns post data sent with the request. Returns an error when no data was sent with the request.
		"""
		subdom_funcs = self.synchronous_command('Network.getRequestPostData',
		    requestId=requestId)
		return subdom_funcs

	def Network_getResponseBodyForInterception(self, interceptionId):
		"""
		Function path: Network.getResponseBodyForInterception
			Domain: Network
			Method name: getResponseBodyForInterception
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'interceptionId' (type: InterceptionId) -> Identifier for the intercepted request to get body for.
			Returns:
				'body' (type: string) -> Response body.
				'base64Encoded' (type: boolean) -> True, if content was sent as base64.
		
			Description: Returns content served for the given currently intercepted request.
		"""
		subdom_funcs = self.synchronous_command(
		    'Network.getResponseBodyForInterception', interceptionId=interceptionId)
		return subdom_funcs

	def Network_takeResponseBodyForInterceptionAsStream(self, interceptionId):
		"""
		Function path: Network.takeResponseBodyForInterceptionAsStream
			Domain: Network
			Method name: takeResponseBodyForInterceptionAsStream
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'interceptionId' (type: InterceptionId) -> No description
			Returns:
				'stream' (type: IO.StreamHandle) -> No description
		
			Description: Returns a handle to the stream representing the response body. Note that after this command,
the intercepted request can't be continued as is -- you either need to cancel it or to provide
the response body. The stream only supports sequential read, IO.read will fail if the position
is specified.
		"""
		subdom_funcs = self.synchronous_command(
		    'Network.takeResponseBodyForInterceptionAsStream', interceptionId=
		    interceptionId)
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
		
			Description: This method sends a new XMLHttpRequest which is identical to the original one. The following
parameters should be identical: method, url, async, request body, extra headers, withCredentials
attribute, user, password.
		"""
		subdom_funcs = self.synchronous_command('Network.replayXHR', requestId=
		    requestId)
		return subdom_funcs

	def Network_searchInResponseBody(self, requestId, query, **kwargs):
		"""
		Function path: Network.searchInResponseBody
			Domain: Network
			Method name: searchInResponseBody
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> Identifier of the network response to search.
					'query' (type: string) -> String to search for.
				Optional arguments:
					'caseSensitive' (type: boolean) -> If true, search is case sensitive.
					'isRegex' (type: boolean) -> If true, treats string parameter as regex.
			Returns:
				'result' (type: array) -> List of search matches.
		
			Description: Searches for given string in response content.
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
		subdom_funcs = self.synchronous_command('Network.searchInResponseBody',
		    requestId=requestId, query=query, **kwargs)
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

	def Network_setCacheDisabled(self, cacheDisabled):
		"""
		Function path: Network.setCacheDisabled
			Domain: Network
			Method name: setCacheDisabled
		
			Parameters:
				Required arguments:
					'cacheDisabled' (type: boolean) -> Cache disabled state.
			No return value.
		
			Description: Toggles ignoring cache for each request. If `true`, cache will not be used.
		"""
		assert isinstance(cacheDisabled, (bool,)
		    ), "Argument 'cacheDisabled' must be of type '['bool']'. Received type: '%s'" % type(
		    cacheDisabled)
		subdom_funcs = self.synchronous_command('Network.setCacheDisabled',
		    cacheDisabled=cacheDisabled)
		return subdom_funcs

	def Network_setCookie(self, name, value, **kwargs):
		"""
		Function path: Network.setCookie
			Domain: Network
			Method name: setCookie
		
			Parameters:
				Required arguments:
					'name' (type: string) -> Cookie name.
					'value' (type: string) -> Cookie value.
				Optional arguments:
					'url' (type: string) -> The request-URI to associate with the setting of the cookie. This value can affect the
default domain, path, source port, and source scheme values of the created cookie.
					'domain' (type: string) -> Cookie domain.
					'path' (type: string) -> Cookie path.
					'secure' (type: boolean) -> True if cookie is secure.
					'httpOnly' (type: boolean) -> True if cookie is http-only.
					'sameSite' (type: CookieSameSite) -> Cookie SameSite type.
					'expires' (type: TimeSinceEpoch) -> Cookie expiration date, session cookie if not set
					'priority' (type: CookiePriority) -> Cookie Priority type.
					'sameParty' (type: boolean) -> True if cookie is SameParty.
					'sourceScheme' (type: CookieSourceScheme) -> Cookie source scheme type.
					'sourcePort' (type: integer) -> Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
An unspecified port value allows protocol clients to emulate legacy cookie scope for the port.
This is a temporary ability and it will be removed in the future.
			Returns:
				'success' (type: boolean) -> Always set to true. If an error occurs, the response indicates protocol error.
		
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
		if 'sameParty' in kwargs:
			assert isinstance(kwargs['sameParty'], (bool,)
			    ), "Optional argument 'sameParty' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['sameParty'])
		if 'sourcePort' in kwargs:
			assert isinstance(kwargs['sourcePort'], (int,)
			    ), "Optional argument 'sourcePort' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['sourcePort'])
		expected = ['url', 'domain', 'path', 'secure', 'httpOnly', 'sameSite',
		    'expires', 'priority', 'sameParty', 'sourceScheme', 'sourcePort']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['url', 'domain', 'path', 'secure', 'httpOnly', 'sameSite', 'expires', 'priority', 'sameParty', 'sourceScheme', 'sourcePort']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.setCookie', name=name,
		    value=value, **kwargs)
		return subdom_funcs

	def Network_setCookies(self, cookies):
		"""
		Function path: Network.setCookies
			Domain: Network
			Method name: setCookies
		
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

	def Network_setAttachDebugStack(self, enabled):
		"""
		Function path: Network.setAttachDebugStack
			Domain: Network
			Method name: setAttachDebugStack
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether to attach a page script stack for debugging purpose.
			No return value.
		
			Description: Specifies whether to attach a page script stack id in requests
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Network.setAttachDebugStack',
		    enabled=enabled)
		return subdom_funcs

	def Network_setRequestInterception(self, patterns):
		"""
		Function path: Network.setRequestInterception
			Domain: Network
			Method name: setRequestInterception
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'patterns' (type: array) -> Requests matching any of these patterns will be forwarded and wait for the corresponding
continueInterceptedRequest call.
			No return value.
		
			Description: Sets the requests to intercept that match the provided patterns and optionally resource types.
Deprecated, please use Fetch.enable instead.
		"""
		assert isinstance(patterns, (list, tuple)
		    ), "Argument 'patterns' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    patterns)
		subdom_funcs = self.synchronous_command('Network.setRequestInterception',
		    patterns=patterns)
		return subdom_funcs

	def Network_setUserAgentOverride(self, userAgent, **kwargs):
		"""
		Function path: Network.setUserAgentOverride
			Domain: Network
			Method name: setUserAgentOverride
		
			Parameters:
				Required arguments:
					'userAgent' (type: string) -> User agent to use.
				Optional arguments:
					'acceptLanguage' (type: string) -> Browser langugage to emulate.
					'platform' (type: string) -> The platform navigator.platform should return.
					'userAgentMetadata' (type: Emulation.UserAgentMetadata) -> To be sent in Sec-CH-UA-* headers and returned in navigator.userAgentData
			No return value.
		
			Description: Allows overriding user agent with the given string.
		"""
		assert isinstance(userAgent, (str,)
		    ), "Argument 'userAgent' must be of type '['str']'. Received type: '%s'" % type(
		    userAgent)
		if 'acceptLanguage' in kwargs:
			assert isinstance(kwargs['acceptLanguage'], (str,)
			    ), "Optional argument 'acceptLanguage' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['acceptLanguage'])
		if 'platform' in kwargs:
			assert isinstance(kwargs['platform'], (str,)
			    ), "Optional argument 'platform' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['platform'])
		expected = ['acceptLanguage', 'platform', 'userAgentMetadata']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['acceptLanguage', 'platform', 'userAgentMetadata']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.setUserAgentOverride',
		    userAgent=userAgent, **kwargs)
		return subdom_funcs

	def Network_getSecurityIsolationStatus(self, **kwargs):
		"""
		Function path: Network.getSecurityIsolationStatus
			Domain: Network
			Method name: getSecurityIsolationStatus
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'frameId' (type: Page.FrameId) -> If no frameId is provided, the status of the target is provided.
			Returns:
				'status' (type: SecurityIsolationStatus) -> No description
		
			Description: Returns information about the COEP/COOP isolation status.
		"""
		expected = ['frameId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['frameId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Network.getSecurityIsolationStatus',
		    **kwargs)
		return subdom_funcs

	def Network_loadNetworkResource(self, frameId, url, options):
		"""
		Function path: Network.loadNetworkResource
			Domain: Network
			Method name: loadNetworkResource
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'frameId' (type: Page.FrameId) -> Frame id to get the resource for.
					'url' (type: string) -> URL of the resource to get content for.
					'options' (type: LoadNetworkResourceOptions) -> Options for the request.
			Returns:
				'resource' (type: LoadNetworkResourcePageResult) -> No description
		
			Description: Fetches the resource and returns the content.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		subdom_funcs = self.synchronous_command('Network.loadNetworkResource',
		    frameId=frameId, url=url, options=options)
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

	def Overlay_getHighlightObjectForTest(self, nodeId, **kwargs):
		"""
		Function path: Overlay.getHighlightObjectForTest
			Domain: Overlay
			Method name: getHighlightObjectForTest
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> Id of the node to get highlight object for.
				Optional arguments:
					'includeDistance' (type: boolean) -> Whether to include distance info.
					'includeStyle' (type: boolean) -> Whether to include style info.
					'colorFormat' (type: ColorFormat) -> The color format to get config with (default: hex).
					'showAccessibilityInfo' (type: boolean) -> Whether to show accessibility info (default: true).
			Returns:
				'highlight' (type: object) -> Highlight data for the node.
		
			Description: For testing.
		"""
		if 'includeDistance' in kwargs:
			assert isinstance(kwargs['includeDistance'], (bool,)
			    ), "Optional argument 'includeDistance' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeDistance'])
		if 'includeStyle' in kwargs:
			assert isinstance(kwargs['includeStyle'], (bool,)
			    ), "Optional argument 'includeStyle' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeStyle'])
		if 'showAccessibilityInfo' in kwargs:
			assert isinstance(kwargs['showAccessibilityInfo'], (bool,)
			    ), "Optional argument 'showAccessibilityInfo' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['showAccessibilityInfo'])
		expected = ['includeDistance', 'includeStyle', 'colorFormat',
		    'showAccessibilityInfo']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['includeDistance', 'includeStyle', 'colorFormat', 'showAccessibilityInfo']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.getHighlightObjectForTest',
		    nodeId=nodeId, **kwargs)
		return subdom_funcs

	def Overlay_getGridHighlightObjectsForTest(self, nodeIds):
		"""
		Function path: Overlay.getGridHighlightObjectsForTest
			Domain: Overlay
			Method name: getGridHighlightObjectsForTest
		
			Parameters:
				Required arguments:
					'nodeIds' (type: array) -> Ids of the node to get highlight object for.
			Returns:
				'highlights' (type: object) -> Grid Highlight data for the node ids provided.
		
			Description: For Persistent Grid testing.
		"""
		assert isinstance(nodeIds, (list, tuple)
		    ), "Argument 'nodeIds' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    nodeIds)
		subdom_funcs = self.synchronous_command(
		    'Overlay.getGridHighlightObjectsForTest', nodeIds=nodeIds)
		return subdom_funcs

	def Overlay_getSourceOrderHighlightObjectForTest(self, nodeId):
		"""
		Function path: Overlay.getSourceOrderHighlightObjectForTest
			Domain: Overlay
			Method name: getSourceOrderHighlightObjectForTest
		
			Parameters:
				Required arguments:
					'nodeId' (type: DOM.NodeId) -> Id of the node to highlight.
			Returns:
				'highlight' (type: object) -> Source order highlight data for the node id provided.
		
			Description: For Source Order Viewer testing.
		"""
		subdom_funcs = self.synchronous_command(
		    'Overlay.getSourceOrderHighlightObjectForTest', nodeId=nodeId)
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
Deprecated: Doesn't work reliablity and cannot be fixed due to process
separatation (the owner node might be in a different process). Determine
the owner node in the client and use highlightNode.
		"""
		expected = ['contentColor', 'contentOutlineColor']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['contentColor', 'contentOutlineColor']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.highlightFrame', frameId
		    =frameId, **kwargs)
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
					'selector' (type: string) -> Selectors to highlight relevant nodes.
			No return value.
		
			Description: Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or
objectId must be specified.
		"""
		if 'selector' in kwargs:
			assert isinstance(kwargs['selector'], (str,)
			    ), "Optional argument 'selector' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['selector'])
		expected = ['nodeId', 'backendNodeId', 'objectId', 'selector']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId', 'selector']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.highlightNode',
		    highlightConfig=highlightConfig, **kwargs)
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

	def Overlay_highlightSourceOrder(self, sourceOrderConfig, **kwargs):
		"""
		Function path: Overlay.highlightSourceOrder
			Domain: Overlay
			Method name: highlightSourceOrder
		
			Parameters:
				Required arguments:
					'sourceOrderConfig' (type: SourceOrderConfig) -> A descriptor for the appearance of the overlay drawing.
				Optional arguments:
					'nodeId' (type: DOM.NodeId) -> Identifier of the node to highlight.
					'backendNodeId' (type: DOM.BackendNodeId) -> Identifier of the backend node to highlight.
					'objectId' (type: Runtime.RemoteObjectId) -> JavaScript object id of the node to be highlighted.
			No return value.
		
			Description: Highlights the source order of the children of the DOM node with given id or with the given
JavaScript object wrapper. Either nodeId or objectId must be specified.
		"""
		expected = ['nodeId', 'backendNodeId', 'objectId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['nodeId', 'backendNodeId', 'objectId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.highlightSourceOrder',
		    sourceOrderConfig=sourceOrderConfig, **kwargs)
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
					'highlightConfig' (type: HighlightConfig) -> A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled
== false`.
			No return value.
		
			Description: Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted.
Backend then generates 'inspectNodeRequested' event upon element selection.
		"""
		expected = ['highlightConfig']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['highlightConfig']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.setInspectMode', mode=
		    mode, **kwargs)
		return subdom_funcs

	def Overlay_setShowAdHighlights(self, show):
		"""
		Function path: Overlay.setShowAdHighlights
			Domain: Overlay
			Method name: setShowAdHighlights
		
			Parameters:
				Required arguments:
					'show' (type: boolean) -> True for showing ad highlights
			No return value.
		
			Description: Highlights owner element of all frames detected to be ads.
		"""
		assert isinstance(show, (bool,)
		    ), "Argument 'show' must be of type '['bool']'. Received type: '%s'" % type(
		    show)
		subdom_funcs = self.synchronous_command('Overlay.setShowAdHighlights',
		    show=show)
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

	def Overlay_setShowGridOverlays(self, gridNodeHighlightConfigs):
		"""
		Function path: Overlay.setShowGridOverlays
			Domain: Overlay
			Method name: setShowGridOverlays
		
			Parameters:
				Required arguments:
					'gridNodeHighlightConfigs' (type: array) -> An array of node identifiers and descriptors for the highlight appearance.
			No return value.
		
			Description: Highlight multiple elements with the CSS Grid overlay.
		"""
		assert isinstance(gridNodeHighlightConfigs, (list, tuple)
		    ), "Argument 'gridNodeHighlightConfigs' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    gridNodeHighlightConfigs)
		subdom_funcs = self.synchronous_command('Overlay.setShowGridOverlays',
		    gridNodeHighlightConfigs=gridNodeHighlightConfigs)
		return subdom_funcs

	def Overlay_setShowFlexOverlays(self, flexNodeHighlightConfigs):
		"""
		Function path: Overlay.setShowFlexOverlays
			Domain: Overlay
			Method name: setShowFlexOverlays
		
			Parameters:
				Required arguments:
					'flexNodeHighlightConfigs' (type: array) -> An array of node identifiers and descriptors for the highlight appearance.
			No return value.
		
		"""
		assert isinstance(flexNodeHighlightConfigs, (list, tuple)
		    ), "Argument 'flexNodeHighlightConfigs' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    flexNodeHighlightConfigs)
		subdom_funcs = self.synchronous_command('Overlay.setShowFlexOverlays',
		    flexNodeHighlightConfigs=flexNodeHighlightConfigs)
		return subdom_funcs

	def Overlay_setShowScrollSnapOverlays(self, scrollSnapHighlightConfigs):
		"""
		Function path: Overlay.setShowScrollSnapOverlays
			Domain: Overlay
			Method name: setShowScrollSnapOverlays
		
			Parameters:
				Required arguments:
					'scrollSnapHighlightConfigs' (type: array) -> An array of node identifiers and descriptors for the highlight appearance.
			No return value.
		
		"""
		assert isinstance(scrollSnapHighlightConfigs, (list, tuple)
		    ), "Argument 'scrollSnapHighlightConfigs' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    scrollSnapHighlightConfigs)
		subdom_funcs = self.synchronous_command('Overlay.setShowScrollSnapOverlays',
		    scrollSnapHighlightConfigs=scrollSnapHighlightConfigs)
		return subdom_funcs

	def Overlay_setShowContainerQueryOverlays(self, containerQueryHighlightConfigs
	    ):
		"""
		Function path: Overlay.setShowContainerQueryOverlays
			Domain: Overlay
			Method name: setShowContainerQueryOverlays
		
			Parameters:
				Required arguments:
					'containerQueryHighlightConfigs' (type: array) -> An array of node identifiers and descriptors for the highlight appearance.
			No return value.
		
		"""
		assert isinstance(containerQueryHighlightConfigs, (list, tuple)
		    ), "Argument 'containerQueryHighlightConfigs' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    containerQueryHighlightConfigs)
		subdom_funcs = self.synchronous_command(
		    'Overlay.setShowContainerQueryOverlays',
		    containerQueryHighlightConfigs=containerQueryHighlightConfigs)
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

	def Overlay_setShowLayoutShiftRegions(self, result):
		"""
		Function path: Overlay.setShowLayoutShiftRegions
			Domain: Overlay
			Method name: setShowLayoutShiftRegions
		
			Parameters:
				Required arguments:
					'result' (type: boolean) -> True for showing layout shift regions
			No return value.
		
			Description: Requests that backend shows layout shift regions
		"""
		assert isinstance(result, (bool,)
		    ), "Argument 'result' must be of type '['bool']'. Received type: '%s'" % type(
		    result)
		subdom_funcs = self.synchronous_command('Overlay.setShowLayoutShiftRegions',
		    result=result)
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

	def Overlay_setShowHitTestBorders(self, show):
		"""
		Function path: Overlay.setShowHitTestBorders
			Domain: Overlay
			Method name: setShowHitTestBorders
		
			Parameters:
				Required arguments:
					'show' (type: boolean) -> True for showing hit-test borders
			No return value.
		
			Description: Requests that backend shows hit-test borders on layers
		"""
		assert isinstance(show, (bool,)
		    ), "Argument 'show' must be of type '['bool']'. Received type: '%s'" % type(
		    show)
		subdom_funcs = self.synchronous_command('Overlay.setShowHitTestBorders',
		    show=show)
		return subdom_funcs

	def Overlay_setShowWebVitals(self, show):
		"""
		Function path: Overlay.setShowWebVitals
			Domain: Overlay
			Method name: setShowWebVitals
		
			Parameters:
				Required arguments:
					'show' (type: boolean) -> No description
			No return value.
		
			Description: Request that backend shows an overlay with web vital metrics.
		"""
		assert isinstance(show, (bool,)
		    ), "Argument 'show' must be of type '['bool']'. Received type: '%s'" % type(
		    show)
		subdom_funcs = self.synchronous_command('Overlay.setShowWebVitals', show=show
		    )
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

	def Overlay_setShowHinge(self, **kwargs):
		"""
		Function path: Overlay.setShowHinge
			Domain: Overlay
			Method name: setShowHinge
		
			Parameters:
				Optional arguments:
					'hingeConfig' (type: HingeConfig) -> hinge data, null means hideHinge
			No return value.
		
			Description: Add a dual screen device hinge
		"""
		expected = ['hingeConfig']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['hingeConfig']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Overlay.setShowHinge', **kwargs)
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

	def Page_addScriptToEvaluateOnNewDocument(self, source, **kwargs):
		"""
		Function path: Page.addScriptToEvaluateOnNewDocument
			Domain: Page
			Method name: addScriptToEvaluateOnNewDocument
		
			Parameters:
				Required arguments:
					'source' (type: string) -> No description
				Optional arguments:
					'worldName' (type: string) -> If specified, creates an isolated world with the given name and evaluates given script in it.
This world name will be used as the ExecutionContextDescription::name when the corresponding
event is emitted.
					'includeCommandLineAPI' (type: boolean) -> Specifies whether command line API should be available to the script, defaults
to false.
			Returns:
				'identifier' (type: ScriptIdentifier) -> Identifier of the added script.
		
			Description: Evaluates given script in every frame upon creation (before loading frame's scripts).
		"""
		assert isinstance(source, (str,)
		    ), "Argument 'source' must be of type '['str']'. Received type: '%s'" % type(
		    source)
		if 'worldName' in kwargs:
			assert isinstance(kwargs['worldName'], (str,)
			    ), "Optional argument 'worldName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['worldName'])
		if 'includeCommandLineAPI' in kwargs:
			assert isinstance(kwargs['includeCommandLineAPI'], (bool,)
			    ), "Optional argument 'includeCommandLineAPI' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['includeCommandLineAPI'])
		expected = ['worldName', 'includeCommandLineAPI']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['worldName', 'includeCommandLineAPI']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'Page.addScriptToEvaluateOnNewDocument', source=source, **kwargs)
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

	def Page_captureScreenshot(self, **kwargs):
		"""
		Function path: Page.captureScreenshot
			Domain: Page
			Method name: captureScreenshot
		
			Parameters:
				Optional arguments:
					'format' (type: string) -> Image compression format (defaults to png).
					'quality' (type: integer) -> Compression quality from range [0..100] (jpeg only).
					'clip' (type: Viewport) -> Capture the screenshot of a given region only.
					'fromSurface' (type: boolean) -> Capture the screenshot from the surface, rather than the view. Defaults to true.
					'captureBeyondViewport' (type: boolean) -> Capture the screenshot beyond the viewport. Defaults to false.
			Returns:
				'data' (type: string) -> Base64-encoded image data. (Encoded as a base64 string when passed over JSON)
		
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
		if 'captureBeyondViewport' in kwargs:
			assert isinstance(kwargs['captureBeyondViewport'], (bool,)
			    ), "Optional argument 'captureBeyondViewport' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['captureBeyondViewport'])
		expected = ['format', 'quality', 'clip', 'fromSurface',
		    'captureBeyondViewport']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['format', 'quality', 'clip', 'fromSurface', 'captureBeyondViewport']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.captureScreenshot', **kwargs)
		return subdom_funcs

	def Page_captureSnapshot(self, **kwargs):
		"""
		Function path: Page.captureSnapshot
			Domain: Page
			Method name: captureSnapshot
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'format' (type: string) -> Format (defaults to mhtml).
			Returns:
				'data' (type: string) -> Serialized page data.
		
			Description: Returns a snapshot of the page as a string. For MHTML format, the serialization includes
iframes, shadow DOM, external resources, and element-inline styles.
		"""
		if 'format' in kwargs:
			assert isinstance(kwargs['format'], (str,)
			    ), "Optional argument 'format' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['format'])
		expected = ['format']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['format']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.captureSnapshot', **kwargs)
		return subdom_funcs

	def Page_clearDeviceMetricsOverride(self):
		"""
		Function path: Page.clearDeviceMetricsOverride
			Domain: Page
			Method name: clearDeviceMetricsOverride
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Clears the overridden device metrics.
		"""
		subdom_funcs = self.synchronous_command('Page.clearDeviceMetricsOverride')
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

	def Page_clearGeolocationOverride(self):
		"""
		Function path: Page.clearGeolocationOverride
			Domain: Page
			Method name: clearGeolocationOverride
		
			No return value.
		
			Description: Clears the overridden Geolocation Position and Error.
		"""
		subdom_funcs = self.synchronous_command('Page.clearGeolocationOverride')
		return subdom_funcs

	def Page_createIsolatedWorld(self, frameId, **kwargs):
		"""
		Function path: Page.createIsolatedWorld
			Domain: Page
			Method name: createIsolatedWorld
		
			Parameters:
				Required arguments:
					'frameId' (type: FrameId) -> Id of the frame in which the isolated world should be created.
				Optional arguments:
					'worldName' (type: string) -> An optional name which is reported in the Execution Context.
					'grantUniveralAccess' (type: boolean) -> Whether or not universal access should be granted to the isolated world. This is a powerful
option, use with caution.
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

	def Page_getAppManifest(self):
		"""
		Function path: Page.getAppManifest
			Domain: Page
			Method name: getAppManifest
		
			Returns:
				'url' (type: string) -> Manifest location.
				'errors' (type: array) -> No description
				'data' (type: string) -> Manifest content.
				'parsed' (type: AppManifestParsedProperties) -> Parsed manifest properties
		
		"""
		subdom_funcs = self.synchronous_command('Page.getAppManifest')
		return subdom_funcs

	def Page_getInstallabilityErrors(self):
		"""
		Function path: Page.getInstallabilityErrors
			Domain: Page
			Method name: getInstallabilityErrors
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'installabilityErrors' (type: array) -> No description
		
		"""
		subdom_funcs = self.synchronous_command('Page.getInstallabilityErrors')
		return subdom_funcs

	def Page_getManifestIcons(self):
		"""
		Function path: Page.getManifestIcons
			Domain: Page
			Method name: getManifestIcons
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'primaryIcon' (type: string) -> No description
		
		"""
		subdom_funcs = self.synchronous_command('Page.getManifestIcons')
		return subdom_funcs

	def Page_getCookies(self):
		"""
		Function path: Page.getCookies
			Domain: Page
			Method name: getCookies
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'cookies' (type: array) -> Array of cookie objects.
		
			Description: Returns all browser cookies. Depending on the backend support, will return detailed cookie
information in the `cookies` field.
		"""
		subdom_funcs = self.synchronous_command('Page.getCookies')
		return subdom_funcs

	def Page_getFrameTree(self):
		"""
		Function path: Page.getFrameTree
			Domain: Page
			Method name: getFrameTree
		
			Returns:
				'frameTree' (type: FrameTree) -> Present frame tree structure.
		
			Description: Returns present frame tree structure.
		"""
		subdom_funcs = self.synchronous_command('Page.getFrameTree')
		return subdom_funcs

	def Page_getLayoutMetrics(self):
		"""
		Function path: Page.getLayoutMetrics
			Domain: Page
			Method name: getLayoutMetrics
		
			Returns:
				'layoutViewport' (type: LayoutViewport) -> Deprecated metrics relating to the layout viewport. Can be in DP or in CSS pixels depending on the `enable-use-zoom-for-dsf` flag. Use `cssLayoutViewport` instead.
				'visualViewport' (type: VisualViewport) -> Deprecated metrics relating to the visual viewport. Can be in DP or in CSS pixels depending on the `enable-use-zoom-for-dsf` flag. Use `cssVisualViewport` instead.
				'contentSize' (type: DOM.Rect) -> Deprecated size of scrollable area. Can be in DP or in CSS pixels depending on the `enable-use-zoom-for-dsf` flag. Use `cssContentSize` instead.
				'cssLayoutViewport' (type: LayoutViewport) -> Metrics relating to the layout viewport in CSS pixels.
				'cssVisualViewport' (type: VisualViewport) -> Metrics relating to the visual viewport in CSS pixels.
				'cssContentSize' (type: DOM.Rect) -> Size of scrollable area in CSS pixels.
		
			Description: Returns metrics relating to the layouting of the page, such as viewport bounds/scale.
		"""
		subdom_funcs = self.synchronous_command('Page.getLayoutMetrics')
		return subdom_funcs

	def Page_getNavigationHistory(self):
		"""
		Function path: Page.getNavigationHistory
			Domain: Page
			Method name: getNavigationHistory
		
			Returns:
				'currentIndex' (type: integer) -> Index of the current navigation history entry.
				'entries' (type: array) -> Array of navigation history entries.
		
			Description: Returns navigation history for the current page.
		"""
		subdom_funcs = self.synchronous_command('Page.getNavigationHistory')
		return subdom_funcs

	def Page_resetNavigationHistory(self):
		"""
		Function path: Page.resetNavigationHistory
			Domain: Page
			Method name: resetNavigationHistory
		
			No return value.
		
			Description: Resets navigation history for the current page.
		"""
		subdom_funcs = self.synchronous_command('Page.resetNavigationHistory')
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

	def Page_handleJavaScriptDialog(self, accept, **kwargs):
		"""
		Function path: Page.handleJavaScriptDialog
			Domain: Page
			Method name: handleJavaScriptDialog
		
			Parameters:
				Required arguments:
					'accept' (type: boolean) -> Whether to accept or dismiss the dialog.
				Optional arguments:
					'promptText' (type: string) -> The text to enter into the dialog prompt before accepting. Used only if this is a prompt
dialog.
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
					'frameId' (type: FrameId) -> Frame id to navigate, if not specified navigates the top frame.
					'referrerPolicy' (type: ReferrerPolicy) -> Referrer-policy used for the navigation.
			Returns:
				'frameId' (type: FrameId) -> Frame id that has navigated (or failed to navigate)
				'loaderId' (type: Network.LoaderId) -> Loader identifier.
				'errorText' (type: string) -> User friendly error message, present if and only if navigation has failed.
		
			Description: Navigates current page to the given URL.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		if 'referrer' in kwargs:
			assert isinstance(kwargs['referrer'], (str,)
			    ), "Optional argument 'referrer' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['referrer'])
		expected = ['referrer', 'transitionType', 'frameId', 'referrerPolicy']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['referrer', 'transitionType', 'frameId', 'referrerPolicy']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.navigate', url=url, **kwargs)
		return subdom_funcs

	def Page_navigateToHistoryEntry(self, entryId):
		"""
		Function path: Page.navigateToHistoryEntry
			Domain: Page
			Method name: navigateToHistoryEntry
		
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

	def Page_printToPDF(self, **kwargs):
		"""
		Function path: Page.printToPDF
			Domain: Page
			Method name: printToPDF
		
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
					'pageRanges' (type: string) -> Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means
print all pages.
					'ignoreInvalidPageRanges' (type: boolean) -> Whether to silently ignore invalid but successfully parsed page ranges, such as '3-2'.
Defaults to false.
					'headerTemplate' (type: string) -> HTML template for the print header. Should be valid HTML markup with following
classes used to inject printing values into them:
- `date`: formatted print date
- `title`: document title
- `url`: document location
- `pageNumber`: current page number
- `totalPages`: total pages in the document

For example, `<span class=title></span>` would generate span containing the title.
					'footerTemplate' (type: string) -> HTML template for the print footer. Should use the same format as the `headerTemplate`.
					'preferCSSPageSize' (type: boolean) -> Whether or not to prefer page size as defined by css. Defaults to false,
in which case the content will be scaled to fit the paper size.
					'transferMode' (type: string) -> return as stream
			Returns:
				'data' (type: string) -> Base64-encoded pdf data. Empty if |returnAsStream| is specified. (Encoded as a base64 string when passed over JSON)
				'stream' (type: IO.StreamHandle) -> A handle of the stream that holds resulting PDF data.
		
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
		if 'headerTemplate' in kwargs:
			assert isinstance(kwargs['headerTemplate'], (str,)
			    ), "Optional argument 'headerTemplate' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['headerTemplate'])
		if 'footerTemplate' in kwargs:
			assert isinstance(kwargs['footerTemplate'], (str,)
			    ), "Optional argument 'footerTemplate' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['footerTemplate'])
		if 'preferCSSPageSize' in kwargs:
			assert isinstance(kwargs['preferCSSPageSize'], (bool,)
			    ), "Optional argument 'preferCSSPageSize' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['preferCSSPageSize'])
		if 'transferMode' in kwargs:
			assert isinstance(kwargs['transferMode'], (str,)
			    ), "Optional argument 'transferMode' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['transferMode'])
		expected = ['landscape', 'displayHeaderFooter', 'printBackground',
		    'scale', 'paperWidth', 'paperHeight', 'marginTop', 'marginBottom',
		    'marginLeft', 'marginRight', 'pageRanges', 'ignoreInvalidPageRanges',
		    'headerTemplate', 'footerTemplate', 'preferCSSPageSize', 'transferMode']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['landscape', 'displayHeaderFooter', 'printBackground', 'scale', 'paperWidth', 'paperHeight', 'marginTop', 'marginBottom', 'marginLeft', 'marginRight', 'pageRanges', 'ignoreInvalidPageRanges', 'headerTemplate', 'footerTemplate', 'preferCSSPageSize', 'transferMode']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.printToPDF', **kwargs)
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
Argument will be ignored if reloading dataURL origin.
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

	def Page_removeScriptToEvaluateOnNewDocument(self, identifier):
		"""
		Function path: Page.removeScriptToEvaluateOnNewDocument
			Domain: Page
			Method name: removeScriptToEvaluateOnNewDocument
		
			Parameters:
				Required arguments:
					'identifier' (type: ScriptIdentifier) -> No description
			No return value.
		
			Description: Removes given script from the list.
		"""
		subdom_funcs = self.synchronous_command(
		    'Page.removeScriptToEvaluateOnNewDocument', identifier=identifier)
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

	def Page_setBypassCSP(self, enabled):
		"""
		Function path: Page.setBypassCSP
			Domain: Page
			Method name: setBypassCSP
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> Whether to bypass page CSP.
			No return value.
		
			Description: Enable page Content Security Policy by-passing.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Page.setBypassCSP', enabled=enabled)
		return subdom_funcs

	def Page_getPermissionsPolicyState(self, frameId):
		"""
		Function path: Page.getPermissionsPolicyState
			Domain: Page
			Method name: getPermissionsPolicyState
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'frameId' (type: FrameId) -> No description
			Returns:
				'states' (type: array) -> No description
		
			Description: Get Permissions Policy state on given frame.
		"""
		subdom_funcs = self.synchronous_command('Page.getPermissionsPolicyState',
		    frameId=frameId)
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
					'mobile' (type: boolean) -> Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
autosizing and more.
				Optional arguments:
					'scale' (type: number) -> Scale to apply to resulting view image.
					'screenWidth' (type: integer) -> Overriding screen width value in pixels (minimum 0, maximum 10000000).
					'screenHeight' (type: integer) -> Overriding screen height value in pixels (minimum 0, maximum 10000000).
					'positionX' (type: integer) -> Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
					'positionY' (type: integer) -> Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
					'dontSetVisibleSize' (type: boolean) -> Do not set visible view size, rely upon explicit setVisibleSize call.
					'screenOrientation' (type: Emulation.ScreenOrientation) -> Screen orientation override.
					'viewport' (type: Viewport) -> The viewport dimensions and scale. If not set, the override is cleared.
			No return value.
		
			Description: Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
query results).
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
		    'positionY', 'dontSetVisibleSize', 'screenOrientation', 'viewport']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['scale', 'screenWidth', 'screenHeight', 'positionX', 'positionY', 'dontSetVisibleSize', 'screenOrientation', 'viewport']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.setDeviceMetricsOverride',
		    width=width, height=height, deviceScaleFactor=deviceScaleFactor,
		    mobile=mobile, **kwargs)
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

	def Page_setFontFamilies(self, fontFamilies):
		"""
		Function path: Page.setFontFamilies
			Domain: Page
			Method name: setFontFamilies
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'fontFamilies' (type: FontFamilies) -> Specifies font families to set. If a font family is not specified, it won't be changed.
			No return value.
		
			Description: Set generic font families.
		"""
		subdom_funcs = self.synchronous_command('Page.setFontFamilies',
		    fontFamilies=fontFamilies)
		return subdom_funcs

	def Page_setFontSizes(self, fontSizes):
		"""
		Function path: Page.setFontSizes
			Domain: Page
			Method name: setFontSizes
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'fontSizes' (type: FontSizes) -> Specifies font sizes to set. If a font size is not specified, it won't be changed.
			No return value.
		
			Description: Set default font sizes.
		"""
		subdom_funcs = self.synchronous_command('Page.setFontSizes', fontSizes=
		    fontSizes)
		return subdom_funcs

	def Page_setDocumentContent(self, frameId, html):
		"""
		Function path: Page.setDocumentContent
			Domain: Page
			Method name: setDocumentContent
		
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

	def Page_setDownloadBehavior(self, behavior, **kwargs):
		"""
		Function path: Page.setDownloadBehavior
			Domain: Page
			Method name: setDownloadBehavior
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'behavior' (type: string) -> Whether to allow all or deny all download requests, or use default Chrome behavior if
available (otherwise deny).
				Optional arguments:
					'downloadPath' (type: string) -> The default path to save downloaded files to. This is required if behavior is set to 'allow'
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
		
			Description: Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
unavailable.
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

	def Page_setLifecycleEventsEnabled(self, enabled):
		"""
		Function path: Page.setLifecycleEventsEnabled
			Domain: Page
			Method name: setLifecycleEventsEnabled
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> If true, starts emitting lifecycle events.
			No return value.
		
			Description: Controls whether page will emit lifecycle events.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Page.setLifecycleEventsEnabled',
		    enabled=enabled)
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
		
			Description: Starts sending each frame using the `screencastFrame` event.
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

	def Page_stopLoading(self):
		"""
		Function path: Page.stopLoading
			Domain: Page
			Method name: stopLoading
		
			No return value.
		
			Description: Force the page stop all navigations and pending resource fetches.
		"""
		subdom_funcs = self.synchronous_command('Page.stopLoading')
		return subdom_funcs

	def Page_crash(self):
		"""
		Function path: Page.crash
			Domain: Page
			Method name: crash
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Crashes renderer on the IO thread, generates minidumps.
		"""
		subdom_funcs = self.synchronous_command('Page.crash')
		return subdom_funcs

	def Page_close(self):
		"""
		Function path: Page.close
			Domain: Page
			Method name: close
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Tries to close page, running its beforeunload hooks, if any.
		"""
		subdom_funcs = self.synchronous_command('Page.close')
		return subdom_funcs

	def Page_setWebLifecycleState(self, state):
		"""
		Function path: Page.setWebLifecycleState
			Domain: Page
			Method name: setWebLifecycleState
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'state' (type: string) -> Target lifecycle state
			No return value.
		
			Description: Tries to update the web lifecycle state of the page.
It will transition the page to the given state according to:
https://github.com/WICG/web-lifecycle/
		"""
		assert isinstance(state, (str,)
		    ), "Argument 'state' must be of type '['str']'. Received type: '%s'" % type(
		    state)
		subdom_funcs = self.synchronous_command('Page.setWebLifecycleState',
		    state=state)
		return subdom_funcs

	def Page_stopScreencast(self):
		"""
		Function path: Page.stopScreencast
			Domain: Page
			Method name: stopScreencast
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Stops sending each frame in the `screencastFrame`.
		"""
		subdom_funcs = self.synchronous_command('Page.stopScreencast')
		return subdom_funcs

	def Page_setProduceCompilationCache(self, enabled):
		"""
		Function path: Page.setProduceCompilationCache
			Domain: Page
			Method name: setProduceCompilationCache
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> No description
			No return value.
		
			Description: Forces compilation cache to be generated for every subresource script.
See also: `Page.produceCompilationCache`.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Page.setProduceCompilationCache',
		    enabled=enabled)
		return subdom_funcs

	def Page_produceCompilationCache(self, scripts):
		"""
		Function path: Page.produceCompilationCache
			Domain: Page
			Method name: produceCompilationCache
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'scripts' (type: array) -> No description
			No return value.
		
			Description: Requests backend to produce compilation cache for the specified scripts.
Unlike setProduceCompilationCache, this allows client to only produce cache
for specific scripts. `scripts` are appeneded to the list of scripts
for which the cache for would produced. Disabling compilation cache with
`setProduceCompilationCache` would reset all pending cache requests.
The list may also be reset during page navigation.
When script with a matching URL is encountered, the cache is optionally
produced upon backend discretion, based on internal heuristics.
See also: `Page.compilationCacheProduced`.
		"""
		assert isinstance(scripts, (list, tuple)
		    ), "Argument 'scripts' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    scripts)
		subdom_funcs = self.synchronous_command('Page.produceCompilationCache',
		    scripts=scripts)
		return subdom_funcs

	def Page_addCompilationCache(self, url, data):
		"""
		Function path: Page.addCompilationCache
			Domain: Page
			Method name: addCompilationCache
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'url' (type: string) -> No description
					'data' (type: string) -> Base64-encoded data (Encoded as a base64 string when passed over JSON)
			No return value.
		
			Description: Seeds compilation cache for given url. Compilation cache does not survive
cross-process navigation.
		"""
		assert isinstance(url, (str,)
		    ), "Argument 'url' must be of type '['str']'. Received type: '%s'" % type(
		    url)
		assert isinstance(data, (str,)
		    ), "Argument 'data' must be of type '['str']'. Received type: '%s'" % type(
		    data)
		subdom_funcs = self.synchronous_command('Page.addCompilationCache', url=
		    url, data=data)
		return subdom_funcs

	def Page_clearCompilationCache(self):
		"""
		Function path: Page.clearCompilationCache
			Domain: Page
			Method name: clearCompilationCache
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Clears seeded compilation cache.
		"""
		subdom_funcs = self.synchronous_command('Page.clearCompilationCache')
		return subdom_funcs

	def Page_generateTestReport(self, message, **kwargs):
		"""
		Function path: Page.generateTestReport
			Domain: Page
			Method name: generateTestReport
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'message' (type: string) -> Message to be displayed in the report.
				Optional arguments:
					'group' (type: string) -> Specifies the endpoint group to deliver the report to.
			No return value.
		
			Description: Generates a report for testing.
		"""
		assert isinstance(message, (str,)
		    ), "Argument 'message' must be of type '['str']'. Received type: '%s'" % type(
		    message)
		if 'group' in kwargs:
			assert isinstance(kwargs['group'], (str,)
			    ), "Optional argument 'group' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['group'])
		expected = ['group']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['group']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Page.generateTestReport',
		    message=message, **kwargs)
		return subdom_funcs

	def Page_waitForDebugger(self):
		"""
		Function path: Page.waitForDebugger
			Domain: Page
			Method name: waitForDebugger
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Pauses page execution. Can be resumed using generic Runtime.runIfWaitingForDebugger.
		"""
		subdom_funcs = self.synchronous_command('Page.waitForDebugger')
		return subdom_funcs

	def Page_setInterceptFileChooserDialog(self, enabled):
		"""
		Function path: Page.setInterceptFileChooserDialog
			Domain: Page
			Method name: setInterceptFileChooserDialog
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'enabled' (type: boolean) -> No description
			No return value.
		
			Description: Intercept file chooser requests and transfer control to protocol clients.
When file chooser interception is enabled, native file chooser dialog is not shown.
Instead, a protocol event `Page.fileChooserOpened` is emitted.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command('Page.setInterceptFileChooserDialog',
		    enabled=enabled)
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

	def Performance_enable(self, **kwargs):
		"""
		Function path: Performance.enable
			Domain: Performance
			Method name: enable
		
			Parameters:
				Optional arguments:
					'timeDomain' (type: string) -> Time domain to use for collecting and reporting duration metrics.
			No return value.
		
			Description: Enable collecting and reporting metrics.
		"""
		if 'timeDomain' in kwargs:
			assert isinstance(kwargs['timeDomain'], (str,)
			    ), "Optional argument 'timeDomain' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['timeDomain'])
		expected = ['timeDomain']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['timeDomain']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Performance.enable', **kwargs)
		return subdom_funcs

	def Performance_setTimeDomain(self, timeDomain):
		"""
		Function path: Performance.setTimeDomain
			Domain: Performance
			Method name: setTimeDomain
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'timeDomain' (type: string) -> Time domain
			No return value.
		
			Description: Sets time domain to use for collecting and reporting duration metrics.
Note that this must be called before enabling metrics collection. Calling
this method while metrics collection is enabled returns an error.
		"""
		assert isinstance(timeDomain, (str,)
		    ), "Argument 'timeDomain' must be of type '['str']'. Received type: '%s'" % type(
		    timeDomain)
		subdom_funcs = self.synchronous_command('Performance.setTimeDomain',
		    timeDomain=timeDomain)
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

	def PerformanceTimeline_enable(self, eventTypes):
		"""
		Function path: PerformanceTimeline.enable
			Domain: PerformanceTimeline
			Method name: enable
		
			Parameters:
				Required arguments:
					'eventTypes' (type: array) -> The types of event to report, as specified in
https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype
The specified filter overrides any previous filters, passing empty
filter disables recording.
Note that not all types exposed to the web platform are currently supported.
			No return value.
		
			Description: Previously buffered events would be reported before method returns.
See also: timelineEventAdded
		"""
		assert isinstance(eventTypes, (list, tuple)
		    ), "Argument 'eventTypes' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    eventTypes)
		subdom_funcs = self.synchronous_command('PerformanceTimeline.enable',
		    eventTypes=eventTypes)
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

	def Security_setIgnoreCertificateErrors(self, ignore):
		"""
		Function path: Security.setIgnoreCertificateErrors
			Domain: Security
			Method name: setIgnoreCertificateErrors
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'ignore' (type: boolean) -> If true, all certificate errors will be ignored.
			No return value.
		
			Description: Enable/disable whether all certificate errors should be ignored.
		"""
		assert isinstance(ignore, (bool,)
		    ), "Argument 'ignore' must be of type '['bool']'. Received type: '%s'" % type(
		    ignore)
		subdom_funcs = self.synchronous_command('Security.setIgnoreCertificateErrors'
		    , ignore=ignore)
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
		
			Description: Enable/disable overriding certificate errors. If enabled, all certificate error events need to
be handled by the DevTools client and should be answered with `handleCertificateError` commands.
		"""
		assert isinstance(override, (bool,)
		    ), "Argument 'override' must be of type '['bool']'. Received type: '%s'" % type(
		    override)
		subdom_funcs = self.synchronous_command(
		    'Security.setOverrideCertificateErrors', override=override)
		return subdom_funcs

	def ServiceWorker_deliverPushMessage(self, origin, registrationId, data):
		"""
		Function path: ServiceWorker.deliverPushMessage
			Domain: ServiceWorker
			Method name: deliverPushMessage
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> No description
					'registrationId' (type: RegistrationID) -> No description
					'data' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		assert isinstance(data, (str,)
		    ), "Argument 'data' must be of type '['str']'. Received type: '%s'" % type(
		    data)
		subdom_funcs = self.synchronous_command('ServiceWorker.deliverPushMessage',
		    origin=origin, registrationId=registrationId, data=data)
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

	def ServiceWorker_dispatchSyncEvent(self, origin, registrationId, tag,
	    lastChance):
		"""
		Function path: ServiceWorker.dispatchSyncEvent
			Domain: ServiceWorker
			Method name: dispatchSyncEvent
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> No description
					'registrationId' (type: RegistrationID) -> No description
					'tag' (type: string) -> No description
					'lastChance' (type: boolean) -> No description
			No return value.
		
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
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

	def ServiceWorker_dispatchPeriodicSyncEvent(self, origin, registrationId, tag
	    ):
		"""
		Function path: ServiceWorker.dispatchPeriodicSyncEvent
			Domain: ServiceWorker
			Method name: dispatchPeriodicSyncEvent
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> No description
					'registrationId' (type: RegistrationID) -> No description
					'tag' (type: string) -> No description
			No return value.
		
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		assert isinstance(tag, (str,)
		    ), "Argument 'tag' must be of type '['str']'. Received type: '%s'" % type(
		    tag)
		subdom_funcs = self.synchronous_command(
		    'ServiceWorker.dispatchPeriodicSyncEvent', origin=origin,
		    registrationId=registrationId, tag=tag)
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

	def ServiceWorker_stopAllWorkers(self):
		"""
		Function path: ServiceWorker.stopAllWorkers
			Domain: ServiceWorker
			Method name: stopAllWorkers
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('ServiceWorker.stopAllWorkers')
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

	def Storage_clearDataForOrigin(self, origin, storageTypes):
		"""
		Function path: Storage.clearDataForOrigin
			Domain: Storage
			Method name: clearDataForOrigin
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
					'storageTypes' (type: string) -> Comma separated list of StorageType to clear.
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

	def Storage_getCookies(self, **kwargs):
		"""
		Function path: Storage.getCookies
			Domain: Storage
			Method name: getCookies
		
			Parameters:
				Optional arguments:
					'browserContextId' (type: Browser.BrowserContextID) -> Browser context to use when called on the browser endpoint.
			Returns:
				'cookies' (type: array) -> Array of cookie objects.
		
			Description: Returns all browser cookies.
		"""
		expected = ['browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Storage.getCookies', **kwargs)
		return subdom_funcs

	def Storage_setCookies(self, cookies, **kwargs):
		"""
		Function path: Storage.setCookies
			Domain: Storage
			Method name: setCookies
		
			Parameters:
				Required arguments:
					'cookies' (type: array) -> Cookies to be set.
				Optional arguments:
					'browserContextId' (type: Browser.BrowserContextID) -> Browser context to use when called on the browser endpoint.
			No return value.
		
			Description: Sets given cookies.
		"""
		assert isinstance(cookies, (list, tuple)
		    ), "Argument 'cookies' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    cookies)
		expected = ['browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Storage.setCookies', cookies=
		    cookies, **kwargs)
		return subdom_funcs

	def Storage_clearCookies(self, **kwargs):
		"""
		Function path: Storage.clearCookies
			Domain: Storage
			Method name: clearCookies
		
			Parameters:
				Optional arguments:
					'browserContextId' (type: Browser.BrowserContextID) -> Browser context to use when called on the browser endpoint.
			No return value.
		
			Description: Clears cookies.
		"""
		expected = ['browserContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['browserContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Storage.clearCookies', **kwargs)
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
				'overrideActive' (type: boolean) -> Whether or not the origin has an active storage quota override
				'usageBreakdown' (type: array) -> Storage usage per type (bytes).
		
			Description: Returns usage and quota in bytes.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		subdom_funcs = self.synchronous_command('Storage.getUsageAndQuota',
		    origin=origin)
		return subdom_funcs

	def Storage_overrideQuotaForOrigin(self, origin, **kwargs):
		"""
		Function path: Storage.overrideQuotaForOrigin
			Domain: Storage
			Method name: overrideQuotaForOrigin
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
				Optional arguments:
					'quotaSize' (type: number) -> The quota size (in bytes) to override the original quota with.
If this is called multiple times, the overridden quota will be equal to
the quotaSize provided in the final call. If this is called without
specifying a quotaSize, the quota will be reset to the default value for
the specified origin. If this is called multiple times with different
origins, the override will be maintained for each origin until it is
disabled (called without a quotaSize).
			No return value.
		
			Description: Override quota for the specified origin
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		if 'quotaSize' in kwargs:
			assert isinstance(kwargs['quotaSize'], (float, int)
			    ), "Optional argument 'quotaSize' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['quotaSize'])
		expected = ['quotaSize']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['quotaSize']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Storage.overrideQuotaForOrigin',
		    origin=origin, **kwargs)
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

	def Storage_trackIndexedDBForOrigin(self, origin):
		"""
		Function path: Storage.trackIndexedDBForOrigin
			Domain: Storage
			Method name: trackIndexedDBForOrigin
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
			No return value.
		
			Description: Registers origin to be notified when an update occurs to its IndexedDB.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		subdom_funcs = self.synchronous_command('Storage.trackIndexedDBForOrigin',
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

	def Storage_untrackIndexedDBForOrigin(self, origin):
		"""
		Function path: Storage.untrackIndexedDBForOrigin
			Domain: Storage
			Method name: untrackIndexedDBForOrigin
		
			Parameters:
				Required arguments:
					'origin' (type: string) -> Security origin.
			No return value.
		
			Description: Unregisters origin from receiving notifications for IndexedDB.
		"""
		assert isinstance(origin, (str,)
		    ), "Argument 'origin' must be of type '['str']'. Received type: '%s'" % type(
		    origin)
		subdom_funcs = self.synchronous_command('Storage.untrackIndexedDBForOrigin',
		    origin=origin)
		return subdom_funcs

	def Storage_getTrustTokens(self):
		"""
		Function path: Storage.getTrustTokens
			Domain: Storage
			Method name: getTrustTokens
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'tokens' (type: array) -> No description
		
			Description: Returns the number of stored Trust Tokens per issuer for the
current browsing context.
		"""
		subdom_funcs = self.synchronous_command('Storage.getTrustTokens')
		return subdom_funcs

	def Storage_clearTrustTokens(self, issuerOrigin):
		"""
		Function path: Storage.clearTrustTokens
			Domain: Storage
			Method name: clearTrustTokens
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'issuerOrigin' (type: string) -> No description
			Returns:
				'didDeleteTokens' (type: boolean) -> True if any tokens were deleted, false otherwise.
		
			Description: Removes all Trust Tokens issued by the provided issuerOrigin.
Leaves other stored data, including the issuer's Redemption Records, intact.
		"""
		assert isinstance(issuerOrigin, (str,)
		    ), "Argument 'issuerOrigin' must be of type '['str']'. Received type: '%s'" % type(
		    issuerOrigin)
		subdom_funcs = self.synchronous_command('Storage.clearTrustTokens',
		    issuerOrigin=issuerOrigin)
		return subdom_funcs

	def SystemInfo_getInfo(self):
		"""
		Function path: SystemInfo.getInfo
			Domain: SystemInfo
			Method name: getInfo
		
			Returns:
				'gpu' (type: GPUInfo) -> Information about the GPUs on the system.
				'modelName' (type: string) -> A platform-dependent description of the model of the machine. On Mac OS, this is, for
example, 'MacBookPro'. Will be the empty string if not supported.
				'modelVersion' (type: string) -> A platform-dependent description of the version of the machine. On Mac OS, this is, for
example, '10.1'. Will be the empty string if not supported.
				'commandLine' (type: string) -> The command line string used to launch the browser. Will be the empty string if not
supported.
		
			Description: Returns information about the system.
		"""
		subdom_funcs = self.synchronous_command('SystemInfo.getInfo')
		return subdom_funcs

	def SystemInfo_getProcessInfo(self):
		"""
		Function path: SystemInfo.getProcessInfo
			Domain: SystemInfo
			Method name: getProcessInfo
		
			Returns:
				'processInfo' (type: array) -> An array of process info blocks.
		
			Description: Returns information about all running processes.
		"""
		subdom_funcs = self.synchronous_command('SystemInfo.getProcessInfo')
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

	def Target_attachToTarget(self, targetId, **kwargs):
		"""
		Function path: Target.attachToTarget
			Domain: Target
			Method name: attachToTarget
		
			Parameters:
				Required arguments:
					'targetId' (type: TargetID) -> No description
				Optional arguments:
					'flatten' (type: boolean) -> Enables "flat" access to the session via specifying sessionId attribute in the commands.
We plan to make this the default, deprecate non-flattened mode,
and eventually retire it. See crbug.com/991325.
			Returns:
				'sessionId' (type: SessionID) -> Id assigned to the session.
		
			Description: Attaches to the target with given id.
		"""
		if 'flatten' in kwargs:
			assert isinstance(kwargs['flatten'], (bool,)
			    ), "Optional argument 'flatten' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['flatten'])
		expected = ['flatten']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['flatten']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.attachToTarget', targetId
		    =targetId, **kwargs)
		return subdom_funcs

	def Target_attachToBrowserTarget(self):
		"""
		Function path: Target.attachToBrowserTarget
			Domain: Target
			Method name: attachToBrowserTarget
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'sessionId' (type: SessionID) -> Id assigned to the session.
		
			Description: Attaches to the browser target, only uses flat sessionId mode.
		"""
		subdom_funcs = self.synchronous_command('Target.attachToBrowserTarget')
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
				'success' (type: boolean) -> Always set to true. If an error occurs, the response indicates protocol error.
		
			Description: Closes the target. If the target is a page that gets closed too.
		"""
		subdom_funcs = self.synchronous_command('Target.closeTarget', targetId=
		    targetId)
		return subdom_funcs

	def Target_exposeDevToolsProtocol(self, targetId, **kwargs):
		"""
		Function path: Target.exposeDevToolsProtocol
			Domain: Target
			Method name: exposeDevToolsProtocol
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'targetId' (type: TargetID) -> No description
				Optional arguments:
					'bindingName' (type: string) -> Binding name, 'cdp' if not specified.
			No return value.
		
			Description: Inject object to the target's main frame that provides a communication
channel with browser target.

Injected object will be available as `window[bindingName]`.

The object has the follwing API:
- `binding.send(json)` - a method to send messages over the remote debugging protocol
- `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.
		"""
		if 'bindingName' in kwargs:
			assert isinstance(kwargs['bindingName'], (str,)
			    ), "Optional argument 'bindingName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['bindingName'])
		expected = ['bindingName']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['bindingName']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.exposeDevToolsProtocol',
		    targetId=targetId, **kwargs)
		return subdom_funcs

	def Target_createBrowserContext(self, **kwargs):
		"""
		Function path: Target.createBrowserContext
			Domain: Target
			Method name: createBrowserContext
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'disposeOnDetach' (type: boolean) -> If specified, disposes this context when debugging session disconnects.
					'proxyServer' (type: string) -> Proxy server, similar to the one passed to --proxy-server
					'proxyBypassList' (type: string) -> Proxy bypass list, similar to the one passed to --proxy-bypass-list
			Returns:
				'browserContextId' (type: Browser.BrowserContextID) -> The id of the context created.
		
			Description: Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
one.
		"""
		if 'disposeOnDetach' in kwargs:
			assert isinstance(kwargs['disposeOnDetach'], (bool,)
			    ), "Optional argument 'disposeOnDetach' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['disposeOnDetach'])
		if 'proxyServer' in kwargs:
			assert isinstance(kwargs['proxyServer'], (str,)
			    ), "Optional argument 'proxyServer' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['proxyServer'])
		if 'proxyBypassList' in kwargs:
			assert isinstance(kwargs['proxyBypassList'], (str,)
			    ), "Optional argument 'proxyBypassList' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['proxyBypassList'])
		expected = ['disposeOnDetach', 'proxyServer', 'proxyBypassList']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['disposeOnDetach', 'proxyServer', 'proxyBypassList']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.createBrowserContext', **
		    kwargs)
		return subdom_funcs

	def Target_getBrowserContexts(self):
		"""
		Function path: Target.getBrowserContexts
			Domain: Target
			Method name: getBrowserContexts
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'browserContextIds' (type: array) -> An array of browser context ids.
		
			Description: Returns all browser contexts created with `Target.createBrowserContext` method.
		"""
		subdom_funcs = self.synchronous_command('Target.getBrowserContexts')
		return subdom_funcs

	def Target_createTarget(self, url, **kwargs):
		"""
		Function path: Target.createTarget
			Domain: Target
			Method name: createTarget
		
			Parameters:
				Required arguments:
					'url' (type: string) -> The initial URL the page will be navigated to. An empty string indicates about:blank.
				Optional arguments:
					'width' (type: integer) -> Frame width in DIP (headless chrome only).
					'height' (type: integer) -> Frame height in DIP (headless chrome only).
					'browserContextId' (type: Browser.BrowserContextID) -> The browser context to create the page in.
					'enableBeginFrameControl' (type: boolean) -> Whether BeginFrames for this target will be controlled via DevTools (headless chrome only,
not supported on MacOS yet, false by default).
					'newWindow' (type: boolean) -> Whether to create a new Window or Tab (chrome-only, false by default).
					'background' (type: boolean) -> Whether to create the target in background or foreground (chrome-only,
false by default).
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
		if 'enableBeginFrameControl' in kwargs:
			assert isinstance(kwargs['enableBeginFrameControl'], (bool,)
			    ), "Optional argument 'enableBeginFrameControl' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['enableBeginFrameControl'])
		if 'newWindow' in kwargs:
			assert isinstance(kwargs['newWindow'], (bool,)
			    ), "Optional argument 'newWindow' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['newWindow'])
		if 'background' in kwargs:
			assert isinstance(kwargs['background'], (bool,)
			    ), "Optional argument 'background' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['background'])
		expected = ['width', 'height', 'browserContextId',
		    'enableBeginFrameControl', 'newWindow', 'background']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['width', 'height', 'browserContextId', 'enableBeginFrameControl', 'newWindow', 'background']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.createTarget', url=url,
		    **kwargs)
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

	def Target_disposeBrowserContext(self, browserContextId):
		"""
		Function path: Target.disposeBrowserContext
			Domain: Target
			Method name: disposeBrowserContext
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'browserContextId' (type: Browser.BrowserContextID) -> No description
			No return value.
		
			Description: Deletes a BrowserContext. All the belonging pages will be closed without calling their
beforeunload hooks.
		"""
		subdom_funcs = self.synchronous_command('Target.disposeBrowserContext',
		    browserContextId=browserContextId)
		return subdom_funcs

	def Target_getTargetInfo(self, **kwargs):
		"""
		Function path: Target.getTargetInfo
			Domain: Target
			Method name: getTargetInfo
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Optional arguments:
					'targetId' (type: TargetID) -> No description
			Returns:
				'targetInfo' (type: TargetInfo) -> No description
		
			Description: Returns information about a target.
		"""
		expected = ['targetId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['targetId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.getTargetInfo', **kwargs)
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
Consider using flat mode instead; see commands attachToTarget, setAutoAttach,
and crbug.com/991325.
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

	def Target_setAutoAttach(self, autoAttach, waitForDebuggerOnStart, **kwargs):
		"""
		Function path: Target.setAutoAttach
			Domain: Target
			Method name: setAutoAttach
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'autoAttach' (type: boolean) -> Whether to auto-attach to related targets.
					'waitForDebuggerOnStart' (type: boolean) -> Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger`
to run paused targets.
				Optional arguments:
					'flatten' (type: boolean) -> Enables "flat" access to the session via specifying sessionId attribute in the commands.
We plan to make this the default, deprecate non-flattened mode,
and eventually retire it. See crbug.com/991325.
			No return value.
		
			Description: Controls whether to automatically attach to new targets which are considered to be related to
this one. When turned on, attaches to all existing related targets as well. When turned off,
automatically detaches from all currently attached targets.
		"""
		assert isinstance(autoAttach, (bool,)
		    ), "Argument 'autoAttach' must be of type '['bool']'. Received type: '%s'" % type(
		    autoAttach)
		assert isinstance(waitForDebuggerOnStart, (bool,)
		    ), "Argument 'waitForDebuggerOnStart' must be of type '['bool']'. Received type: '%s'" % type(
		    waitForDebuggerOnStart)
		if 'flatten' in kwargs:
			assert isinstance(kwargs['flatten'], (bool,)
			    ), "Optional argument 'flatten' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['flatten'])
		expected = ['flatten']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['flatten']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Target.setAutoAttach',
		    autoAttach=autoAttach, waitForDebuggerOnStart=waitForDebuggerOnStart,
		    **kwargs)
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
		
			Description: Controls whether to discover available targets and notify via
`targetCreated/targetInfoChanged/targetDestroyed` events.
		"""
		assert isinstance(discover, (bool,)
		    ), "Argument 'discover' must be of type '['bool']'. Received type: '%s'" % type(
		    discover)
		subdom_funcs = self.synchronous_command('Target.setDiscoverTargets',
		    discover=discover)
		return subdom_funcs

	def Target_setRemoteLocations(self, locations):
		"""
		Function path: Target.setRemoteLocations
			Domain: Target
			Method name: setRemoteLocations
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'locations' (type: array) -> List of remote locations.
			No return value.
		
			Description: Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
`true`.
		"""
		assert isinstance(locations, (list, tuple)
		    ), "Argument 'locations' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    locations)
		subdom_funcs = self.synchronous_command('Target.setRemoteLocations',
		    locations=locations)
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

	def Tracing_requestMemoryDump(self, **kwargs):
		"""
		Function path: Tracing.requestMemoryDump
			Domain: Tracing
			Method name: requestMemoryDump
		
			Parameters:
				Optional arguments:
					'deterministic' (type: boolean) -> Enables more deterministic results by forcing garbage collection
					'levelOfDetail' (type: MemoryDumpLevelOfDetail) -> Specifies level of details in memory dump. Defaults to "detailed".
			Returns:
				'dumpGuid' (type: string) -> GUID of the resulting global memory dump.
				'success' (type: boolean) -> True iff the global memory dump succeeded.
		
			Description: Request a global memory dump.
		"""
		if 'deterministic' in kwargs:
			assert isinstance(kwargs['deterministic'], (bool,)
			    ), "Optional argument 'deterministic' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['deterministic'])
		expected = ['deterministic', 'levelOfDetail']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['deterministic', 'levelOfDetail']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Tracing.requestMemoryDump', **kwargs
		    )
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
					'transferMode' (type: string) -> Whether to report trace events as series of dataCollected events or to save trace to a
stream (defaults to `ReportEvents`).
					'streamFormat' (type: StreamFormat) -> Trace data format to use. This only applies when using `ReturnAsStream`
transfer mode (defaults to `json`).
					'streamCompression' (type: StreamCompression) -> Compression format to use. This only applies when using `ReturnAsStream`
transfer mode (defaults to `none`)
					'traceConfig' (type: TraceConfig) -> No description
					'perfettoConfig' (type: string) -> Base64-encoded serialized perfetto.protos.TraceConfig protobuf message
When specified, the parameters `categories`, `options`, `traceConfig`
are ignored. (Encoded as a base64 string when passed over JSON)
					'tracingBackend' (type: TracingBackend) -> Backend type (defaults to `auto`)
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
		if 'perfettoConfig' in kwargs:
			assert isinstance(kwargs['perfettoConfig'], (str,)
			    ), "Optional argument 'perfettoConfig' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['perfettoConfig'])
		expected = ['categories', 'options', 'bufferUsageReportingInterval',
		    'transferMode', 'streamFormat', 'streamCompression', 'traceConfig',
		    'perfettoConfig', 'tracingBackend']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['categories', 'options', 'bufferUsageReportingInterval', 'transferMode', 'streamFormat', 'streamCompression', 'traceConfig', 'perfettoConfig', 'tracingBackend']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Tracing.start', **kwargs)
		return subdom_funcs

	def Fetch_disable(self):
		"""
		Function path: Fetch.disable
			Domain: Fetch
			Method name: disable
		
			No return value.
		
			Description: Disables the fetch domain.
		"""
		subdom_funcs = self.synchronous_command('Fetch.disable')
		return subdom_funcs

	def Fetch_enable(self, **kwargs):
		"""
		Function path: Fetch.enable
			Domain: Fetch
			Method name: enable
		
			Parameters:
				Optional arguments:
					'patterns' (type: array) -> If specified, only requests matching any of these patterns will produce
fetchRequested event and will be paused until clients response. If not set,
all requests will be affected.
					'handleAuthRequests' (type: boolean) -> If true, authRequired events will be issued and requests will be paused
expecting a call to continueWithAuth.
			No return value.
		
			Description: Enables issuing of requestPaused events. A request will be paused until client
calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.
		"""
		if 'patterns' in kwargs:
			assert isinstance(kwargs['patterns'], (list, tuple)
			    ), "Optional argument 'patterns' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['patterns'])
		if 'handleAuthRequests' in kwargs:
			assert isinstance(kwargs['handleAuthRequests'], (bool,)
			    ), "Optional argument 'handleAuthRequests' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['handleAuthRequests'])
		expected = ['patterns', 'handleAuthRequests']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['patterns', 'handleAuthRequests']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Fetch.enable', **kwargs)
		return subdom_funcs

	def Fetch_failRequest(self, requestId, errorReason):
		"""
		Function path: Fetch.failRequest
			Domain: Fetch
			Method name: failRequest
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> An id the client received in requestPaused event.
					'errorReason' (type: Network.ErrorReason) -> Causes the request to fail with the given reason.
			No return value.
		
			Description: Causes the request to fail with specified reason.
		"""
		subdom_funcs = self.synchronous_command('Fetch.failRequest', requestId=
		    requestId, errorReason=errorReason)
		return subdom_funcs

	def Fetch_fulfillRequest(self, requestId, responseCode, **kwargs):
		"""
		Function path: Fetch.fulfillRequest
			Domain: Fetch
			Method name: fulfillRequest
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> An id the client received in requestPaused event.
					'responseCode' (type: integer) -> An HTTP response code.
				Optional arguments:
					'responseHeaders' (type: array) -> Response headers.
					'binaryResponseHeaders' (type: string) -> Alternative way of specifying response headers as a \\0-separated
series of name: value pairs. Prefer the above method unless you
need to represent some non-UTF8 values that can't be transmitted
over the protocol as text. (Encoded as a base64 string when passed over JSON)
					'body' (type: string) -> A response body. (Encoded as a base64 string when passed over JSON)
					'responsePhrase' (type: string) -> A textual representation of responseCode.
If absent, a standard phrase matching responseCode is used.
			No return value.
		
			Description: Provides response to the request.
		"""
		assert isinstance(responseCode, (int,)
		    ), "Argument 'responseCode' must be of type '['int']'. Received type: '%s'" % type(
		    responseCode)
		if 'responseHeaders' in kwargs:
			assert isinstance(kwargs['responseHeaders'], (list, tuple)
			    ), "Optional argument 'responseHeaders' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['responseHeaders'])
		if 'binaryResponseHeaders' in kwargs:
			assert isinstance(kwargs['binaryResponseHeaders'], (str,)
			    ), "Optional argument 'binaryResponseHeaders' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['binaryResponseHeaders'])
		if 'body' in kwargs:
			assert isinstance(kwargs['body'], (str,)
			    ), "Optional argument 'body' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['body'])
		if 'responsePhrase' in kwargs:
			assert isinstance(kwargs['responsePhrase'], (str,)
			    ), "Optional argument 'responsePhrase' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['responsePhrase'])
		expected = ['responseHeaders', 'binaryResponseHeaders', 'body',
		    'responsePhrase']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['responseHeaders', 'binaryResponseHeaders', 'body', 'responsePhrase']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Fetch.fulfillRequest', requestId
		    =requestId, responseCode=responseCode, **kwargs)
		return subdom_funcs

	def Fetch_continueRequest(self, requestId, **kwargs):
		"""
		Function path: Fetch.continueRequest
			Domain: Fetch
			Method name: continueRequest
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> An id the client received in requestPaused event.
				Optional arguments:
					'url' (type: string) -> If set, the request url will be modified in a way that's not observable by page.
					'method' (type: string) -> If set, the request method is overridden.
					'postData' (type: string) -> If set, overrides the post data in the request. (Encoded as a base64 string when passed over JSON)
					'headers' (type: array) -> If set, overrides the request headers.
			No return value.
		
			Description: Continues the request, optionally modifying some of its parameters.
		"""
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
		if 'headers' in kwargs:
			assert isinstance(kwargs['headers'], (list, tuple)
			    ), "Optional argument 'headers' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['headers'])
		expected = ['url', 'method', 'postData', 'headers']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['url', 'method', 'postData', 'headers']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Fetch.continueRequest',
		    requestId=requestId, **kwargs)
		return subdom_funcs

	def Fetch_continueWithAuth(self, requestId, authChallengeResponse):
		"""
		Function path: Fetch.continueWithAuth
			Domain: Fetch
			Method name: continueWithAuth
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> An id the client received in authRequired event.
					'authChallengeResponse' (type: AuthChallengeResponse) -> Response to  with an authChallenge.
			No return value.
		
			Description: Continues a request supplying authChallengeResponse following authRequired event.
		"""
		subdom_funcs = self.synchronous_command('Fetch.continueWithAuth',
		    requestId=requestId, authChallengeResponse=authChallengeResponse)
		return subdom_funcs

	def Fetch_getResponseBody(self, requestId):
		"""
		Function path: Fetch.getResponseBody
			Domain: Fetch
			Method name: getResponseBody
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> Identifier for the intercepted request to get body for.
			Returns:
				'body' (type: string) -> Response body.
				'base64Encoded' (type: boolean) -> True, if content was sent as base64.
		
			Description: Causes the body of the response to be received from the server and
returned as a single string. May only be issued for a request that
is paused in the Response stage and is mutually exclusive with
takeResponseBodyForInterceptionAsStream. Calling other methods that
affect the request or disabling fetch domain before body is received
results in an undefined behavior.
		"""
		subdom_funcs = self.synchronous_command('Fetch.getResponseBody',
		    requestId=requestId)
		return subdom_funcs

	def Fetch_takeResponseBodyAsStream(self, requestId):
		"""
		Function path: Fetch.takeResponseBodyAsStream
			Domain: Fetch
			Method name: takeResponseBodyAsStream
		
			Parameters:
				Required arguments:
					'requestId' (type: RequestId) -> No description
			Returns:
				'stream' (type: IO.StreamHandle) -> No description
		
			Description: Returns a handle to the stream representing the response body.
The request must be paused in the HeadersReceived stage.
Note that after this command the request can't be continued
as is -- client either needs to cancel it or to provide the
response body.
The stream only supports sequential read, IO.read will fail if the position
is specified.
This method is mutually exclusive with getResponseBody.
Calling other methods that affect the request or disabling fetch
domain before body is received results in an undefined behavior.
		"""
		subdom_funcs = self.synchronous_command('Fetch.takeResponseBodyAsStream',
		    requestId=requestId)
		return subdom_funcs

	def WebAudio_enable(self):
		"""
		Function path: WebAudio.enable
			Domain: WebAudio
			Method name: enable
		
			No return value.
		
			Description: Enables the WebAudio domain and starts sending context lifetime events.
		"""
		subdom_funcs = self.synchronous_command('WebAudio.enable')
		return subdom_funcs

	def WebAudio_disable(self):
		"""
		Function path: WebAudio.disable
			Domain: WebAudio
			Method name: disable
		
			No return value.
		
			Description: Disables the WebAudio domain.
		"""
		subdom_funcs = self.synchronous_command('WebAudio.disable')
		return subdom_funcs

	def WebAudio_getRealtimeData(self, contextId):
		"""
		Function path: WebAudio.getRealtimeData
			Domain: WebAudio
			Method name: getRealtimeData
		
			Parameters:
				Required arguments:
					'contextId' (type: GraphObjectId) -> No description
			Returns:
				'realtimeData' (type: ContextRealtimeData) -> No description
		
			Description: Fetch the realtime data from the registered contexts.
		"""
		subdom_funcs = self.synchronous_command('WebAudio.getRealtimeData',
		    contextId=contextId)
		return subdom_funcs

	def WebAuthn_enable(self):
		"""
		Function path: WebAuthn.enable
			Domain: WebAuthn
			Method name: enable
		
			No return value.
		
			Description: Enable the WebAuthn domain and start intercepting credential storage and
retrieval with a virtual authenticator.
		"""
		subdom_funcs = self.synchronous_command('WebAuthn.enable')
		return subdom_funcs

	def WebAuthn_disable(self):
		"""
		Function path: WebAuthn.disable
			Domain: WebAuthn
			Method name: disable
		
			No return value.
		
			Description: Disable the WebAuthn domain.
		"""
		subdom_funcs = self.synchronous_command('WebAuthn.disable')
		return subdom_funcs

	def WebAuthn_addVirtualAuthenticator(self, options):
		"""
		Function path: WebAuthn.addVirtualAuthenticator
			Domain: WebAuthn
			Method name: addVirtualAuthenticator
		
			Parameters:
				Required arguments:
					'options' (type: VirtualAuthenticatorOptions) -> No description
			Returns:
				'authenticatorId' (type: AuthenticatorId) -> No description
		
			Description: Creates and adds a virtual authenticator.
		"""
		subdom_funcs = self.synchronous_command('WebAuthn.addVirtualAuthenticator',
		    options=options)
		return subdom_funcs

	def WebAuthn_removeVirtualAuthenticator(self, authenticatorId):
		"""
		Function path: WebAuthn.removeVirtualAuthenticator
			Domain: WebAuthn
			Method name: removeVirtualAuthenticator
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
			No return value.
		
			Description: Removes the given authenticator.
		"""
		subdom_funcs = self.synchronous_command('WebAuthn.removeVirtualAuthenticator'
		    , authenticatorId=authenticatorId)
		return subdom_funcs

	def WebAuthn_addCredential(self, authenticatorId, credential):
		"""
		Function path: WebAuthn.addCredential
			Domain: WebAuthn
			Method name: addCredential
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
					'credential' (type: Credential) -> No description
			No return value.
		
			Description: Adds the credential to the specified authenticator.
		"""
		subdom_funcs = self.synchronous_command('WebAuthn.addCredential',
		    authenticatorId=authenticatorId, credential=credential)
		return subdom_funcs

	def WebAuthn_getCredential(self, authenticatorId, credentialId):
		"""
		Function path: WebAuthn.getCredential
			Domain: WebAuthn
			Method name: getCredential
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
					'credentialId' (type: string) -> No description
			Returns:
				'credential' (type: Credential) -> No description
		
			Description: Returns a single credential stored in the given virtual authenticator that
matches the credential ID.
		"""
		assert isinstance(credentialId, (str,)
		    ), "Argument 'credentialId' must be of type '['str']'. Received type: '%s'" % type(
		    credentialId)
		subdom_funcs = self.synchronous_command('WebAuthn.getCredential',
		    authenticatorId=authenticatorId, credentialId=credentialId)
		return subdom_funcs

	def WebAuthn_getCredentials(self, authenticatorId):
		"""
		Function path: WebAuthn.getCredentials
			Domain: WebAuthn
			Method name: getCredentials
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
			Returns:
				'credentials' (type: array) -> No description
		
			Description: Returns all the credentials stored in the given virtual authenticator.
		"""
		subdom_funcs = self.synchronous_command('WebAuthn.getCredentials',
		    authenticatorId=authenticatorId)
		return subdom_funcs

	def WebAuthn_removeCredential(self, authenticatorId, credentialId):
		"""
		Function path: WebAuthn.removeCredential
			Domain: WebAuthn
			Method name: removeCredential
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
					'credentialId' (type: string) -> No description
			No return value.
		
			Description: Removes a credential from the authenticator.
		"""
		assert isinstance(credentialId, (str,)
		    ), "Argument 'credentialId' must be of type '['str']'. Received type: '%s'" % type(
		    credentialId)
		subdom_funcs = self.synchronous_command('WebAuthn.removeCredential',
		    authenticatorId=authenticatorId, credentialId=credentialId)
		return subdom_funcs

	def WebAuthn_clearCredentials(self, authenticatorId):
		"""
		Function path: WebAuthn.clearCredentials
			Domain: WebAuthn
			Method name: clearCredentials
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
			No return value.
		
			Description: Clears all the credentials from the specified device.
		"""
		subdom_funcs = self.synchronous_command('WebAuthn.clearCredentials',
		    authenticatorId=authenticatorId)
		return subdom_funcs

	def WebAuthn_setUserVerified(self, authenticatorId, isUserVerified):
		"""
		Function path: WebAuthn.setUserVerified
			Domain: WebAuthn
			Method name: setUserVerified
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
					'isUserVerified' (type: boolean) -> No description
			No return value.
		
			Description: Sets whether User Verification succeeds or fails for an authenticator.
The default is true.
		"""
		assert isinstance(isUserVerified, (bool,)
		    ), "Argument 'isUserVerified' must be of type '['bool']'. Received type: '%s'" % type(
		    isUserVerified)
		subdom_funcs = self.synchronous_command('WebAuthn.setUserVerified',
		    authenticatorId=authenticatorId, isUserVerified=isUserVerified)
		return subdom_funcs

	def WebAuthn_setAutomaticPresenceSimulation(self, authenticatorId, enabled):
		"""
		Function path: WebAuthn.setAutomaticPresenceSimulation
			Domain: WebAuthn
			Method name: setAutomaticPresenceSimulation
		
			Parameters:
				Required arguments:
					'authenticatorId' (type: AuthenticatorId) -> No description
					'enabled' (type: boolean) -> No description
			No return value.
		
			Description: Sets whether tests of user presence will succeed immediately (if true) or fail to resolve (if false) for an authenticator.
The default is true.
		"""
		assert isinstance(enabled, (bool,)
		    ), "Argument 'enabled' must be of type '['bool']'. Received type: '%s'" % type(
		    enabled)
		subdom_funcs = self.synchronous_command(
		    'WebAuthn.setAutomaticPresenceSimulation', authenticatorId=
		    authenticatorId, enabled=enabled)
		return subdom_funcs

	def Media_enable(self):
		"""
		Function path: Media.enable
			Domain: Media
			Method name: enable
		
			No return value.
		
			Description: Enables the Media domain
		"""
		subdom_funcs = self.synchronous_command('Media.enable')
		return subdom_funcs

	def Media_disable(self):
		"""
		Function path: Media.disable
			Domain: Media
			Method name: disable
		
			No return value.
		
			Description: Disables the Media domain.
		"""
		subdom_funcs = self.synchronous_command('Media.disable')
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

	def Console_enable(self):
		"""
		Function path: Console.enable
			Domain: Console
			Method name: enable
		
			No return value.
		
			Description: Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.
		"""
		subdom_funcs = self.synchronous_command('Console.enable')
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

	def Debugger_enable(self, **kwargs):
		"""
		Function path: Debugger.enable
			Domain: Debugger
			Method name: enable
		
			Parameters:
				Optional arguments:
					'maxScriptsCacheSize' (type: number) -> The maximum size in bytes of collected scripts (not referenced by other heap objects)
the debugger can hold. Puts no limit if paramter is omitted.
			Returns:
				'debuggerId' (type: Runtime.UniqueDebuggerId) -> Unique identifier of the debugger.
		
			Description: Enables debugger for the given page. Clients should not assume that the debugging has been
enabled until the result for this command is received.
		"""
		if 'maxScriptsCacheSize' in kwargs:
			assert isinstance(kwargs['maxScriptsCacheSize'], (float, int)
			    ), "Optional argument 'maxScriptsCacheSize' must be of type '['float', 'int']'. Received type: '%s'" % type(
			    kwargs['maxScriptsCacheSize'])
		expected = ['maxScriptsCacheSize']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['maxScriptsCacheSize']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.enable', **kwargs)
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
					'objectGroup' (type: string) -> String object group name to put result into (allows rapid releasing resulting object handles
using `releaseObjectGroup`).
					'includeCommandLineAPI' (type: boolean) -> Specifies whether command line API should be available to the evaluated expression, defaults
to false.
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause
execution. Overrides `setPauseOnException` state.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object that should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'throwOnSideEffect' (type: boolean) -> Whether to throw an exception if side effect cannot be ruled out during evaluation.
					'timeout' (type: Runtime.TimeDelta) -> Terminate execution after timing out (number of milliseconds).
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
		    'returnByValue', 'generatePreview', 'throwOnSideEffect', 'timeout']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['objectGroup', 'includeCommandLineAPI', 'silent', 'returnByValue', 'generatePreview', 'throwOnSideEffect', 'timeout']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.evaluateOnCallFrame',
		    callFrameId=callFrameId, expression=expression, **kwargs)
		return subdom_funcs

	def Debugger_getPossibleBreakpoints(self, start, **kwargs):
		"""
		Function path: Debugger.getPossibleBreakpoints
			Domain: Debugger
			Method name: getPossibleBreakpoints
		
			Parameters:
				Required arguments:
					'start' (type: Location) -> Start of range to search possible breakpoint locations in.
				Optional arguments:
					'end' (type: Location) -> End of range to search possible breakpoint locations in (excluding). When not specified, end
of scripts is used as end of range.
					'restrictToFunction' (type: boolean) -> Only consider locations which are in the same (non-nested) function as start.
			Returns:
				'locations' (type: array) -> List of the possible breakpoint locations.
		
			Description: Returns possible locations for breakpoint. scriptId in start and end range locations should be
the same.
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

	def Debugger_getScriptSource(self, scriptId):
		"""
		Function path: Debugger.getScriptSource
			Domain: Debugger
			Method name: getScriptSource
		
			Parameters:
				Required arguments:
					'scriptId' (type: Runtime.ScriptId) -> Id of the script to get source for.
			Returns:
				'scriptSource' (type: string) -> Script source (empty in case of Wasm bytecode).
				'bytecode' (type: string) -> Wasm bytecode. (Encoded as a base64 string when passed over JSON)
		
			Description: Returns source for the script with given id.
		"""
		subdom_funcs = self.synchronous_command('Debugger.getScriptSource',
		    scriptId=scriptId)
		return subdom_funcs

	def Debugger_getWasmBytecode(self, scriptId):
		"""
		Function path: Debugger.getWasmBytecode
			Domain: Debugger
			Method name: getWasmBytecode
		
			Parameters:
				Required arguments:
					'scriptId' (type: Runtime.ScriptId) -> Id of the Wasm script to get source for.
			Returns:
				'bytecode' (type: string) -> Script source. (Encoded as a base64 string when passed over JSON)
		
			Description: This command is deprecated. Use getScriptSource instead.
		"""
		subdom_funcs = self.synchronous_command('Debugger.getWasmBytecode',
		    scriptId=scriptId)
		return subdom_funcs

	def Debugger_getStackTrace(self, stackTraceId):
		"""
		Function path: Debugger.getStackTrace
			Domain: Debugger
			Method name: getStackTrace
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'stackTraceId' (type: Runtime.StackTraceId) -> No description
			Returns:
				'stackTrace' (type: Runtime.StackTrace) -> No description
		
			Description: Returns stack trace with given `stackTraceId`.
		"""
		subdom_funcs = self.synchronous_command('Debugger.getStackTrace',
		    stackTraceId=stackTraceId)
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

	def Debugger_pauseOnAsyncCall(self, parentStackTraceId):
		"""
		Function path: Debugger.pauseOnAsyncCall
			Domain: Debugger
			Method name: pauseOnAsyncCall
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'parentStackTraceId' (type: Runtime.StackTraceId) -> Debugger will pause when async call with given stack trace is started.
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('Debugger.pauseOnAsyncCall',
		    parentStackTraceId=parentStackTraceId)
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
				'asyncStackTraceId' (type: Runtime.StackTraceId) -> Async stack trace, if any.
		
			Description: Restarts particular call frame from the beginning.
		"""
		subdom_funcs = self.synchronous_command('Debugger.restartFrame',
		    callFrameId=callFrameId)
		return subdom_funcs

	def Debugger_resume(self, **kwargs):
		"""
		Function path: Debugger.resume
			Domain: Debugger
			Method name: resume
		
			Parameters:
				Optional arguments:
					'terminateOnResume' (type: boolean) -> Set to true to terminate execution upon resuming execution. In contrast
to Runtime.terminateExecution, this will allows to execute further
JavaScript (i.e. via evaluation) until execution of the paused code
is actually resumed, at which point termination is triggered.
If execution is currently not paused, this parameter has no effect.
			No return value.
		
			Description: Resumes JavaScript execution.
		"""
		if 'terminateOnResume' in kwargs:
			assert isinstance(kwargs['terminateOnResume'], (bool,)
			    ), "Optional argument 'terminateOnResume' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['terminateOnResume'])
		expected = ['terminateOnResume']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['terminateOnResume']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.resume', **kwargs)
		return subdom_funcs

	def Debugger_searchInContent(self, scriptId, query, **kwargs):
		"""
		Function path: Debugger.searchInContent
			Domain: Debugger
			Method name: searchInContent
		
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

	def Debugger_setAsyncCallStackDepth(self, maxDepth):
		"""
		Function path: Debugger.setAsyncCallStackDepth
			Domain: Debugger
			Method name: setAsyncCallStackDepth
		
			Parameters:
				Required arguments:
					'maxDepth' (type: integer) -> Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async
call stacks (default).
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
		
			Description: Replace previous blackbox patterns with passed ones. Forces backend to skip stepping/pausing in
scripts with url matching one of the patterns. VM will try to leave blackboxed script by
performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
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
		
			Description: Makes backend skip steps in the script in blackboxed ranges. VM will try leave blacklisted
scripts by performing 'step in' several times, finally resorting to 'step out' if unsuccessful.
Positions array contains positions where blackbox state is changed. First interval isn't
blackboxed. Array should be sorted.
		"""
		assert isinstance(positions, (list, tuple)
		    ), "Argument 'positions' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
		    positions)
		subdom_funcs = self.synchronous_command('Debugger.setBlackboxedRanges',
		    scriptId=scriptId, positions=positions)
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
					'condition' (type: string) -> Expression to use as a breakpoint condition. When specified, debugger will only stop on the
breakpoint if this expression evaluates to true.
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

	def Debugger_setInstrumentationBreakpoint(self, instrumentation):
		"""
		Function path: Debugger.setInstrumentationBreakpoint
			Domain: Debugger
			Method name: setInstrumentationBreakpoint
		
			Parameters:
				Required arguments:
					'instrumentation' (type: string) -> Instrumentation name.
			Returns:
				'breakpointId' (type: BreakpointId) -> Id of the created breakpoint for further reference.
		
			Description: Sets instrumentation breakpoint.
		"""
		assert isinstance(instrumentation, (str,)
		    ), "Argument 'instrumentation' must be of type '['str']'. Received type: '%s'" % type(
		    instrumentation)
		subdom_funcs = self.synchronous_command(
		    'Debugger.setInstrumentationBreakpoint', instrumentation=instrumentation)
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
					'urlRegex' (type: string) -> Regex pattern for the URLs of the resources to set breakpoints on. Either `url` or
`urlRegex` must be specified.
					'scriptHash' (type: string) -> Script hash of the resources to set breakpoint on.
					'columnNumber' (type: integer) -> Offset in the line to set breakpoint at.
					'condition' (type: string) -> Expression to use as a breakpoint condition. When specified, debugger will only stop on the
breakpoint if this expression evaluates to true.
			Returns:
				'breakpointId' (type: BreakpointId) -> Id of the created breakpoint for further reference.
				'locations' (type: array) -> List of the locations this breakpoint resolved into upon addition.
		
			Description: Sets JavaScript breakpoint at given location specified either by URL or URL regex. Once this
command is issued, all existing parsed scripts will have breakpoints resolved and returned in
`locations` property. Further matching script parsing will result in subsequent
`breakpointResolved` events issued. This logical breakpoint will survive page reloads.
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
		if 'scriptHash' in kwargs:
			assert isinstance(kwargs['scriptHash'], (str,)
			    ), "Optional argument 'scriptHash' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['scriptHash'])
		if 'columnNumber' in kwargs:
			assert isinstance(kwargs['columnNumber'], (int,)
			    ), "Optional argument 'columnNumber' must be of type '['int']'. Received type: '%s'" % type(
			    kwargs['columnNumber'])
		if 'condition' in kwargs:
			assert isinstance(kwargs['condition'], (str,)
			    ), "Optional argument 'condition' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['condition'])
		expected = ['url', 'urlRegex', 'scriptHash', 'columnNumber', 'condition']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['url', 'urlRegex', 'scriptHash', 'columnNumber', 'condition']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.setBreakpointByUrl',
		    lineNumber=lineNumber, **kwargs)
		return subdom_funcs

	def Debugger_setBreakpointOnFunctionCall(self, objectId, **kwargs):
		"""
		Function path: Debugger.setBreakpointOnFunctionCall
			Domain: Debugger
			Method name: setBreakpointOnFunctionCall
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'objectId' (type: Runtime.RemoteObjectId) -> Function object id.
				Optional arguments:
					'condition' (type: string) -> Expression to use as a breakpoint condition. When specified, debugger will
stop on the breakpoint if this expression evaluates to true.
			Returns:
				'breakpointId' (type: BreakpointId) -> Id of the created breakpoint for further reference.
		
			Description: Sets JavaScript breakpoint before each call to the given function.
If another function was created from the same source as a given one,
calling it will also trigger the breakpoint.
		"""
		if 'condition' in kwargs:
			assert isinstance(kwargs['condition'], (str,)
			    ), "Optional argument 'condition' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['condition'])
		expected = ['condition']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['condition']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command(
		    'Debugger.setBreakpointOnFunctionCall', objectId=objectId, **kwargs)
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

	def Debugger_setPauseOnExceptions(self, state):
		"""
		Function path: Debugger.setPauseOnExceptions
			Domain: Debugger
			Method name: setPauseOnExceptions
		
			Parameters:
				Required arguments:
					'state' (type: string) -> Pause on exceptions mode.
			No return value.
		
			Description: Defines pause on exceptions state. Can be set to stop on all exceptions, uncaught exceptions or
no exceptions. Initial pause on exceptions state is `none`.
		"""
		assert isinstance(state, (str,)
		    ), "Argument 'state' must be of type '['str']'. Received type: '%s'" % type(
		    state)
		subdom_funcs = self.synchronous_command('Debugger.setPauseOnExceptions',
		    state=state)
		return subdom_funcs

	def Debugger_setReturnValue(self, newValue):
		"""
		Function path: Debugger.setReturnValue
			Domain: Debugger
			Method name: setReturnValue
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'newValue' (type: Runtime.CallArgument) -> New return value.
			No return value.
		
			Description: Changes return value in top frame. Available only at return break position.
		"""
		subdom_funcs = self.synchronous_command('Debugger.setReturnValue',
		    newValue=newValue)
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
					'dryRun' (type: boolean) -> If true the change will not actually be applied. Dry run may be used to get result
description without actually modifying the code.
			Returns:
				'callFrames' (type: array) -> New stack trace in case editing has happened while VM was stopped.
				'stackChanged' (type: boolean) -> Whether current call stack  was modified after applying the changes.
				'asyncStackTrace' (type: Runtime.StackTrace) -> Async stack trace, if any.
				'asyncStackTraceId' (type: Runtime.StackTraceId) -> Async stack trace, if any.
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

	def Debugger_setVariableValue(self, scopeNumber, variableName, newValue,
	    callFrameId):
		"""
		Function path: Debugger.setVariableValue
			Domain: Debugger
			Method name: setVariableValue
		
			Parameters:
				Required arguments:
					'scopeNumber' (type: integer) -> 0-based number of scope as was listed in scope chain. Only 'local', 'closure' and 'catch'
scope types are allowed. Other scopes could be manipulated manually.
					'variableName' (type: string) -> Variable name.
					'newValue' (type: Runtime.CallArgument) -> New variable value.
					'callFrameId' (type: CallFrameId) -> Id of callframe that holds variable.
			No return value.
		
			Description: Changes value of variable in a callframe. Object-based scopes are not supported and must be
mutated manually.
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

	def Debugger_stepInto(self, **kwargs):
		"""
		Function path: Debugger.stepInto
			Domain: Debugger
			Method name: stepInto
		
			Parameters:
				Optional arguments:
					'breakOnAsyncCall' (type: boolean) -> Debugger will pause on the execution of the first async task which was scheduled
before next pause.
					'skipList' (type: array) -> The skipList specifies location ranges that should be skipped on step into.
			No return value.
		
			Description: Steps into the function call.
		"""
		if 'breakOnAsyncCall' in kwargs:
			assert isinstance(kwargs['breakOnAsyncCall'], (bool,)
			    ), "Optional argument 'breakOnAsyncCall' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['breakOnAsyncCall'])
		if 'skipList' in kwargs:
			assert isinstance(kwargs['skipList'], (list, tuple)
			    ), "Optional argument 'skipList' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['skipList'])
		expected = ['breakOnAsyncCall', 'skipList']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['breakOnAsyncCall', 'skipList']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.stepInto', **kwargs)
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

	def Debugger_stepOver(self, **kwargs):
		"""
		Function path: Debugger.stepOver
			Domain: Debugger
			Method name: stepOver
		
			Parameters:
				Optional arguments:
					'skipList' (type: array) -> The skipList specifies location ranges that should be skipped on step over.
			No return value.
		
			Description: Steps over the statement.
		"""
		if 'skipList' in kwargs:
			assert isinstance(kwargs['skipList'], (list, tuple)
			    ), "Optional argument 'skipList' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
			    kwargs['skipList'])
		expected = ['skipList']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['skipList']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Debugger.stepOver', **kwargs)
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
		
			Description: Enables console to refer to the node with given id via $x (see Command Line API for more details
$x functions).
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.addInspectedHeapObject'
		    , heapObjectId=heapObjectId)
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

	def HeapProfiler_disable(self):
		"""
		Function path: HeapProfiler.disable
			Domain: HeapProfiler
			Method name: disable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.disable')
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

	def HeapProfiler_getSamplingProfile(self):
		"""
		Function path: HeapProfiler.getSamplingProfile
			Domain: HeapProfiler
			Method name: getSamplingProfile
		
			Returns:
				'profile' (type: SamplingHeapProfile) -> Return the sampling profile being collected.
		
		"""
		subdom_funcs = self.synchronous_command('HeapProfiler.getSamplingProfile')
		return subdom_funcs

	def HeapProfiler_startSampling(self, **kwargs):
		"""
		Function path: HeapProfiler.startSampling
			Domain: HeapProfiler
			Method name: startSampling
		
			Parameters:
				Optional arguments:
					'samplingInterval' (type: number) -> Average sample interval in bytes. Poisson distribution is used for the intervals. The
default value is 32768 bytes.
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

	def HeapProfiler_stopTrackingHeapObjects(self, **kwargs):
		"""
		Function path: HeapProfiler.stopTrackingHeapObjects
			Domain: HeapProfiler
			Method name: stopTrackingHeapObjects
		
			Parameters:
				Optional arguments:
					'reportProgress' (type: boolean) -> If true 'reportHeapSnapshotProgress' events will be generated while snapshot is being taken
when the tracking is stopped.
					'treatGlobalObjectsAsRoots' (type: boolean) -> No description
			No return value.
		
		"""
		if 'reportProgress' in kwargs:
			assert isinstance(kwargs['reportProgress'], (bool,)
			    ), "Optional argument 'reportProgress' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['reportProgress'])
		if 'treatGlobalObjectsAsRoots' in kwargs:
			assert isinstance(kwargs['treatGlobalObjectsAsRoots'], (bool,)
			    ), "Optional argument 'treatGlobalObjectsAsRoots' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['treatGlobalObjectsAsRoots'])
		expected = ['reportProgress', 'treatGlobalObjectsAsRoots']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['reportProgress', 'treatGlobalObjectsAsRoots']. Passed kwargs: %s" % passed_keys
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
					'treatGlobalObjectsAsRoots' (type: boolean) -> If true, a raw snapshot without artifical roots will be generated
			No return value.
		
		"""
		if 'reportProgress' in kwargs:
			assert isinstance(kwargs['reportProgress'], (bool,)
			    ), "Optional argument 'reportProgress' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['reportProgress'])
		if 'treatGlobalObjectsAsRoots' in kwargs:
			assert isinstance(kwargs['treatGlobalObjectsAsRoots'], (bool,)
			    ), "Optional argument 'treatGlobalObjectsAsRoots' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['treatGlobalObjectsAsRoots'])
		expected = ['reportProgress', 'treatGlobalObjectsAsRoots']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['reportProgress', 'treatGlobalObjectsAsRoots']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('HeapProfiler.takeHeapSnapshot',
		    **kwargs)
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

	def Profiler_enable(self):
		"""
		Function path: Profiler.enable
			Domain: Profiler
			Method name: enable
		
			No return value.
		
		"""
		subdom_funcs = self.synchronous_command('Profiler.enable')
		return subdom_funcs

	def Profiler_getBestEffortCoverage(self):
		"""
		Function path: Profiler.getBestEffortCoverage
			Domain: Profiler
			Method name: getBestEffortCoverage
		
			Returns:
				'result' (type: array) -> Coverage data for the current isolate.
		
			Description: Collect coverage data for the current isolate. The coverage data may be incomplete due to
garbage collection.
		"""
		subdom_funcs = self.synchronous_command('Profiler.getBestEffortCoverage')
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

	def Profiler_startPreciseCoverage(self, **kwargs):
		"""
		Function path: Profiler.startPreciseCoverage
			Domain: Profiler
			Method name: startPreciseCoverage
		
			Parameters:
				Optional arguments:
					'callCount' (type: boolean) -> Collect accurate call counts beyond simple 'covered' or 'not covered'.
					'detailed' (type: boolean) -> Collect block-based coverage.
					'allowTriggeredUpdates' (type: boolean) -> Allow the backend to send updates on its own initiative
			Returns:
				'timestamp' (type: number) -> Monotonically increasing time (in seconds) when the coverage update was taken in the backend.
		
			Description: Enable precise code coverage. Coverage data for JavaScript executed before enabling precise code
coverage may be incomplete. Enabling prevents running optimized code and resets execution
counters.
		"""
		if 'callCount' in kwargs:
			assert isinstance(kwargs['callCount'], (bool,)
			    ), "Optional argument 'callCount' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['callCount'])
		if 'detailed' in kwargs:
			assert isinstance(kwargs['detailed'], (bool,)
			    ), "Optional argument 'detailed' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['detailed'])
		if 'allowTriggeredUpdates' in kwargs:
			assert isinstance(kwargs['allowTriggeredUpdates'], (bool,)
			    ), "Optional argument 'allowTriggeredUpdates' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['allowTriggeredUpdates'])
		expected = ['callCount', 'detailed', 'allowTriggeredUpdates']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['callCount', 'detailed', 'allowTriggeredUpdates']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Profiler.startPreciseCoverage',
		    **kwargs)
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

	def Profiler_stopPreciseCoverage(self):
		"""
		Function path: Profiler.stopPreciseCoverage
			Domain: Profiler
			Method name: stopPreciseCoverage
		
			No return value.
		
			Description: Disable precise code coverage. Disabling releases unnecessary execution count records and allows
executing optimized code.
		"""
		subdom_funcs = self.synchronous_command('Profiler.stopPreciseCoverage')
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

	def Profiler_takePreciseCoverage(self):
		"""
		Function path: Profiler.takePreciseCoverage
			Domain: Profiler
			Method name: takePreciseCoverage
		
			Returns:
				'result' (type: array) -> Coverage data for the current isolate.
				'timestamp' (type: number) -> Monotonically increasing time (in seconds) when the coverage update was taken in the backend.
		
			Description: Collect coverage data for the current isolate, and resets execution counters. Precise code
coverage needs to have started.
		"""
		subdom_funcs = self.synchronous_command('Profiler.takePreciseCoverage')
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

	def Profiler_enableCounters(self):
		"""
		Function path: Profiler.enableCounters
			Domain: Profiler
			Method name: enableCounters
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Enable counters collection.
		"""
		subdom_funcs = self.synchronous_command('Profiler.enableCounters')
		return subdom_funcs

	def Profiler_disableCounters(self):
		"""
		Function path: Profiler.disableCounters
			Domain: Profiler
			Method name: disableCounters
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Disable counters collection.
		"""
		subdom_funcs = self.synchronous_command('Profiler.disableCounters')
		return subdom_funcs

	def Profiler_getCounters(self):
		"""
		Function path: Profiler.getCounters
			Domain: Profiler
			Method name: getCounters
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'result' (type: array) -> Collected counters information.
		
			Description: Retrieve counters.
		"""
		subdom_funcs = self.synchronous_command('Profiler.getCounters')
		return subdom_funcs

	def Profiler_enableRuntimeCallStats(self):
		"""
		Function path: Profiler.enableRuntimeCallStats
			Domain: Profiler
			Method name: enableRuntimeCallStats
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Enable run time call stats collection.
		"""
		subdom_funcs = self.synchronous_command('Profiler.enableRuntimeCallStats')
		return subdom_funcs

	def Profiler_disableRuntimeCallStats(self):
		"""
		Function path: Profiler.disableRuntimeCallStats
			Domain: Profiler
			Method name: disableRuntimeCallStats
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Disable run time call stats collection.
		"""
		subdom_funcs = self.synchronous_command('Profiler.disableRuntimeCallStats')
		return subdom_funcs

	def Profiler_getRuntimeCallStats(self):
		"""
		Function path: Profiler.getRuntimeCallStats
			Domain: Profiler
			Method name: getRuntimeCallStats
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'result' (type: array) -> Collected runtime call counter information.
		
			Description: Retrieve run time call stats.
		"""
		subdom_funcs = self.synchronous_command('Profiler.getRuntimeCallStats')
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
					'objectId' (type: RemoteObjectId) -> Identifier of the object to call function on. Either objectId or executionContextId should
be specified.
					'arguments' (type: array) -> Call arguments. All call arguments must belong to the same JavaScript world as the target
object.
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause
execution. Overrides `setPauseOnException` state.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object which should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'userGesture' (type: boolean) -> Whether execution should be treated as initiated by user in the UI.
					'awaitPromise' (type: boolean) -> Whether execution should `await` for resulting value and return once awaited promise is
resolved.
					'executionContextId' (type: ExecutionContextId) -> Specifies execution context which global object will be used to call function on. Either
executionContextId or objectId should be specified.
					'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects. If objectGroup is not
specified and objectId is, objectGroup will be inherited from object.
			Returns:
				'result' (type: RemoteObject) -> Call result.
				'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		
			Description: Calls function with given declaration on the given object. Object group of the result is
inherited from the target object.
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
					'executionContextId' (type: ExecutionContextId) -> Specifies in which execution context to perform script run. If the parameter is omitted the
evaluation will be performed in the context of the inspected page.
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

	def Runtime_enable(self):
		"""
		Function path: Runtime.enable
			Domain: Runtime
			Method name: enable
		
			No return value.
		
			Description: Enables reporting of execution contexts creation by means of `executionContextCreated` event.
When the reporting gets enabled the event will be sent immediately for each existing execution
context.
		"""
		subdom_funcs = self.synchronous_command('Runtime.enable')
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
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause
execution. Overrides `setPauseOnException` state.
					'contextId' (type: ExecutionContextId) -> Specifies in which execution context to perform evaluation. If the parameter is omitted the
evaluation will be performed in the context of the inspected page.
This is mutually exclusive with `uniqueContextId`, which offers an
alternative way to identify the execution context that is more reliable
in a multi-process environment.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object that should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'userGesture' (type: boolean) -> Whether execution should be treated as initiated by user in the UI.
					'awaitPromise' (type: boolean) -> Whether execution should `await` for resulting value and return once awaited promise is
resolved.
					'throwOnSideEffect' (type: boolean) -> Whether to throw an exception if side effect cannot be ruled out during evaluation.
This implies `disableBreaks` below.
					'timeout' (type: TimeDelta) -> Terminate execution after timing out (number of milliseconds).
					'disableBreaks' (type: boolean) -> Disable breakpoints during execution.
					'replMode' (type: boolean) -> Setting this flag to true enables `let` re-declaration and top-level `await`.
Note that `let` variables can only be re-declared if they originate from
`replMode` themselves.
					'allowUnsafeEvalBlockedByCSP' (type: boolean) -> The Content Security Policy (CSP) for the target might block 'unsafe-eval'
which includes eval(), Function(), setTimeout() and setInterval()
when called with non-callable arguments. This flag bypasses CSP for this
evaluation and allows unsafe-eval. Defaults to true.
					'uniqueContextId' (type: string) -> An alternative way to specify the execution context to evaluate in.
Compared to contextId that may be reused accross processes, this is guaranteed to be
system-unique, so it can be used to prevent accidental evaluation of the expression
in context different than intended (e.g. as a result of navigation accross process
boundaries).
This is mutually exclusive with `contextId`.
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
		if 'throwOnSideEffect' in kwargs:
			assert isinstance(kwargs['throwOnSideEffect'], (bool,)
			    ), "Optional argument 'throwOnSideEffect' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['throwOnSideEffect'])
		if 'disableBreaks' in kwargs:
			assert isinstance(kwargs['disableBreaks'], (bool,)
			    ), "Optional argument 'disableBreaks' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['disableBreaks'])
		if 'replMode' in kwargs:
			assert isinstance(kwargs['replMode'], (bool,)
			    ), "Optional argument 'replMode' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['replMode'])
		if 'allowUnsafeEvalBlockedByCSP' in kwargs:
			assert isinstance(kwargs['allowUnsafeEvalBlockedByCSP'], (bool,)
			    ), "Optional argument 'allowUnsafeEvalBlockedByCSP' must be of type '['bool']'. Received type: '%s'" % type(
			    kwargs['allowUnsafeEvalBlockedByCSP'])
		if 'uniqueContextId' in kwargs:
			assert isinstance(kwargs['uniqueContextId'], (str,)
			    ), "Optional argument 'uniqueContextId' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['uniqueContextId'])
		expected = ['objectGroup', 'includeCommandLineAPI', 'silent', 'contextId',
		    'returnByValue', 'generatePreview', 'userGesture', 'awaitPromise',
		    'throwOnSideEffect', 'timeout', 'disableBreaks', 'replMode',
		    'allowUnsafeEvalBlockedByCSP', 'uniqueContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['objectGroup', 'includeCommandLineAPI', 'silent', 'contextId', 'returnByValue', 'generatePreview', 'userGesture', 'awaitPromise', 'throwOnSideEffect', 'timeout', 'disableBreaks', 'replMode', 'allowUnsafeEvalBlockedByCSP', 'uniqueContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.evaluate', expression=
		    expression, **kwargs)
		return subdom_funcs

	def Runtime_getIsolateId(self):
		"""
		Function path: Runtime.getIsolateId
			Domain: Runtime
			Method name: getIsolateId
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'id' (type: string) -> The isolate id.
		
			Description: Returns the isolate id.
		"""
		subdom_funcs = self.synchronous_command('Runtime.getIsolateId')
		return subdom_funcs

	def Runtime_getHeapUsage(self):
		"""
		Function path: Runtime.getHeapUsage
			Domain: Runtime
			Method name: getHeapUsage
		
			WARNING: This function is marked 'Experimental'!
		
			Returns:
				'usedSize' (type: number) -> Used heap size in bytes.
				'totalSize' (type: number) -> Allocated heap size in bytes.
		
			Description: Returns the JavaScript heap usage.
It is the total usage of the corresponding isolate not scoped to a particular Runtime.
		"""
		subdom_funcs = self.synchronous_command('Runtime.getHeapUsage')
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
					'ownProperties' (type: boolean) -> If true, returns properties belonging only to the element itself, not to its prototype
chain.
					'accessorPropertiesOnly' (type: boolean) -> If true, returns accessor properties (with getter/setter) only; internal properties are not
returned either.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the results.
			Returns:
				'result' (type: array) -> Object properties.
				'internalProperties' (type: array) -> Internal object properties (only of the element itself).
				'privateProperties' (type: array) -> Object private properties.
				'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		
			Description: Returns properties of a given object. Object group of the result is inherited from the target
object.
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

	def Runtime_globalLexicalScopeNames(self, **kwargs):
		"""
		Function path: Runtime.globalLexicalScopeNames
			Domain: Runtime
			Method name: globalLexicalScopeNames
		
			Parameters:
				Optional arguments:
					'executionContextId' (type: ExecutionContextId) -> Specifies in which execution context to lookup global scope variables.
			Returns:
				'names' (type: array) -> No description
		
			Description: Returns all let, const and class variables from global scope.
		"""
		expected = ['executionContextId']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['executionContextId']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.globalLexicalScopeNames',
		    **kwargs)
		return subdom_funcs

	def Runtime_queryObjects(self, prototypeObjectId, **kwargs):
		"""
		Function path: Runtime.queryObjects
			Domain: Runtime
			Method name: queryObjects
		
			Parameters:
				Required arguments:
					'prototypeObjectId' (type: RemoteObjectId) -> Identifier of the prototype to return objects for.
				Optional arguments:
					'objectGroup' (type: string) -> Symbolic group name that can be used to release the results.
			Returns:
				'objects' (type: RemoteObject) -> Array with objects.
		
		"""
		if 'objectGroup' in kwargs:
			assert isinstance(kwargs['objectGroup'], (str,)
			    ), "Optional argument 'objectGroup' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['objectGroup'])
		expected = ['objectGroup']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['objectGroup']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.queryObjects',
		    prototypeObjectId=prototypeObjectId, **kwargs)
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

	def Runtime_runScript(self, scriptId, **kwargs):
		"""
		Function path: Runtime.runScript
			Domain: Runtime
			Method name: runScript
		
			Parameters:
				Required arguments:
					'scriptId' (type: ScriptId) -> Id of the script to run.
				Optional arguments:
					'executionContextId' (type: ExecutionContextId) -> Specifies in which execution context to perform script run. If the parameter is omitted the
evaluation will be performed in the context of the inspected page.
					'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects.
					'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause
execution. Overrides `setPauseOnException` state.
					'includeCommandLineAPI' (type: boolean) -> Determines whether Command Line API should be available during the evaluation.
					'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object which should be sent by value.
					'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
					'awaitPromise' (type: boolean) -> Whether execution should `await` for resulting value and return once awaited promise is
resolved.
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

	def Runtime_setAsyncCallStackDepth(self, maxDepth):
		"""
		Function path: Runtime.setAsyncCallStackDepth
			Domain: Runtime
			Method name: setAsyncCallStackDepth
		
			Parameters:
				Required arguments:
					'maxDepth' (type: integer) -> Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async
call stacks (default).
			No return value.
		
			Description: Enables or disables async call stacks tracking.
		"""
		assert isinstance(maxDepth, (int,)
		    ), "Argument 'maxDepth' must be of type '['int']'. Received type: '%s'" % type(
		    maxDepth)
		subdom_funcs = self.synchronous_command('Runtime.setAsyncCallStackDepth',
		    maxDepth=maxDepth)
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

	def Runtime_setMaxCallStackSizeToCapture(self, size):
		"""
		Function path: Runtime.setMaxCallStackSizeToCapture
			Domain: Runtime
			Method name: setMaxCallStackSizeToCapture
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'size' (type: integer) -> No description
			No return value.
		
		"""
		assert isinstance(size, (int,)
		    ), "Argument 'size' must be of type '['int']'. Received type: '%s'" % type(
		    size)
		subdom_funcs = self.synchronous_command(
		    'Runtime.setMaxCallStackSizeToCapture', size=size)
		return subdom_funcs

	def Runtime_terminateExecution(self):
		"""
		Function path: Runtime.terminateExecution
			Domain: Runtime
			Method name: terminateExecution
		
			WARNING: This function is marked 'Experimental'!
		
			No return value.
		
			Description: Terminate current or next JavaScript execution.
Will cancel the termination when the outer-most script execution ends.
		"""
		subdom_funcs = self.synchronous_command('Runtime.terminateExecution')
		return subdom_funcs

	def Runtime_addBinding(self, name, **kwargs):
		"""
		Function path: Runtime.addBinding
			Domain: Runtime
			Method name: addBinding
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'name' (type: string) -> No description
				Optional arguments:
					'executionContextId' (type: ExecutionContextId) -> If specified, the binding would only be exposed to the specified
execution context. If omitted and `executionContextName` is not set,
the binding is exposed to all execution contexts of the target.
This parameter is mutually exclusive with `executionContextName`.
					'executionContextName' (type: string) -> If specified, the binding is exposed to the executionContext with
matching name, even for contexts created after the binding is added.
See also `ExecutionContext.name` and `worldName` parameter to
`Page.addScriptToEvaluateOnNewDocument`.
This parameter is mutually exclusive with `executionContextId`.
			No return value.
		
			Description: If executionContextId is empty, adds binding with the given name on the
global objects of all inspected contexts, including those created later,
bindings survive reloads.
Binding function takes exactly one argument, this argument should be string,
in case of any other input, function throws an exception.
Each binding function call produces Runtime.bindingCalled notification.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		if 'executionContextName' in kwargs:
			assert isinstance(kwargs['executionContextName'], (str,)
			    ), "Optional argument 'executionContextName' must be of type '['str']'. Received type: '%s'" % type(
			    kwargs['executionContextName'])
		expected = ['executionContextId', 'executionContextName']
		passed_keys = list(kwargs.keys())
		assert all([(key in expected) for key in passed_keys]
		    ), "Allowed kwargs are ['executionContextId', 'executionContextName']. Passed kwargs: %s" % passed_keys
		subdom_funcs = self.synchronous_command('Runtime.addBinding', name=name,
		    **kwargs)
		return subdom_funcs

	def Runtime_removeBinding(self, name):
		"""
		Function path: Runtime.removeBinding
			Domain: Runtime
			Method name: removeBinding
		
			WARNING: This function is marked 'Experimental'!
		
			Parameters:
				Required arguments:
					'name' (type: string) -> No description
			No return value.
		
			Description: This method does not remove binding function from global object but
unsubscribes current runtime agent from Runtime.bindingCalled notifications.
		"""
		assert isinstance(name, (str,)
		    ), "Argument 'name' must be of type '['str']'. Received type: '%s'" % type(
		    name)
		subdom_funcs = self.synchronous_command('Runtime.removeBinding', name=name)
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
