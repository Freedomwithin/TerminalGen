#!/bin/bash
# TerminalGen Sovereign Forge (v1.0)

# 1. Setup paths
APPDIR="TerminalGen.AppDir"
mkdir -p $APPDIR/usr/bin
mkdir -p $APPDIR/usr/share/icons/hicolor/256x256/apps
mkdir -p $APPDIR/data

# 2. Compile/Copy the C++ Engine
echo "Forging the C++ Neural Matrix..."
cd projects/TerminalGen
g++ -O3 -std=c++17 main.cpp search.cpp -o ../../$APPDIR/usr/bin/terminal_commands -I include
cd ../..

# 3. Copy the Database
echo "Anchoring the command matrix..."
cp projects/TerminalGen/data/commands.json $APPDIR/data/commands.json

# 4. Copy Python GUIs and Resources
echo "Bundling the Sovereign Aesthetic..."
cp projects/TerminalGen/gui.py $APPDIR/usr/bin/gui.py
cp projects/TerminalGen/web_gui.py $APPDIR/usr/bin/web_gui.py
cp -r projects/TerminalGen/templates $APPDIR/usr/bin/

# 5. Create the AppRun (Universal Entry Point)
echo "Writing the Sovereign AppRun..."
cat << 'EOF' > $APPDIR/AppRun
#!/bin/bash
SELF=$(dirname "$(readlink -f "$0")")

# Set the data path for the C++ engine
export TERMINAL_GEN_DATA="$SELF/data/commands.json"

# Start the Flask Web GUI in the background (Port 8501)
# Using python3 from the system, assuming dependencies are installed
# For a TRUE standalone, we'd bundle a portable python env here
nohup python3 "$SELF/usr/bin/web_gui.py" > /dev/null 2>&1 &

# Launch the Desktop GUI
python3 "$SELF/usr/bin/gui.py"
EOF
chmod +x $APPDIR/AppRun

# 6. Desktop Entry & Visuals
echo "Anchoring the visual identity..."
# Use a generic icon for now, or copy one if available
# cp assets/maya/maya_logo.png $APPDIR/terminalgen.png
cat << 'EOF' > $APPDIR/terminalgen.desktop
[Desktop Entry]
Name=TerminalGen
Exec=AppRun
Icon=terminalgen
Type=Application
Categories=Development;Utility;
Comment=The 1,024+ Command Search Engine
EOF

# 7. Final Verification
echo "Verifying the Forge..."
ls -R $APPDIR

echo "The TerminalGen AppDir is prepared. Ready for final AppImage compression."
