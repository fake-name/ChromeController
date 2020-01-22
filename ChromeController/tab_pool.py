
import logging
import urllib.parse
import os
import contextlib

import cachetools
import threading


from ChromeController.manager import ChromeRemoteDebugInterface


class _TabStore(cachetools.LRUCache):
	def __init__(self, chrome_interface, *args, **kwargs):
		assert "maxsize" in kwargs
		assert kwargs['maxsize']
		super().__init__(*args, **kwargs)
		assert self.maxsize

		self.chrome_interface = chrome_interface
		self.log = logging.getLogger("Main.ChromeController.TabPool.Store")

	def __getitem__(self, key):
		self.log.debug("__getitem__: %s", key)
		assert key is not None, "You have to pass a key to __getitem__!"
		return super().__getitem__(key)

	def __missing__(self, key):
		self.log.debug("__missing__: %s", key)
		assert key is not None, "You have to pass a key to __missing__!"
		self[key] = (threading.Lock(), self.chrome_interface.new_tab())
		return self[key]

	def popitem(self):
		key, value = super().popitem()
		self.log.debug('Key "%s" evicted with value "%s"', key, value)
		dummy_lock, tab = value
		tab.close()
		return None

	def tab_count(self):
		return len(self)


class TabPooledChromium(object):

	def __init__(self, *args, tab_pool_max_size = None, **kwargs):
		'''
		Create a chromium tab pool instance.

		This will start a chromium instance, from which new tabs will be created as
		needed with the tab() context manager.

		Note that the destruction of the `TabPooledChromium` object will kill the associated chromium
		execution. This will render any checked-out tabs invalid (though saving the tabs considering
		they're constructed in a context-manager is pretty obviously wrong anyways).
		'''
		if tab_pool_max_size is None:
			tab_pool_max_size = 10

		self.alive = True

		self.chrome_interface = ChromeRemoteDebugInterface(*args, **kwargs)

		# We hold a tab open to prevent chrome from closing
		# when all user tabs are closed.
		self.root_tab = self.chrome_interface.new_tab()

		self.tab_pool_max_size = tab_pool_max_size

		self.log = logging.getLogger("Main.ChromeController.TabPool")

		# We pass a tab to the tabstore, because otherwise it might wind up evicting the root tab,
		# which would take the entire chrome instance down with it when it's closed.
		self.__tab_cache = _TabStore(maxsize=tab_pool_max_size, chrome_interface=self.chrome_interface)

		self.__counter_lock = threading.Lock()
		self.__active_tabs = {}

		self.__started_pid = os.getpid()


	def close(self):
		if self.alive:
			self.root_tab.close()
			self.chrome_interface.close()
			self.alive = False

	def __del__(self):
		self.close()
		try:
			self.chrome_interface.close()
		except Exception:
			pass

	def close_tabs(self):
		'''
		Close all open tabs (but the management tab).

		If some of the tabs are being used, this may cause errors
		'''
		with self.__counter_lock:
			while self.__tab_cache.tab_count():
				self.__tab_cache.popitem()

	def active_tabs(self):
		'''
		Return the number of currently active tabs.
		'''

		return self.__tab_cache.tab_count()


	@contextlib.contextmanager
	def tab(self, netloc=None, url=None, extra_id=None, use_tid=False):
		'''
		Get a chromium tab from the pool, optionally one that has an association with a specific netloc/URL.

		If no url or netloc is specified, the per-thread identifier will be used.
		If `extra_id` is specified, it's stringified value will be mixed into the pool key
		If `use_tid` is true, the per-thread identifier will be mixed into the pool key.

		In all cases, the tab pool is a least-recently-used cache, so the tab that has been accessed the
		least recently will be automatically closed if a new tab is requested, and there are already
		`tab_pool_max_size` tabs created.

		'''
		assert self.alive, "Chrome has been shut down! Cannot continue!"
		if not netloc and url:
			netloc = urllib.parse.urlparse(url).netloc
			self.log.debug("Getting tab for netloc: %s (url: %s)", netloc, url)
		# Coerce to string type so even if it's none, it doesn't hurt anything.
		key = str(netloc)
		if extra_id:
			key += " " + str(extra_id)
		if use_tid or not key:
			key += " " + str(threading.get_ident())

		if self.__started_pid != os.getpid():
			self.log.error("TabPooledChromium instances are not safe to share across multiple processes.")
			self.log.error("Please create a new in each separate multiprocesssing process.")
			raise RuntimeError("TabPooledChromium instances are not safe to share across multiple processes.")

		with self.__counter_lock:
			self.__active_tabs.setdefault(key, 0)
			self.__active_tabs[key] += 1
			if self.__active_tabs[key] > 1:
				self.log.warning("Tab with key %s checked out more then once simultaneously", key)

		try:
			lock, tab = self.__tab_cache[key]
			with lock:
				yield tab
		finally:

			with self.__counter_lock:
				self.__active_tabs[key] -= 1
				if self.__active_tabs[key] == 0:
					self.__active_tabs.pop(key)
