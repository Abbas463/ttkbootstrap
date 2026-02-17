import tkinter as tk
from ttkbootstrap import Style

app=tk.Tk()
style=Style(theme="darkly")
app.title('GUI')
app.geometry('100x100')

button1=tk.Button(app, text="Button1")
button1.pack()

button2=tk.Button(app, text="Button2")
button2.pack()

button3=tk.Button(app, text="Button3")
button3.pack()

app.mainloop()