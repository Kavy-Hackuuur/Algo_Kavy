import tkinter as tk

class CodeDisplay:
    def __init__(self, parent):
        self.text_widget = tk.Text(parent, wrap=tk.WORD, state=tk.DISABLED, font=("Courier", 12))
        self.text_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    def load_code(self, code_lines):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete("1.0", tk.END)
        for line in code_lines:
            self.text_widget.insert(tk.END, line + "\n")
        self.text_widget.config(state=tk.DISABLED)
    
    def highlight_line(self, line_number):
        self.text_widget.tag_remove("highlight", "1.0", tk.END)
        self.text_widget.tag_add("highlight", f"{line_number}.0", f"{line_number}.end")
        self.text_widget.tag_config("highlight", background="yellow")
        self.text_widget.see(f"{line_number}.0")
