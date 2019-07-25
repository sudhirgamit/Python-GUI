from tkinter import *

def mydata():
    print("My Name Is Gamit Sudhir...!")
root=Tk()
root.title("Calling Function")
root.geometry("500x400")
button1=Button(root,text="Display",fg="white",bg="skyblue",width=20,command=mydata)
button2=Button(root,text="Exit",fg="white",bg="skyblue",width=20,command=quit)
button1.pack()
button2.pack()
root.mainloop()