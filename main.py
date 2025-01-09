import tkinter as tk
from datetime import datetime, timedelta

class StopwatchGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Worklogger Stopwatch")
        self.root.minsize(300, 150)
        self.root.configure(bg='black')
        
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.is_running = False
        self.elapsed_time = timedelta()
        self.start_time = None
        
        self.time_label = tk.Label(
            main_frame,
            text="00:00:00.00",
            font=("calibri", 40),
            wraplength=400,
            bg='black',
            fg='#00ff00'
        )
        self.time_label.pack(expand=True, fill='both', pady=20)
        
        button_frame = tk.Frame(main_frame, bg='black')
        button_frame.pack(expand=True, fill='x', pady=10)
        
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        self.start_button = tk.Button(
            button_frame,
            text="Start",
            command=self.start_stop,
            font=("Arial", 14),
            width=10,
            height=2,
            bg='black',
            fg='#00ff00',
            highlightbackground='#00ff00',
            activebackground='black',
            activeforeground='#00ff00'
        )
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset,
            font=("Arial", 14),
            width=10,
            height=2,
            bg='black',
            fg='#00ff00',
            highlightbackground='#00ff00',
            activebackground='black',
            activeforeground='#00ff00'
        )
        self.reset_button.grid(row=0, column=1, padx=10)
        
        self.update_time()
        
    def start_stop(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(text="Start")
            if self.start_time:
                self.elapsed_time += datetime.now() - self.start_time
        else:
            self.is_running = True
            self.start_button.config(text="Stop")
            self.start_time = datetime.now()
    
    def reset(self):
        self.is_running = False
        self.start_button.config(text="Start")
        self.elapsed_time = timedelta()
        self.start_time = None
        self.time_label.config(text="00:00:00.00")
    
    

if __name__ == "__main__":
    stopwatch = StopwatchGUI()
    stopwatch.run()
