from tkinter import *

root=Tk()
root.title("Student Log In")
root.geometry("500x400")
label1=Label(root,text="Email Id",font=10)
label2=Label(root,text="Password",font=10)
label1.grid(row=0,column=0,sticky="w")
label2.grid(row=1,column=0)
entry1=Entry(root)
entry2=Entry(root)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

check=Checkbutton(root,text="Areyou agree me...!")
button1=Button(root,text="Log In",fg="white",bg="skyblue")
check.grid(column=1)
button1.grid(column=1)
root.mainloop()