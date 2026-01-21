from flask import Flask, render_template, request, jsonify
import json
import subprocess
import os

app = Flask(__name__)

# Load commands
try:
    with open('data/commands.json', 'r') as f:
        COMMANDS = json.load(f)
except:
    COMMANDS = []

@app.route('/')
def index():
    return render_template('index.html', commands=COMMANDS)

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = []
    for cmd in COMMANDS:
        if (query in cmd['name'].lower() or 
            query in cmd['description'].lower() or 
            query in cmd['usage'].lower()):
            results.append(cmd)
    return jsonify(results)

@app.route('/cli')
def run_cli():
    query = request.args.get('q', '')
    try:
        result = subprocess.run(["./terminal_commands", query], 
                              capture_output=True, text=True, timeout=5)
        return jsonify({"output": result.stdout + result.stderr})
    except:
        return jsonify({"output": "⚠️ CLI executable not found - run './terminal_commands'"})

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    print("🚀 Launching TerminalGen AI 2026 Web GUI...")
    print("📱 Open: http://localhost:8501")
    app.run(host='0.0.0.0', port=8501, debug=False)
