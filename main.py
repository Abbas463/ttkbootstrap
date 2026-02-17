import tkinter as tk
import ttkbootstrap as ttkb
from ttkbootstrap import Style

app = tk.Tk()
style = Style(theme = "darkly")
app.title('GUI')
app.geometry('100x100')
app.state('zoomed')

button1 = ttkb.Button(app, text = "Button1", bootstyle = 'info')
button1.pack()

button2 = ttkb.Button(app, text = "Button2", bootstyle = 'success')
button2.pack()

button3 = ttkb.Button(app, text = "Button3", bootstyle = 'warning')
button3.pack()

app.mainloop()