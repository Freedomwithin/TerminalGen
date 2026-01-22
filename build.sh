#!/bin/bash
python3 -m venv v&&. v/bin/activate&&pip install flet&&python3 web_gui.py --web-render html&&mkdir -p build/web&&cp -r dist/* build/web/
