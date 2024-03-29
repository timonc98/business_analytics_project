from tkinter import *
from tkcalendar import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import psycopg2
from datetime import date
from datetime import datetime, timedelta
import ast
#from django.db import transaction, DatabaseError


## Datum
today = date.today()
print("Today's date:", today.day)
print(today.isoweekday())

#### Farben
LGrey = '#1b1b1b'
DGrey = '#242424'
RGrey = '#2e2e2e'
HGrey = '#545454'

#Wndow Config
root = Tk()
#root.geometry("1100x800")
root.config(bg=DGrey)
root.title('Business Athletics')

## Clear Frame
def clear_frame(Frame_Name):
   for widgets in Frame_Name.winfo_children():
      widgets.destroy()

#### Diese Funktion dient den Active und inactiven Buttons mit den Bildern
def Active_Button(ButtonName,Canvas_Name,Frame,ImageName_Active,ImageName_Inctive,Commando,Color,ButtonOrder):
    Creat_Bild_active = Image.open(ImageName_Active)
    Creat_Bild_inactive = Image.open(ImageName_Inctive)

    Creat_Bild_active =  Creat_Bild_active.resize((200, 100))
    Creat_Bild_inactive =  Creat_Bild_inactive.resize((200, 100))

    Frame.btn_active = ImageTk.PhotoImage(Creat_Bild_active)
    Frame.btn_inactive = ImageTk.PhotoImage(Creat_Bild_inactive)

    def on_enter(self):
        ButtonName.config(image=Frame.btn_active)

    def on_leave(event):
        ButtonName.config(image=Frame.btn_inactive)

   
    ButtonName.config(image=Frame.btn_inactive, bg=Color, width=200, height=100, bd=0, relief='sunken',activebackground=LGrey, command=Commando)

    Canvas_Name.create_window(100,50, window=ButtonName)

    ButtonName.bind("<Enter>", on_enter)
    ButtonName.bind("<Leave>", on_leave)

### Database
# Verbindung zu der Datenbank
con = psycopg2.connect(database="postgres", user="postgres", password="password", host="127.0.0.1", port="5432")

print("Database opened successfully")

# DIeser Abschnitt erstellt die Tabellen falls dieser nicht existerien



cur = con.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS ATHLETE 
    (Gender_variable  TEXT     NOT NULL,
    Text_Athlete_Name TEXT       NOT NULL,
    Text_Athlete_Weight      INT    NOT NULL,
    Text_Athlete_Size INT NOT NULL,
    AGE INT NOT NULL,
    athleten_ID SERIAL PRIMARY KEY);''')


cur.execute('''CREATE TABLE IF NOT EXISTS TRAINING 
    (Text_Course_Designation TEXT NOT NULL,
    Text_Course_Description TEXT       NOT NULL,
    trainings_ID      SERIAL    PRIMARY KEY);''')

cur.execute('''CREATE TABLE IF NOT EXISTS TRAINING_DATA 
    (ID_variable_Data INT NOT NULL,
    Text_Traning_Date TEXT       NOT NULL,
    Text_Training_Start      TEXT    NOT NULL,
    duration      FLOAT    NOT NULL,
    Text_Training_END TEXT NOT NULL,
    TNR_variable_Data INT NOT NULL,
    Number      SERIAL    PRIMARY KEY);''')

con.commit()
print("Table created successfully")

#### Weitere Funktion
# Darunter Funktionen zur aktuallisieren und Elementen in der GUI

# Informationslist dient nur dem Programierer
athletes = []

# Error Funktion mit Fenster
def Erros(ErrorText):
   messagebox.showerror('Python Error', 'Error: ' + ErrorText)
#    con = psycopg2.connect(database="postgres", user="postgres", password="Lukasso007", host="127.0.0.1", port="5432")
#    cur = con.cursor()
#    return cur 

# Add Information
def TNR_Drop_Aktu():
    cur.execute("SELECT trainings_ID FROM TRAINING ")
    ALL_TNR = cur.fetchall()
    OPTIONS_TNR = ['']

    for PID in ALL_TNR:
        OPTIONS_TNR.append(PID[0])
    print(OPTIONS_TNR)
    return OPTIONS_TNR

def Id_Drop_Aktu():
    cur.execute("SELECT athleten_ID FROM ATHLETE ")
    ALL_ID = cur.fetchall()
    OPTIONS_ID = ['']

    for PID in ALL_ID:
        OPTIONS_ID.append(PID[0])
    print(OPTIONS_ID)
    return OPTIONS_ID

def Calendar_select(event):
    ID = ID_variable_Data.get()

    cur.execute("SELECT * FROM training_data WHERE id_variable_data=" + ID)
    Trainings_data = cur.fetchall()
    Text = ''
    for ele in Trainings_data:
        if ele[1] == cal.get_date():
            cur.execute("SELECT text_course_description FROM TRAINING WHERE trainings_ID=" + str(ele[5]))
            Trainings_Name = cur.fetchall()
            Text += "{0:5} {1:5} {2:5} {3:5}".format(ele[6], ele[2], ele[4], Trainings_Name[0][0])# + '\n'

    Output_lable.config(text=(cal.get_date() + '\n' + Text))



### Button Funktions

'''
In diesem abschnitt sind alle Button Funktionen
Um Daten hinzuzufügen, löschen und aktualisieren

'''

def Aktualisieren(event):

    record_id = event.widget.get()
    cur.execute("SELECT * FROM ATHLETE WHERE athleten_ID=" + record_id)
    records = cur.fetchall()

    if (records[0][0]) == 'Male':
        Gender_variable.set(OPTIONS[1])
    elif (records[0][0]) == 'Female':
        Gender_variable.set(OPTIONS[2])
    else:
        Gender_variable.set(OPTIONS[3])

    Text_Athlete_Name.delete("1.0",END)
    Text_Athlete_Name.insert("1.0",records[0][1])
    Text_Athlete_Weight.delete("1.0",END)
    Text_Athlete_Weight.insert("1.0",records[0][2])
    Text_Athlete_Size.delete("1.0",END)
    Text_Athlete_Size.insert("1.0",records[0][3])

    Day_Variable.set(int(str(records[0][4])[0:2]))
    Month_Variable.set(int(str(records[0][4])[2:4]))
    Year_Variable.set(int(str(records[0][4])[4:8]))

def Aktualisieren_TNR(event):

    record_TNR = event.widget.get()
    cur.execute("SELECT * FROM TRAINING WHERE trainings_ID=" + record_TNR)
    records = cur.fetchall()

    Text_Course_Designation.delete("1.0",END)
    Text_Course_Designation.insert("1.0",records[0][0])
    Text_Course_Description.delete("1.0",END)
    Text_Course_Description.insert("1.0",records[0][1])


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

def Create_Athlete_Button():
    #try:
    AGE = int(Day_Variable.get())*1000000 + int(Month_Variable.get())*10000 + int(Year_Variable.get())
    cur.execute("INSERT INTO ATHLETE (Gender_variable,Text_Athlete_Name,Text_Athlete_Weight,Text_Athlete_Size,AGE) VALUES (%s,%s,%s,%s,%s)"
    ,(Gender_variable.get(),Text_Athlete_Name.get("1.0",END), Text_Athlete_Weight.get("1.0",END),Text_Athlete_Size.get("1.0",END),AGE))
    con.commit()
    OPTIONS_ID = Id_Drop_Aktu()
    Text_Athlete_ID2['values'] = OPTIONS_ID
    Text_Athlete_ID2.current(len(OPTIONS_ID)-1)

    #except DatabaseError:
    #     Erros('No entery')
    #     con.rollback()

def Delete_Athlete_Button():
    record_id = ID_variable.get()
    cur.execute("DELETE FROM  ATHLETE WHERE athleten_ID='%s'" %(record_id))
    con.commit()
    cur.execute("DELETE FROM training_data WHERE id_variable_data='%s'" %(record_id))
    con.commit()

    Text_Athlete_Name.delete("1.0",END)
    Text_Athlete_Weight.delete("1.0",END)
    Text_Athlete_Size.delete("1.0",END)
    OPTIONS_ID = Id_Drop_Aktu()
    Text_Athlete_ID2['values'] = OPTIONS_ID
    Text_Athlete_ID2.current(0)

def Change_Athlete_Button():
    record_id = ID_variable.get()
    AGE = int(Day_Variable.get())*1000000 + int(Month_Variable.get())*10000 + int(Year_Variable.get())
    cur.execute("SELECT * FROM ATHLETE WHERE athleten_ID=" + record_id)

    cur.execute("Update ATHLETE set gender_variable='%s' , text_Athlete_Name='%s' , text_Athlete_Weight='%s' , text_Athlete_Size='%s', AGE='%s' where athleten_id='%s'" 
                %(Gender_variable.get(),Text_Athlete_Name.get("1.0",END),Text_Athlete_Weight.get("1.0",END),Text_Athlete_Size.get("1.0",END),AGE,record_id))
    
    con.commit()



def Create_Training_Button():
    cur.execute("INSERT INTO TRAINING (Text_Course_Designation,Text_Course_Description) VALUES (%s,%s)"
    ,(Text_Course_Designation.get("1.0",END),Text_Course_Description.get("1.0",END)))
    con.commit()
    OPTIONS_ID = TNR_Drop_Aktu()
    Text_Course_TNr['values'] = OPTIONS_ID
    Text_Course_TNr.current(len(OPTIONS_ID)-1)

def Delete_Training_Button():
    record_TNR = TNR_variable.get()
    cur.execute("DELETE FROM  TRAINING WHERE trainings_ID='%s'" %(record_TNR))
    con.commit()

    cur.execute("DELETE FROM training_data WHERE tnr_variable_data='%s'" %(record_TNR))
    con.commit()

    Text_Course_Designation.delete("1.0",END)
    Text_Course_Description.delete("1.0",END)
    OPTIONS_TNR = TNR_Drop_Aktu()
    Text_Course_TNr['values'] = OPTIONS_TNR
    Text_Course_TNr.current(0)

def Change_Training_Button():
    record_TNR = TNR_variable.get()

    cur.execute("SELECT * FROM TRAINING WHERE trainings_ID=" + record_TNR)

    cur.execute("Update TRAINING set Text_Course_Designation='%s' , Text_Course_Description='%s' where trainings_ID='%s'" 
                %(Text_Course_Designation.get("1.0",END),Text_Course_Description.get("1.0",END),record_TNR))
    
    con.commit()

def Save_Training_Data_Button():
    Start = str(Text_Training_Start_Hour.get())+':' + str(Text_Training_Start_Min.get())
    Stop = str(Text_Training_Stop_Hour.get())+':' + str(Text_Training_Stop_Min.get())
    print (int(Text_Training_Start_Hour.get()))
    duration= float(Text_Training_Stop_Hour.get()) - float(Text_Training_Start_Hour.get()) + (float(Text_Training_Stop_Min.get())- float(Text_Training_Start_Min.get()))/60
    cur.execute("INSERT INTO TRAINING_DATA (ID_variable_Data,Text_Traning_Date,Text_Training_Start,Text_Training_END,duration,TNR_variable_Data) VALUES (%s,%s,%s,%s,%s,%s)"
    ,(ID_variable_Data.get(),cal.get_date(),Start,Stop, duration,TNR_variable_Data.get()))
    con.commit()

    ID = ID_variable_Data.get()

    cur.execute("SELECT * FROM training_data WHERE id_variable_data=" + ID)
    Trainings_data = cur.fetchall()
    Text = ''
    for ele in Trainings_data:
        if ele[1] == cal.get_date():
            cur.execute("SELECT text_course_description FROM TRAINING WHERE trainings_ID=" + str(ele[5]))
            Trainings_Name = cur.fetchall()
            Text += "{0:5} {1:5} {2:5} {3:5}".format(ele[6], ele[2], ele[4], Trainings_Name[0][0]) + '\n'
    
    Output_lable.config(text=(cal.get_date() + '\n' + Text))

#Weiter Delete Fenster um Training zu löschen:
def Delete_Training_Data_Button():
    def Delete_Training():
        

        print(Delete_Number.get())

        cur.execute("DELETE FROM TRAINING_DATA WHERE number=" + (Delete_Number.get()))
        con.commit()

        ID = ID_variable_Data.get()
        cur.execute("SELECT * FROM training_data WHERE id_variable_data=" + ID)
        Trainings_data = cur.fetchall()
        Text = ''
        for ele in Trainings_data:
            if ele[1] == cal.get_date():
                cur.execute("SELECT text_course_description FROM TRAINING WHERE trainings_ID=" + str(ele[6]))
                Trainings_Name = cur.fetchall()
                Text += "{0:5} {1:5} {2:5} {3:5}".format(ele[6], ele[4], ele[2], Trainings_Name[0][0]) + '\n'

        Output_lable.config(text=(cal.get_date() + '\n' + Text))
        Delete_window.destroy()

            

    Delete_window = Toplevel()
    #Delete_window .geometry('180x100')
    Delete_window.config(bg=DGrey)
    Delete_window.title('Delete Window')

    Delete_lable = Label(Delete_window,text='Delete Number:',bg=DGrey,fg='White',pady = 2,font=('Calibri', 15))
    Delete_lable.grid(column=0,row=0,padx=10,pady=5,sticky='nsew')
    Delete_Number = Spinbox(Delete_window, justify=CENTER,width=0,from_=1,to=999999)
    Delete_Number.grid(column=0,row=1,padx=10,pady=5,sticky='nsew')
    Delete_button = Button(Delete_window,text="Delete Training",command=Delete_Training)
    Delete_button.grid(column=0,row=2,padx=10,pady=5,sticky='nsew')

#Weiteres Fenster um Trainingsplan hinzuzufügen
#Hier kann der Nutzer einen Trainingsplan für die Nächste woche planen
def training_schedule():
    mylist = []
    Data_List = StringVar(value=mylist)
    def Schedual_Display(event=None):
        Tabel = "{0:5} {1:7} {2:5} {3:5}".format("Day","Start","Stop","Type")
        ID = ID_variable_Data.get()
        Wekday_names = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

        if var.get() == 0:
            Weekday = today.weekday()
            
            Output_text = ''
            List = []
            cur.execute("SELECT * FROM training_data WHERE id_variable_data=" + ID)
            Trainings_data = cur.fetchall()
            # for Weekday in range(1,8):
            
            for Record in Trainings_data:

                datetime_object = datetime.strptime(Record[1], '%d.%m.%Y').date()
                Trainings_Name = ""

                if ((datetime_object >= today- timedelta(days=7)) and (datetime_object<= today)):
                    List.append((datetime_object.weekday(),Record[2],Record[4],Record[5],Record[3]))
            List.sort()
            for ele in List:
                cur.execute("SELECT text_course_description FROM TRAINING WHERE trainings_ID=" + str(ele[3]))
                Trainings_Name = cur.fetchall()
                Output_text += "{0:5} {1:5} {2:5} {3:5}".format(Wekday_names[ele[0]],ele[1],ele[2],Trainings_Name[0][0])
                #Record[1].weekday()

            Display_Lable.config(text=("ID = "+ str(ID) + '\n' + Tabel + '\n' + Output_text))
            Data_List.set(List)
        
        elif var.get() == 1:
            List = []
            Output_text = ''
            List = [(0,"15:00","17:00",1,2),(1,"15:00","17:00",1,2),(2,"15:00","17:00",1,2),(3,"15:00","17:00",1,2),(4,"15:00","17:00",1,2),(5,"-","-","-","-"),(6,"-","-","-","-")]
            for ele in List:
                if isinstance(ele[3], int) == True:
                    cur.execute("SELECT text_course_description FROM TRAINING WHERE trainings_ID=" + str(ele[3]))
                    Trainings_Name = cur.fetchall()
                    Output_text += "{0:5} {1:7} {2:5} {3:5}".format(Wekday_names[ele[0]],ele[1],ele[2],Trainings_Name[0][0])
                else:
                    Output_text += "{0:5} {1:7} {2:5} {3:5}".format(Wekday_names[ele[0]],ele[1],ele[2],ele[3]) + "\n"

            Display_Lable.config(text=("ID = "+ str(ID) + '\n' + Tabel + '\n' + Output_text))
            Data_List.set(List)

        elif var.get() == 2:
            List = []
            Output_text = ''
            List = [(0,"16:00","17:00",2,2),(1,"16:00","17:00",2,2),(2,"16:00","17:00",2,2),(3,"16:00","17:00",2,2),(4,"16:00","18:00",1,2),(5,"-","-","-","-"),(6,"-","-","-","-")]
            for ele in List:
                if isinstance(ele[3], int) == True:
                    cur.execute("SELECT text_course_description FROM TRAINING WHERE trainings_ID=" + str(ele[3]))
                    Trainings_Name = cur.fetchall()
                    Output_text += "{0:5} {1:7} {2:5} {3:5}".format(Wekday_names[ele[0]],ele[1],ele[2],Trainings_Name[0][0])
                else:
                    Output_text += "{0:5} {1:7} {2:5} {3:5}".format(Wekday_names[ele[0]],ele[1],ele[2],ele[3]) + "\n"

            Display_Lable.config(text=("ID = "+ str(ID) + '\n' + Tabel + '\n' + Output_text))
            Data_List.set(List)

        elif var.get() == 3:
            List = []
            Output_text = ''
            List = [(0,"15:00","17:00",1,2),(1,"15:00","17:00",2,2),(2,"15:00","17:00",3,2),(3,"15:00","17:00",1,2),(4,"15:00","17:00",2,2),(5,"15:00","17:00",3,2),(6,"-","-","-","-")]
            for ele in List:
                if isinstance(ele[3], int) == True:
                    cur.execute("SELECT text_course_description FROM TRAINING WHERE trainings_ID=" + str(ele[3]))
                    Trainings_Name = cur.fetchall()
                    Output_text += "{0:5} {1:7} {2:5} {3:5}".format(Wekday_names[ele[0]],ele[1],ele[2],Trainings_Name[0][0])
                else:
                    Output_text += "{0:5} {1:7} {2:5} {3:5}".format(Wekday_names[ele[0]],ele[1],ele[2],ele[3]) + "\n"

            Display_Lable.config(text=("ID = "+ str(ID) + '\n' + Tabel + '\n' + Output_text))
            Data_List.set(List)

    def Apply_Training():
        
        ID = ID_variable_Data.get()
        Data = ast.literal_eval('[' + Data_List.get()[1:-1] + ']')
        print(Data[0])
        for Element in Data:        
            if isinstance(Element[3], int) == True:

                Day = today + timedelta(days=(Element[0] + 1 - today.weekday()+6))
                Day = Day.strftime("%d.%m.%Y") 
                cur.execute("INSERT INTO TRAINING_DATA (ID_variable_Data,Text_Traning_Date,Text_Training_Start,duration,Text_Training_END,TNR_variable_Data) VALUES (%s,%s,%s,%s,%s,%s)"
                ,(ID,Day,Element[1],Element[4],Element[2],Element[3]))
                con.commit()


        Schedule_window.destroy()
    
    Schedule_window = Toplevel()
    Schedule_window.config(bg=DGrey)
    Schedule_window.title('Training Schedule')

    Schedule_Lable = Label(Schedule_window,text='Choose Training Schedule:',bg=DGrey,fg='White',pady = 2,font=('Calibri', 18))
    Schedule_Lable.grid(column=0,row=0,padx=10,pady=5,sticky='nsew')


    Schedule_Frame_Right = Frame(Schedule_window,width=100,height=500,bg=DGrey,bd=5, highlightbackground='white')
    Schedule_Frame_Right.grid(column=0,row=1,padx=10,pady=5)
    Schedule_Frame_Left = Frame(Schedule_window,width=200,height=500,bg=DGrey,bd=5, highlightbackground='white')
    Schedule_Frame_Left.grid(column=1,row=1,padx=10,pady=5)


    Ckeckbox_text = ['Repeat Training','Training Schedule 1','Training Schedule 2','Training Schedule 3']
    var = IntVar()         #Creating a variable which will track the selected checkbutton
    cb = []                   #Empty list which is going to hold all the checkbutton
    for i in range(4):
        cb.append(Checkbutton(Schedule_Frame_Right, text=Ckeckbox_text[i],bg=DGrey,fg='White',onvalue = i,variable=var,command= lambda : Schedual_Display(),activebackground='black', activeforeground='white',selectcolor="black",))
                            
        cb[i].grid(column=0,row=i,padx=10,pady=5,sticky='nsew')          
    

    
    Display_Lable = Label(Schedule_Frame_Left, text='',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15),width=50,height=20, anchor='n',justify="left")
    Display_Lable.grid(column=0,row=0,padx=10,pady=5,columnspan=2)

    Training_Choosen = Button(Schedule_Frame_Left,text="Apply Training",command=lambda: Apply_Training())
    Training_Choosen.grid(column=2,row=1,padx=10,pady=5,sticky='nsew')

    Schedual_Display(event=None)
## Erster Button Create Athlete -> in Second Frame
def Athlete_Window():
    clear_frame(Second_Fame)
    
    global Gender_variable,Text_Athlete_Name, Text_Athlete_Weight, Text_Athlete_Size, OPTIONS, OPTIONS_ID, ID_variable, Text_Athlete_ID, Text_Athlete_ID2, AGE_Day, AGE_Month, AGE_Year, Day_Variable,Year_Variable,Month_Variable
    OPTIONS_ID = Id_Drop_Aktu()

    Second_Window_TOP = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5, highlightbackground='white')
    Second_Window_TOP.grid(column=0,row=0,padx=10,pady=5,columnspan = 2)

    Label_Second_Window = Label(Second_Window_TOP,text='Create Athlete',bg=LGrey,fg='White',font=('Calibri', 20))
    Label_Second_Window.grid(pady = 45,padx=10, columnspan = 2)

    Second_Window_RIGHT = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5, highlightbackground='white')
    Second_Window_RIGHT.grid(column=0,row=1,padx=10,pady=5,sticky='nsew')

    Second_Window_LEFT = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5,highlightbackground=RGrey)
    Second_Window_LEFT.grid(column=1,row=1,padx=10,pady=5,sticky='nsew')

    #### Widgets
    Label_Athlete_Gender = Label(Second_Window_RIGHT,text='Gender',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Athlete_Gender.grid(column=0,row=0,padx=10,pady=5,sticky='w')
    
    OPTIONS = ['','Male','Female','Divers']
    Gender_variable = StringVar(Second_Window_RIGHT)
    Gender_variable.set(OPTIONS[1])
    Athlete_Gender = ttk.OptionMenu(Second_Window_RIGHT,Gender_variable, *OPTIONS )
    Athlete_Gender.grid(column=1,row=0,padx=10,pady=5,sticky='nsew')
   

    Label_Athlete_Name = Label(Second_Window_RIGHT,text='Name',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Athlete_Name.grid(column=0,row=1,padx=10,pady=5,sticky='w')
    Text_Athlete_Name = Text(Second_Window_RIGHT, height = 1, width = 20)
    Text_Athlete_Name.grid(column=1,row=1,padx=10,pady=5,sticky='nsew')
    Text_Athlete_Name.bind("<Tab>", focus_next_widget)

    Label_AGE = Label(Second_Window_RIGHT,text='Age',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_AGE.grid(column=0,row=2,padx=10,pady=5,sticky='w')

    Day_Variable = IntVar()
    Month_Variable = IntVar()
    Year_Variable = IntVar()
    Age_Frame = Frame(Second_Window_RIGHT,width=450,height=720,bg=LGrey,bd=5, highlightbackground='white')
    Age_Frame.grid(column=1,row=2,padx=10,pady=5,sticky='nsew')
    AGE_Day = Spinbox(Age_Frame, justify=CENTER,width=10,from_=1, to=31,textvariable=Day_Variable)
    AGE_Day.grid(column=0,row=2,padx=5,pady=5,sticky='nsew')
    AGE_Day.bind("<Tab>", focus_next_widget)
    AGE_Month = Spinbox(Age_Frame, justify=CENTER,width=10,from_=1, to=12,textvariable=Month_Variable)
    AGE_Month.grid(column=1,row=2,padx=5,pady=5,sticky='nsew')
    AGE_Month.bind("<Tab>", focus_next_widget)
    AGE_Year = Spinbox(Age_Frame, justify=CENTER,width=10,from_=1900, to=2022,textvariable=Year_Variable)
    AGE_Year.grid(column=2,row=2,padx=5,pady=5,sticky='nsew')
    AGE_Year.bind("<Tab>", focus_next_widget)

    Label_Athlete_Weight = Label(Second_Window_RIGHT,text='Weight',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Athlete_Weight.grid(column=0,row=3,padx=10,pady=5,sticky='w')
    Text_Athlete_Weight = Text(Second_Window_RIGHT, height = 1, width = 20)
    Text_Athlete_Weight.grid(column=1,row=3,padx=10,pady=5,sticky='nsew')
    Text_Athlete_Weight.bind("<Tab>", focus_next_widget)

    Label_Athlete_Size = Label(Second_Window_RIGHT,text='Size',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Athlete_Size.grid(column=0,row=4,padx=10,pady=5,sticky='w')
    Text_Athlete_Size = Text(Second_Window_RIGHT, height = 1, width = 20)
    Text_Athlete_Size.grid(column=1,row=4,padx=10,pady=5,sticky='nsew')
    Text_Athlete_Size.bind("<Tab>", focus_next_widget)

    Label_Athlete_ID = Label(Second_Window_LEFT,text='ID',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Athlete_ID.grid(column=0,row=0,padx=1,pady=10,sticky='ew')

    ID_variable = StringVar(Second_Window_LEFT)
    Text_Athlete_ID2 = ttk.Combobox(Second_Window_LEFT, textvariable=ID_variable, values=OPTIONS_ID)
    Text_Athlete_ID2.current(0)
    Text_Athlete_ID2.bind("<<ComboboxSelected>>", Aktualisieren)
    Text_Athlete_ID2.grid(column=1,row=0,padx=1,pady=10,sticky='nsew')
    Text_Athlete_ID2.bind("<Tab>", focus_next_widget)

    Empty_row = Label(Second_Window_LEFT, text='     \n   ', bg=LGrey)
    Empty_row.grid(column=0, row=2,padx=50,pady=5, )
    Empty_row = Label(Second_Window_RIGHT, text='     \n   ', bg=LGrey)
    Empty_row.grid(column=0, row=5,padx=50,pady=5, )
    ## Der Untere Teil dient der Activen und Inactiven Button
    # dort muss als erste eine Canvas erstelltwerden  werden in dem ein Button eingefügt werden kann
    # danach wird der Button mit Bildern und Funktionen verändert
    canvas_Second_Window = Canvas(Second_Window_RIGHT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window.grid(row=6,padx=50,pady=5, columnspan = 2,sticky='ew')
    canvas_Second_Window2 = Canvas(Second_Window_LEFT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window2.grid(row=3,padx=50,pady=5, columnspan = 2,sticky='w')
    canvas_Second_Window3= Canvas(Second_Window_LEFT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window3.grid(row=4,padx=50,pady=5, columnspan = 2,sticky='n')

    Create_Athlete = Button(canvas_Second_Window)
    Create_Athlete.grid(column=0,row=0)
    Change_Athlete= Button(canvas_Second_Window2)
    Change_Athlete.grid(column=0,row=0)
    Delete_Athlete= Button(canvas_Second_Window3)
    Delete_Athlete.grid(column=0,row=0)
    
    Active_Button(Create_Athlete,canvas_Second_Window,canvas_Second_Window,"Images\Create_Athlete_active.png","Images\Create_Athlete_inactive.png",Create_Athlete_Button,LGrey,LEFT)
    Active_Button(Change_Athlete,canvas_Second_Window2,canvas_Second_Window2,"Images\Change_Athlete_active.png","Images\Change_Athlete_inactive.png",Change_Athlete_Button,LGrey,LEFT)
    Active_Button(Delete_Athlete,canvas_Second_Window3,canvas_Second_Window3,"Images\Delete_Athlete_active.png","Images\Delete_Athlete_inactive.png",Delete_Athlete_Button,LGrey,LEFT)
# Zweiter Button Create Course -> in Second Frae
def Course_Window():
    clear_frame(Second_Fame)
    
    global Text_Course_Designation,Text_Course_Description,Text_Course_TNr, TNR_variable
    OPTIONS_TNR = TNR_Drop_Aktu()

    Second_Window_TOP = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5, highlightbackground='white')
    Second_Window_TOP.grid(column=0,row=0,padx=10,pady=5,columnspan = 2)

    Label_Second_Window = Label(Second_Window_TOP,text='Create Training',bg=LGrey,fg='White',font=('Calibri', 20))
    Label_Second_Window.grid(pady = 45,padx=10, columnspan = 2)

    Second_Window_RIGHT = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5, highlightbackground='white')
    Second_Window_RIGHT.grid(column=0,row=1,padx=10,pady=5,sticky='nsew')

    Second_Window_LEFT = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5,highlightbackground=RGrey)
    Second_Window_LEFT.grid(column=1,row=1,padx=10,pady=5,sticky='nsew')

    #### Widgets

    Label_Course_Designation = Label(Second_Window_RIGHT,text='Designation',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Course_Designation.grid(column=0,row=0,padx=10,pady=5,sticky='w')
    Text_Course_Designation = Text(Second_Window_RIGHT, height = 1, width = 20)
    Text_Course_Designation.grid(column=1,row=0,padx=10,pady=5,sticky='nsew')
    Text_Course_Designation.bind("<Tab>", focus_next_widget)

    Label_Course_Description = Label(Second_Window_RIGHT,text='Description',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Course_Description.grid(column=0,row=1,padx=10,pady=5,sticky='w')
    Text_Course_Description = Text(Second_Window_RIGHT, height = 5, width = 20)
    Text_Course_Description.grid(column=1,row=1,padx=10,pady=5,sticky='nsew')
    Text_Course_Description.bind("<Tab>", focus_next_widget)

    Label_Course_TNr = Label(Second_Window_LEFT,text='TNr',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Course_TNr.grid(column=0,row=0,padx=10,pady=5,sticky='w')


    TNR_variable = StringVar(Second_Window_LEFT)
    Text_Course_TNr = ttk.Combobox(Second_Window_LEFT, textvariable=TNR_variable, values=OPTIONS_TNR)
    Text_Course_TNr.current(0)
    Text_Course_TNr.bind("<<ComboboxSelected>>", Aktualisieren_TNR)
    Text_Course_TNr.grid(column=1,row=0,padx=10,pady=5,sticky='nsew')
    Text_Course_TNr.bind("<Tab>", focus_next_widget)


    Empty_row = Label(Second_Window_LEFT, text='     \n   ', bg=LGrey)
    Empty_row.grid(column=0, row=1,padx=50,pady=5)
    Empty_row = Label(Second_Window_RIGHT, text='     \n   ', bg=LGrey)
    Empty_row.grid(column=0, row=2,padx=50,pady=5)

    canvas_Second_Window = Canvas(Second_Window_RIGHT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window.grid(row=5,padx=50,pady=5, columnspan = 2,sticky='ew')
    canvas_Second_Window2 = Canvas(Second_Window_LEFT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window2.grid(row=3,padx=50,pady=5, columnspan = 2,sticky='w')
    canvas_Second_Window3= Canvas(Second_Window_LEFT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window3.grid(row=4,padx=50,pady=5, columnspan = 2,sticky='n')

    Create_Training = Button(canvas_Second_Window)
    Create_Training.grid(column=0,row=0)
    Change_Traning= Button(canvas_Second_Window2)
    Change_Traning.grid(column=0,row=0)
    Delete_Training= Button(canvas_Second_Window3)
    Delete_Training.grid(column=0,row=0)
    
    Active_Button(Create_Training,canvas_Second_Window,canvas_Second_Window,"Images\Create_Course_active.png","Images\Create_Course_inactive.png",Create_Training_Button,LGrey,LEFT)
    Active_Button(Change_Traning,canvas_Second_Window2,canvas_Second_Window2,"Images\Change_Training_active.png","Images\Change_Training_inactive.png",Change_Training_Button,LGrey,LEFT)
    Active_Button(Delete_Training,canvas_Second_Window3,canvas_Second_Window3,"Images\Delete_Training_active.png","Images\Delete_Training_inactive.png",Delete_Training_Button,LGrey,LEFT)

# Dritter Frame Enter Tranining -> in second frame
def Enter_Training_Window():
    clear_frame(Second_Fame)
    
    global Text_Training_Stop_Hour,Text_Training_Stop_Min,Text_Training_Start_Hour,Text_Training_Start_Min,Output_lable,Text_Course_TNr,ID_variable_Data,TNR_variable_Data,cal

    OPTIONS_ID = Id_Drop_Aktu() 
    OPTIONS_TNR = TNR_Drop_Aktu()

    Second_Window_TOP = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5, highlightbackground='white')
    Second_Window_TOP.grid(column=0,row=0,padx=10,pady=5,columnspan = 2)

    Label_Second_Window = Label(Second_Window_TOP,text='Enter Trainings Data',bg=LGrey,fg='White',font=('Calibri', 20))
    Label_Second_Window.grid(pady = 45,padx=10, columnspan = 2)

    Second_Window_RIGHT = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5, highlightbackground='white')
    Second_Window_RIGHT.grid(column=0,row=1,padx=10,pady=5,sticky='nsew')

    Second_Window_LEFT = Frame(Second_Fame,width=450,height=720,bg=LGrey,bd=5,highlightbackground=RGrey)
    Second_Window_LEFT.grid(column=1,row=1,padx=10,pady=5,sticky='nsew')

    Thirdframe = Frame(Second_Fame,width=100,height=720,bg=LGrey,bd=5,highlightbackground=RGrey)
    Thirdframe.grid(column=2,row=1,padx=10,pady=5,sticky='nsew')

    #### Widgets

    Label_Athlete_Gender = Label(Second_Window_RIGHT,text='Athlete ID',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Athlete_Gender.grid(column=0,row=0,padx=10,pady=5,sticky='w')

    ID_variable_Data = StringVar(Second_Window_LEFT)
    Text_Athlete_ID2 = ttk.Combobox(Second_Window_RIGHT, textvariable=ID_variable_Data, values=OPTIONS_ID)
    #Text_Athlete_ID2.bind("<<ComboboxSelected>>", Aktualisieren)
    Text_Athlete_ID2.grid(column=1,row=0,padx=10,pady=5,sticky='nsew')
    Text_Athlete_ID2.bind("<Tab>", focus_next_widget)

    Label_Traning_Date = Label(Second_Window_RIGHT,text='Date',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Traning_Date.grid(column=0,row=1,padx=10,pady=5,sticky='w')
    cal = Calendar(Second_Window_RIGHT,date_pattern='dd.mm.yyyy',selectmode="day", year=today.year, month=today.month, day=today.day)
    cal.grid(column=1,row=1,padx=10,pady=5)
    cal.bind("<Tab>", focus_next_widget)
    cal.bind("<<CalendarSelected>>", Calendar_select)

    Time_Frame = Frame(Second_Window_RIGHT,bg=LGrey,bd=5, highlightbackground='white')
    Time_Frame.grid(column=1,row=2,padx=10,pady=5)

    Label_Training_Start = Label(Time_Frame,text='Start Time',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Training_Start.grid(column=0,row=2, columnspan = 2,padx=10,pady=5,sticky='nsew')

    Text_Training_Start_Hour = Spinbox(Time_Frame, justify=CENTER,width=10,from_=00, to=24,format="%02.0f")
    Text_Training_Start_Hour.grid(column=0,row=3,padx=5,pady=5,sticky='nsew')
    Text_Training_Start_Hour.bind("<Tab>", focus_next_widget)
    Text_Training_Start_Min = Spinbox(Time_Frame, justify=CENTER,width=10,from_=00, to=60,format="%02.0f")
    Text_Training_Start_Min.grid(column=1,row=3,padx=5,pady=5,sticky='nsew')
    Text_Training_Start_Min.bind("<Tab>", focus_next_widget)

    
    Label_Training_END = Label(Time_Frame,text='End Time',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Training_END.grid(column=0,row=4, columnspan = 2,padx=10,pady=5,sticky='nsew')

    
    Text_Training_Stop_Hour = Spinbox(Time_Frame, justify=CENTER,width=10,from_=00, to=24,format="%02.0f")
    Text_Training_Stop_Hour.grid(column=0,row=5,padx=5,pady=5,sticky='nsew')
    Text_Training_Stop_Hour.bind("<Tab>", focus_next_widget)
    Text_Training_Stop_Min = Spinbox(Time_Frame, justify=CENTER,width=10,from_=00, to=60,format="%02.0f")
    Text_Training_Stop_Min.grid(column=1,row=5, padx=5,pady=5,sticky='nsew')
    Text_Training_Stop_Min.bind("<Tab>", focus_next_widget)


    Label_Course_TNr = Label(Second_Window_LEFT,text='Course (TNr)',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Label_Course_TNr.grid(column=0,row=0,padx=10,pady=5,sticky='w')

    TNR_variable_Data = StringVar(Second_Window_LEFT)
    Text_Course_TNr = ttk.Combobox(Second_Window_LEFT, textvariable=TNR_variable_Data, values=OPTIONS_TNR)
    Text_Course_TNr.current(1)
    #Text_Course_TNr.bind("<<ComboboxSelected>>", Aktualisieren_TNR)
    Text_Course_TNr.grid(column=1,row=0,padx=10,pady=5,sticky='nsew')
    Text_Course_TNr.bind("<Tab>", focus_next_widget)

    Output_Name = Label(Thirdframe, text='Training',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15))
    Output_Name.grid(column=0,row=0,padx=10,pady=5)
    Output_lable = Label(Thirdframe, text='',bg=LGrey,fg='White',pady = 2,font=('Calibri', 15),justify="left")
    Output_lable.grid(column=0,row=1,padx=10,pady=5)

    
    canvas_Second_Window2 = Canvas(Second_Window_LEFT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window2.grid(row=1,padx=50,pady=5, columnspan = 2,sticky='n')
    canvas_Second_Window3= Canvas(Second_Window_LEFT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window3.grid(row=2,padx=50,pady=5, columnspan = 2,sticky='n')
    canvas_Second_Window4= Canvas(Second_Window_LEFT,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
    canvas_Second_Window4.grid(row=3,padx=50,pady=5, columnspan = 2,sticky='n')

    Change_Athlete= Button(canvas_Second_Window2)
    Change_Athlete.grid(column=0,row=0)
    Delete_Athlete= Button(canvas_Second_Window3)
    Delete_Athlete.grid(column=0,row=0)
    repeat_Training = Button(canvas_Second_Window4)
    repeat_Training.grid(column=0,row=0)

    
    Active_Button(Change_Athlete,canvas_Second_Window2,canvas_Second_Window2,"Images\Save_Training_Data_active.png","Images\Save_Training_Data_inactive.png",Save_Training_Data_Button,LGrey,LEFT)
    Active_Button(Delete_Athlete,canvas_Second_Window3,canvas_Second_Window3,"Images\Delete_Training_Data_active.png","Images\Delete_Training_Data_inactive.png",Delete_Training_Data_Button,LGrey,LEFT)
    Active_Button(repeat_Training,canvas_Second_Window4,canvas_Second_Window4,"Images\Training_schedual_active.png","Images\Training_schedual_inactive.png",training_schedule,LGrey,LEFT)
    
def quit():
    root.destroy()
    

### Main WIndow mit den Knöpfen -> Create Training, Create Course und Enter Training

Main_frame = Frame(root,width=300,height=500,bg=LGrey,bd=5, highlightbackground='white')
Main_frame.grid(column=0,row=0,padx=10,pady=5)

Second_Fame = Frame(root,width=680,height=500,bg=LGrey,bd=5,highlightbackground=RGrey)
Second_Fame.grid(column=1,row=0,padx=10,pady=5,sticky='nsew')

### Start Fenster
Label_Main = Label(Main_frame,text='Training Management',bg=LGrey,fg='White',pady = 50,font=('Calibri', 20))
Label_Main.grid(column=0,row=0,padx=10,pady=5)

canvas_main = Canvas(Main_frame,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
canvas_main.grid(column=0,row=1,padx=10,pady=5)

canvas_main2 = Canvas(Main_frame,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
canvas_main2.grid(column=0,row=2,padx=10,pady=5)

canvas_main3 = Canvas(Main_frame,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
canvas_main3.grid(column=0,row=3,padx=10,pady=5)

canvas_main4 = Canvas(Main_frame,width=200,height=100, bg=LGrey,bd=0, highlightbackground=LGrey)
canvas_main4.grid(column=0,row=4,padx=10,pady=5)

Button1 = Button(canvas_main)
Button1.grid(column=0,row=0)

Button2 = Button(canvas_main2)
Button2.grid(column=0,row=0)

Button3 = Button(canvas_main3)
Button3.grid(column=0,row=0)

Button4 = Button(canvas_main4)
Button4.grid(column=0,row=0)

## Create Athlete
Active_Button(Button1,canvas_main,canvas_main,"Images\Create_Athlete_active.png","Images\Create_Athlete_inactive.png",Athlete_Window,LGrey,LEFT)
## Create Course
Active_Button(Button2,canvas_main2,canvas_main2,"Images\Create_Course_active.png","Images\Create_Course_inactive.png",Course_Window,LGrey,LEFT)
##Enter Training Data
Active_Button(Button3,canvas_main3,canvas_main3,"Images\Enter_Trainings_Data_active.png","Images\Enter_Trainings_Data_inactive.png",Enter_Training_Window,LGrey,LEFT)
## Quite
Active_Button(Button4,canvas_main4,canvas_main4,"Images\Quit_active.png","Images\Quit_inactive.png",quit,LGrey,LEFT)


root.mainloop()