
import distutils.spawn
import os.path
import subprocess
import pprint
import base64
import signal
import time
import requests.exceptions

from .Generator import gen

CromeRemoteDebugInterfaceBase = gen.get_class_def()

class CromeRemoteDebugInterface(CromeRemoteDebugInterfaceBase):
	pass
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		resp1 = self.synchronous_command("Page.enable", {})
		resp2 = self.synchronous_command("DOM.enable", {})
		# resp3 = self.synchronous_command("Network.enable", {})

		print(resp1)
		print(resp2)
		# print(resp3)


	def set_viewport_size(self, x_pix, y_pix):
		ret = self.synchronous_command("Emulation.setVisibleSize", {"width": int(x_pix), "height": int(y_pix)})
		# Command has an empty return
		return ret


	def take_screeshot(self):
		resp = self.transport.synchronous_command("Page.captureScreenshot", {})
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
		ret = self.synchronous_command("Page.navigate", {"url": "http://www.google.com"})
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
