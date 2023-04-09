# Import Tkinter
from tkinter import *
import pymysql
import tkinter.messagebox as m
# Creating a Main Window
r = Tk()
r.geometry("400x400")
r.title("My Title")
r.configure(bg="Orange")

# Connection Function
def CreateConn():
    return pymysql.connect(host="localhost",database="tkinter",user="root",password="",port=3306)


def InsertData():
    r = ern.get()
    f = efn.get()
    l = eln.get()
    e = eem.get()

    if(r=="" or f=="" or l=="" or e==""):
        m.showinfo("Insert Status","All Fields are Mandatory")
    else:
        try:
            conn = CreateConn()
            cursor = conn.cursor()
            args = (r,f,l,e)
            query = "insert into student(rollno,fname,lname,email)values(%s,%s,%s,%s)"
            cursor.execute(query,args)
            conn.commit()
            m.showinfo("Insert Status","Data Inserted")
            conn.close()
        except Exception as ee:
            print("Insert Exception : ",ee)


# Adding Labels in Main Window
rn = Label(r,text="Roll No",bg="orange")
rn.place(x=20,y=20)


fn = Label(r,text="Firstname",bg="orange")
fn.place(x=20,y=60)

ln = Label(r,text="Lastname",bg="orange")
ln.place(x=20,y=100)

em = Label(r,text="Email",bg="orange")
em.place(x=20,y=140)


# Adding Entery box into Main Window

ern = Entry()
ern.place(x=100,y=20)

efn = Entry()
efn.place(x=100,y=60)  

eln = Entry()
eln.place(x=100,y=100)

eem = Entry()
eem.place(x=100,y=140)


# Adding Buttons into Main Window
button1 = Button(r,text="Insert",bg="Green",command=InsertData)
button1.place(x=20,y=200)

mainloop()