# TerminalGen: 1,085+ Commands

**Lightning-fast C++17 "Memory Daemon"** | **Neon Desktop GUI** | **Ghost Injection (⚡ INJECT)**  

**Instant fuzzy search across 1,085+ DevOps commands (bash, git, docker, k8s, aws, python, powershell).
Replaces tldr/cheat.sh with 1000x speed + native support for Linux Mint, Windows, and macOS. Search "docker", get every command instantly. Fully offline capable with a native C++ engine.**

## Click the image to see the demo!
[![TerminalGen demo picture](https://github.com/user-attachments/assets/48a0dc55-2d9c-4422-866c-ab5b34a8ba30)](https://terminal-moyt0r11s-jonathon-koerners-projects.vercel.app/)

## New in v1.0 (Sovereign RC)
- **⚡ Ghost Injection**: One-click command injection directly into your active terminal window (Kitty/X11).
- **🎨 Sovereign Aesthetic**: De-noised neon UI with rounded icon and indigo/night palette.
- **🚀 C++17 Neural Matrix**: Sub-millisecond fuzzy search (<1ms) across 1,085+ nodes.
- **📦 Portable AppImage**: Fully bundled 1.8MB binary for immediate Linux deployment.

## One-Click Setup (30 seconds)

### Linux / macOS
```bash
git clone https://github.com/Freedomwithin/TerminalGen.git
cd TerminalGen
chmod +x setup.sh
./setup.sh  # Compiles Native C++ CLI + launches Desktop + Web GUIs instantly!
```

### Windows (WSL / PowerShell)
Requirements: `g++` (MinGW or MSVC), `python3`
```powershell
# Compile the native CLI
g++ main.cpp search.cpp -o terminal_commands -std=c++17 -Iinclude

# Run the GUIs
python gui.py
```

## Features
- **Native C++ Engine**: Powered by `nlohmann/json` and a Repository Pattern architecture for <1ms search times.
- **Desktop GUI**: Tkinter-based, dark neon theme (`#050510`), auto-displays command details.
- **Ghost Inject**: Direct terminal command insertion using `xdotool` logic.
- **Web GUI**: Flask-based interface accessible at `http://localhost:8501`.

## CLI Examples
```bash
./terminal_commands "docker"     # → docker ps/rm/run/images/stop
./terminal_commands "git"        # → git commit/push/clone/status  
./terminal_commands "ip"         # → ip link/route/neigh
./terminal_commands list         # → All 1,085+ commands
```

## Command Coverage (1,085 Total)
- **Core (256)**: ls -la, git status, python -m, node, rust
- **DevOps (384)**: docker ps, kubectl get pods, aws s3 ls, terraform
- **Networking (64)**: ip link, ss -tuln, traceroute, dig (Enhanced!)
- **Foundry (64)**: android-sdk, gradle, buildozer (Sovereign Foundry)
- **fsociety (32)**: hydra, nmap, exploit-db (Mr. Robot Collection)
- **System (192)**: htop, pmap, pstree, iotop
- **Windows (128)**: Get-Process, winget install, Stop-Service

## Tech Stack
- **data/commands.json**: 1,085+ normalized and categorized commands.
- **main.cpp / search.cpp**: Native C++17 fuzzy search engine using Repository Pattern.
- **gui.py**: Python Tkinter Desktop UI with `xdotool` injection support.
- **web_gui.py**: Flask Web Server with safe CLI execution.

## License
MIT © 2026 Freedomwithin
