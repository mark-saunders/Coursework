from vpython import *
from tkinter import *
from numpy import *

cube_interface = canvas(title="Rubik's cube solver", height=500, width=500)
scene.ambient = color.gray(0.1)
root = Tk()
root.geometry('1920x1080')

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
_1 = OptionMenu(root, clicked, *options).grid(row=1,column=4)
_2 = OptionMenu(root, clicked, *options).grid(row=1,column=5)
_3 = OptionMenu(root, clicked, *options).grid(row=1,column=6)
_4 = OptionMenu(root, clicked, *options).grid(row=2,column=4)
_5 = OptionMenu(root, clicked, *options).grid(row=2,column=6)
_6 = OptionMenu(root, clicked, *options).grid(row=3,column=4)
_7 = OptionMenu(root, clicked, *options).grid(row=3,column=5)
_8 = OptionMenu(root, clicked, *options).grid(row=3,column=6)

#start = Button(root, command= show, text='start').grid(row=10,column=1)


cube_data = [
    # edge pieces
    ['WRG', np.array([-1, 1, 1])],
    ['WRB', np.array([1, 1, 1])],
    ['WGO', np.array([-1, 1, -1])],
    ['WOB', np.array([1, 1, -1])],
    ['YRG', np.array([-1, -1, 1])],
    ['YRB', np.array([1, -1, 1])],
    ['YOG', np.array([-1, -1, -1])],
    ['YOB', np.array([1, -1, -1])],
    # corner pieces
    ['WR', np.array([0, 1, 1])],
    ['WB', np.array([1, 1, 0])],
    ['WO', np.array([0, 1, -1])],
    ['WG', np.array([-1, 1, 0])],
    ['RG', np.array([-1, 0, 1])],
    ['RB', np.array([1, 0, 1])],
    ['OB', np.array([1, 0, -1])],
    ['OG', np.array([-1, 0, -1])],
    ['YR', np.array([0, -1, 1])],
    ['YB', np.array([1, -1, 0])],
    ['YO', np.array([0, -1, -1])],
    ['YG', np.array([-1, -1, 0])],
    # centres
    ['w', np.array([0, 1.25, 0])],
    ['Y', np.array([0, -1.25, 0])],
    ['G', np.array([-1.25, 0, 0])],
    ['O', np.array([0, 0, -1.25])],
    ['B', np.array([1.25, 0, 0])],
    ['R', np.array([0, 0, 1.25])]
    ]



root.mainloop()