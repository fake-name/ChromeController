
import logging
import urllib.parse
import cachetools

from ChromeController.cr_exceptions import ChromeNavigateTimedOut
from ChromeController.cr_exceptions import ChromeError
from ChromeController.resources import js
from ChromeController.manager import ChromeRemoteDebugInterface



class ChromeTabPool(object):

	def __init__(self, *args, tab_pool_max_size = None, **kwargs):

		self.chrome_interface = ChromeRemoteDebugInterface(*args, **kwargs)
		self.tab_pool_max_size = tab_pool_max_size

		self.log = logging.getLogger("Main.ChromeController.TabPool")

		class TabStore(cachetools.LRUCache):

			def __getitem__(inner_self, url):
				nl = urllib.parse.urlparse(url).netloc
				key = hash(nl) % inner_self.maxsize
				return super.__getitem__(key)

			def __missing__(inner_self, key):
				inner_self[key] = self.chrome_interface.new_tab()
				return inner_self[key]


			def popitem(inner_self):
				key, value = super().popitem()
				print('Key "%s" evicted with value "%s"' % (key, value))
				return key, value

		self.tab_cache = TabStore(maxsize=tab_pool_max_size)
