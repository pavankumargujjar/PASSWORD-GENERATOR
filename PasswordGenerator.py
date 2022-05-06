#PASSWORD GENERATOR(PROJ3)

from tkinter import *                 #used for UI
import random, string
import paperclip               #used to copy and paste...

root = Tk()
root.title("Pride Password Generator")
root.geometry("400x400")
root.resizable(0,0)

heading = Label(root,text="PRIDE PASSWORD GENERATOR",font=("arial 15 bold")).pack()

pass_label =Label(root, text="Password Length", font=("arial 10 bold")).pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable= pass_len, width = 15).pack()

pass_str = StringVar()

def Generator():
    password =''
    for x in range(0, 4):
        password = random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    pass_str.set(password)


Button(root, text="Generator Password", command="Generator").pack(pady=5)

Entry(root, textvariable = pass_str).pack()

def Copy_password():
    paperclip.copy(pass_str.get())

Button(root, text="Copy To Clipboard", command = "Copy_password").pack(pady=5)

root.mainloop()


