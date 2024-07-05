import tkinter as tk
from tkinter import ttk
import time
import threading

class ProgressBarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Bar Example")

        self.progress = tk.DoubleVar()
        
        self.label = tk.Label(root, text="Progress:")
        self.label.pack(pady=10)

        self.progressbar = ttk.Progressbar(root, variable=self.progress, maximum=100)
        self.progressbar.pack(fill=tk.X, padx=20, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_task)
        self.start_button.pack(pady=10)
        
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)

    def start_task(self):
        self.progress.set(0)
        self.status_label.config(text="Task in progress...")
        threading.Thread(target=self.run_task).start()

    def run_task(self):
        num_steps = 100
        for i in range(num_steps):
            time.sleep(0.1)  # Simulating a task with a delay
            self.progress.set((i + 1) / num_steps * 100)
        self.status_label.config(text="Task completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProgressBarApp(root)
    root.mainloop()
