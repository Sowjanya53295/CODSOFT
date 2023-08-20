import tkinter as tk

def press(value):
    current_value=entry.get()
    new_value=current_value +str(value)
    entry.delete(0,tk.END)
    entry.insert(0,new_value)
    
def evaluate():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"ERROR")
    

def clear_field():
      entry.delete(0,tk.END)
    
root=tk.Tk()
root.config(background="white")
root.title("Sample Calculator")

entry=tk.Entry(root ,width=20,font=20)
entry.grid(row=0,column=0,columnspan=10)

button1=tk.Button(root, text="1",font=16,fg='black',bg='white',command=lambda: press(1),height=3,width=7)
button1.grid(row=2,column=1)

button2=tk.Button(root,text="2",font=16,fg='black',bg='white',command=lambda:press(2),height=3,width=7)
button2.grid(row=2,column=2)

button3=tk.Button(root,text="3",font=16,fg='black',bg='white',command=lambda:press(3),height=3,width=7)
button3.grid(row=2,column=3)

button4=tk.Button(root,text="4",font=16,fg='black',bg='white',command=lambda:press(4),height=3,width=7)
button4.grid(row=3,column=1)

button5=tk.Button(root,text="5",font=16,fg='black',bg='white',command=lambda:press(5),height=3,width=7)
button5.grid(row=3,column=2)

button6=tk.Button(root,text="6",font=16,fg='black',bg='white',command=lambda:press(6),height=3,width=7)
button6.grid(row=3,column=3)

button7=tk.Button(root,text="7",font=16,fg='black',bg='white',command=lambda:press(7),height=3,width=7)
button7.grid(row=4,column=1)

button8=tk.Button(root,text="8",font=16,fg='black',bg='white',command=lambda:press(8),height=3,width=7)
button8.grid(row=4,column=2)

button9=tk.Button(root,text="9",font=16,fg='black',bg='white',command=lambda:press(9),height=3,width=7)
button9.grid(row=4,column=3)

button0=tk.Button(root,text="0",font=16,fg='black',bg='white',command=lambda:press(0),height=3,width=7)
button0.grid(row=5,column=2)

plus=tk.Button(root,text="+",font=16,fg='black',bg='white',command=lambda:press("+"),height=3,width=7)
plus.grid(row=2,column=4)

minus=tk.Button(root,text="-",font=16,fg='black',bg='white',command=lambda:press("-"),height=3,width=7)
minus.grid(row=3,column=4)

multiply=tk.Button(root,text="*",font=16,fg='black',bg='white',command=lambda:press("*"),height=3,width=7)
multiply.grid(row=4,column=4)

divide=tk.Button(root,text="/",font=16,fg='black',bg='white',command=lambda:press("/"),height=3,width=7)
divide.grid(row=5,column=4)

decimal=tk.Button(root,text=".",font=16,fg='black',bg='white',command=lambda:press("."),height=3,width=7)
decimal.grid(row=5,column=3)

open=tk.Button(root,text="(",font=16,fg='black',bg='white',command=lambda:press("("),height=3,width=7)
open.grid(row=6,column=3)

close=tk.Button(root,text=")",font=16,fg='black',bg='white',command=lambda:press(")"),height=3,width=7)
close.grid(row=6,column=4)

clear=tk.Button(root,text="Clear",font=16,fg='black',bg='white',command=clear_field,height=3,width=7)
clear.grid(row=6,column=2)

equal=tk.Button(root,text="=",font=16,fg='black',bg='white',command=evaluate,height=3,width=7)
equal.grid(row=5,column=1)

root.mainloop()