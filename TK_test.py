

from tkinter import *
from tkinter import ttk
### Functions

def Window_Zwei():
    athletic = Tk()
    athletic.geometry("900x500")
    athletic.mainloop()

######## Lukas ######## 
Window = Tk()
s = ttk.Style()

Window.geometry("900x500")
Window.configure(background='lightgrey')

s.configure('Frame1.TFrame', background='lightgrey')
frm = ttk.Frame(Window, padding=10,style='Frame1.TFrame')

frm.grid()
ttk.Label(frm, text="Hello World!",background='lightgrey').grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=Window_Zwei).grid(column=1, row=0)
Text(frm, height = 5, width = 52).grid(column=2, row=0)
Window.mainloop()

######## Timon ########


######## Alex ########


######## Marcel ########

#meine eigene Branch