import os
from tkinter import *
from tkinter import messagebox

global e1
global e2

root = Tk()
root.title("Login")
root.geometry("300x200")

def Ok():
    global e1, e2
    uname = e1.get()
    password = e2.get()

    if(uname == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
        return False


    elif(uname == "Admin" and password == "123"):

        messagebox.showinfo("","Login Success")
        os.system("python3 main.py")
        root.destroy()

        return True

    else :
        messagebox.showinfo("","Incorrent Username and Password")
        return False

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)
Button(root, text="Login", command=Ok,height = 3, width = 13).place(x=10, y=100)

while True:


    global e1, e2
    e1 = Entry(root)
    e1.place(x=140, y=10)

    e2 = Entry(root)
    e2.place(x=140, y=40)
    e2.config(show="*")

    if Ok():
        os.system("python3 main_kinter.py")
        break

    root.mainloop()