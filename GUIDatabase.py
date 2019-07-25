import pymysql
from tkinter import *
from tkinter import messagebox

cn = pymysql.connect("localhost","root","","Student")
cursor=cn.cursor()

def Create():
    try:
        query="create table study(name varchar(20),city varchar(20),email varchar(30),password varchar(20))"
        cursor.execute(query)
        messagebox.showinfo("Success","Successfully Created Table..!")
    except:
        messagebox.showerror("Error","Please Try Again..!")

def Insert():
    name = entry1.get()
    city = entry2.get()
    email = entry3.get()
    passwd = entry4.get()

    if(name=="" or city=="" or email=="" or passwd==""):
        messagebox.showwarning("Warning", "Please field the textbox..!")
    else:
        try:
            query = "insert into study(name,city,email,password)values('%s','%s','%s','%s')" % (name,city,email,passwd)
            cursor.execute(query)
            cn.commit()
            messagebox.showinfo("Success", "Successfully Inserted Record..!")
        except:
            messagebox.showerror("Error", "Please Try Again..!")
    #print(name," ",city," ",email," ",passwd)

def Update():
    name = entry1.get()
    city = entry2.get()
    email = entry3.get()
    passwd = entry4.get()

    if (name == "" or city == "" or email == "" or passwd == ""):
        messagebox.showwarning("Warning", "Please field the textbox..!")
    else:
        try:
            query = "update study set city='%s',email='%s',password='%s' where name='%s'" % (city, email, passwd, name)
            cursor.execute(query)
            cn.commit()
            messagebox.showinfo("Success", "Successfully Updated Record..!")
        except:
            messagebox.showerror("Error", "Please Try Again..!")

def Delete():
    name = entry1.get()

    if (name == ""):
        messagebox.showwarning("Warning", "Please field the textbox..!")
    else:
        try:
            query = "delete from study where name='%s'" % (name)
            cursor.execute(query)
            cn.commit()
            messagebox.showinfo("Success", "Successfully Deleted Record..!")
        except:
            messagebox.showerror("Error", "Please Try Again..!")

def Select():
    name = entry1.get()
    city = entry2.get()
    email = entry3.get()
    passwd = entry4.get()
    try:
        query = "select * from study where name='%s' or city='%s' or email='%s' or password='%s'" % (name,city,email,passwd)
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            label6.configure(text=i)
    except:
        messagebox.showerror("Error", "No Records..!")

#def Clear():
#    entry1.get()
#    entry2.get()
#    entry3.get()
#    entry4.get()

root = Tk()
root.title("Student Register")
root.geometry("350x500+350+350")
root.minsize(width=350,height=500)
root.maxsize(width=350,height=500)

frame1 = Frame(root)
frame1.pack()

frame2 = Frame(root)
frame2.pack()

frame3 = Frame(root)
frame3.pack()

frame4 = Frame(root)
frame4.pack()

frame5 = Frame(root)
frame5.pack()

frame6 = Frame(root)
frame6.pack()

frame7 = Frame(root)
frame7.pack()

frame8 = Frame(root)
frame8.pack()


label1 = Label(frame1,text="Name",bd=4,font=("",13,""))
label1.pack(side=LEFT,padx=5,pady=10)

entry1 = Entry(frame1,font=("",12,""),width=25)
entry1.pack(side=LEFT)

label2 = Label(frame2,text="City",bd=4,font=("",13,""))
label2.pack(side=LEFT,padx=12,pady=10)

entry2 = Entry(frame2,font=("",12,""),width=25)
entry2.pack(side=LEFT)

label3 = Label(frame3,text="Email",bd=4,font=("",13,""))
label3.pack(side=LEFT,padx=7,pady=10)

entry3 = Entry(frame3,font=("",12,""),width=25)
entry3.pack(side=LEFT)

label4 = Label(frame4,text="Passwd",bd=4,font=("",13,""))
label4.pack(side=LEFT,pady=10)

entry4 = Entry(frame4,font=("",12,""),width=25)
entry4.pack(side=LEFT)

btnsubmit = Button(frame5,text="Create",width=8,height=2,bg="skyblue",fg="black",command=Create)
btnsubmit.pack(side=LEFT,pady=10)
btnsubmit = Button(frame5,text="Insert",width=8,height=2,bg="skyblue",fg="black",command=Insert)
btnsubmit.pack(side=LEFT,pady=10)
btnsubmit = Button(frame5,text="Update",width=8,height=2,bg="skyblue",fg="black",command=Update)
btnsubmit.pack(side=LEFT,pady=10)
btnsubmit = Button(frame5,text="Delete",width=8,height=2,bg="skyblue",fg="black",command=Delete)
btnsubmit.pack(side=LEFT,pady=10)
btnsubmit = Button(frame5,text="Select",width=8,height=2,bg="skyblue",fg="black",command=Select)
btnsubmit.pack(side=LEFT,pady=10)

#btnsubmit = Button(frame6,text="Clear",width=8,height=2,bg="skyblue",fg="black",command=Clear)
#btnsubmit.pack(pady=10)

label5 = Label(frame7,text="Name       City      Email       Password",bd=4,font=("",13,""))
label5.pack(pady=10)
label6 = Label(frame8,text="No Records..!",bd=4,font=("",13,""),bg="white",fg="black",width=50,height=5)
label6.pack(pady=10)

root.mainloop()
