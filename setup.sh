#!/bin/bash
echo "🚀 TerminalGen - ONE-CLICK SETUP"

# 1. Install JSON library
mkdir -p include/nlohmann
curl -o include/nlohmann/json.hpp https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp
echo "✅ JSON library installed"

# 2. Compile C++ CLI
g++ main.cpp -o terminal_commands -std=c++17
echo "✅ C++ CLI compiled"

# 3. Test CLI
echo "🧪 Testing (process):"
./terminal_commands "process"
echo ""

# 4. Python setup
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Venv created"
fi

source venv/bin/activate
pip install -q flet requests flask
echo "✅ Python deps installed"

# 5. Launch BOTH GUIs
echo "🎨 Launching GUIs..."
python3 gui.py &           # Desktop (Tkinter)
python3 web_gui.py &       # Web (Flet - localhost:8501)
echo "✅ Desktop GUI launched"
echo "✅ Web GUI: http://localhost:8501"

echo ""
echo "🎉 TerminalGen FULLY READY!"
echo "=================================="
echo "CLI:  ./terminal_commands 'keyword'"
echo "Web:  http://localhost:8501"
echo "Desktop: New window opened"
echo "=================================="
