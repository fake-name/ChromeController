

def capture_loading_events(message):
	if not message:
		return False
	if "method" not in message:
		return False
	if message['method'] != 'Network.requestWillBeSent':
		return False
	if 'params' not in message:
		return False
	mparams = message['params']
	if 'type' not in mparams:
		return False
	if 'requestId' not in mparams:
		return False
	if 'documentURL' not in mparams:
		return False
	if mparams['type'] == 'Document':
		# pprint.pprint(message['params'])
		return True
	return False



def check_frame_navigated_command(expected_id):
	def check_frame_navigated(message):
		if not message:
			return False
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
	return check_frame_navigated

def check_frame_load_command(method_name):
	def frame_loading_tracker(message):
		if not message:
			return False
		if "method" not in message:
			return False
		if message['method'] != method_name:
			return False
		if 'params' not in message:
			return False
		return True

		# Disabled. See https://bugs.chromium.org/p/chromedriver/issues/detail?id=1387
		# params = message['params']
		# if 'frameId' not in params:
		# 	return False
		# if 'frameId' in params:
		# 	ret = params['frameId'] == expected_id
		# 	# print("frame_loading_tracker", message)
		# return False

	return frame_loading_tracker



def wait_for_methods(method_list):
	def wait_for_methods_tracker(message):
		if not message:
			return False
		if "method" not in message:
			return False
		if message['method'] not in method_list:
			return False
		if 'params' not in message:
			return False
		return True

	return wait_for_methods_tracker



def check_frame_loader_command(method_name, loader_id):
	def frame_loading_tracker_with_loader(message):
		if not message:
			return False
		if "method" not in message:
			return False
		if message['method'] != method_name:
			return False
		if 'params' not in message:
			return False
		if 'loaderId' not in message['params']:
			return False
		if message['params']["loaderId"] == loader_id:
			return True

		return False


	return frame_loading_tracker_with_loader

def check_load_event_fired(message):
	if not message:
		return False
	if "method" not in message:
		return False
	if message['method'] == 'Page.loadEventFired':
		# print("check_load_event_fired", message)
		return True
	return False


def network_response_recieved_for_url(url, expected_id):
	def network_response_recieved_tracker(message):
		if not message:
			return False
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
				# Checking the url in the response breaks if
				# the remote issues a 301 or 302.
				if url:
					response = params['response']
					if 'url' in response:
						return url == response['url']
				else:
					return True

		return False
	return network_response_recieved_tracker
