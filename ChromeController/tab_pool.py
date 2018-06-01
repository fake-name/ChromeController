
import logging
import urllib.parse
import contextlib

import cachetools


from ChromeController.manager import ChromeRemoteDebugInterface


class TabStore(cachetools.LRUCache):
	def __init__(self, chrome_interface, *args, **kwargs):
		assert "maxsize" in kwargs
		assert kwargs['maxsize']
		super().__init__(*args, **kwargs)
		assert self.maxsize

		self.chrome_interface = chrome_interface
		self.log = logging.getLogger("Main.ChromeController.TabPool.Store")

	def __getitem__(self, nl):
		self.log.debug("__getitem__: %s", nl)
		assert nl is not None, "You have to pass a key to __getitem__!"
		key = hash(nl) % self.maxsize
		return super().__getitem__(key)

	def __missing__(self, key):
		self.log.debug("__missing__: %s", key)
		assert key is not None, "You have to pass a key to __missing__!"
		self[key] = self.chrome_interface.new_tab()
		return self[key]


	def popitem(self):
		key, value = super().popitem()
		print('Key "%s" evicted with value "%s"' % (key, value))
		return key, value

class TabPooledChromium(object):

	def __init__(self, *args, tab_pool_max_size = None, **kwargs):
		if tab_pool_max_size is None:
			tab_pool_max_size = 5

		self.chrome_interface = ChromeRemoteDebugInterface(*args, **kwargs)
		self.tab_pool_max_size = tab_pool_max_size

		self.log = logging.getLogger("Main.ChromeController.TabPool")

		self.tab_cache = TabStore(maxsize=tab_pool_max_size, chrome_interface=self.chrome_interface)


	@contextlib.contextmanager
	def tab(self, netloc=None, url=None):
		assert netloc or url
		if not netloc:
			netloc = urllib.parse.urlparse(url).netloc
			self.log.debug("Getting tab for netloc: %s (url: %s)", netloc, url)

		yield self.tab_cache[netloc]
