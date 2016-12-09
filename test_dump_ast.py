

import os.path
import astor
import pprint

import WebRequest

import ChromeController.manager as mgr
import ChromeController



def test_func(self, expression, **kwargs):
	"""
	Python Function: Runtime_evaluate
		Domain: Runtime
		Method name: evaluate

		Parameters:
			'expression' (type: string) -> Expression to evaluate.
			'objectGroup' (type: string) -> Symbolic group name that can be used to release multiple objects.
			'includeCommandLineAPI' (type: boolean) -> Determines whether Command Line API should be available during the evaluation.
			'silent' (type: boolean) -> In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides <code>setPauseOnException</code> state.
			'contextId' (type: ExecutionContextId) -> Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page.
			'returnByValue' (type: boolean) -> Whether the result is expected to be a JSON object that should be sent by value.
			'generatePreview' (type: boolean) -> Whether preview should be generated for the result.
			'userGesture' (type: boolean) -> Whether execution should be treated as initiated by user in the UI.
			'awaitPromise' (type: boolean) -> Whether execution should wait for promise to be resolved. If the result of evaluation is not a Promise, it's considered to be an error.
		Returns:
			'result' (type: RemoteObject) -> Evaluation result.
			'exceptionDetails' (type: ExceptionDetails) -> Exception details.
		Description: Evaluates expression on global object.
	"""
	assert isinstance(expression, (str,)
		), 'Argument expression must be of type (str, ). Received type: %s' % type(
		expression)

	expected = [
		'objectGroup',
		'includeCommandLineAPI',
		'silent',
		'contextId',
		'returnByValue',
		'generatePreview',
		'userGesture',
		'awaitPromise',
	]

	print("Wat?", expression)

	if 'objectGroup' in kwargs:
		assert isinstance(kwargs['objectGroup'], (str,)
			), 'Argument objectGroup must be of type (str, ). Received type: %s' % type(
			kwargs['objectGroup'])
	if 'includeCommandLineAPI' in kwargs:
		assert isinstance(kwargs['includeCommandLineAPI'], (bool,)
			), 'Argument includeCommandLineAPI must be of type (bool, ). Received type: %s' % type(
			kwargs['includeCommandLineAPI'])
	if 'silent' in kwargs:
		assert isinstance(kwargs['silent'], (bool,)
			), 'Argument silent must be of type (bool, ). Received type: %s' % type(
			kwargs['silent'])
	if 'returnByValue' in kwargs:
		assert isinstance(kwargs['returnByValue'], (bool,)
			), 'Argument returnByValue must be of type (bool, ). Received type: %s' % type(
			kwargs['returnByValue'])
	if 'generatePreview' in kwargs:
		assert isinstance(kwargs['generatePreview'], (bool,)
			), 'Argument generatePreview must be of type (bool, ). Received type: %s' % type(
			kwargs['generatePreview'])
	if 'userGesture' in kwargs:
		assert isinstance(kwargs['userGesture'], (bool,)
			), 'Argument userGesture must be of type (bool, ). Received type: %s' % type(
			kwargs['userGesture'])
	if 'awaitPromise' in kwargs:
		assert isinstance(kwargs['awaitPromise'], (bool,)
			), 'Argument awaitPromise must be of type (bool, ). Received type: %s' % type(
			kwargs['awaitPromise'])

	passed_keys = list(kwargs.keys())
	assert all([key in expected for key in kwargs.keys()]), "Passed: %s" % passed_keys


	self.synchronous_command('Runtime.evaluate', kwargs)



def func():

	class TestWat(object):
		def __init__(self, *args, **kwargs):
			print("Lol?", (args, kwargs))
			super().__init__(*args, **kwargs)
			super().__init__(args, kwargs)

	instance = TestWat()


def docstring_dbg():
	print(astor.dump_tree(astor.code_to_ast(test_func)))



if __name__ == '__main__':
	docstring_dbg()
