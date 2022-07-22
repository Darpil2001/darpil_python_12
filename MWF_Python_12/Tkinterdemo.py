from tkinter import*
import mysql. connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_12"
        )
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
       msg.showinfo("Insert status","All Fileds Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,email,mobile) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Successfully")

root=Tk()
root.geometry("420x370")
root.title("My Tkinter example")
root.resizable(False,False)

l_id=Label(root,text="id")
l_id.place(x=80,y=50)

l_fname=Label(root,text="first name")
l_fname.place(x=80,y=100)

l_lname=Label(root,text="last name")
l_lname.place(x=80,y=150)

l_email=Label(root,text="email")
l_email.place(x=80,y=200)

l_mobile=Label(root,text="mobile")
l_mobile.place(x=80,y=250)

e_id=Entry(root)
e_id.place(x=180,y=50)

e_fname=Entry(root)
e_fname.place(x=180,y=100)

e_lname=Entry(root)
e_lname.place(x=180,y=150)

e_email=Entry(root)
e_email.place(x=180,y=200)

e_mobile=Entry(root)
e_mobile.place(x=180,y=250)

insert=Button(root,text="insert",command=insert_data)
insert.place(x=50,y=300)

insert=Button(root,text="search")
insert.place(x=130,y=300)

insert=Button(root,text="update")
insert.place(x=214,y=300)

insert=Button(root,text="delete")
insert.place(x=298,y=300)

root.mainloop()






        
        
    
