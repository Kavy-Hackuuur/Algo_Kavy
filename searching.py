import tkinter as tk
from tkinter import messagebox
import time

def linear_search(self , data , root):
    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    n = len(data)
    for i in range(n):
        if not self.running:
            break
        self.update_plot(data, ["red" if x == i else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        if data[i] == self.target_value:
            self.update_plot(data, ["green" if x == i else "blue" for x in range(n)])
            return

    messagebox.showinfo("Result", "Value not found in the array.")
    self.update_plot(data, ["yellow" if x == i else "blue" for x in range(n)])

def binary_search(self , data , root):
    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    data.sort()
    self.update_plot(data, ["blue"] * len(data))
    low, high = 0, len(data) - 1

    while low <= high and self.running:

        mid = (low + high) // 2
        self.update_plot(data, ["red" if x == mid else "blue" for x in range(len(data))])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        if data[mid] == self.target_value:
            self.update_plot(data, ["green" if x == mid else "blue" for x in range(len(data))])
            return
        elif data[mid] < self.target_value:
            low = mid + 1
        else:
            high = mid - 1

    messagebox.showinfo("Result", "Value not found in the array.")

def jump_search(self , data , root):
    if self.target_value is None:
        messagebox.showerror("Error", "Target value not provided.")
        return

    data.sort()
    self.update_plot(data, ["blue"] * len(data))

    n = len(data)
    step = int(n**0.5)
    prev = 0

    while data[min(step, n) - 1] < self.target_value:
        self.update_plot(data, ["red" if x >= prev and x < min(step, n) else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        prev = step
        step += int(n**0.5)
        if prev >= n:
            messagebox.showinfo("Result", "Value not found in the array.")
            return

    for i in range(prev, min(step, n)):
        self.update_plot(data, ["red" if x == i else "blue" for x in range(n)])
        root.update_idletasks()
        time.sleep(1 / self.speed)

        if data[i] == self.target_value:
            self.update_plot(data, ["green" if x == i else "blue" for x in range(n)])
            return

    messagebox.showinfo("Result", "Value not found in the array.")





#--------------------------------------------------------------------------------------------------
    # def linear_search(self):
    #     if self.target_value is None:
    #         messagebox.showerror("Error", "Target value not provided.")
    #         return

    #     n = len(self.data)
    #     for i in range(n):
    #         if not self.running:
    #             break
    #         self.update_plot(self.data, ["red" if x == i else "blue" for x in range(n)])
    #         self.root.update_idletasks()
    #         time.sleep(1 / self.speed)

    #         if self.data[i] == self.target_value:
    #             self.update_plot(self.data, ["green" if x == i else "blue" for x in range(n)])
    #             return

    #     messagebox.showinfo("Result", "Value not found in the array.")
    #     self.update_plot(self.data, ["yellow" if x == i else "blue" for x in range(n)])

    # def binary_search(self):
    #     if self.target_value is None:
    #         messagebox.showerror("Error", "Target value not provided.")
    #         return

    #     self.data.sort()
    #     self.update_plot(self.data, ["blue"] * len(self.data))

    #     low, high = 0, len(self.data) - 1
    #     while low <= high and self.running:
    #         mid = (low + high) // 2
    #         self.update_plot(self.data, ["red" if x == mid else "blue" for x in range(len(self.data))])
    #         self.root.update_idletasks()
    #         time.sleep(1 / self.speed)

    #         if self.data[mid] == self.target_value:
    #             self.update_plot(self.data, ["green" if x == mid else "blue" for x in range(len(self.data))])
    #             return
    #         elif self.data[mid] < self.target_value:
    #             low = mid + 1
    #         else:
    #             high = mid - 1

    #     messagebox.showinfo("Result", "Value not found in the array.")

    # def jump_search(self):
    #     if self.target_value is None:
    #         messagebox.showerror("Error", "Target value not provided.")
    #         return

    #     self.data.sort()
    #     self.update_plot(self.data, ["blue"] * len(self.data))

    #     n = len(self.data)
    #     step = int(n**0.5)
    #     prev = 0

    #     while self.data[min(step, n) - 1] < self.target_value:
    #         self.update_plot(self.data, ["red" if x >= prev and x < min(step, n) else "blue" for x in range(n)])
    #         self.root.update_idletasks()
    #         time.sleep(1 / self.speed)

    #         prev = step
    #         step += int(n**0.5)
    #         if prev >= n:
    #             messagebox.showinfo("Result", "Value not found in the array.")
    #             return

    #     for i in range(prev, min(step, n)):
    #         self.update_plot(self.data, ["red" if x == i else "blue" for x in range(n)])
    #         self.root.update_idletasks()
    #         time.sleep(1 / self.speed)

    #         if self.data[i] == self.target_value:
    #             self.update_plot(self.data, ["green" if x == i else "blue" for x in range(n)])
    #             return

    #     messagebox.showinfo("Result", "Value not found in the array.")