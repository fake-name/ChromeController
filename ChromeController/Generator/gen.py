"""
"""
import json
import ast
import astor
import pprint

import os.path


CHECKS = {
	"array"   : "(list, tuple)",
	"boolean" : "(bool, )",
	"integer" : "(int, )",
	"number"  : "(float, int)",
	"string"  : "(str, )",
}

class JsonInterfaceGenerator():
	"""

	"""

	def __init__(self, protocol_major=1, protocol_minor=2):
		""" init """
		print(__file__)

		protocol_major = str(protocol_major)
		protocol_minor = str(protocol_minor)

		protocol_rev = "{}.{}".format(protocol_major, protocol_minor)

		json_file = "browser_protocol-r{}.json".format(protocol_rev)
		folder = os.path.split(__file__)[0]
		protocol_file_path = os.path.join(folder, "../", 'protocols', json_file)
		protocol_file_path = os.path.abspath(protocol_file_path)
		assert(os.path.exists(protocol_file_path)), "Protocol file '{}' appears to be missing!".format(protocol_file_path)


		self.types = {}

		with open(protocol_file_path) as fp:
			protocol_str = fp.read()

		self.protocol = json.loads(protocol_str)

		self.__validate_protocol_version(protocol_major, protocol_minor)
		self.__build_interface_class()


	def __validate_protocol_version(self, protocol_major, protocol_minor):
		errm_1 = "Major version mismatch: {} - {}".format(self.protocol['version']["major"], protocol_major)
		errm_2 = "Minor version mismatch: {} - {}".format(self.protocol['version']["minor"], protocol_minor)

		v_1 = self.protocol['version']["major"]
		v_2 = self.protocol['version']["minor"]

		assert isinstance(protocol_major, str)
		assert isinstance(protocol_minor, str)

		assert v_1 == protocol_major, errm_1
		assert v_2 == protocol_minor, errm_2


	def __build_interface_class(self):
		# body = ast.
		body = [
			ast.Expr(value=ast.Str(s='\n\n\t')),
			self.__build__init()
		]
		for subdom in self.protocol['domains']:
			subdom_funcs = self.__build_domain_interface(subdom)
			body += subdom_funcs

		# print(body)

		self.interface_class = ast.ClassDef(
				name           = "CromeRemoteDebugInterface",
				bases          = [ast.Str("object")],
				body           = body,
				keywords       = [],
				decorator_list = [],
				starargs       = None,
				kwargs         = None,
				lineno         = 0,
				col_offset     = 0,
				)

		# code = astor.dump_tree(self.interface_class)
		# print(code)

	def __build__init(self):
		sig = ast.arguments(
					args=[],
					vararg=None,
					varargannotation=None,
					kwonlyargs=[],
					kwarg=None,
					kwargannotation=None,
					defaults=[],
					kw_defaults=[])

		func = ast.FunctionDef(
			name = "__init__",
			args = sig,
			body = [ast.Pass()],
			decorator_list = [],
			lineno     = 0,
			col_offset = 0,
			)

		return func

	def __build_domain_interface(self, subdom):
		assert "domain" in subdom

		dom_desc  = subdom.get("descripton", "")
		dom_name  = subdom['domain']
		full_name = subdom['domain']
		if subdom.get("experimental"):
			full_name = "exp_{}".format(full_name)

		for typen in subdom.get('types', []):
			typestr = "{}_{}".format(dom_name, typen['id'])
			assert typen['id'] not in self.types, "Duplicate type name: {}".format(typen['id'])
			self.types[typestr] = typen

		functions = []
		for command in subdom.get('commands', []):
			func = self.__build_function(dom_name, full_name, command)
			functions.append(func)

		return functions


	def __build_function(self, dom_name, full_name, func_params):

		assert 'name' in func_params
		func_name = func_params['name']
		# print(dom_name, full_name, func_name)

		args = [ast.arg('self', None)]
		message_params = []
		func_body = []
		for param in func_params.get("parameters", []):
			argname = param['name']
			message_params.append(ast.Name(id=argname, ctx=ast.Load()))
			args.append(ast.arg(argname, None))
			param_type = param.get("type", None)
			if param_type in CHECKS:
				checker_str = "assert isinstance({argname}, {typetuple}), \"Argument {argname} must be of type {typetuple}. Received type: %s\" % type({argname})".format(
						argname = argname,
						typetuple = CHECKS[param_type],
					)
				checker = ast.parse(checker_str)

				if checker.body:
					func_body.append(checker.body.pop())

		fname = ast.Name(id="\"{}.{}\"".format(dom_name, func_name), ctx=ast.Load())
		message_params = [fname] + message_params
		# print(message_params)
		communicate_call = ast.Call(
				func=ast.Attribute(value=ast.Name(id='self', ctx=ast.Load()), ctx=ast.Load(), attr='transport.synchronous_command'),
				args=message_params,
				keywords=[])

		do_communicate = ast.Assign(targets=[ast.Name(id='subdom_funcs', ctx=ast.Store())], value=communicate_call)
		func_ret = ast.Return(value=ast.Name(id='subdom_funcs', ctx=ast.Load()))

		func_body.append(do_communicate)
		func_body.append(func_ret)

		# send_message = Expr(
		# 	value=Call(
		# 		func=Attribute(value=Name(id='self', ctx=ast.Load()), attr='__build_interface_class'),
		# 		args=[],
		# 		keywords=[]))],

		# func_body = [ast.Pass()]


		sig = ast.arguments(
					args=args,
					vararg=None,
					varargannotation=None,
					kwonlyargs=[],
					kwarg=None,
					kwargannotation=None,
					defaults=[],
					kw_defaults=[])

		func = ast.FunctionDef(
			name = "{}_{}".format(full_name, func_name),
			args = sig,
			body = func_body,
			decorator_list = [],
			lineno     = 0,
			col_offset = 0,
			)

		return func

	def __to_module(self):

		module_components = [
			ast.ImportFrom(module="ChromeController.transport", names=[ast.alias('ChromeSocketManager', None)], level=0),
			ast.ImportFrom(module="ChromeController.manager",   names=[ast.alias('ChromeInterface',     None)], level=0),
			self.interface_class,
		]

		mod = ast.Module(module_components, lineno=1, col_offset=1)

		# print_call = ast.Expr(
		# 		ast.Call(
		# 		func=ast.Name(id='print', ctx=ast.Load()),
		# 		args=[ast.Str(s="PyCon2010!", ctx=ast.Load())],
		# 		keywords=[]))
		# mod = ast.Module([print_call])

		# mod.lineno = 1
		# mod.col_offset  = 1
		mod = ast.fix_missing_locations(mod)

		return mod



	def dump_class(self):
		indent = "    "
		return astor.to_source(self.__to_module(), indent_with=indent)

	def dump_ast(self):
		return astor.dump_tree(self.__to_module())

	def compile_class(self):
		mod = self.__to_module()
		# print(mod.lineno)
		# print(mod.body)
		# print(mod.body[2])
		# print(mod.body[2].lineno)
		# print(mod.body[2].body)

		return compile(self.__to_module(), "", "exec")



def print_file_ast():
	with open(__file__) as fp:
		this_source = fp.read()
	this_ast = ast.parse(this_source)

	print("AST:")
	print("astor.dump_tree(this_ast)")
	print(astor.dump_tree(this_ast))

def test():
	print(JsonInterfaceGenerator)
	# print_file_ast()
	instance = JsonInterfaceGenerator()
	print("ast:")
	print(instance.dump_ast())
	newsauce = instance.dump_class()
	print("Class:")
	print(newsauce)
	print(instance.compile_class())
	# print(instance)

if __name__ == '__main__':
	test()



