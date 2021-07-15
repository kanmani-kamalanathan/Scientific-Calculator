from tkinter import *
import math

exp=""

def press(num):
    global exp
    exp=exp+str(num)
    eq.set(exp)

def sine(num):
    try:
        global exp
        ans=str(math.sin(float(num)))
        eq.set(ans)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def cosine(num):
    try:
        global exp
        ans=str(math.cos(float(num)))
        eq.set(ans)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def tangent(num):
    try:
        global exp
        ans=str(math.tan(float(num)))
        eq.set(ans)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def square(num):
    try:
        global exp
        ans=str(float(num)**2)
        eq.set(ans)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def square_root(num):
    try:
        global exp
        ans=str(math.sqrt(float(num)))
        eq.set(ans)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def lg(num):
    try:
        global exp
        ans=str(math.log(float(num)))
        eq.set(ans)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def fact(num):
    try:
        global exp
        ans=str(math.factorial(int(num)))
        eq.set(ans)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def equalpress():
    try:
        global exp
        total=str(eval(exp))
        eq.set(total)
        exp=""
    except:
        eq.set(" error ")
        exp=""

def clear():
    global exp
    exp=""
    eq.set("")

if __name__=="__main__":
    gui=Tk()
    gui.configure(background="black")
    gui.title("Calculator")
    gui.geometry("425x460")
    eq=StringVar()
    exp_field=Entry(gui,textvariable=eq)
    exp_field.grid(columnspan=7,ipadx=140,ipady=10,padx=10,pady=10)
    
    button1=Button(gui,text='1',fg='black',bg='blue',command=lambda:press(1),height=3,width=12)
    button1.grid(row=4,column=0,padx=5,pady=5)
    button2=Button(gui,text='2',fg='black',bg='blue',command=lambda:press(2),height=3,width=12)
    button2.grid(row=4,column=1,padx=5,pady=5)
    button3=Button(gui,text='3',fg='black',bg='blue',command=lambda:press(3),height=3,width=12)
    button3.grid(row=4,column=2,padx=5,pady=5)
    
    button4=Button(gui,text='4',fg='black',bg='blue',command=lambda:press(4),height=3,width=12)
    button4.grid(row=5,column=0,padx=5,pady=5)
    button5=Button(gui,text='5',fg='black',bg='blue',command=lambda:press(5),height=3,width=12)
    button5.grid(row=5,column=1,padx=5,pady=5)
    button6=Button(gui,text='6',fg='black',bg='blue',command=lambda:press(6),height=3,width=12)
    button6.grid(row=5,column=2,padx=5,pady=5)
    
    button7=Button(gui,text='7',fg='black',bg='blue',command=lambda:press(7),height=3,width=12)
    button7.grid(row=6,column=0,padx=5,pady=5)
    button8=Button(gui,text='8',fg='black',bg='blue',command=lambda:press(8),height=3,width=12)
    button8.grid(row=6,column=1,padx=5,pady=5)
    button9=Button(gui,text='9',fg='black',bg='blue',command=lambda:press(9),height=3,width=12)
    button9.grid(row=6,column=2,padx=5,pady=5)

    button0=Button(gui,text='0',fg='black',bg='blue',command=lambda:press(0),height=3,width=12)
    button0.grid(row=7,column=1,padx=5,pady=5)

    plus=Button(gui,text='+',fg='black',bg='green',command=lambda:press("+"),height=3,width=12)
    plus.grid(row=4,column=3,padx=5,pady=5)
    minus=Button(gui,text='-',fg='black',bg='green',command=lambda:press("-"),height=3,width=12)
    minus.grid(row=5,column=3,padx=5,pady=5)
    multiply=Button(gui,text='*',fg='black',bg='green',command=lambda:press("*"),height=3,width=12)
    multiply.grid(row=6,column=3,padx=5,pady=5)
    divide=Button(gui,text='/',fg='black',bg='green',command=lambda:press("/"),height=3,width=12)
    divide.grid(row=7,column=3,padx=5,pady=5)

    point=Button(gui,text='.',fg='black',bg='green',command=lambda:press("."),height=3,width=12)
    point.grid(row=7,column=0,padx=5,pady=5)
    equal=Button(gui,text='=',fg='black',bg='green',command=equalpress,height=3,width=12)
    equal.grid(row=7,column=2,padx=5,pady=5)
    clear=Button(gui,text='Clear',fg='black',bg='green',command=clear,height=3,width=12)
    clear.grid(row=2,column=3,padx=5,pady=5)

    s=Button(gui,text='sin',fg='black',bg='green',command=lambda:sine(exp),height=3,width=12)
    s.grid(row=3,column=0,padx=5,pady=5)

    cs=Button(gui,text='cos',fg='black',bg='green',command=lambda:cosine(exp),height=3,width=12)
    cs.grid(row=3,column=1,padx=5,pady=5)

    t=Button(gui,text='tan',fg='black',bg='green',command=lambda:tangent(exp),height=3,width=12)
    t.grid(row=3,column=2,padx=5,pady=5)

    sq=Button(gui,text='x\u00b2',fg='black',bg='green',command=lambda:square(exp),height=3,width=12)
    sq.grid(row=2,column=1,padx=5,pady=5)

    sr=Button(gui,text='√x',fg='black',bg='green',command=lambda:square_root(exp),height=3,width=12)
    sr.grid(row=2,column=2,padx=5,pady=5)

    l=Button(gui,text='log',fg='black',bg='green',command=lambda:lg(exp),height=3,width=12)
    l.grid(row=2,column=0,padx=5,pady=5)

    f=Button(gui,text='x!',fg='black',bg='green',command=lambda:fact(exp),height=3,width=12)
    f.grid(row=3,column=3,padx=5,pady=5)

    gui.mainloop()
