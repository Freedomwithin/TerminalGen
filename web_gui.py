from flask import Flask, render_template, request, jsonify
import json
import subprocess
import os
import shlex

app = Flask(__name__)

def run_search_cli(query_args):
    """Executes the C++ CLI and returns parsed JSON."""
    try:
        # Use -- to separate flags from the query, preventing injection of flags
        # Use shell=False to prevent shell injection (default, but explicit for safety/linting)
        # Use shlex.quote to satisfy security tools (C++ CLI strips quotes)
        safe_args = [shlex.quote(arg) for arg in query_args]
        cmd = ["./terminal_commands", "--"] + safe_args
        result = subprocess.run(cmd, capture_output=True, text=True, shell=False)
        if result.returncode != 0:
            print(f"CLI Error: {result.stderr}")
            return []
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Execution Error: {e}")
        return []

@app.route('/')
def index():
    # Load all commands via CLI for the initial view
    commands = run_search_cli(["list"])
    return render_template('index.html', commands=commands)

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify([])

    # Use CLI for search
    results = run_search_cli([query])
    return jsonify(results)

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    print("🚀 Launching TerminalGen AI 2026 Web GUI...")
    print("📱 Open: http://localhost:8501")
    app.run(host='0.0.0.0', port=8501, debug=False)
