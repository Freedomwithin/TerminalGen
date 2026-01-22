#!/bin/bash
# Build static web version of Flet app
source venv/bin/activate
flet publish web_gui.py --web-render html --route-url-strategy hash --assets-dir assets
