#!/bin/bash
python3 -m venv venv && . venv/bin/activate && pip install flet==0.80.2 && python3 -m flet publish web_gui.py --web-render html --route-url-strategy hash --assets-dir assets && mkdir -p build/web && cp -r dist/* build/web/ 2>/dev/null || true
