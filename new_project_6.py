import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
import time
from sorting import *
from searching import *

class AlgorithmVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualizer")
        self.root.state('zoomed')  # Allow maximized window

        # Control Variables
        self.running = False
        self.target_value = None
        self.speed = 1

        # UI Elements
        self.create_widgets()
        self.update_ui()

        self.data = []

    def create_widgets(self):
        # Header Frame
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, pady=10)

        ttk.Label(header_frame, text="Algorithm Visualizer", font=("Helvetica", 20, "bold")).pack()

        # Control Frame
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, pady=10)

        self.type_label = ttk.Label(control_frame, text="Select Type:")
        self.type_label.grid(row=0, column=0, padx=10, pady=5)

        self.type_combo = ttk.Combobox(control_frame, values=["Sorting", "Searching"], state="readonly")
        self.type_combo.grid(row=0, column=1, padx=10, pady=5)
        self.type_combo.current(0)

        self.algorithm_label = ttk.Label(control_frame, text="Select Algorithm:")
        self.algorithm_label.grid(row=0, column=2, padx=10, pady=5)

        self.algorithm_combo = ttk.Combobox(control_frame, values=[], state="readonly")
        self.algorithm_combo.grid(row=0, column=3, padx=10, pady=5)

        self.run_button = ttk.Button(control_frame, text="Run", command=self.start_algorithm)
        self.run_button.grid(row=0, column=4, padx=10, pady=5)

        self.stop_button = ttk.Button(control_frame, text="Stop", command=self.stop_algorithm)
        self.stop_button.grid(row=0, column=5, padx=10, pady=5)

        self.reset_button = ttk.Button(control_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=6, padx=10, pady=5)

        self.generate_button = ttk.Button(control_frame, text="Generate Array", command=self.generate_array)
        self.generate_button.grid(row=1, column=4, padx=10, pady=5)

        self.data_label = ttk.Label(control_frame, text="Array Size:")
        self.data_label.grid(row=1, column=0, padx=10, pady=5)

        self.data_size_spinbox = ttk.Spinbox(control_frame, from_=5, to=50, increment=1)
        self.data_size_spinbox.grid(row=1, column=1, padx=10, pady=5)

        self.target_label = ttk.Label(control_frame, text="Target Value (For Searching):")
        self.target_label.grid(row=1, column=2, padx=10, pady=5)

        self.target_entry = ttk.Entry(control_frame)
        self.target_entry.grid(row=1, column=3, padx=10, pady=5)

        self.speed_label = ttk.Label(control_frame, text="Speed (1x - 5x):")
        self.speed_label.grid(row=1, column=5, padx=10, pady=5)

        self.speed_scale = ttk.Scale(control_frame, from_=1, to=5, orient="horizontal", command=self.update_speed)
        self.speed_scale.set(1)
        self.speed_scale.grid(row=1, column=6, padx=10, pady=5)

        # Update UI after all widgets are defined
        self.type_combo.bind("<<ComboboxSelected>>", self.update_ui)
        self.update_ui()       

        # Visualization Frame
        self.canvas_frame = ttk.Frame(self.root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def update_ui(self, event=None):
        type_selected = self.type_combo.get()
        if type_selected == "Sorting":
            self.algorithm_combo["values"] = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"]
            self.data_label.grid(row=1, column=0, padx=10, pady=5)
            self.data_size_spinbox.grid(row=1, column=1, padx=10, pady=5)
            self.target_label.grid_remove()
            self.target_entry.grid_remove()
        elif type_selected == "Searching":
            self.algorithm_combo["values"] = ["Linear Search", "Binary Search", "Jump Search"]
            self.data_label.grid(row=1, column=0, padx=10, pady=5)
            self.data_size_spinbox.grid(row=1, column=1, padx=10, pady=5)
            self.target_label.grid(row=1, column=2, padx=10, pady=5)
            self.target_entry.grid(row=1, column=3, padx=10, pady=5)
        self.algorithm_combo.current(0)

    def generate_array(self):
        try:
            size = int(self.data_size_spinbox.get())
            if size <= 0:
                raise ValueError("Size must be greater than 0.")
            self.data = [random.randint(1, 100) for _ in range(size)]
            self.update_plot(self.data, ["blue"] * len(self.data))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for the array size.")

    def update_speed(self, event=None):
        self.speed = int(self.speed_scale.get())

    def update_plot(self, data, colors):
        self.ax.clear()
        bars = self.ax.bar(range(len(data)), data, color=colors)
        for bar, val in zip(bars, data):
            bar_height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width() / 2, bar_height - bar_height * 0.1, str(val), 
                         ha='center', va='bottom', fontsize=10 if bar_height > 15 else 8, color="white")
        self.ax.set_title("Algorithm Visualization")
        self.ax.set_xlim(-1, len(data))
        self.ax.set_ylim(0, max(data) + 10)
        self.canvas.draw()

    def start_algorithm(self):
        if not self.running:
            self.running = True
            algorithm = self.algorithm_combo.get()
            if self.type_combo.get() == "Searching":
                try:
                    self.target_value = int(self.target_entry.get())
                except ValueError:
                    self.target_value = None
                    messagebox.showerror("Error", "Please enter a valid integer for the target value.")
                    return

            thread = threading.Thread(target=self.run_algorithm, args=(algorithm,))
            thread.start()

    def stop_algorithm(self):
        self.running = False

    def reset(self):
        self.running = False
        self.data = []
        self.update_plot([], [])


    def run_algorithm(self, algorithm):
        if algorithm == "Bubble Sort":
            bubble_sort(self , self.data , self.root)
        elif algorithm == "Insertion Sort":
            # self.insertion_sort()
            insertion_sort(self , self.data , self.root)
        elif algorithm == "Merge Sort":
            merge_sort(self , 0 , len(self.data) - 1)
        elif algorithm == "Selection Sort":
            selection_sort(self , self.data , self.root)
        elif algorithm == "Linear Search":
            linear_search(self , self.data , self.root)
        elif algorithm == "Binary Search":
            binary_search(self , self.data , self.root)
        elif algorithm == "Jump Search":
            jump_search(self , self.data , self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()
