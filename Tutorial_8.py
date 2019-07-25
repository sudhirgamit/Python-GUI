from tkinter import *

root=Tk()
root.title("Event")
root.geometry("500x400")

def left(event):
    print("left button click in mouse..!")

def right(event):
    print("right button click in mouse..!")

def middle(event):
    print("middle button click in mouse..!")

frame=Frame(root,width="400",height=300)
frame.pack()
frame.bind("<Button-1>",left)
frame.bind("<Button-2>",middle)
frame.bind("<Button-3>",right)
root.mainloop()