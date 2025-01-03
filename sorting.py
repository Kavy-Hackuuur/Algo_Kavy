# from proj_new import *
# root = tk.Tk()
# algo = AlgorithmVisualizer(root)

import tkinter as tk
import time


def insertion_sort(self , data , root):
    n = len(data)
    for i in range(1, n):
        if not self.running:
            break
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            if not self.running:
                break
            self.update_plot(data, ["red" if x == j or x == i else "blue" for x in range(n)])
            root.update_idletasks()
            time.sleep(1 / self.speed)

            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

    self.update_plot(data, ["green"] * n)

def bubble_sort(self , data , root):
    n = len(data)
    for i in range(n):
        if not self.running:
            break
        for j in range(n - i - 1):
            if not self.running:
                break
            self.update_plot(self.data, ["red" if x == j or x == j+1 else "blue" for x in range(n)])
            root.update_idletasks()
            time.sleep(1 / self.speed)

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    self.update_plot(data, ["green"] * n)

def selection_sort(self , data , root):
    n = len(data)
    for i in range(n):
        if not self.running:
            break
        min_idx = i
        for j in range(i + 1, n):
            if not self.running:
                break
                    
            self.update_plot(data, ["red" if x == j or x == min_idx else "blue" for x in range(n)])
            root.update_idletasks()
            time.sleep(1 / self.speed)

            if self.data[j] < data[min_idx]:
                min_idx = j

        data[i], data[min_idx] = data[min_idx], data[i]
    self.update_plot(data, ["green"] * n)

def merge_sort(self , left, right):
    if left >= right or not self.running:
        return

    mid = (left + right) // 2
    merge_sort(self ,left, mid)
    merge_sort(self ,mid + 1, right)
    merge(self , left , mid , right)

def merge(self, left, mid, right):
    if not self.running:
        return

    left_part = self.data[left:mid + 1]
    right_part = self.data[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if not self.running:
            return

        self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
        self.root.update_idletasks()
        time.sleep(1 / self.speed)

        if left_part[i] <= right_part[j]:
            self.data[k] = left_part[i]
            i += 1
        else:
            self.data[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        if not self.running:
            return

        self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
        self.root.update_idletasks()
        time.sleep(1 / self.speed)

        self.data[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        if not self.running:
            return

        self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
        self.root.update_idletasks()
        time.sleep(1 / self.speed)

        self.data[k] = right_part[j]
        j += 1
        k += 1

    self.update_plot(self.data, ["green" if x >= left and x <= right else "blue" for x in range(len(self.data))])




#--------------------------------------------------------------------------------------------------
    # def bubble_sort(self):
    #     n = len(self.data)
    #     for i in range(n):
    #         if not self.running:
    #             break
    #         for j in range(n - i - 1):
    #             if not self.running:
    #                 break
    #             self.update_plot(self.data, ["red" if x == j or x == j+1 else "blue" for x in range(n)])
    #             self.root.update_idletasks()
    #             time.sleep(1 / self.speed)

    #             if self.data[j] > self.data[j + 1]:
    #                 self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    #     self.update_plot(self.data, ["green"] * n)

    # def insertion_sort(self):
    #     n = len(self.data)
    #     for i in range(1, n):
    #         if not self.running:
    #             break
    #         key = self.data[i]
    #         j = i - 1
    #         while j >= 0 and key < self.data[j]:
    #             if not self.running:
    #                 break
    #             self.update_plot(self.data, ["red" if x == j or x == i else "blue" for x in range(n)])
    #             self.root.update_idletasks()
    #             time.sleep(1 / self.speed)

    #             self.data[j + 1] = self.data[j]
    #             j -= 1
    #         self.data[j + 1] = key

    #     self.update_plot(self.data, ["green"] * n)

    # def merge_sort(self, left, right):
    #     if left >= right or not self.running:
    #         return

    #     mid = (left + right) // 2
    #     self.merge_sort(left, mid)
    #     self.merge_sort(mid + 1, right)
    #     self.merge(left, mid, right)

    # def merge(self, left, mid, right):
    #     if not self.running:
    #         return

    #     left_part = self.data[left:mid + 1]
    #     right_part = self.data[mid + 1:right + 1]

    #     i = j = 0
    #     k = left

    #     while i < len(left_part) and j < len(right_part):
    #         if not self.running:
    #             return

    #         self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
    #         self.root.update_idletasks()
    #         time.sleep(1 / self.speed)

    #         if left_part[i] <= right_part[j]:
    #             self.data[k] = left_part[i]
    #             i += 1
    #         else:
    #             self.data[k] = right_part[j]
    #             j += 1
    #         k += 1

    #     while i < len(left_part):
    #         if not self.running:
    #             return

    #         self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
    #         self.root.update_idletasks()
    #         time.sleep(1 / self.speed)

    #         self.data[k] = left_part[i]
    #         i += 1
    #         k += 1

    #     while j < len(right_part):
    #         if not self.running:
    #             return

    #         self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
    #         self.root.update_idletasks()
    #         time.sleep(1 / self.speed)

    #         self.data[k] = right_part[j]
    #         j += 1
    #         k += 1

    #     self.update_plot(self.data, ["green" if x >= left and x <= right else "blue" for x in range(len(self.data))])

    # def selection_sort(self):
    #     n = len(self.data)
    #     for i in range(n):
    #         if not self.running:
    #             break
    #         min_idx = i
    #         for j in range(i + 1, n):
    #             if not self.running:
    #                 break

    #             self.update_plot(self.data, ["red" if x == j or x == min_idx else "blue" for x in range(n)])
    #             self.root.update_idletasks()
    #             time.sleep(1 / self.speed)

    #             if self.data[j] < self.data[min_idx]:
    #                 min_idx = j

    #         self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]

    #     self.update_plot(self.data, ["green"] * n)

