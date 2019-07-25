from tkinter import *

root=Tk()
root.title("MyGUI")
root.geometry("500x400")
label1=Label(root, text="My first label", fg="red")
label1.pack()
label2=Label(root, text="My second label",fg="white", bg="skyblue")
label2.pack()
root.mainloop()