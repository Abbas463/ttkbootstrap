import tkinter as tk
from ttkbootstrap import Style

win=tk.Tk()
win.title('GUI')
win.geometry('100x100')

button1=tk.Button(win, text="Button1")
button1.pack()

button2=tk.Button(win, text="Button2")
button2.pack()

button3=tk.Button(win, text="Button3")
button3.pack()

win.mainloop()