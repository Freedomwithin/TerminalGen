# TerminalGen

A lightning-fast C++ command-line tool that puts hundreds of essential commands at your fingertips. Instantly look up command-line syntax, descriptions, and usage examples—all from a comprehensive JSON database.

## Description

Tired of searching for the right command? TerminalGen is your ultimate reference tool, giving you immediate access to a vast library of commands across multiple programming languages, package managers, networking tools, system utilities, and more.

Whether you're using the command-line interface (CLI) for quick lookups or the graphical user interface (GUI) for an interactive experience, this tool ensures you have tons of powerful commands just a search away.

- Look up thousands of commands in seconds
- Search by name, keyword, or category
- Supports programming, security, networking, system monitoring, and more
Never forget a command again!

## Why My Project Stand Out

- Faster lookups with C++: A C++ implementation ensures lightning-fast command lookups, giving you immediate access to the commands you need.
- Wide coverage of system tools, penetration testing, networking, and package managers: This tool covers a broad range of commands from system tools and networking utilities to penetration testing and package managers.
- CLI and GUI options to cater to different preferences: Whether you prefer working in the command line or using a graphical interface, this tool has you covered with both CLI and GUI options.
- Easily extensible: The tool is designed to be easily expanded—anyone can add more commands in the JSON format, making it highly customizable and scalable for different needs.

## Installation/Setup

1.  **Clone the repository (if applicable):**

    ```bash
    git clone https://github.com/Freedomwithin/TerminalGen

    cd TerminalGen
    ```

2.  **Download the nlohmann/json library:**

    * Create the include directories:

        ```bash
        mkdir include
        mkdir include/nlohmann
        ```

    * Download the single header file:

        ```bash
        curl -o include/nlohmann/json.hpp https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp
        ```

3.  **Compile the program:**

    ```bash
    g++ main.cpp -o terminal_commands -std=c++17
    ```

4.  **Ensure the `commands.json` file is in the `data` directory.**

- Make data directory if it does not exists 
```bash
mkdir -p data
```

5.  **Install Python and Tkinter:**

    * If you don't have Python installed, download it from [python.org](https://www.python.org/).
    * Tkinter is typically included with Python installations.

## Usage

## Usage

### Command-Line Interface (CLI)

1. **Run the executable:**
    ```bash
    ./terminal_commands
    ```
2. **Enter a command name** at the prompt to view its description and usage.
3. **Type `list` or `l`** to see all available commands.
4. **Type `search` or `s`** to search for commands by name, description, or usage.
5. **Type `help` or `h`** for help.
6. **Type `exit`** to quit the program.

### Graphical User Interface (GUI)

1. **Run the Python GUI script:**
    ```bash
    python gui.py
    ```
2. **Enter a command name or search term** in the input field.
3. **Click "Lookup Command"** to view the command details.
4. **Double-click a command in the list** to fill the input field.

## Dependencies

* **nlohmann/json:** A C++ JSON library (header-only).
* **A C++17 compatible compiler (e.g., g++).**
* **Python 3.x and Tkinter.**

## Example `commands.json` Structure

```json
[
    {
        "name": "git commit",
        "description": "Commit changes",
        "usage": "git commit -m 'message'",
        "language": "git"
    },
    {
        "name": "cargo build",
        "description": "Build your Rust project",
        "usage": "cargo build",
        "language": "cargo"
    }
]
```

### Included Languages and Categories
This repository contains a comprehensive list of **216 commands** across **175 languages and categories**, including:

<details>
  <summary><u><strong><em>Click to expand languages and categories</em></strong></u></summary

  #### Programming Languages:
  - Bash/Shell, C/C++, C#, Dart, Go, Java, JavaScript (Node.js), Lua, Perl, PHP, Python, Ruby, Rust, Swift

  #### Version Control:
  - Git

  #### Package Managers:
  - apt (Debian/Ubuntu), brew (macOS), cargo (Rust), composer (PHP), dnf (Fedora/CentOS), gem (Ruby), npm (JavaScript), pip (Python), yarn (JavaScript), zypper (openSUSE)

  #### Build Tools:
  - cmake, dotnet, g++ (C++), gradle (Java), javac (Java), make, mvn (Java), rustc (Rust)

  #### Databases:
  - SQL

  #### Text Editors:
  - Nano, Vim

  #### Terminal Multiplexers:
  - abduco, byobu, dtach, dvtm, ratpoison, screen, tmux

  #### Terminal Emulators:
  - alacritty, cool-retro-term, eterm, gnome-terminal, guake, kitty, konsole, lxterminal, mate-terminal, roxterm, rxvt, sakura, st, terminology, tilda, tilix, urxvt, xfce4-terminal, xterm, yakuake

  #### Networking Tools:
  - autossh, curl, curlftpfs, dig, fuseiso, httpie, ifconfig, ip, mosh, nc, ncat, netcat, netstat, ping, route, scp, ssh, sshfs, sshuttle, ss, socat, telnet, traceroute, wget

  #### System Monitoring:
  - df, df -h, free, free -m, htop, iostat, lsof, ps, sar, top, uptime, vmstat

  #### Text Processing:
  - awk, cat, cp, cut, diff, find, grep, head, jq, less, mv, paste, rm, rmdir, sed, sort, tail, tee, touch, tr, uniq, wc

  #### Cloud CLIs:
  - aws (AWS CLI), az (Azure CLI), gcloud (Google Cloud CLI)

  #### Containerization:
  - Docker

  #### Orchestration:
  - Kubernetes

  #### DevOps Tools:
  - ansible-playbook (Ansible), terraform (Terraform), vagrant (Vagrant)

  #### CI/CD:
  - circleci, gitlab-ci, jenkins, travis-ci

  #### Monitoring and Logging:
  - elk (Elasticsearch, Logstash, Kibana), grafana, prometheus, splunk

  #### Security and Compliance:
  - aide, aircrack-ng, arachni, armitage, arpspoof, auditd, beef, bettercap, bloodhound, burpsuite, chkrootkit, clamav, cobaltstrike, commix, crackmapexec, dirb, driftnet, dnschef, dnsenum, dnsrecon, dnsspoof...

</details>


### Recent Updates

### - Added Search Functionality:
- CLI: Implemented a search (or s) command that allows users to search for commands by name, description, or usage. The search term is passed as a command-line argument to the C++ executable.
### - Added GUI:
- GUI: Added a search feature to the GUI, allowing users to enter a search term and view matching commands.
- Implemented a graphical user interface using Tkinter, providing a user-friendly way to interact with the command lookup tool.
- The GUI allows users to enter command names or search terms, view command details, and browse available commands.
### - Added Shorthand Options:
- Added shorthand options for the CLI commands. l for list, s for search, and h for help.


### Contributing
Feel free to submit pull requests to improve the project. You can add more commands to the commands.json file, improve the CLI, or add new features.

### License

[MIT License](https://opensource.org/licenses/MIT)

Copyright (c) [2025] [Freedomwithin]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
