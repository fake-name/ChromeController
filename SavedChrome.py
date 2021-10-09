

import logging
import traceback
import sqlite3
import time
import random
import json

import ChromeController


NEXT_BUTTON_XPATH = '//a[text()="Next"]'

class DbInterface():
	def __init__(self, save_path):
		self.log = logging.getLogger("Main.DB")

		self.db = sqlite3.connect(save_path)
		self.db.enable_load_extension(True)
		self.check_init_db()

	def check_init_db(self):
		cur = self.db.cursor()

		cur.execute("""
			CREATE TABLE IF NOT EXISTS web_pages
			(url text UNIQUE, referrer text, content text, meta text);
			""")
		cur.execute("""
			CREATE TABLE IF NOT EXISTS key_value
			(key text UNIQUE, value text);
			""")
		self.db.commit()

	def insert_kv(self, key, value):

		cur = self.db.cursor()
		cur.execute("""
			INSERT OR REPLACE INTO key_value (key, value)
			VALUES (?, ?)
			""", (key, json.dumps(value)))
		self.db.commit()


	def get_kv(self, key):

		cur = self.db.cursor()
		cur.execute("""
			SELECT (value) FROM key_value
			WHERE (key = ?)
			""", (key, ))
		res = cur.fetchone()
		self.db.commit()

		if res:
			return json.loads(res[0])
		else:
			return None


	def have_kv(self, key):
		cur = self.db.cursor()
		cur.execute("""
			SELECT COUNT(*) FROM key_value
			WHERE key = ?;
			""", (key, ))
		res = cur.fetchone()
		self.db.commit()

		return res[0]

	def get_page(self, url):
		cur = self.db.cursor()
		cur.execute("""
			SELECT url, referrer, content, meta FROM web_pages
			WHERE url = ?;
			""", (url, ))
		res = cur.fetchone()
		self.db.commit()
		if res:
			url, referrer, content, meta = res
			return {
				"url"      : url,
				"referrer" : referrer,
				"content"  : content,
				"meta"     : json.loads(meta),
			}
		return None

	def have_page(self, url):
		cur = self.db.cursor()
		cur.execute("""
			SELECT COUNT(*) FROM web_pages
			WHERE url = ?;
			""", (url, ))
		res = cur.fetchone()
		self.db.commit()

		return res[0]

	def insert_page(self, url, content, meta=None):
		self.log.info("Saving key: %s", url)

		cur = self.db.cursor()

		if meta:
			cur.execute("""
				INSERT OR REPLACE INTO web_pages (url, content, meta)
				VALUES (?, ?, ?)
				""", (url, content, json.dumps(meta)))
		else:
			cur.execute("""
				INSERT OR REPLACE INTO web_pages (url, content)
				VALUES (?, ?)
				""", (url, content))
		self.db.commit()

	def get_page_count(self):

		cur = self.db.cursor()
		cur.execute("""
			SELECT count(1) FROM web_pages;
			""")
		res = cur.fetchone()
		self.db.commit()

		return res[0]

	def get_all_pages(self):
		cur = self.db.cursor()
		cur.execute("""
			SELECT url, referrer, content, meta FROM web_pages
			""")

		ret = []
		for res in cur:
			url, referrer, content, meta = res
			ret.append({
				"url"      : url,
				"referrer" : referrer,
				"content"  : content,
				"meta"     : json.loads(meta),
			})

		self.db.commit()

		return ret


class LoggedChrome(ChromeController.ChromeRemoteDebugInterface):

	def __init__(self, save_to_fn):

		self.db = DbInterface(save_to_fn)

		super().__init__(
				binary='google-chrome',
				headless=False,
			)

		def closure(container, url, content, meta):
			self.content_handler(container, url, content, meta)

		self.install_listener_for_content(closure)

		self.last_save = time.time()

	def content_handler(self, container, url, content, meta):
		self.last_save = time.time()

		self.db.insert_page(url, content, meta)

	def sleep_and_process(self, duration):
		hundred_ms_intervals = int(duration * 10)
		for _ in range(hundred_ms_intervals):
			self.process_available()
			time.sleep(0.1)

		while self.is_still_active():
			self.process_available()
			time.sleep(0.1)

		self.process_available()

	def is_still_active(self):
		ACTIVE_TIME = 10  # seconds

		# Pet chromium
		self.process_available()

		# Return whether the last file saved was within the last ACTIVE_TIME seconds
		if time.time() < self.last_save + ACTIVE_TIME:
			return True
		return False



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


class Bot():

	def __init__(self, filename):
		self.cr = LoggedChrome(filename)
		self.log = logging.getLogger("Main.Bot")

	def _random_sleep_scroll(self):
		steps = int(random.triangular(1,3,6))
		print("Performing %s sleep steps" % (steps, ))
		for x in range(steps):
			self.cr.sleep_and_process(random.triangular(1, 2, 3))
			self.cr.scroll_page(random.triangular(200, 500, 1500))
			print("Sleep step %s done" % (x, ))


	def nav_and_scroll(self, url):
		self.cr.blocking_navigate(url)


	def walk_pages(self, url):

		self.cr.blocking_navigate(url)
		self._random_sleep_scroll()

		while 1:

			# I haven't figured out exactly why you need to call this before find_element,
			# but I think get_dom_root_id() (and therefore DOM0.getDocument()) causes
			# the debug tools to load the DOM in the remote browser, or something.
			# If you remove it, find_element() (and as such DOM.performSearch)
			# returns invalid, but not empty results!
			self.cr.get_dom_root_id()

			node_ids = self.cr.find_element(NEXT_BUTTON_XPATH)

			if not node_ids:
				print("No next button results!")
				# import pdb
				# pdb.set_trace()
				return

			next_button_id = node_ids[0]

			try:
				# get_dom_item_center_coords scrolls the item into view if needed.
				x_pos, y_pos = self.cr.get_dom_item_center_coords(next_button_id)
				self.cr.sleep_and_process(random.triangular(5, 10, 20))

				self.log.info("Extracting rendered source.")
				rendered = self.cr.get_rendered_page_source()
				current_url = self.cr.get_current_url()

				self.cr.db.insert_page(url=current_url, content=rendered)

				self.log.info("Clicking next button at %s", ((x_pos, y_pos), ))
				self.cr.click_item_at_coords(x_pos, y_pos)

			except Exception:

				print("Failure?")
				traceback.print_exc()

				import IPython
				# IPython.embed()
				import pdb
				pdb.set_trace()


			self._random_sleep_scroll()

def test():
	bt = Bot()

	# cr.blocking_navigate("https://www.wlnupdates.com")
	# cr.sleep_and_process(10)
	# cr.db.get_page_count()

	bt.test()

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)
	test()



