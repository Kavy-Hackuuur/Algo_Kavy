import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
import time
import networkx as nx
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
        self.graph = None
        self.graph_positions = None
        self.data = []

        # UI Elements
        self.create_widgets()
        self.update_ui()

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

        self.type_combo = ttk.Combobox(control_frame, values=["Sorting", "Searching", "Graph Traversal"], state="readonly")
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

        self.generate_button = ttk.Button(control_frame, text="Generate", command=self.generate_data)
        self.generate_button.grid(row=1, column=4, padx=10, pady=5)

        self.data_label = ttk.Label(control_frame, text="Input Size:")
        self.data_label.grid(row=1, column=0, padx=10, pady=5)

        self.data_size_spinbox = ttk.Spinbox(control_frame, from_=5, to=50, increment=1)
        self.data_size_spinbox.grid(row=1, column=1, padx=10, pady=5)

        self.target_label = ttk.Label(control_frame, text="Target Value:")
        self.target_label.grid(row=1, column=2, padx=10, pady=5)

        self.target_entry = ttk.Entry(control_frame)
        self.target_entry.grid(row=1, column=3, padx=10, pady=5)

        self.speed_label = ttk.Label(control_frame, text="Speed (1x - 5x):")
        self.speed_label.grid(row=1, column=5, padx=10, pady=5)

        self.speed_scale = ttk.Scale(control_frame, from_=1, to=5, orient="horizontal", command=self.update_speed)
        self.speed_scale.set(1)
        self.speed_scale.grid(row=1, column=6, padx=10, pady=5)

        # Visualization Frame
        self.canvas_frame = ttk.Frame(self.root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.type_combo.bind("<<ComboboxSelected>>", self.update_ui)

    def update_ui(self, event=None):
        type_selected = self.type_combo.get()
        if type_selected == "Sorting":
            self.algorithm_combo["values"] = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"]
        elif type_selected == "Searching":
            self.algorithm_combo["values"] = ["Linear Search", "Binary Search", "Jump Search"]
        elif type_selected == "Graph Traversal":
            self.algorithm_combo["values"] = ["BFS", "DFS"]
        self.algorithm_combo.current(0)

    def generate_data(self):
        if self.type_combo.get() == "Graph Traversal":
            try:
                num_nodes = int(self.data_size_spinbox.get())
                if num_nodes <= 0:
                    raise ValueError("Size must be greater than 0.")
                self.generate_graph(num_nodes)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer.")
        else:
            try:
                size = int(self.data_size_spinbox.get())
                if size <= 0:
                    raise ValueError("Size must be greater than 0.")
                self.data = [random.randint(1, 100) for _ in range(size)]
                self.update_plot(self.data, ["blue"] * len(self.data))
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer for the array size.")

    def generate_graph(self, num_nodes):
        self.graph = nx.erdos_renyi_graph(n=num_nodes, p=0.3)
        for node in self.graph.nodes:
            self.graph.nodes[node]['value'] = random.randint(1, 100)
        self.graph_positions = nx.spring_layout(self.graph)  # Save fixed positions
        self.update_graph_plot()

    def update_graph_plot(self, highlight_node=None, target_value=None, found=None):
        self.ax.clear()
        pos = self.graph_positions  # Use fixed positions
        node_colors = []

        for node in self.graph.nodes:
            if node == highlight_node:
                node_colors.append('green' if found else 'yellow')
            else:
                node_colors.append('red' if found is False else 'blue')

        nx.draw(self.graph, pos, ax=self.ax, node_color=node_colors, with_labels=True, 
                labels={n: self.graph.nodes[n]['value'] for n in self.graph.nodes})
        self.canvas.draw()

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

    def bfs(self, start_node, target_value):
        visited = set()
        queue = [start_node]

        while queue and self.running:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            self.update_graph_plot(current, target_value)
            time.sleep(1 / self.speed)

            if self.graph.nodes[current]['value'] == target_value:
                self.update_graph_plot(current, target_value, found=True)
                return

            queue.extend(neighbor for neighbor in self.graph.neighbors(current) if neighbor not in visited)

        self.update_graph_plot(found=False)

    def dfs(self, current, target_value, visited=None):
        if visited is None:
            visited = set()
        if current in visited or not self.running:
            return

        visited.add(current)
        self.update_graph_plot(current, target_value)
        time.sleep(1 / self.speed)

        if self.graph.nodes[current]['value'] == target_value:
            self.update_graph_plot(current, target_value, found=True)
            return

        for neighbor in self.graph.neighbors(current):
            self.dfs(neighbor, target_value, visited)

        if current == 0 and not self.running:
            self.update_graph_plot(found=False)

    def start_algorithm(self):
        if not self.running:
            self.running = True
            algorithm = self.algorithm_combo.get()
            if self.type_combo.get() == "Sorting":
                thread = threading.Thread(target=self.run_sorting, args=(algorithm,))
            elif self.type_combo.get() == "Searching":
                try:
                    self.target_value = int(self.target_entry.get())
                except ValueError:
                    self.target_value = None
                    messagebox.showerror("Error", "Please enter a valid integer for the target value.")
                    return
                thread = threading.Thread(target=self.run_searching, args=(algorithm,))
            elif self.type_combo.get() == "Graph Traversal":
                try:
                    self.target_value = int(self.target_entry.get())
                except ValueError:
                    self.target_value = None
                    messagebox.showerror("Error", "Please enter a valid integer for the target value.")
                    return
                start_node = random.choice(list(self.graph.nodes))
                if algorithm == "BFS":
                    thread = threading.Thread(target=self.bfs, args=(start_node, self.target_value))
                elif algorithm == "DFS":
                    thread = threading.Thread(target=self.dfs, args=(start_node, self.target_value))
            thread.start()

    def run_sorting(self, algorithm):
        if algorithm == "Bubble Sort":
            bubble_sort(self, self.data, self.root)
        elif algorithm == "Insertion Sort":
            insertion_sort(self, self.data, self.root)
        elif algorithm == "Merge Sort":
            merge_sort(self, 0, len(self.data) - 1)
        elif algorithm == "Selection Sort":
            selection_sort(self, self.data, self.root)

    def run_searching(self, algorithm):
        if algorithm == "Linear Search":
            linear_search(self, self.data, self.root)
        elif algorithm == "Binary Search":
            binary_search(self, self.data, self.root)
        elif algorithm == "Jump Search":
            jump_search(self, self.data, self.root)

    def stop_algorithm(self):
        self.running = False

    def reset(self):
        self.running = False
        self.data = []
        self.graph = None
        self.graph_positions = None
        self.ax.clear()
        self.canvas.draw()

    def update_speed(self, event=None):
        self.speed = int(self.speed_scale.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()
