from tkinter import *
from vpython import *

root = Tk()
root.geometry('1920x1080')

cube_interface = canvas(title="Rubik's cube solver", height=500, width=500)
cube = box(size=vector(1,1,1), color = color.white)


def show():
    if clicked.get() == options[0]:
        cube.color = color.white
    elif clicked.get() == options[1]:
        cube.color = color.green
    elif clicked.get() == options[2]:
        cube.color = color.orange
    elif clicked.get() == options[3]:
        cube.color = color.blue
    elif clicked.get() == options[4]:
        cube.color = color.red
    elif clicked.get() == options[5]:
        cube.color = color.yellow

options = [
    'White',
    'Green',
    'Orange',
    'Blue',
    'Red',
    'Yellow'
]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

mybutton = Button(root, command= show, text='apply to cube').pack()

root.mainloop()