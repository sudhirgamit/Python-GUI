from tkinter import *

root=Tk()
root.title("My GUI Menu")
root.geometry("500x400")
root.minsize(width=445,height=345)
root.maxsize(width=550,height=450)
topframe=Frame(root)
bottomframe=Frame(root)
topframe.pack()
bottomframe.pack(side=BOTTOM)
button1=Button(topframe,text="File",bg="skyblue", fg="white",width=10)
button2=Button(topframe,text="Edit", bg="skyblue", fg="white",width=10)
button3=Button(topframe,text="View", bg="skyblue", fg="white",width=10)
button4=Button(topframe,text="Tools", bg="skyblue", fg="white",width=10)
button5=Button(topframe,text="Code",bg="skyblue", fg="white",width=10)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
label1=Label(root,text="Left side label",fg="white",bg="orange")
label2=Label(root,text="Right side label",fg="white",bg="skyblue")
label1.pack(side=LEFT,fill=Y,padx=20,pady=20)
label2.pack(side=BOTTOM,fill=X,padx=20,pady=20)
root.mainloop()