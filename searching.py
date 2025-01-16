import tkinter as tk
from tkinter import messagebox
import time

def linear_search(self , data , root , code_display):

    t = int(1/self.speed) * 250

    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    code_display.highlight_line(1)
    root.after(t)

    n = len(data)

    code_display.highlight_line(2)
    root.after(t)
    
    for i in range(n):
        
        code_display.highlight_line(2)
        root.after(t)

        if not self.running:
            break
        self.update_plot(data, ["red" if x == i else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)
        
        code_display.highlight_line(3)
        root.after(t)
        
        if data[i] == self.target_value:
            self.update_plot(data, ["green" if x == i else "blue" for x in range(n)])

            code_display.highlight_line(4)
            root.after(t)    
            
            return

    messagebox.showinfo("Result", "Value not found in the array.")
    self.update_plot(data, ["yellow" if x == i else "blue" for x in range(n)])

def binary_search(self , data , root , code_display):
    
    t = int(1/self.speed) * 250

    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    data.sort()
    self.update_plot(data, ["blue"] * len(data))
    low, high = 0, len(data) - 1

    code_display.highlight_line(1)
    root.after(t)

    while low <= high and self.running:

        code_display.highlight_line(1)
        root.after(t)
        
        code_display.highlight_line(2)
        root.after(t)

        mid = (low + high) // 2
        
        self.update_plot(data, ["red" if x == mid else "blue" for x in range(len(data))])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        code_display.highlight_line(3)
        root.after(t)

        if data[mid] == self.target_value:
            
            code_display.highlight_line(4)
            root.after(t)

            self.update_plot(data, ["green" if x == mid else "blue" for x in range(len(data))])
            return

        code_display.highlight_line(5)
        root.after(t)

        if data[mid] < self.target_value:
            
            code_display.highlight_line(6)
            root.after(t)

            low = mid + 1
        
        code_display.highlight_line(7)
        root.after(t)

        if data[mid] > self.target_value:
            
            code_display.highlight_line(8)
            root.after(t)
            high = mid - 1

    messagebox.showinfo("Result", "Value not found in the array.")

def jump_search(self , data , root , code_display):

    t = int(1/self.speed) * 250

    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    data.sort()
    self.update_plot(data, ["blue"] * len(data))

    n = len(data)

    code_display.highlight_line(1)
    root.after(t)

    step = int(n**0.5)

    code_display.highlight_line(2)
    root.after(t)
    
    prev = 0

    code_display.highlight_line(3)
    root.after(t)

    while data[min(step, n) - 1] < self.target_value:

        code_display.highlight_line(3)
        root.after(t)

        self.update_plot(data, ["red" if x >= prev and x < min(step, n) else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        code_display.highlight_line(4)
        root.after(t)

        prev = step

        code_display.highlight_line(5)
        root.after(t)

        step += int(n**0.5)

        code_display.highlight_line(6)
        root.after(t)

        if prev >= n:
            messagebox.showinfo("Result", "Value not found in the array.")

            code_display.highlight_line(7)
            root.after(t)

            return
    code_display.highlight_line(8)
    root.after(t)

    for i in range(prev, min(step, n)):

        code_display.highlight_line(8)
        root.after(t)

        code_display.highlight_line(9)
        root.after(t)
        code_display.highlight_line(10)
        root.after(t)

        self.update_plot(data, ["red" if x == i else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        code_display.highlight_line(12)
        root.after(t)

        if data[i] == self.target_value:
            self.update_plot(data, ["green" if x == i else "blue" for x in range(n)])
            
            code_display.highlight_line(13)
            root.after(t)

            return

    code_display.highlight_line(11)
    root.after(t)

    messagebox.showinfo("Result", "Value not found in the array.")
