import tkinter as tk
from tkinter import ttk, scrolledtext
import json
import subprocess
import math
import os
import shlex

class TerminalGenFuturism:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🤖 TERMINALGEN AI v2026")
        self.root.geometry("1400x900")
        # Darker theme as requested
        self.bg_color = '#050510'
        self.panel_color = '#0a0a1a'
        self.accent_color = '#00ffcc'
        self.text_color = '#ffffff'
        self.matrix_green = '#22c55e'
        self.matrix_pink = '#ec4899'
        self.cli_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "terminal_commands")

        self.root.configure(bg=self.bg_color)
        self.root.resizable(True, True)
        
        self.commands = [] # Will be populated by search results
        self.time = 0
        self.setup_futuristic_ui()
        self.start_particle_system()

        # Initial load
        self.show_all_commands()
    
    def run_cli(self, args):
        try:
            cmd = [self.cli_path] + args
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"CLI Error: {result.stderr}")
                return []
            return json.loads(result.stdout)
        except Exception as e:
            print(f"Execution Error: {e}")
            return []

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def create_gradient_canvas(self, parent, width, height, color1='#050510', color2='#1a0033'):
        canvas = tk.Canvas(parent, width=width, height=height, highlightthickness=0, bg=color1)
        
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)
        
        for i in range(width):
            ratio = i / width
            r = int(r1 * (1 - ratio) + r2 * ratio)
            g = int(g1 * (1 - ratio) + g2 * ratio)
            b = int(b1 * (1 - ratio) + b2 * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            canvas.create_line(i, 0, i, height, fill=color, width=1)
        
        canvas.pack(fill='both', expand=True)
        return canvas
    
    def start_particle_system(self):
        self.animate_particles()
        self.root.after(50, self.start_particle_system)
    
    def animate_particles(self):
        self.time += 0.05
        if hasattr(self, 'canvas'):
            self.canvas.delete("particle")
            
            for i in range(40):
                x = 100 + math.sin(self.time + i * 0.3) * 300 + i * 25
                y = 100 + math.cos(self.time * 0.8 + i * 0.2) * 200 + i * 15
                size = 3 + math.sin(self.time * 4 + i) * 2
                
                r = int(0 + 155 * 0.7)
                g = int(255 * 0.7)
                b = int(204 * 0.7)
                color = f'#{r:02x}{g:02x}{b:02x}'
                
                self.canvas.create_oval(x-size, y-size, x+size, y+size, 
                                      fill=color, outline='', tags="particle")
    
    def setup_futuristic_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg=self.panel_color)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Holographic title
        title_frame = tk.Frame(main_frame, bg=self.panel_color, relief='raised', bd=1)
        title_frame.pack(fill='x', pady=(0,20))
        
        self.canvas = self.create_gradient_canvas(title_frame, 1300, 100, color1=self.bg_color, color2=self.panel_color)
        title_label = tk.Label(self.canvas, text="🤖 TERMINALGEN — SOVEREIGN AI", 
                              font=('Arial', 32, 'bold'), bg=self.panel_color, fg=self.accent_color)
        title_label.place(x=650, y=35, anchor='center')
        
        # Glass search bar
        search_frame = tk.Frame(main_frame, bg=self.panel_color, relief='raised', bd=1)
        search_frame.pack(fill='x', pady=10)
        
        tk.Label(search_frame, text="🧠 NEURAL COMMAND SEARCH", 
                font=('Arial', 14, 'bold'), bg=self.panel_color, fg=self.accent_color).pack(side='left', padx=20, pady=15)
        
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, 
                                   font=('Arial', 14), bg='#0f0f23', fg=self.text_color, 
                                   insertbackground=self.accent_color, relief='solid', bd=1,
                                   highlightthickness=2, highlightcolor=self.accent_color)
        self.search_entry.pack(side='left', padx=20, pady=15, fill='x', expand=True)
        self.search_entry.bind('<KeyRelease>', self.ai_live_search)
        
        # Neon buttons
        btn_frame = tk.Frame(search_frame, bg=self.panel_color)
        btn_frame.pack(side='right', padx=20, pady=15)
        
        buttons = [
            ("🌐 ALL", self.show_all_commands, self.matrix_green),
            ("⚡ INJECT", self.inject_to_terminal, self.matrix_pink),
            ("🧹 CLEAR", self.clear_interface, '#4f46e5'),
            ("📋 COPY", self.copy_selected, '#d97706')
        ]
        
        for text, cmd, color in buttons:
            btn = tk.Button(btn_frame, text=text, command=cmd, bg=color, fg='white',
                          font=('Arial', 11, 'bold'), relief='flat', bd=0,
                          padx=25, pady=8)
            btn.pack(side='left', padx=10)
        
        # Split panels
        panels_frame = tk.Frame(main_frame, bg='#0f0f23')
        panels_frame.pack(fill='both', expand=True)
        
        # Left panel - Command Matrix
        left_frame = tk.Frame(panels_frame, bg=self.panel_color, relief='raised', bd=1)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0,15))
        
        tk.Label(left_frame, text="📋 COMMAND MATRIX", font=('Arial', 14, 'bold'),
                bg=self.panel_color, fg=self.matrix_green).pack(pady=15)
        
        list_frame = tk.Frame(left_frame)
        list_frame.pack(fill='both', expand=True, padx=25, pady=15)
        
        self.command_matrix = tk.Listbox(list_frame, bg='#08080f', fg=self.text_color,
                                       font=('Courier', 12), selectbackground=self.accent_color,
                                       selectforeground='white', relief='flat', bd=0)
        matrix_scroll = tk.Scrollbar(list_frame, orient='vertical', bg=self.panel_color)
        self.command_matrix.configure(yscrollcommand=matrix_scroll.set)
        matrix_scroll.config(command=self.command_matrix.yview)
        
        self.command_matrix.pack(side='left', fill='both', expand=True)
        matrix_scroll.pack(side='right', fill='y')
        
        self.command_matrix.bind('<<ListboxSelect>>', self.show_ai_analysis)
        self.command_matrix.bind('<Double-1>', self.instant_copy)
        
        # Right panel - AI Terminal
        right_frame = tk.Frame(panels_frame, bg=self.panel_color, relief='raised', bd=1)
        right_frame.pack(side='right', fill='both', expand=True, padx=(15,0))
        
        tk.Label(right_frame, text="🤖 SOVEREIGN TERMINAL", font=('Arial', 14, 'bold'),
                bg=self.panel_color, fg=self.matrix_pink).pack(pady=15)
        
        self.ai_terminal = scrolledtext.ScrolledText(right_frame, bg='#08080f', fg=self.accent_color,
                                                   font=('Courier', 11, 'bold'), wrap=tk.WORD,
                                                   relief='flat', bd=0)
        self.ai_terminal.pack(fill='both', expand=True, padx=25, pady=15)
        
        # Status bar
        self.stats_label = tk.Label(main_frame, text=f"🧬 Sovereign Resonance Active...",
                                  bg='#0c0c16', fg=self.accent_color, font=('Arial', 10, 'bold'))
        self.stats_label.pack(side='bottom', fill='x', pady=15)
        
    
    def ai_live_search(self, event=None):
        query = self.search_var.get().strip()
        self.command_matrix.delete(0, tk.END)
        
        if not query:
            self.show_all_commands()
            return
            
        results = self.run_cli([query])
        self.commands = results

        for cmd in results:
            lang = cmd.get('language', 'CORE').upper()
            display = f"{lang:<10} | {cmd['name']}"
            self.command_matrix.insert(tk.END, display)
        
        self.stats_label.config(text=f"🧠 Neural matches: {len(results)} | Native CLI accelerated")
    
    def show_all_commands(self):
        self.search_var.set('')
        self.command_matrix.delete(0, tk.END)

        results = self.run_cli(["list"])
        self.commands = results

        for cmd in results:
            lang = cmd.get('language', 'CORE').upper()
            display = f"{lang:<10} | {cmd['name']}"
            self.command_matrix.insert(tk.END, display)
        self.stats_label.config(text=f"🧬 Quantum matrix: {len(self.commands)} nodes | Full spectrum scan")
    
    def show_ai_analysis(self, event=None):
        sel = self.command_matrix.curselection()
        if sel:
            idx = sel[0]
            if idx < len(self.commands):
                cmd = self.commands[idx]
                analysis = f"""
╔══════════════════════════════════════════════════════╗
║  🤖 AI COMMAND ANALYSIS ENGINE v2026                  ║
╠══════════════════════════════════════════════════════║
║  🧬 TARGET: {cmd['name'].upper():<35}                    ║
║  🌐 VECTOR: {cmd.get('language', 'QUANTUM'):<35}         ║
╠══════════════════════════════════════════════════════║
║  💭 INTELLIGENCE:                                      ║
║     {cmd['description']:<52}                           ║
║                                                       ║
║  💻 EXECUTION MATRIX:                                 ║
║     {cmd['usage']:<52}                                 ║
╚══════════════════════════════════════════════════════╝
            """
                self.ai_terminal.delete(1.0, tk.END)
                self.ai_terminal.insert(1.0, analysis)
    
    def instant_copy(self, event=None):
        sel = self.command_matrix.curselection()
        if sel and sel[0] < len(self.commands):
            idx = sel[0]
            cmd = self.commands[idx]
            self.root.clipboard_clear()
            self.root.clipboard_append(cmd['usage'])
            self.ai_terminal.insert(tk.END, "\n\n🧠 QUANTUM TRANSFER COMPLETE → CLIPBOARD")
    
    def inject_to_terminal(self):
        sel = self.command_matrix.curselection()
        if sel and sel[0] < len(self.commands):
            idx = sel[0]
            cmd = self.commands[idx]
            usage = cmd['usage']
            
            # Sovereign Ghost Strike: Hide -> Focus -> Type -> Show
            # We use xdotool to focus the previous window (the terminal) and type the command
            self.root.withdraw() # Hide TerminalGen
            try:
                # 1. Wait a moment for focus to shift naturally to the terminal
                # 2. Focus the terminal (Alt+Tab or just relying on focus-follows-last)
                # 3. Type the command
                subprocess.run(["xdotool", "key", "alt+Tab"], check=False)
                subprocess.run(["sleep", "0.2"], check=False)
                subprocess.run(["xdotool", "type", "--clearmodifiers", usage], check=False)
            except Exception as e:
                print(f"Injection Error: {e}")
            
            self.root.after(500, self.root.deiconify) # Show TerminalGen again
            self.stats_label.config(text="⚡ NEURAL INJECTION COMPLETE → TERMINAL")
    
    def copy_selected(self):
        sel = self.command_matrix.curselection()
        if sel and sel[0] < len(self.commands):
            idx = sel[0]
            cmd = self.commands[idx]
            self.root.clipboard_clear()
            self.root.clipboard_append(cmd['usage'])
            self.stats_label.config(text="📋 QUANTUM TRANSFER → EXECUTION READY")
    
    def clear_interface(self):
        self.search_var.set('')
        self.command_matrix.delete(0, tk.END)
        self.ai_terminal.delete(1.0, tk.END)
        self.commands = []
        self.stats_label.config(text=f"🧬 Neural matrix cleared")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TerminalGenFuturism()
    app.run()
