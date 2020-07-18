
import os
import os.path

def load_evasions():
	'''
	Load the list of evasion JS scripts.
	'''

	rsc_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evasions")
	scripts = os.listdir(rsc_dir)

	# Make script ordering determinstic.
	scripts.sort()

	loaded = {}
	for script in scripts:
		if script.endswith(".js"):
			with open(os.path.join(rsc_dir, script), "r") as fp:
				loaded[script] = fp.read()

	return loaded

def test():
	print("evasions:", load_evasions())

if __name__ == '__main__':
	test()
