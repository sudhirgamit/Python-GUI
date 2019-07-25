from tkinter import *

root=Tk()
root.title("MyGUI")
root.minsize(width=300,height=200)
root.maxsize(width=400,height=300)
root.geometry("500x400")
label=Label(root, text="My Best GUI In Program")
label.pack()
root.mainloop()