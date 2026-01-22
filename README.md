# TerminalGen ★ 450+ Commands

**Lightning-fast C++ CLI** | **Desktop GUI** | **Web GUI**  
**Search 450+ essential commands instantly** (bash/git/docker/python/k8s/powershell)

[![CLI Demo](https://img.shields.io/badge/CLI-Demo-brightgreen)](https://github.com/Freedomwithin/TerminalGen)
[![Desktop GUI](https://img.shields.io/badge/GUI-Desktop-blue)](https://github.com/Freedomwithin/TerminalGen)
[![Web GUI](https://img.shields.io/badge/Web-localhost:8501-orange)](https://github.com/Freedomwithin/TerminalGen)

## 🚀 One-Click Setup (30 seconds)

```bash
git clone https://github.com/Freedomwithin/TerminalGen.git
cd TerminalGen
chmod +x setup.sh
./setup.sh  # Compiles CLI + launches Desktop + Web GUIs!
Linux/WSL/Mac: Native support
Windows: WSL or Git Bash
```

🎯 What You Get Instantly
text
✅ C++ CLI: ./terminal_commands "docker" → docker ps/rm/run
✅ Desktop GUI: Futuristic Tkinter window (1400x900)
✅ Web GUI: http://localhost:8501 (Flet-powered)
✅ 450+ commands: bash/git/python/docker/k8s/powershell
💥 Usage Examples
bash
# CLI (lightning fast)
./terminal_commands "process"    # → htop ps pgrep pstree pmap
./terminal_commands "docker"     # → docker ps rm run images
./terminal_commands list         # → All 450 commands
./terminal_commands "git"        # → git commit push clone

# GUIs auto-launch
Desktop: New window opens (search + copy)
Web:     http://localhost:8501
📊 Coverage (450+ Commands)
Category	Examples
Core	bash, git, python, rust, node, powershell
DevOps	docker, kubernetes, terraform, aws/azure/gcp
System	htop, iotop, dig, nslookup, pmap, pstree
Windows	Get-Process, Stop-Process, winget
🎨 Triple Threat Interface
C++ CLI - Zero startup, instant search

Desktop GUI - Futuristic dark theme (#0a0a1a)

Web GUI - http://localhost:8501 (browser-friendly)

🛠️ Under the Hood
text
450+ commands → data/commands.json
C++ fuzzy search → main.cpp (nlohmann/json)
Desktop GUI → gui.py (Tkinter)
Web GUI → web_gui.py (Flet)
One-click → setup.sh
✨ Why TerminalGen Beats Everything
Feature	TerminalGen	tldr	cheat.sh
Speed	C++ (instant)	JS (medium)	Network (slow)
Offline	✅ 450+ local	✅	❌
GUI	✅ Desktop + Web	❌	❌
Windows	✅ PowerShell	✅	✅
Categories	25+	10+	Varies
🤝 Contributing
Add commands: data/commands.json

Submit PR with new entries

Improve fuzzy search algorithm

New GUI themes/languages

📄 License
MIT © 2026 Freedomwithin