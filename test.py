

import os.path
import time
import ChromeController

def test():
	crbin = os.path.abspath("../AutoTriever/Headless/headless_shell")
	cr = ChromeController.ChromeInterface(binary=crbin)
	print(cr)
	time.sleep(10)



if __name__ == '__main__':
	test()
