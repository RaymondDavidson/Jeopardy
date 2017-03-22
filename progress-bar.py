import Tkinter as tk
import ttk as ttk
root = tk.Tk()
s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
p = ttk.Progressbar(root, style="red.Horizontal.TProgressbar", orient="horizontal", length=600, mode="determinate", maximum=4, value=1)
p.pack()
