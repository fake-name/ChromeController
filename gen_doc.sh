#!/bin/bash


set -e

# # In a script, because I'll fucking forget if I don't write it down.
# # The crome build process is pretty bizarre.
# if [ ! -f ../Chromium/src/out/Headless/headless_shell ]; then
# 	echo "No headless shell file found. Doing a build!"
# 	cd ../Chromium/src
# 	gclient fetch
# 	gclient sync
# 	mkdir -p out/Headless
# 	echo 'import("//build/args/headless.gn")' > out/Headless/args.gn
# 	echo 'is_debug = false' >> out/Headless/args.gn
# 	gn gen out/Headless
# 	ninja -C out/Headless headless_shell

# 	Update the json files.
# 	cp ../Chromium/src/third_party/WebKit/Source/core/inspector/browser_protocol.json ./ChromeController/protocols/browser_protocol-r1.2.json
# 	cp ../Chromium/src/out/Headless/gen/blink/core/inspector/protocol.json            ./ChromeController/protocols/js_protocol-r1.2.json
# fi

pypy3 gen_class.py


pypy3 -m pydoc -w ChromeController.TabPooledChromium
pypy3 -m pydoc -w ChromeController.ChromeExecutionManager
pypy3 -m pydoc -w ChromeController.ChromeRemoteDebugInterface
pypy3 -m pydoc -w ChromeController.Generator
pypy3 -m pydoc -w ChromeController.Generator.Generated
pypy3 -m pydoc -w ChromeController.Generator.gen
pypy3 -m pydoc -w ChromeController
pypy3 -m pydoc -w ChromeController.filter_funcs
pypy3 -m pydoc -w ChromeController.exit_handler
pypy3 -m pydoc -w ChromeController.__main__
pypy3 -m pydoc -w ChromeController.manager
pypy3 -m pydoc -w ChromeController.cr_exceptions
pypy3 -m pydoc -w ChromeController.chrome_context
pypy3 -m pydoc -w ChromeController.manager_base
pypy3 -m pydoc -w ChromeController.tab_pool
pypy3 -m pydoc -w ChromeController.transport

mv ChromeController.chrome_context.html                ./docs/ChromeController.chrome_context.html
mv ChromeController.cr_exceptions.html                 ./docs/ChromeController.cr_exceptions.html
mv ChromeController.Generator.gen.html                 ./docs/ChromeController.Generator.gen.html
mv ChromeController.Generator.Generated.html           ./docs/ChromeController.Generator.Generated.html
mv ChromeController.Generator.html                     ./docs/ChromeController.Generator.html
mv ChromeController.exit_handler.html                  ./docs/ChromeController.exit_handler.html
mv ChromeController.filter_funcs.html                  ./docs/ChromeController.filter_funcs.html
mv ChromeController.__main__.html                      ./docs/ChromeController.__main__.html
mv ChromeController.html                               ./docs/ChromeController.html
mv ChromeController.manager_base.html                  ./docs/ChromeController.manager_base.html
mv ChromeController.tab_pool.html                      ./docs/ChromeController.tab_pool.html
mv ChromeController.manager.html                       ./docs/ChromeController.manager.html
mv ChromeController.transport.html                     ./docs/ChromeController.transport.html
mv ChromeController.ChromeRemoteDebugInterface.html    ./docs/ChromeController.ChromeRemoteDebugInterface.html
mv ChromeController.ChromeExecutionManager.html        ./docs/ChromeController.ChromeExecutionManager.html
mv ChromeController.TabPooledChromium.html             ./docs/ChromeController.TabPooledChromium.html

