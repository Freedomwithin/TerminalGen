#!/bin/bash
# Move to the project directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Start the Flask engine using the venv's Python
# The '&' at the end lets it run in the background
./venv/bin/python3 web_gui.py > /dev/null 2>&1 &