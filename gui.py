import tkinter as tk
import subprocess
import json

def load_commands(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def run_command(command):
    try:
        process = subprocess.Popen(["./terminal_commands", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        return stdout + stderr
    except FileNotFoundError:
        return "Error: terminal_commands executable not found."
    except Exception as e:
        return f"Error: {e}"

def lookup_command():
    command_name = entry.get()
    result = run_command(command_name)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

def populate_list():
    commands = load_commands("data/commands.json")
    listbox.delete(0, tk.END)
    for command in commands:
        listbox.insert(tk.END, command["name"])

def listbox_click(event):
    selected_command = listbox.get(listbox.curselection())
    entry.delete(0, tk.END)
    entry.insert(tk.END, selected_command)

root = tk.Tk()
root.title("Terminal Commands GUI")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

lookup_button = tk.Button(root, text="Lookup Command", command=lookup_command)
lookup_button.pack()

output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=10)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)
listbox.bind('<Double-1>', listbox_click)

populate_list()

root.mainloop()