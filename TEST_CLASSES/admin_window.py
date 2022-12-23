from operator import imod


import tkinter as tk

win = tk.Tk()
win.title("Admin Window")
win.geometry("500x400")
win.resizable(False, False)


button = tk.Button(win, text="Create user")
button.pack()

win.mainloop()

