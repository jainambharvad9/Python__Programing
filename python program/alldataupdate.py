import mysql.connector as mysql
from tkinter import*
import tkinter.messagebox as messagebox


root=Tk()
root.geometry("300x300")
root.title("Login:")
id=Label(root,text="Enter Id:")
id.place(x=50,y=30)
id_entry=Entry(root)
id_entry.place(x=150,y=30)
name=Label(root,text="Enter Name")
name.place(x=50,y=80)
name_entry=Entry(root)
name_entry.place(x=150,y=80)
phone=Label(root,text="Phone")
phone.place(x=50,y=130)
phone_entry=Entry(root)
phone_entry.place(x=150,y=130)





def update():
    id=id_entry.get()
    name=name_entry.get()
    phone=phone_entry.get()
    
    if(id=="" or name=="" or phone==""):
        messagebox.showinfo("Alert","Please Enter All Field")
    else:
        con=mysql.connect( host="localhost",user="root",password="",database="tybca")
        cursor=con.cursor()
        cursor.execute("update person set name='"+ name +"' ")
        cursor.execute("commit")
        messagebox.showinfo("Status","Complate")
        con.close()

submit=Button(root,text="submit",command=insert)
submit.place(x=150,y=180)
submit=Button(root,text="submit",command=insert)
submit.place(x=150,y=180)
submit=Button(root,text="submit",command=insert)
submit.place(x=150,y=180)

