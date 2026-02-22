#!/bin/bash
# Move to the project directory
cd /home/freedomwithin/Documents/Tech/GitHub_Reops/TerminalGen

# Start the Flask engine using the venv's Python
# The '&' at the end lets it run in the background
./venv/bin/python3 web_gui.py > /dev/null 2>&1 &