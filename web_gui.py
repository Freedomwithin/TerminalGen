from flask import Flask, render_template, request, jsonify
import json
import subprocess
import os
import shlex

app = Flask(__name__)

def run_search_cli(query_args):
    """Executes the C++ CLI and returns parsed JSON."""
    try:
        # Move to the script's directory for the command execution
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cli_exe = os.path.join(script_dir, "terminal_commands")

        # Don't quote if it's a list for subprocess.run; subprocess handles it safely.
        # But we still use -- to separate flags from the query.
        cmd = [cli_exe, "--"] + query_args
        result = subprocess.run(cmd, capture_output=True, text=True, shell=False, cwd=script_dir)
        if result.returncode != 0:
            return []
        return json.loads(result.stdout)
    except Exception as e:
        return []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '').strip()
    # If no query, return 'list' for the initial load
    if not query:
        results = run_search_cli(["list"])
    else:
        results = run_search_cli([query])
    return jsonify(results)

@app.route('/cli')
def run_cli_route():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({"output": "No query provided"})
    
    # Run the search CLI and return the raw first match as a 'simulated' execution
    results = run_search_cli([query])
    if results:
        return jsonify({"output": f"Executing: {results[0]['usage']}\n\n{results[0]['description']}"})
    return jsonify({"output": "Command not found in neural matrix"})

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    print("🚀 Launching TerminalGen AI 2026 Web GUI...")
    print("📱 Open: http://localhost:8501")
    app.run(host='0.0.0.0', port=8501, debug=False)
