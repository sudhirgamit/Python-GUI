from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""

def btn_1_click():
    global val
    val = val + "1"
    data.set(val)

def btn_2_click():
    global val
    val = val + "2"
    data.set(val)

def btn_3_click():
    global val
    val = val + "3"
    data.set(val)

def btn_add_click():
    global A
    global operator
    global val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_4_click():
    global val
    val = val + "4"
    data.set(val)

def btn_5_click():
    global val
    val = val + "5"
    data.set(val)

def btn_6_click():
    global val
    val = val + "6"
    data.set(val)

def btn_sub_click():
    global A
    global operator
    global val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_7_click():
    global val
    val = val + "7"
    data.set(val)

def btn_8_click():
    global val
    val = val + "8"
    data.set(val)

def btn_9_click():
    global val
    val = val + "9"
    data.set(val)

def btn_mul_click():
    global A
    global operator
    global val
    A = float(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_0_click():
    global val
    val = val + "0"
    data.set(val)

def btn_clr_click():
    global A
    global operator
    global val
    A = 0
    val = ""
    operator = ""
    data.set(val)

def btn_equal_click():
    global A
    global operator
    global val
    val1=val
    if operator=="+":
        x = int((val1.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator=="-":
        x = int((val1.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator=="*":
        x = int((val1.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator=="/":
        x = float((val1.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Not Support")
            A = ""
            val = ""
            data.set(val)
        else:
            c = A / x
            data.set(c)
            val = str(c)


def btn_div_click():
    global A
    global operator
    global val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)


root=Tk()
root.geometry("300x400+300+300")
root.title("Calculator")
root.maxsize(width=300,height=350)
root.minsize(width=300,height=350)

frame1=Frame(root)
frame1.pack()

frame2=Frame(root)
frame2.pack()

frame3=Frame(root)
frame3.pack()

frame4=Frame(root)
frame4.pack()

frame5=Frame(root)
frame5.pack()

data=StringVar()
label=Label(frame1,anchor=SE,textvariable=data,font=("",30,"bold"),width=25,bd=3,background="white",fg="black")
label.pack()
label1=Label(frame1)
label1.pack(pady=7)
btn1=Button(frame1,text="1",bg="skyblue", fg="black",width=8,height=2,command=btn_1_click)
btn1.pack(side=LEFT,pady=10,padx=5)
btn2=Button(frame1,text="2",bg="skyblue", fg="black",width=8,height=2,command=btn_2_click)
btn2.pack(side=LEFT,pady=10,padx=5)
btn3=Button(frame1,text="3",bg="skyblue", fg="black",width=8,height=2,command=btn_3_click)
btn3.pack(side=LEFT,pady=10,padx=5)
btnadd=Button(frame1,text="+",bg="skyblue", fg="black",width=8,height=2,command=btn_add_click)
btnadd.pack(side=LEFT,pady=10,padx=5)

btn4=Button(frame2,text="4",bg="skyblue", fg="black",width=8,height=2,command=btn_4_click)
btn4.pack(side=LEFT,pady=10,padx=5)
btn5=Button(frame2,text="5",bg="skyblue", fg="black",width=8,height=2,command=btn_5_click)
btn5.pack(side=LEFT,pady=10,padx=5)
btn6=Button(frame2,text="6",bg="skyblue", fg="black",width=8,height=2,command=btn_6_click)
btn6.pack(side=LEFT,pady=10,padx=5)
btnsub=Button(frame2,text="-",bg="skyblue", fg="black",width=8,height=2,command=btn_sub_click)
btnsub.pack(side=LEFT,pady=10,padx=5)

btn7=Button(frame3,text="7",bg="skyblue", fg="black",width=8,height=2,command=btn_7_click)
btn7.pack(side=LEFT,pady=10,padx=5)
btn8=Button(frame3,text="8",bg="skyblue", fg="black",width=8,height=2,command=btn_8_click)
btn8.pack(side=LEFT,pady=10,padx=5)
btn9=Button(frame3,text="9",bg="skyblue", fg="black",width=8,height=2,command=btn_9_click)
btn9.pack(side=LEFT,pady=10,padx=5)
btnmul=Button(frame3,text="*",bg="skyblue", fg="black",width=8,height=2,command=btn_mul_click)
btnmul.pack(side=LEFT,pady=10,padx=5)

btn0=Button(frame4,text="0",bg="skyblue", fg="black",width=8,height=2,command=btn_0_click)
btn0.pack(side=LEFT,pady=10,padx=5)
btndiv=Button(frame4,text="/",bg="skyblue", fg="black",width=8,height=2,command=btn_div_click)
btndiv.pack(side=LEFT,pady=10,padx=5)
btnclr=Button(frame4,text="C",bg="skyblue", fg="black",width=8,height=2,command=btn_clr_click)
btnclr.pack(side=LEFT,pady=10,padx=5)
btnequal=Button(frame4,text="=",bg="skyblue", fg="black",width=8,height=2,command=btn_equal_click)
btnequal.pack(side=LEFT,pady=10,padx=5)
root.mainloop()