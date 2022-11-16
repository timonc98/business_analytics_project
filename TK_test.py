from tkinter import *
from tkinter import ttk
######## Lukas ######## 
Window = Tk()
Window.geometry("900x500")
Window.configure(background='lightblue')

frm = ttk.Frame(Window, padding=10)

frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=Window.destroy).grid(column=1, row=0)
ttk = Text(frm, height = 5, width = 52).grid(column=2, row=0)
Window.mainloop()

######## Timon ########


######## Alex ########


######## Marcel ########