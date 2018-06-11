
class ChromeControllerException(RuntimeError):
	pass

class ChromeStartupException(ChromeControllerException):
	pass

class ReusedPortError(ChromeStartupException):
	pass

class ChromeConnectFailure(ChromeControllerException):
	pass

class ChromeCommunicationsError(ChromeControllerException):
	pass
class ChromeTabNotFoundError(ChromeCommunicationsError):
	pass

class ChromeError(ChromeControllerException):
	pass
class ChromeDiedError(ChromeError):
	pass

class ChromeNavigateTimedOut(ChromeError):
	pass
class ChromeResponseNotReceived(ChromeError):
	pass