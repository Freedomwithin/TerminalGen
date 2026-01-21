import tkinter as tk
from tkinter import ttk, scrolledtext
import json
import subprocess
import math

class TerminalGenFuturism:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🤖 TERMINALGEN AI v2026")
        self.root.geometry("1400x900")
        self.root.configure(bg='#0a0a1a')
        self.root.resizable(True, True)
        
        self.commands = self.load_commands()
        self.time = 0
        self.setup_futuristic_ui()
        self.start_particle_system()
    
    def load_commands(self):
        try:
            with open('data/commands.json', 'r') as f:
                return json.load(f)
        except:
            return []
    
    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def create_gradient_canvas(self, parent, width, height, color1='#0a0a1a', color2='#1a0033'):
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
        main_frame = tk.Frame(self.root, bg='#0f0f23')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Holographic title
        title_frame = tk.Frame(main_frame, bg='#1a1a2e', relief='raised', bd=3)
        title_frame.pack(fill='x', pady=(0,20))
        
        self.canvas = self.create_gradient_canvas(title_frame, 1300, 100)
        title_label = tk.Label(self.canvas, text="🤖 TERMINALGEN AI 2026", 
                              font=('Arial', 32, 'bold'), bg='#1a1a2e', fg='#00ffcc')
        title_label.place(x=650, y=35, anchor='center')
        
        # Glass search bar
        search_frame = tk.Frame(main_frame, bg='#1a1a2e', relief='raised', bd=3)
        search_frame.pack(fill='x', pady=10)
        
        tk.Label(search_frame, text="🧠 NEURAL COMMAND SEARCH", 
                font=('Arial', 16, 'bold'), bg='#1a1a2e', fg='#00ffcc').pack(side='left', padx=20, pady=15)
        
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, 
                                   font=('Arial', 14), bg='#0f0f23', fg='white', 
                                   insertbackground='#00ffcc', relief='solid', bd=3,
                                   highlightthickness=3, highlightcolor='#00ffcc')
        self.search_entry.pack(side='left', padx=20, pady=15, fill='x', expand=True)
        self.search_entry.bind('<KeyRelease>', self.ai_live_search)
        
        # Neon buttons
        btn_frame = tk.Frame(search_frame, bg='#1a1a2e')
        btn_frame.pack(side='right', padx=20, pady=15)
        
        buttons = [
            ("🌐 ALL", self.show_all_commands, '#00ff88'),
            ("⚡ CLI", self.run_cli_live, '#ff0080'),
            ("🧹 CLEAR", self.clear_interface, '#6666ff'),
            ("📋 COPY", self.copy_selected, '#ffaa00')
        ]
        
        for text, cmd, color in buttons:
            btn = tk.Button(btn_frame, text=text, command=cmd, bg=color, fg='black',
                          font=('Arial', 12, 'bold'), relief='raised', bd=4,
                          padx=25, pady=10)
            btn.pack(side='left', padx=10)
        
        # Split panels
        panels_frame = tk.Frame(main_frame, bg='#0f0f23')
        panels_frame.pack(fill='both', expand=True)
        
        # Left panel - Command Matrix
        left_frame = tk.Frame(panels_frame, bg='#1a1a2e', relief='raised', bd=3)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0,15))
        
        tk.Label(left_frame, text="📋 QUANTUM MATRIX", font=('Arial', 16, 'bold'),
                bg='#1a1a2e', fg='#00ff88').pack(pady=15)
        
        list_frame = tk.Frame(left_frame)
        list_frame.pack(fill='both', expand=True, padx=25, pady=15)
        
        self.command_matrix = tk.Listbox(list_frame, bg='#0f0f23', fg='#00ffcc', 
                                       font=('Courier', 12), selectbackground='#00ff88',
                                       selectforeground='black', relief='solid', bd=3)
        matrix_scroll = tk.Scrollbar(list_frame, orient='vertical', bg='#1a1a2e')
        self.command_matrix.configure(yscrollcommand=matrix_scroll.set)
        matrix_scroll.config(command=self.command_matrix.yview)
        
        self.command_matrix.pack(side='left', fill='both', expand=True)
        matrix_scroll.pack(side='right', fill='y')
        
        self.command_matrix.bind('<<ListboxSelect>>', self.show_ai_analysis)
        self.command_matrix.bind('<Double-1>', self.instant_copy)
        
        # Right panel - AI Terminal
        right_frame = tk.Frame(panels_frame, bg='#1a1a2e', relief='raised', bd=3)
        right_frame.pack(side='right', fill='both', expand=True, padx=(15,0))
        
        tk.Label(right_frame, text="🤖 AI TERMINAL", font=('Arial', 16, 'bold'),
                bg='#1a1a2e', fg='#ff0080').pack(pady=15)
        
        self.ai_terminal = scrolledtext.ScrolledText(right_frame, bg='#0f0f23', fg='#00ffcc',
                                                   font=('Courier', 11, 'bold'), wrap=tk.WORD,
                                                   relief='solid', bd=3)
        self.ai_terminal.pack(fill='both', expand=True, padx=25, pady=15)
        
        # Status bar
        self.stats_label = tk.Label(main_frame, text=f"🧬 {len(self.commands)} quantum nodes | Neural sync ready",
                                  bg='#0f0f23', fg='#00ffcc', font=('Arial', 12, 'bold'))
        self.stats_label.pack(side='bottom', fill='x', pady=15)
        
        self.show_all_commands()
    
    def ai_live_search(self, event=None):
        query = self.search_var.get().lower()
        self.command_matrix.delete(0, tk.END)
        matches = 0
        
        for cmd in self.commands:
            score = 0
            if query in cmd['name'].lower(): score += 3
            if query in cmd['description'].lower(): score += 2  
            if query in cmd['usage'].lower(): score += 1
            
            if score > 0:
                confidence = "█" * int(score * 3) + "░" * (9 - int(score * 3))
                display = f"[{confidence}] {cmd.get('language', 'AI')} {cmd['name']}"
                self.command_matrix.insert(tk.END, display)
                matches += 1
        
        self.stats_label.config(text=f"🧠 Neural matches: {matches} | Pattern recognition active")
    
    def show_all_commands(self):
        self.search_var.set('')
        self.command_matrix.delete(0, tk.END)
        for cmd in self.commands:
            display = f"[████████░] {cmd.get('language', 'CORE')} {cmd['name']}"
            self.command_matrix.insert(tk.END, display)
        self.stats_label.config(text=f"🧬 Quantum matrix: {len(self.commands)} nodes | Full spectrum scan")
    
    def show_ai_analysis(self, event=None):
        sel = self.command_matrix.curselection()
        if sel:
            idx = sel[0]
            cmd = self.commands[idx]
            analysis = f"""
╔══════════════════════════════════════════════════════╗
║  🤖 AI COMMAND ANALYSIS ENGINE v2026                  ║
╠══════════════════════════════════════════════════════║
║  🧬 TARGET: {cmd['name'].upper():<35}                    ║
║  🌐 VECTOR: {cmd.get('language', 'QUANTUM'):<35}         ║
║  📊 CONFIDENCE: ██████████100%                        ║
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
        if sel:
            idx = sel[0]
            cmd = self.commands[idx]
            self.root.clipboard_clear()
            self.root.clipboard_append(cmd['usage'])
            self.ai_terminal.insert(tk.END, "\n\n🧠 QUANTUM TRANSFER COMPLETE → CLIPBOARD")
    
    def run_cli_live(self):
        query = self.search_var.get()
        if query:
            try:
                process = subprocess.Popen(["./terminal_commands", query], 
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()
                result = stdout + stderr if stdout else "CLI → No output"
                self.ai_terminal.delete(1.0, tk.END)
                self.ai_terminal.insert(1.0, f"⚡ LIVE CLI EXECUTION:\n\n{result}")
            except:
                self.ai_terminal.delete(1.0, tk.END)
                self.ai_terminal.insert(1.0, "⚠️  CLI NODE OFFLINE")
    
    def copy_selected(self):
        sel = self.command_matrix.curselection()
        if sel:
            idx = sel[0]
            cmd = self.commands[idx]
            self.root.clipboard_clear()
            self.root.clipboard_append(cmd['usage'])
            self.stats_label.config(text="📋 QUANTUM TRANSFER → EXECUTION READY")
    
    def clear_interface(self):
        self.search_var.set('')
        self.command_matrix.delete(0, tk.END)
        self.ai_terminal.delete(1.0, tk.END)
        self.stats_label.config(text=f"🧬 Neural matrix cleared | {len(self.commands)} nodes ready")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TerminalGenFuturism()
    app.run()
