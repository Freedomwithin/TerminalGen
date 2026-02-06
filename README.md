# TerminalGen: 1,024+ Commands

**Lightning-fast C++ CLI** | **Neon Desktop GUI** | **Quantum Web GUI**  

**Instant fuzzy search across 1,024+ DevOps commands (bash, git, docker, k8s, aws, python, powershell).
Replaces tldr/cheat.sh with 1000x speed + native support for Linux Mint, Windows, and macOS. Search "docker", get every command instantly. Fully offline capable with a native C++ engine.**

## Click the image to see the demo!
[![TerminalGen demo picture](https://github.com/user-attachments/assets/48a0dc55-2d9c-4422-866c-ab5b34a8ba30)](https://terminal-moyt0r11s-jonathon-koerners-projects.vercel.app/)

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
- **Web GUI**: Flask-based interface accessible at `http://localhost:8501`.
- **Security First**: Strict input sanitization and safe subprocess handling.

## CLI Examples
```bash
./terminal_commands "docker"     # → docker ps/rm/run/images/stop
./terminal_commands "git"        # → git commit/push/clone/status  
./terminal_commands "ip"         # → ip link/route/neigh (New!)
./terminal_commands list         # → All 1,024+ commands
```

### Configuration
You can specify a custom commands database location:
```bash
# Via Environment Variable
export TERMINAL_GEN_DATA=/path/to/my_commands.json
./terminal_commands "search"

# Via CLI Flag
./terminal_commands --data custom.json "search"
```

## Command Coverage (1,024+ Total)
- **Core (256)**: ls -la, git status, python -m, node, rust
- **DevOps (384)**: docker ps, kubectl get pods, aws s3 ls, terraform
- **Networking (64)**: ip link, ss -tuln, traceroute, dig, nslookup (Enhanced!)
- **System (192)**: htop, dig, pmap, pstree, iotop
- **Windows (128)**: Get-Process, winget install, Stop-Service
- **Cloud (64)**: gcloud compute, az login, terraform apply

## Tech Stack
- **data/commands.json**: 1,024+ normalized and categorized commands.
- **main.cpp / search.cpp**: Native C++17 fuzzy search engine using Repository Pattern.
- **gui.py**: Python Tkinter Desktop UI with `subprocess` integration.
- **web_gui.py**: Flask Web Server with safe CLI execution.
- **setup.sh**: Automated build and launch script.

## License
MIT © 2026 Freedomwithin
