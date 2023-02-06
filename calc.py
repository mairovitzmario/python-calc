from tkinter import *
import tkinter as tk
from math import *

def sigma(formula, k, n, sgn='+'):
    if sgn!='+' and sgn!='*':
        return 'incorrect expression'
    if sgn=='+':
        s=0
    else:
        s=1
    for x in range(k,n+1):
        f_aux = formula.replace('k', str(x))
        try:
            e = eval(f_aux)
            if e.__class__ != int and e.__class__ != float:
                raise ValueError
            if sgn=='+':
                s+=e
            else:
                s*=e
        except:
            s = 'incorrect expression'
            break
    return s

def calculator(txt):
    try:
        e = eval(txt)
        print(e.__class__)
        if e.__class__ != int and e.__class__ != float:
            raise ValueError
    except:
        e = 'incorrect expression'
    return e


def update_textbox():
    txt = txt_input.get("1.0","end-1c")
    e = calculator(txt)
    txt_output.delete("1.0", "end")
    txt_output.insert(tk.END, str(e))

root = Tk()
root.title('Calculator')
root.geometry("550x240")

txt_input = Text(root, height = 5, width = 52)
txt_output = Text(root, height=5, width=10)
 
l = Label(root, text = "Calculator")
l.config(font =("Courier", 14))
l1 = Label(root, text = "Enter expression:")
l2 = Label(root, text = "Result:")
l1.config(font =("Courier", 14))
l2.config(font =("Courier", 14))

b1 = Button(root, text = "Calculate", command=update_textbox)
 
l.grid(row=0,padx=0,pady=10)
l1.grid(row=1, column=0,padx=12)
txt_input.grid(row = 2,column = 0,padx=12,pady=20)
l2.grid(row = 1, column=1,padx=10)
txt_output.grid(row = 2,column=1,pady=20)
b1.grid(row=3,column=0)

mainloop()