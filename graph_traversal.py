import tkinter as tk
import time

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