

import os.path
import astor
import pprint
import ast



def build_ast_class():
	'''
		ClassDef(name='TestWat',
			bases=[Name(id='object')],
			keywords=[],
			starargs=None,
			kwargs=None,
			body=[
				FunctionDef(name='__init__',
					args=arguments(args=[arg(arg='self', annotation=None)],
						vararg=arg(arg='args', annotation=None),
						kwonlyargs=[],
						kw_defaults=[],
						kwarg=arg(arg='kwargs', annotation=None),
						defaults=[]),
					body=[
						Expr(
							value=Call(
								func=Attribute(
									value=Call(func=Name(id='super'), args=[], keywords=[], starargs=None, kwargs=None),
									attr='__init__'),
								args=[Name(id='self')],
								keywords=[],
								starargs=Name(id='args'),
								kwargs=Name(id='kwargs')))],
					decorator_list=[],
					returns=None)],
			decorator_list=[]),

	'''


	init_call = ast.Call(func=ast.Name(id='super', ctx=ast.Load()), args=[], keywords=[])
	super_func = ast.Call(
							func=ast.Attribute(value=init_call, attr='__init__', ctx=ast.Load()),
							args=[ast.Name(id='self', ctx=ast.Load())],
							starargs=ast.Name(id='args', ctx=ast.Load()),
							kwargs=ast.Name(id='kwargs', ctx=ast.Load()),
							keywords=[],
					)

	super_init = ast.Expr(
						value=super_func,
						lineno     = 3,
						col_offset = 0,
					)


	body = [super_init]
	# body = [ast.Pass()]


	sig = ast.arguments(
				args=[ast.arg('self', None)],
				vararg=ast.arg(arg='args', annotation=None),
				kwarg=ast.arg(arg='kwargs', annotation=None),
				varargannotation=None,
				kwonlyargs=[],
				kwargannotation=None,
				defaults=[],
				kw_defaults=[])

	init_func = ast.FunctionDef(
		name = "__init__",
		args = sig,
		body = body,
		decorator_list = [],
		lineno     = 2,
		col_offset = 0,
		)


	body = [
		ast.Expr(value=ast.Str(s='\n\n\t')),
		init_func
	]

	# print(body)

	interface_class = ast.ClassDef(
			name           = "Test-Class",
			bases          = [],
			body           = body,
			keywords       = [],
			decorator_list = [],
			starargs       = None,
			kwargs         = None,
			lineno         = 1,
			col_offset     = 0,
			)
	print("Interface class:", interface_class)
	return interface_class

def build_module():

	module_components = [
		# ast.ImportFrom(module="ChromeController.transport",    names=[ast.alias('ChromeSocketManager', None)], level=0),
		# ast.ImportFrom(module="ChromeController.manager_base", names=[ast.alias('ChromeInterface',     None)], level=0),
		build_ast_class(),
	]

	mod = ast.Module(module_components, lineno=1, col_offset=1)

	mod = ast.fix_missing_locations(mod)
	print("Module:", mod)
	return mod

def wat():
	clsdef = build_module()
	print("Clsdef: ", clsdef)
	code = compile(clsdef, "no filename", "exec")
	exec(code)


if __name__ == '__main__':
	# wat()
	wat()
	# docstring_dbg()
