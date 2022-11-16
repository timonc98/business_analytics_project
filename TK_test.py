

from tkinter import *
from tkinter import ttk
import tkinter.font as font
### Functions

def Create_Athlete():
    athletic = Tk()
    athletic.configure(bg='blue')
    athletic.title("Create Athlete")
    #athletic.geometry("900x500")
    athletic.columnconfigure(0, weight=1) 
    athletic.rowconfigure(0, weight=1)
   
    ss = ttk.Style()
    s.configure('Frame1.TFrame', background='lightgrey')

    frm_ath = ttk.Frame(athletic,style='Frame1.TFrame')
    frm_ath.grid(column=0, row=0)
   

    ttk.Label(frm_ath, text="Create Athlete",background='').grid(column=0, row=0,padx=10, pady=10)

    frm_ath1 = ttk.Frame(frm_ath, style='Frame1.TFrame')
    frm_ath1.grid(column=0, row=1)
    frm_ath2 = ttk.Frame(frm_ath, style='Frame1.TFrame')
    frm_ath2.grid(column=1, row=1)

    ttk.Label(frm_ath1, text="Gender",background='').grid(column=0, row=1)
    OPTIONS = ['Male','Femal','Divers']
    variable = StringVar(frm_ath1)
    variable.set(OPTIONS[0])
    Gender = ttk.OptionMenu(frm_ath1, variable, *OPTIONS ).grid(column=1, row=1,padx=10, pady=10)

    ttk.Label(frm_ath1, text="Name",background='').grid(column=0, row=2,padx=10, pady=10)
    Name = Text(frm_ath1, height = 1, width = 10).grid(column=1, row=2)
    ttk.Label(frm_ath1, text="Weight",background='').grid(column=0, row=3,padx=10, pady=10)
    Weight = Text(frm_ath1, height = 1, width = 10).grid(column=1, row=3)
    ttk.Label(frm_ath1, text="Size",background='').grid(column=0, row=4,padx=10, pady=10)
    Size = Text(frm_ath1, height = 1, width = 10).grid(column=1, row=4)
    ttk.Label(frm_ath2, text="ID",background='').grid(column=0, row=5,padx=10, pady=10)
    ID  = Text(frm_ath2,state=DISABLED, height = 1, width = 10).grid(column=1, row=5)

    Button(frm_ath1, text="Create Athlete", bg='GREY', command=()).grid(column=0, row=6,padx=10, pady=10)
    Button(frm_ath2, text="Delete Athlete", bg='GREY', command=()).grid(column=0, row=7,padx=10, pady=10)


    Button(frm_ath, text="Quit", bg='GREY', command=athletic.destroy).grid(column=0, row=2,padx=10, pady=10)
    athletic.mainloop()

def Create_Course():
    Create_Window = Tk()
    Create_Window.title("Creat Training")
    Create_Window.geometry("900x500")
    Create_Window.columnconfigure(0, weight=1) 
    Create_Window.rowconfigure(0, weight=1)
    Create_Window.configure(background='lightgrey')
    s.configure('Frame1.TFrame', background='lightgrey')
    frm_creat = ttk.Frame(Create_Window, padding=10,style='Frame1.TFrame')
    frm_creat.grid()

    ttk.Label(frm_creat, text="Create Athlete",background='').grid(column=0, row=0,padx=10, pady=10)

    frm_creat1 = ttk.Frame(frm_creat, style='Frame1.TFrame')
    frm_creat1.grid(column=0, row=1)
    frm_creat2 = ttk.Frame(frm_creat, style='Frame1.TFrame')
    frm_creat2.grid(column=1, row=1)

    ttk.Label(frm_creat1, text="Designation",background='').grid(column=0, row=1)
    Designation = Text(frm_creat1, height = 1, width = 10).grid(column=1, row=1,padx=10, pady=10)
    ttk.Label(frm_creat1, text="Description",background='').grid(column=0, row=2)
    Discription = Text(frm_creat1, height = 3, width = 10).grid(column=1, row=2)
    ttk.Label(frm_creat2, text="TNr",background='').grid(column=0, row=5,padx=10, pady=10)
    TNr  = Text(frm_creat2,state=DISABLED, height = 1, width = 10).grid(column=1, row=5)

    Button(frm_creat1, text="Create Training", bg='GREY', command=()).grid(column=0, row=6,padx=10, pady=10)
    Button(frm_creat2, text="Delete Training", bg='GREY', command=()).grid(column=0, row=7,padx=10, pady=10)

    Button(frm_creat, text="Quit", bg='GREY', command=Create_Window.destroy).grid(column=0, row=2,padx=10, pady=10)
    Create_Window.mainloop()

def Training_Data():
    Training_Window = Tk()
    Training_Window.title("Enter Training Data")
    Training_Window.geometry("900x500")
    Training_Window.columnconfigure(0, weight=1) 
    Training_Window.rowconfigure(0, weight=1)
    Training_Window.configure(background='lightgrey')
    s.configure('Frame1.TFrame', background='lightgrey')
    frm_train = ttk.Frame(Training_Window, padding=10,style='Frame1.TFrame')
    frm_train.grid()

    ttk.Label(frm_train, text="Create Athlete",background='').grid(column=0, row=0,padx=10, pady=10)

    frm_train1 = ttk.Frame(frm_train, style='Frame1.TFrame')
    frm_train1.grid(column=0, row=1)
    frm_train2 = ttk.Frame(frm_train, style='Frame1.TFrame')
    frm_train2.grid(column=1, row=1)

    ttk.Label(frm_train1, text="Athlete ID",background='').grid(column=0, row=1)
    ID = Text(frm_train1, height = 1, width = 10).grid(column=1, row=1,padx=10, pady=10)
    ttk.Label(frm_train1, text="Date",background='').grid(column=0, row=2)
    Date = Text(frm_train1, height = 1, width = 10).grid(column=1, row=2,padx=10, pady=10)
    ttk.Label(frm_train1, text="Start TIme",background='').grid(column=0, row=3)
    Start_Time = Text(frm_train1, height = 1, width = 10).grid(column=1, row=3,padx=10, pady=10)
    ttk.Label(frm_train1, text="End Time",background='').grid(column=0, row=4)
    End_time = Text(frm_train1, height = 1, width = 10).grid(column=1, row=4)
    ttk.Label(frm_train2, text="Course (TNr)",background='').grid(column=0, row=5,padx=10, pady=10)
    TNr  = Text(frm_train2,state=DISABLED, height = 1, width = 10).grid(column=1, row=5)

    Button(frm_train2, text="Save Training Data", bg='GREY', command=()).grid(column=0, row=6,padx=10, pady=10)
    Button(frm_train2, text="Delete Training Data", bg='GREY', command=()).grid(column=0, row=7,padx=10, pady=10)

    Button(frm_train, text="Quit", bg='GREY', command=Training_Window.destroy).grid(column=0, row=2,padx=10, pady=10)

    Training_Window.mainloop()

######## Lukas ######## 
Window = Tk()
Window.title("Main Window - Training Managment")
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
Button(frm, text="Quit", font=myFont, bg='GREY', command=Window.destroy).grid(column=0, row=3,padx=10, pady=10)

Window.mainloop()

######## Timon ########


######## Alex ########


######## Marcel ########

#meine eigene Branch