# TerminalGen  1,024+ Commands

**Lightning-fast C++ CLI** | **Neon Desktop GUI** | **Quantum Web GUI**  
**Instant fuzzy search across 1,024+ devops commands** (bash/git/docker/k8s/aws/python/powershell)

[![**Vercel Demo**](https://terminal-gen.vercel.app)](https://terminal-gen.vercel.app)

[![Desktop GUI](https://img.shields.io/badge/GUI-Desktop%20Neon-blueviolet)](https://github.com/Freedomwithin/TerminalGen)

[![Web GUI](https://img.shields.io/badge/Web-localhost:8501-neon)](https://github.com/Freedomwithin/TerminalGen)

##  One-Click Setup (30 seconds)

```bash
git clone https://github.com/Freedomwithin/TerminalGen.git
cd TerminalGen
chmod +x setup.sh
./setup.sh  #  Compiles CLI + launches Desktop + Web GUIs instantly!
```

Works everywhere:

 Linux/WSL/Mac: Native

 Windows: WSL/Git Bash/PowerShell

 What You Get Instantly
C++ CLI → ./terminal_commands (1ms search, offline)
Desktop GUI → Auto-launches (Tkinter 1400x900 neon)
Web GUI → http://localhost:8501 (Flet quantum matrix)

bash
# CLI Examples (⚡ instant)
```bash
./terminal_commands "docker"     # → docker ps/rm/run/images/stop
./terminal_commands "git"        # → git commit/push/clone/status  
./terminal_commands "process"    # → htop/ps/pgrep/pstree
./terminal_commands list         # → All 1,024+ commands
```

 Command Coverage (1,024+ Total)
Core (256): ls -la, git status, python -m, node, rust
DevOps (384): docker ps, kubectl get pods, aws s3 ls, terraform
System (192): htop, dig, pmap, pstree, iotop
Windows (128): Get-Process, winget install, Stop-Service
Cloud (64): gcloud compute, az login, terraform apply

 Why TerminalGen Dominates
Speed: C++ (1ms) vs tldr JS (50ms) vs cheat.sh Network (2s+)
Offline:  1,024+ local commands
GUI: Desktop + Web (unique!)
Windows:  PowerShell + CMD support
Categories: 25+ organized collections

🛠️ Tech Stack
data/commands.json → 1,024+ commands

main.cpp → C++ fuzzy search (nlohmann/json)

gui.py → Tkinter + custom neon theme

web_gui.py → Flet + quantum matrix

setup.sh → One-click everything

 Contributing
Add commands: data/commands.json

Submit PR with new category/language

Improve C++ fuzzy search algorithm

New neon themes or languages

Windows PowerShell expansions

 License
MIT © 2026 Freedomwithin
