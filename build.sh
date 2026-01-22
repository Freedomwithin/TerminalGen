#!/bin/bash
python3 -m venv v&&. v/bin/activate&&pip install flet&&flet pack web_gui.py --product terminalgen --icon assets/icon.png&&mkdir -p build/web&&cp -r dist/web/* build/web/
