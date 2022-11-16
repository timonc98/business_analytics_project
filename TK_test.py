

from tkinter import *
from tkinter import ttk
import tkinter.font as font
### Functions

def Create_Athlete():
    athletic = Tk()
    athletic.geometry("900x500")
    athletic.configure(background='lightgrey')
    s.configure('Frame1.TFrame', background='lightgrey')
    frm_ath = ttk.Frame(athletic, padding=10,style='Frame1.TFrame')
    frm_ath.grid()
    ttk.Label(frm_ath, text="Hello World!",background='lightgrey').grid(column=0, row=0)
    Text(frm_ath, height = 5, width = 52).grid(column=2, row=0)
    athletic.mainloop()

def Create_Course():
    athletic = Tk()
    athletic.geometry("900x500")
    athletic.configure(background='lightgrey')
    s.configure('Frame1.TFrame', background='lightgrey')
    frm_ath = ttk.Frame(athletic, padding=10,style='Frame1.TFrame')
    frm_ath.grid()
    ttk.Label(frm_ath, text="Hello World!",background='lightgrey').grid(column=0, row=0)
    Text(frm_ath, height = 5, width = 52).grid(column=2, row=0)
    athletic.mainloop()

def Training_Data():
    athletic = Tk()
    athletic.geometry("900x500")
    athletic.configure(background='lightgrey')
    s.configure('Frame1.TFrame', background='lightgrey')
    frm_ath = ttk.Frame(athletic, padding=10,style='Frame1.TFrame')
    frm_ath.grid()
    ttk.Label(frm_ath, text="Hello World!",background='lightgrey').grid(column=0, row=0)
    Text(frm_ath, height = 5, width = 52).grid(column=2, row=0)
    athletic.mainloop()

######## Lukas ######## 
Window = Tk()
s = ttk.Style()
Window.columnconfigure(0, weight=1) 
Window.rowconfigure(0, weight=1)
Window.geometry("500x500")
Window.configure(background='lightgrey')

s.configure('Frame1.TFrame', background='lightgrey')
frm = ttk.Frame(Window ,style='Frame1.TFrame')

frm.grid()
myFont = font.Font(family='Helvetica',size=15)
Button(frm, text="Create Athlete", font=myFont, bg='GREY', command=Create_Athlete).grid(column=0, row=0,padx=10, pady=10)
Button(frm, text="Create Course", font=myFont, bg='GREY', command=Create_Course).grid(column=0, row=1,padx=10, pady=10)
Button(frm, text="Enter Training Data (complete)", font=myFont, bg='GREY', command=Training_Data).grid(column=0, row=2,padx=10, pady=10)


Window.mainloop()

######## Timon ########


######## Alex ########


######## Marcel ########

#meine eigene Branch