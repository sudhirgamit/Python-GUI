from tkinter import *
import tkinter.messagebox
import tkinter.filedialog

def custom_quit():
    ans=tkinter.messagebox.askokcancel("Are You Sure ?","Do You Want Exit If You All Data Can Be Lose To Exit..")
    if(ans):
        print("Exit")
        quit()
def new():
    print("New File")

def normal():
    print("Normal Size Of Window")
    root.geometry("500x400")
def small():
    print("Small Size Of Window")
    root.geometry("300x200")
root=Tk()
root.geometry("500x400")
root.title("Notepad")

menu1=Menu(root)
root.config(menu=menu1)

submenu1=Menu(menu1)
menu1.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="New",command=new)
submenu1.add_command(label="Open..",command=open)
submenu1.add_command(label="Save")
submenu1.add_command(label="Save As..")
submenu1.add_command(label="Print")
submenu1.add_separator()
submenu1.add_command(label="Exit",command=custom_quit)

submenu2=Menu(menu1)
menu1.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Normal Size", command=normal)
submenu2.add_command(label="Small Size",command=small)
submenu2.add_command(label="Undo")
submenu2.add_command(label="Cut")
submenu2.add_command(label="Copy")
submenu2.add_command(label="Paste")
submenu2.add_command(label="Delete")
submenu2.add_command(label="Select All")

submenu3=Menu(menu1)
menu1.add_cascade(label="Format",menu=submenu3)
submenu3.add_command(label="Word Wrap")
submenu3.add_command(label="Font..")


submenu4=Menu(menu1)
menu1.add_cascade(label="View",menu=submenu4)
submenu4.add_command(label="Status Bar")

submenu5=Menu(menu1)
menu1.add_cascade(label="Help",menu=submenu5)
submenu5.add_command(label="View Help")
submenu5.add_command(label="About Notepad")

#--------------Status Bar-----------
status=Label(root,text="Running...",relief=SUNKEN,anchor=W,bd=1)
status.pack(side=BOTTOM,fill=X)
root.mainloop()