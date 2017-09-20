
class ChromeControllerException(RuntimeError):
	pass

class ChromeStartupException(ChromeControllerException):
	pass

class ChromeConnectFailure(ChromeControllerException):
	pass

class ChromeCommunicationsError(ChromeControllerException):
	pass

class ChromeError(ChromeControllerException):
	pass

class ChromeNavigateTimedOut(ChromeError):
	pass