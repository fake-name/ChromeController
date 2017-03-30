#!/bin/bash


set -e

cp ../Chromium/src/components/ui_devtools/protocol.json                ./ChromeController/protocols/browser_protocol-r1.2.json
cp ../Chromium/src/out/Headless/gen/blink/core/inspector/protocol.json ./ChromeController/protocols/js_protocol-r1.2.json

python3 -m pydoc -w ChromeController.CromeRemoteDebugInterface
python3 -m pydoc -w ChromeController.ChromeSocketManager
python3 -m pydoc -w ChromeController.Generator
python3 -m pydoc -w ChromeController.Generator.gen
python3 -m pydoc -w ChromeController
python3 -m pydoc -w ChromeController.manager
python3 -m pydoc -w ChromeController.manager_base
python3 -m pydoc -w ChromeController.transport

mv ChromeController.CromeRemoteDebugInterface.html ./docs/ChromeController.CromeRemoteDebugInterface.html
mv ChromeController.ChromeSocketManager.html ./docs/ChromeController.ChromeSocketManager.html
mv ChromeController.Generator.html ./docs/ChromeController.Generator.html
mv ChromeController.Generator.gen.html ./docs/ChromeController.Generator.gen.html
mv ChromeController.html ./docs/ChromeController.html

mv ChromeController.manager.html ./docs/ChromeController.manager.html
mv ChromeController.manager_base.html ./docs/ChromeController.manager_base.html
mv ChromeController.transport.html ./docs/ChromeController.transport.html




