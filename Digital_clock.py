#designing a Digital Clock

import tkinter as tk
from tkinter import ttk

from time import strftime

def time():
  current_time = strftime("%I:%M:%S %p \n%a")
  label.config(text=current_time)
  label.after(1000, time)

root = tk.Tk()

root.title("CLOCK")

label = tk.Label(root, font=("Courier",55,'bold'), background = "white", foreground='red')
label.pack(anchor='center')

time()

root.mainloop()