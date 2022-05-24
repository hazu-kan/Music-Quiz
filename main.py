from tkinter import *

root = Tk()

canvas = Canvas(root, width = 700, height = 700)
canvas.pack()

img = PhotoImage(file="images/home_screen.png") 
canvas.create_image(0,0, anchor=NW, image=img) 

mainloop() 