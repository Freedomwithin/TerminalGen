# TerminalGen ★ 450+ Commands

A lightning-fast C++ command-line tool that puts **450+ essential commands** at your fingertips. Instantly look up command-line syntax, descriptions, and usage examples.

## Description

Tired of searching for the right command? TerminalGen is your ultimate reference tool, giving you immediate access to a vast library of commands across multiple programming languages, package managers, networking tools, system utilities, and more.

Whether you're using the command-line interface (CLI) for quick lookups or the graphical user interface (GUI) for an interactive experience, this tool ensures you have tons of powerful commands just a search away.

- Look up thousands of commands in seconds
- Search by name, keyword, or category
- Supports programming, security, networking, system monitoring, and more
Never forget a command again!

## Quick Start (30 seconds)

```bash
git clone https://github.com/Freedomwithin/TerminalGen
cd TerminalGen
mkdir -p include/nlohmann data
curl -o include/nlohmann/json.hpp https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp
g++ main.cpp -o terminalgen -std=c++17
./terminalgen "process"  # → htop/ps/pgrep instantly
```

##  Why TerminalGen?
⚡ Lightning-fast: C++ implementation for instant lookups

📚 450+ commands across 25+ categories (Bash, Git, Python, Docker, K8s, PowerShell, AWS CLI, etc.)

🔍 Fuzzy search: Type "process" → get htop, ps, pgrep, top

🎨 Dual interface: CLI + Python/Tkinter GUI

✨ Extensible: Add commands via simple JSON

📋 Coverage (450+ Commands)
Core: Bash, Git, Python, Rust, Node.js, PowerShell
DevOps: Docker, Kubernetes, Terraform, AWS/Azure/GCP CLIs
System: Monitoring (htop, iotop), networking (dig, nslookup), file processing
Databases: SQL
Windows: PowerShell essentials (Get-Process, Stop-Process)

## 🚀 Usage
Command-Line Interface (CLI)
bash
./terminalgen                    # Interactive mode
./terminalgen "process"         # Direct search
./terminalgen list              # List all commands
./terminalgen search git        # Fuzzy search
./terminalgen help              # Help
# Shortcuts: l=list, s=search, h=help
Graphical User Interface (GUI)
bash
python gui.py
Search by name/description/usage

Double-click to copy command

Browse all 450+ commands

🛠️ Installation
Clone & Setup:

```bash
git clone https://github.com/Freedomwithin/TerminalGen
cd TerminalGen
mkdir -p include/nlohmann data
Download JSON library:
```
```bash
curl -o include/nlohmann/json.hpp https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp
Compile C++ CLI:
```
```bash
g++ main.cpp -o terminalgen -std=c++17
chmod +x terminalgen
Ensure data/commands.json exists (450+ commands included)
```
📦 Dependencies
C++17 compiler (g++)

nlohmann/json (header-only, auto-downloaded)

Python 3 + Tkinter (GUI only)

📁 Example commands.json
json
[
  {
    "name": "git commit",
    "description": "Commit changes",
    "usage": "git commit -m 'message'",
    "language": "git"
  },
  {
    "name": "htop",
    "description": "Interactive process viewer",
    "usage": "htop",
    "language": "bash"
  }
]
✨ Recent Updates
450+ commands (was 216) - comprehensive dev coverage

Fuzzy search upgraded for better relevance

PowerShell commands added for Windows/WSL users

Shorthand CLI: l (list), s (search), h (help)

🤝 Contributing
Add commands to data/commands.json

Submit PR with new entries

Improve search algorithms

Add new language categories

📄 License
MIT License

Copyright (c) 2026 Freedomwithin