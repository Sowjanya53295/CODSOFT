import tkinter as tk
import string
import random

def generator():
    lower_letters=string.ascii_lowercase
    upper_letters= string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    value=lower_letters+upper_letters+digits+symbols
    passwordLength=int(lengthbox.get())
    password=random.sample(value,passwordLength)
    passwordfield.insert(0,password)

def reset():
    passwordfield.delete(0,tk.END)
    
root=tk.Tk()
root.config(bg='black')

passwordLabel=tk.Label(root,text='Password Generator',font=('bold',20))
passwordLabel.grid(pady=15)

LengthLabel=tk.Label(root,text='Password Length',font=('bold',13))
LengthLabel.grid(pady=5)

lengthbox=tk.Entry(root,width=5,bd=2)
lengthbox.grid(pady=5)

generatebutton=tk.Button(root,text="Generate",font=('bold',13),command=generator)
generatebutton.grid(pady=5)

passwordfield=tk.Entry(root,width=30,bd=2)
passwordfield.grid(pady=5)

resetbutton=tk.Button(root,text="Reset",font=('bold',13),command=reset)
resetbutton.grid(pady=5)

root.mainloop()