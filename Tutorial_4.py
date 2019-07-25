from tkinter import *

root=Tk()
root.title("MyGUI")
root.geometry("500x400")
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
label1=Label(topframe,text="Top Frame In Gui", fg="blue")
label1.pack()

label2=Label(bottomframe,text="Bottom Frame In Gui",fg="red")
label2.pack()
root.mainloop()