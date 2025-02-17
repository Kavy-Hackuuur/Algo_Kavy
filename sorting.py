import tkinter as tk
import time
# from code_display import CodeDisplay

def insertion_sort(self , data , root , code_display , step_by_step):
    n = len(data)
    t = int(1/self.speed) * 250

    code_display.highlight_line(2)
    root.after(t)

    for i in range(1, n):

        code_display.highlight_line(2)
        root.after(t)

        if not self.running:
            break

        code_display.highlight_line(3)
        root.after(t)

        key = data[i]

        code_display.highlight_line(4)
        root.after(t)
        
        j = i - 1

        code_display.highlight_line(5)
        root.after(t)

        while j >= 0 and key < data[j]:

            code_display.highlight_line(5)
            root.after(t)
            
            if not self.running:
                break

            self.update_plot(data, ["red" if x == j or x == i else "blue" for x in range(n)])
            root.update_idletasks()
            time.sleep(1 / self.speed)

            code_display.highlight_line(6)
            root.after(t)

            data[j + 1] = data[j]

            code_display.highlight_line(7)
            root.after(t)
            j -= 1

        code_display.highlight_line(8)
        root.after(t)

        data[j + 1] = key

        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()

    self.update_plot(data, ["green"] * n)

def bubble_sort(self , data , root , code_display , step_by_step):
    n = len(data)
    t = int(1/self.speed) * 500

    code_display.highlight_line(2)
    root.after(t)

    for i in range(n):

        # code_display.highlight_line(3)
        # root.after(t)

        if not self.running:
            break

        code_display.highlight_line(3)
        root.after(t)

        for j in range(n - i - 1):

            code_display.highlight_line(3)
            root.after(t)

            if not self.running:
                break

            self.update_plot(self.data, ["red" if x == j or x == j+1 else "blue" for x in range(n)])
            root.update_idletasks()
            time.sleep(1 / self.speed)

            code_display.highlight_line(4)
            root.after(t)

            if data[j] > data[j + 1]:

                code_display.highlight_line(5)
                root.after(t)

                data[j], data[j + 1] = data[j + 1], data[j]
                self.step_history.append(list(data))
            
            if step_by_step:
                self.step_event.clear()
                self.step_event.wait()

    self.update_plot(data, ["green"] * n)

def selection_sort(self , data , root , code_display , step_by_step):
    n = len(data)
    t = int(1/self.speed) * 250

    code_display.highlight_line(2)
    root.after(t)

    for i in range(n):

        code_display.highlight_line(2)
        root.after(t)

        if not self.running:
            break

        code_display.highlight_line(3)
        root.after(t)

        min_idx = i

        code_display.highlight_line(4)
        root.after(t)

        for j in range(i + 1, n):

            code_display.highlight_line(4)
            root.after(t)
            
            if not self.running:
                break

            self.update_plot(data, ["red" if x == j or x == min_idx else "blue" for x in range(n)])
            root.update_idletasks()
            time.sleep(1 / self.speed)

            code_display.highlight_line(5)
            root.after(t)


            if self.data[j] < data[min_idx]:
                
                code_display.highlight_line(6)
                root.after(t)

                min_idx = j

        code_display.highlight_line(7)
        root.after(t)

        data[i], data[min_idx] = data[min_idx], data[i]

        if step_by_step:
            self.step_event.clear()
            self.step_event.wait()

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

        self.step_history.append(list(self.data))  # Save step
        self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
        self.root.update_idletasks()

        self.step_event.clear()  # Pause for step mode
        self.step_event.wait()

    while i < len(left_part):
        if not self.running:
            return

        self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
        self.root.update_idletasks()
        time.sleep(1 / self.speed)

        self.data[k] = left_part[i]
        i += 1
        k += 1

        self.step_history.append(list(self.data))
        self.step_event.clear()
        self.step_event.wait()

    while j < len(right_part):
        if not self.running:
            return

        self.update_plot(self.data, ["red" if x == k else "blue" for x in range(len(self.data))])
        self.root.update_idletasks()
        time.sleep(1 / self.speed)

        self.data[k] = right_part[j]
        j += 1
        k += 1

        self.step_history.append(list(self.data))
        self.step_event.clear()
        self.step_event.wait()

    self.update_plot(self.data, ["green" if x >= left and x <= right else "blue" for x in range(len(self.data))])
