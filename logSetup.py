

import logging
import multiprocessing
import colorama as clr
import threading
import os.path
import os
import sys
import re
import time
import traceback
# Pylint can't figure out what's in the record library for some reason
#pylint: disable-msg=E1101

colours = [clr.Fore.BLUE, clr.Fore.RED, clr.Fore.GREEN, clr.Fore.YELLOW, clr.Fore.MAGENTA, clr.Fore.CYAN, clr.Back.YELLOW + clr.Fore.BLACK, clr.Back.YELLOW + clr.Fore.BLUE, clr.Fore.WHITE]

def getColor(idx):
	return colours[idx%len(colours)]


class UnlockedHandler(logging.Handler):

	def acquire(self):
		"""
		Acquire the I/O thread lock.
		"""
		return

	def release(self):
		"""
		Release the I/O thread lock.
		"""
		return


stdout_lock = multiprocessing.Lock()


# THIS IS HORRIBLE
logging.Handler = UnlockedHandler


def getProcessSafeLogger(logPath):
	if multiprocessing.current_process().name == "MainProcess":
		return logging.getLogger(logPath)
	else:
		return multiprocessing.get_logger(logPath)


def resetLoggingLocks():
	'''
	This function is a HACK!

	Basically, if we fork() while a logging lock is held, the lock
	is /copied/ while in the acquired state. However, since we've
	forked, the thread that acquired the lock no longer exists,
	so it can never unlock the lock, and we end up blocking
	forever.

	Therefore, we manually enter the logging module, and forcefully
	release all the locks it holds.

	THIS IS NOT SAFE (or thread-safe).
	Basically, it MUST be called right after a process
	starts, and no where else.
	'''
	try:
		logging._releaseLock()
	except RuntimeError:
		pass  # The lock is already released

	# Iterate over the root logger hierarchy, and
	# force-free all locks.
	# if logging.Logger.root
	for handler in logging.Logger.manager.loggerDict.values():
		if hasattr(handler, "lock") and handler.lock:
			try:
				handler.lock.release()
			except RuntimeError:
				pass  # The lock is already released



class ColourHandler(UnlockedHandler):

	def __init__(self, level=logging.DEBUG):
		UnlockedHandler.__init__(self, level)
		self.formatter = logging.Formatter('\r%(name)s - %(style)s%(levelname)s - %(message)s'+clr.Style.RESET_ALL)
		clr.init()

		self.logPaths = {}


	def emit(self, record):

		# print record.levelname
		# print record.name

		segments = record.name.split(".")
		tname = threading.current_thread().name
		segments.append(tname)
		if segments[0] == "Main" and len(segments) > 1:
			segments.pop(0)
			segments[0] = "Main."+segments[0]

		nameList = []

		for indice, pathSegment in enumerate(segments):
			if not indice in self.logPaths:
				self.logPaths[indice] = [pathSegment]
			elif not pathSegment in self.logPaths[indice]:
				self.logPaths[indice].append(pathSegment)

			name = clr.Style.RESET_ALL
			name += getColor(self.logPaths[indice].index(pathSegment))
			name += pathSegment
			name += clr.Style.RESET_ALL
			nameList.append(name)


		record.name = ".".join(nameList) + " PID: {} ".format(os.getpid())

		if record.levelname == "DEBUG":
			record.style = clr.Style.DIM
		elif record.levelname == "WARNING":
			record.style = clr.Style.BRIGHT
		elif record.levelname == "ERROR":
			record.style = clr.Style.BRIGHT+clr.Fore.RED
		elif record.levelname == "CRITICAL":
			record.style = clr.Style.BRIGHT+clr.Back.BLUE+clr.Fore.RED
		else:
			record.style = clr.Style.NORMAL

		# record.padding = ""
		record.msg = str(record.msg).encode("utf-8", "replace").decode("utf-8")
		record.padding = ""
		msg = self.format(record)
		msg = str(msg).encode("utf-8", "replace").decode("utf-8")
		locked = False
		try:
			locked = stdout_lock.acquire(timeout=1)
			print(msg)

			# Apparently the answer to "can I break stdout" is yes.
			# /that happened/
		except RuntimeError:
			print("Failure to print!")
		finally:
			if locked:
				stdout_lock.release()

ansi_escape = re.compile(r'\x1b[^m]*m')

class RobustFileHandler(logging.FileHandler):
	"""
	A handler class which writes formatted logging records to disk files.
	"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.output_streams = {}

	def acquire(self):
		"""
		Acquire the I/O thread lock.
		"""
		return

	def release(self):
		"""
		Release the I/O thread lock.
		"""
		return


	def stream_emit(self, record, source_name):
		"""
		Emit a record.

		If a formatter is specified, it is used to format the record.
		The record is then written to the stream with a trailing newline.  If
		exception information is present, it is formatted using
		traceback.print_exception and appended to the stream.  If the stream
		has an 'encoding' attribute, it is used to determine how to do the
		output to the stream.
		"""

		if not source_name in self.output_streams:
			out_path = os.path.abspath("./logs")
			logpath = ansi_escape.sub('', source_name.replace("/", ";").replace(":", ";").replace("?", "-"))
			filename = "log {path}.txt".format(path=logpath)
			print("Opening output log file for path: %s" % filename)
			self.output_streams[source_name] = open(os.path.join(out_path, filename), self.mode, encoding=self.encoding)

		stream = self.output_streams[source_name]
		try:
			msg = self.format(record)
			stream.write(msg)
			stream.write(self.terminator)
			stream.flush()
			self.flush()
		except Exception:
			self.handleError(record)

	def emit(self, record):
		"""
		Emit a record.

		If the stream was not opened because 'delay' was specified in the
		constructor, open it before calling the superclass's emit.
		"""
		failures = 0
		while failures < 3:
			try:
				self.stream_emit(record, record.name)
				break
			except:
				failures += 1
		else:
			traceback.print_stack()
			print("Error writing to file?")


		self.close()


def exceptHook(exc_type, exc_value, exc_traceback):
	if issubclass(exc_type, KeyboardInterrupt):
		sys.__excepthook__(exc_type, exc_value, exc_traceback)
		return
	mainLogger = logging.getLogger("Main")			# Main logger
	mainLogger.critical('Uncaught exception!')
	mainLogger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

# Global hackyness to detect and warn on double-initialization of the logging systems.
LOGGING_INITIALIZED = False

def initLogging(logLevel=logging.INFO):

	global LOGGING_INITIALIZED
	if LOGGING_INITIALIZED:

		print("ERROR - Logging initialized twice!")
		try:
			print(traceback.format_exc())
			return
		except Exception:
			pass

	LOGGING_INITIALIZED = True

	print("Setting up loggers....")

	if not os.path.exists(os.path.join("./logs")):
		os.mkdir(os.path.join("./logs"))

	mainLogger = logging.getLogger("Main")			# Main logger
	mainLogger.setLevel(logLevel)

	ch = ColourHandler()
	mainLogger.addHandler(ch)

	logName	= "log - %s.txt" % (time.strftime("%Y-%m-%d %H;%M;%S", time.gmtime()))

	errLogHandler = RobustFileHandler(os.path.join("./logs", logName))
	errLogHandler.setLevel(logging.INFO)
	# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	# errLogHandler.setFormatter(formatter)

	# mainLogger.addHandler(errLogHandler)

	# Install override for excepthook, to catch all errors
	sys.excepthook = exceptHook

	print("done")


if __name__ == "__main__":
	initLogging()
	log = logging.getLogger("Main.Test")
	log.debug("Testing logging - level: debug")
	log.info("Testing logging - level: info")
	log.warn("Testing logging - level: warn")
	log.error("Testing logging - level: error")
	log.critical("Testing logging - level: critical")
	print()
	log.info("Exception using exc_info:")
	try:
		x = 1 / 0
	except Exception as e:
		log.error("Failed to do thing", exc_info=e)

	print()
	log.info("Exception using manually extracted traceback")
	try:
		x = 1 / 0
	except Exception as e:
		log.error("Failed to do thing")
		for line in traceback.format_exc().strip().split("\n"):
			log.error(line)

