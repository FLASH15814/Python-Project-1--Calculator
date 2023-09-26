#Author name - Ranshiv Kumar
from tkinter import *
import tkinter
top=tkinter.Tk()
top.geometry("250x250")
top.maxsize(width=250,height=180)
top.minsize(width=250,height=180)
top.title("calculator")
top.configure(bg="red")
l=Label(top,text="my calculator",fg="red").grid(row=0,column=1,sticky=W)
l1=Label(top,text="First number",).grid(row=1,column=0,sticky=W)
l2=Label(top,text="Second number",).grid(row=2,column=0,sticky=W)
L3=Label(top,text="Operator",).grid(row=3,column=0,sticky=W)
l4=Label(top,text="Answer",).grid(row=4,column=0,sticky=W)

e1=Entry(top,bd=5)
e1.grid(row=1,column=1)
e2=Entry(top,bd=5)
e2.grid(row=2,column=1)
e3=Entry(top,bd=5)
e3.grid(row=3,column=1)
e4=Entry(top,bd=5)
e4.grid(row=4,column=1)

def func():
    number1=Entry.get(e1)
    number2=Entry.get(e2)
    operator=Entry.get(e3)
    number1=int(number1)
    number2=int(number2)
    if operator=="+":
        answer=number1+number2
    if operator=="-":
        answer=number1-number2
    if operator=="*":
        answer=number1*number2
    if operator=="/":
        answer=number1/number2
    Entry.insert(e4,0,answer)
    print(answer)
B=Button(top,text="submit",command=func,bg="purple").grid(row=5,column=1,)
top.mainloop()
