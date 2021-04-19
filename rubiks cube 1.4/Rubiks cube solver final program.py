from rubik.cube import *
from rubik.solve import *
from rubik.optimize import *
from rubik_solver import utils
import kociemba
from vpython import *
from tkinter import *
import numpy as np

solved_cube_str = Cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")

W = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
G = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
O = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
B = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
R = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
Y = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)

up_piece = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
left_piece = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
back_piece = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
right_piece = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
front_piece = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
down_piece = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)

up_1 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_2 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_3 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_4 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_5 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_6 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_7 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_8 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_9 = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
up_layer = [up_1,up_2,up_3,up_4,up_5,up_6,up_7,up_8,up_9]


left_1 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_2 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_3 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_4 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_5 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_6 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_7 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_8 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_9 = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
left_layer = [left_1,left_2,left_3,left_4,left_5,left_6,left_7,left_8,left_9]

back_1 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_2 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_3 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_4 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_5 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_6 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_7 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_8 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_9 = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
back_layer =[back_1,back_2,back_3,back_4,back_5,back_6,back_7,back_8,back_9]

right_1 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_2 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_3 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_4 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_5 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_6 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_7 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_8 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_9 = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
right_layer = [right_1,right_2,right_3,right_4,right_5,right_6,right_7,right_8,right_9]

front_1 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_2 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_3 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_4 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_5 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_6 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_7 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_8 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_9 = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
front_layer = [front_1,front_2,front_3,front_4,front_5,front_6,front_7,front_8,front_9]

down_1 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_2 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_3 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_4 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_5 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_6 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_7 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_8 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_9 = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)
down_layer = [down_1,down_2,down_3,down_4,down_5,down_6,down_7,down_8,down_9]

class Interface(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('rubiks cube solver input screen')

        self.start = Button(text='start/apply', command=self.apply).grid(column=1, row=10)
        self.move = Button(text='Moves to solve', command=self.moves).grid(column=1,row=12)
        self.solve = Button(text='Solve cube', command=self.solve).grid(column=2,row=12)
        self.reset_cube = Button(text='reset cube', command=self.reset).grid(column=2, row=10)

        self.options = ['White', 'Green', 'Orange', 'Blue', 'Red', 'Yellow']
        self.options_dict = {'Yellow': up_piece, 'Green': left_piece, 'Orange': back_piece, 'Blue': right_piece, 'Red': front_piece, 'White': down_piece}
        self.option_var_up = [
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)]
            ]


        self.option_var_left = [
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)]
        ]

        self.option_var_front = [
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)]
        ]

        self.option_var_right = [
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)]
        ]

        self.option_var_back = [
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)]
        ]

        self.option_var_down = [
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)],
            [StringVar(self), StringVar(self), StringVar(self)]
        ]

        self.create_options()





    def create_options(self):

        U_1 = OptionMenu(self, self.option_var_up[0][0], self.option_var_up[0][0].set(self.options[5]),*self.options).grid(row=1, column=4)
        U_2 = OptionMenu(self, self.option_var_up[0][1], self.option_var_up[0][1].set(self.options[5]),*self.options).grid(row=1, column=5)
        U_3 = OptionMenu(self, self.option_var_up[0][2], self.option_var_up[0][2].set(self.options[5]),*self.options).grid(row=1, column=6)
        U_4 = OptionMenu(self, self.option_var_up[1][0], self.option_var_up[1][0].set(self.options[5]),*self.options).grid(row=2, column=4)
        U_6 = OptionMenu(self, self.option_var_up[1][2], self.option_var_up[1][2].set(self.options[5]),*self.options).grid(row=2, column=6)
        U_7 = OptionMenu(self, self.option_var_up[2][0], self.option_var_up[2][0].set(self.options[5]),*self.options).grid(row=3, column=4)
        U_8 = OptionMenu(self, self.option_var_up[2][1], self.option_var_up[2][1].set(self.options[5]),*self.options).grid(row=3, column=5)
        U_9 = OptionMenu(self, self.option_var_up[2][2], self.option_var_up[2][2].set(self.options[5]),*self.options).grid(row=3, column=6)

        L_1 = OptionMenu(self, self.option_var_left[0][0], self.option_var_left[0][0].set(self.options[1]), *self.options).grid(row=4, column=1)
        L_2 = OptionMenu(self, self.option_var_left[0][1], self.option_var_left[0][1].set(self.options[1]), *self.options).grid(row=4, column=2)
        L_3 = OptionMenu(self, self.option_var_left[0][2], self.option_var_left[0][2].set(self.options[1]), *self.options).grid(row=4, column=3)
        L_4 = OptionMenu(self, self.option_var_left[1][0], self.option_var_left[1][0].set(self.options[1]), *self.options).grid(row=5, column=1)
        L_6 = OptionMenu(self, self.option_var_left[1][2], self.option_var_left[1][2].set(self.options[1]), *self.options).grid(row=5, column=3)
        L_7 = OptionMenu(self, self.option_var_left[2][0], self.option_var_left[2][0].set(self.options[1]), *self.options).grid(row=6, column=1)
        L_8 = OptionMenu(self, self.option_var_left[2][1], self.option_var_left[2][1].set(self.options[1]), *self.options).grid(row=6, column=2)
        L_9 = OptionMenu(self, self.option_var_left[2][2], self.option_var_left[2][2].set(self.options[1]), *self.options).grid(row=6, column=3)

        F_1 = OptionMenu(self, self.option_var_front[0][0], self.option_var_front[0][0].set(self.options[4]), *self.options).grid(row=4, column=4)
        F_2 = OptionMenu(self, self.option_var_front[0][1], self.option_var_front[0][1].set(self.options[4]), *self.options).grid(row=4, column=5)
        F_3 = OptionMenu(self, self.option_var_front[0][2], self.option_var_front[0][2].set(self.options[4]), *self.options).grid(row=4, column=6)
        F_4 = OptionMenu(self, self.option_var_front[1][0], self.option_var_front[1][0].set(self.options[4]), *self.options).grid(row=5, column=4)
        F_6 = OptionMenu(self, self.option_var_front[1][2], self.option_var_front[1][2].set(self.options[4]), *self.options).grid(row=5, column=6)
        F_7 = OptionMenu(self, self.option_var_front[2][0], self.option_var_front[2][0].set(self.options[4]), *self.options).grid(row=6, column=4)
        F_8 = OptionMenu(self, self.option_var_front[2][1], self.option_var_front[2][1].set(self.options[4]), *self.options).grid(row=6, column=5)
        F_9 = OptionMenu(self, self.option_var_front[2][2], self.option_var_front[2][2].set(self.options[4]), *self.options).grid(row=6, column=6)

        R_1 = OptionMenu(self, self.option_var_right[0][0], self.option_var_right[0][0].set(self.options[3]), *self.options).grid(row=4, column=7)
        R_2 = OptionMenu(self, self.option_var_right[0][1], self.option_var_right[0][1].set(self.options[3]), *self.options).grid(row=4, column=8)
        R_3 = OptionMenu(self, self.option_var_right[0][2], self.option_var_right[0][2].set(self.options[3]), *self.options).grid(row=4, column=9)
        R_4 = OptionMenu(self, self.option_var_right[1][0], self.option_var_right[1][0].set(self.options[3]), *self.options).grid(row=5, column=7)
        R_6 = OptionMenu(self, self.option_var_right[1][2], self.option_var_right[1][2].set(self.options[3]), *self.options).grid(row=5, column=9)
        R_7 = OptionMenu(self, self.option_var_right[2][0], self.option_var_right[2][0].set(self.options[3]), *self.options).grid(row=6, column=7)
        R_8 = OptionMenu(self, self.option_var_right[2][1], self.option_var_right[2][1].set(self.options[3]), *self.options).grid(row=6, column=8)
        R_9 = OptionMenu(self, self.option_var_right[2][2], self.option_var_right[2][2].set(self.options[3]), *self.options).grid(row=6, column=9)

        B_1 = OptionMenu(self, self.option_var_back[0][0], self.option_var_back[0][0].set(self.options[2]), *self.options).grid(row=4, column=10)
        B_2 = OptionMenu(self, self.option_var_back[0][1], self.option_var_back[0][1].set(self.options[2]), *self.options).grid(row=4, column=11)
        B_3 = OptionMenu(self, self.option_var_back[0][2], self.option_var_back[0][2].set(self.options[2]), *self.options).grid(row=4, column=12)
        B_4 = OptionMenu(self, self.option_var_back[1][0], self.option_var_back[1][0].set(self.options[2]), *self.options).grid(row=5, column=10)
        B_6 = OptionMenu(self, self.option_var_back[1][2], self.option_var_back[1][2].set(self.options[2]), *self.options).grid(row=5, column=12)
        B_7 = OptionMenu(self, self.option_var_back[2][0], self.option_var_back[2][0].set(self.options[2]), *self.options).grid(row=6, column=10)
        B_8 = OptionMenu(self, self.option_var_back[2][1], self.option_var_back[2][1].set(self.options[2]), *self.options).grid(row=6, column=11)
        B_9 = OptionMenu(self, self.option_var_back[2][2], self.option_var_back[2][2].set(self.options[2]), *self.options).grid(row=6, column=12)

        D_1 = OptionMenu(self, self.option_var_down[0][0], self.option_var_down[0][0].set(self.options[0]), *self.options).grid(row=7, column=4)
        D_2 = OptionMenu(self, self.option_var_down[0][1], self.option_var_down[0][1].set(self.options[0]), *self.options).grid(row=7, column=5)
        D_3 = OptionMenu(self, self.option_var_down[0][2], self.option_var_down[0][2].set(self.options[0]), *self.options).grid(row=7, column=6)
        D_4 = OptionMenu(self, self.option_var_down[1][0], self.option_var_down[1][0].set(self.options[0]), *self.options).grid(row=8, column=4)
        D_6 = OptionMenu(self, self.option_var_down[1][2], self.option_var_down[1][2].set(self.options[0]), *self.options).grid(row=8, column=6)
        D_7 = OptionMenu(self, self.option_var_down[2][0], self.option_var_down[2][0].set(self.options[0]), *self.options).grid(row=9, column=4)
        D_8 = OptionMenu(self, self.option_var_down[2][1], self.option_var_down[2][1].set(self.options[0]), *self.options).grid(row=9, column=5)
        D_9 = OptionMenu(self, self.option_var_down[2][2], self.option_var_down[2][2].set(self.options[0]), *self.options).grid(row=9, column=6)



        layers = [self.option_var_up,self.option_var_left,self.option_var_back,self.option_var_right,self.option_var_front,self.option_var_down]
        selected_layer = [up_layer,left_layer,back_layer,right_layer,front_layer,down_layer]

    def solve(self):
        cube.solve(cube)

    def reset(self):
        cube.reset(cube)

    def apply(self):
        selected_layer = [up_layer, left_layer, back_layer, right_layer, front_layer, down_layer]
        layers = [self.option_var_up, self.option_var_left, self.option_var_back, self.option_var_right,
                  self.option_var_front, self.option_var_down]
        for x in range(6):
            self.test_(selected_layer[x],layers[x])
        cube.__init__(cube)


    def test_(self,layer, option):
        count = 0
        for x in range(3):
            for y in range(3):
                colour_string = option[x][y].get()
                colour = self.options_dict.get(colour_string)
                if colour_string == 'White':
                    layer[count].color = color.white
                elif colour_string == 'Green':
                    layer[count].color = color.green
                elif colour_string == 'Orange':
                    layer[count].color = color.orange
                elif colour_string == 'Blue':
                    layer[count].color = color.blue
                elif colour_string == 'Red':
                    layer[count].color = color.red
                elif colour_string == 'Yellow':
                    layer[count].color = color.yellow
                count = count + 1



    def moves(self):
        cube.keys(cube)





class cube:
    cube_data = [
        # edge pieces
        [[up_7, front_1, left_3], np.array([-1, 1, 1])],
        [[up_9, front_3, right_1], np.array([1, 1, 1])],
        [[up_1, left_1, back_3], np.array([-1, 1, -1])],
        [[up_3, back_1, right_3], np.array([1, 1, -1])],
        [[down_1, front_7, left_9], np.array([-1, -1, 1])],
        [[down_3, front_9, right_7], np.array([1, -1, 1])],
        [[down_7, back_9, left_7], np.array([-1, -1, -1])],
        [[down_9, back_7, right_9], np.array([1, -1, -1])],
        # corner pieces
        [[up_8, front_2], np.array([0, 1, 1])],
        [[up_6, right_2], np.array([1, 1, 0])],
        [[up_2, back_2], np.array([0, 1, -1])],
        [[up_4, left_2], np.array([-1, 1, 0])],
        [[front_4, left_6], np.array([-1, 0, 1])],
        [[front_6, right_4], np.array([1, 0, 1])],
        [[back_4, right_6], np.array([1, 0, -1])],
        [[back_6, left_4], np.array([-1, 0, -1])],
        [[down_2, front_8], np.array([0, -1, 1])],
        [[down_6, right_8], np.array([1, -1, 0])],
        [[down_8, back_8], np.array([0, -1, -1])],
        [[down_4, left_8], np.array([-1, -1, 0])],
        # centres
        [up_piece, np.array([0, 1.25, 0])],
        [down_piece, np.array([0, -1.25, 0])],
        [left_piece, np.array([-1.25, 0, 0])],
        [back_piece, np.array([0, 0, -1.25])],
        [right_piece, np.array([1.25, 0, 0])],
        [front_piece, np.array([0, 0, 1.25])]
    ]

    # cube_str = Cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")
    # cube_str = Cube("yyyyyyyyybbbrrrgggooobbbrrrgggooobbbrrrgggooowwwwwwwww")
    cube_str = Cube("yyyyyyyyybbbrrrgggooobbbrrrgggooobbbrrrgggooowwwwwwwww")


    def __init__(self):
        # White, green, orange, blue, red, yellow corners
        self.Y = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), color=color.yellow,
                         visible=False)
        self.G = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), color=color.green,
                         visible=False)
        self.O = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), color=color.orange,
                         visible=False)
        self.B = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), color=color.blue,
                         visible=False)
        self.R = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), color=color.red,
                         visible=False)
        self.W = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0),
                         visible=False)

        # corner pieces#

        self.WRG = compound([self.cube_data[0][0][0], self.cube_data[0][0][1], self.cube_data[0][0][2]],
                            pos=vector(self.cube_data[0][1][0], self.cube_data[0][1][1], self.cube_data[0][1][2]))
        self.WRB = compound([self.cube_data[1][0][0], self.cube_data[1][0][1], self.cube_data[1][0][2]],
                            pos=vector(self.cube_data[1][1][0], self.cube_data[1][1][1], self.cube_data[1][1][2]))
        self.WGO = compound([self.cube_data[2][0][0], self.cube_data[2][0][1], self.cube_data[2][0][2]],
                            pos=vector(self.cube_data[2][1][0], self.cube_data[2][1][1], self.cube_data[2][1][2]))
        self.WOB = compound([self.cube_data[3][0][0], self.cube_data[3][0][1], self.cube_data[3][0][2]],
                            pos=vector(self.cube_data[3][1][0], self.cube_data[3][1][1], self.cube_data[3][1][2]))
        self.YRG = compound([self.cube_data[4][0][0], self.cube_data[4][0][1], self.cube_data[4][0][2]],
                            pos=vector(self.cube_data[4][1][0], self.cube_data[4][1][1], self.cube_data[4][1][2]))
        self.YRB = compound([self.cube_data[5][0][0], self.cube_data[5][0][1], self.cube_data[5][0][2]],
                            pos=vector(self.cube_data[5][1][0], self.cube_data[5][1][1], self.cube_data[5][1][2]))
        self.YOG = compound([self.cube_data[6][0][0], self.cube_data[6][0][1], self.cube_data[6][0][2]],
                            pos=vector(self.cube_data[6][1][0], self.cube_data[6][1][1], self.cube_data[6][1][2]))
        self.YOB = compound([self.cube_data[7][0][0], self.cube_data[7][0][1], self.cube_data[7][0][2]],
                            pos=vector(self.cube_data[7][1][0], self.cube_data[7][1][1], self.cube_data[7][1][2]))
        # edge pieces#
        self.WR = compound([self.cube_data[8][0][0], self.cube_data[8][0][1]],
                           pos=vector(self.cube_data[8][1][0], self.cube_data[8][1][1], self.cube_data[8][1][2]))
        self.WB = compound([self.cube_data[9][0][0], self.cube_data[9][0][1]],
                           pos=vector(self.cube_data[9][1][0], self.cube_data[9][1][1], self.cube_data[9][1][2]))
        self.WO = compound([self.cube_data[10][0][0], self.cube_data[10][0][1]],
                           pos=vector(self.cube_data[10][1][0], self.cube_data[10][1][1], self.cube_data[10][1][2]))
        self.WG = compound([self.cube_data[11][0][0], self.cube_data[11][0][1]],
                           pos=vector(self.cube_data[11][1][0], self.cube_data[11][1][1], self.cube_data[11][1][2]))
        self.RG = compound([self.cube_data[12][0][0], self.cube_data[12][0][1]],
                           pos=vector(self.cube_data[12][1][0], self.cube_data[12][1][1], self.cube_data[12][1][2]))
        self.RB = compound([self.cube_data[13][0][0], self.cube_data[13][0][1]],
                           pos=vector(self.cube_data[13][1][0], self.cube_data[13][1][1], self.cube_data[13][1][2]))
        self.OB = compound([self.cube_data[14][0][0], self.cube_data[14][0][1]],
                           pos=vector(self.cube_data[14][1][0], self.cube_data[14][1][1], self.cube_data[14][1][2]))
        self.OG = compound([self.cube_data[15][0][0], self.cube_data[15][0][1]],
                           pos=vector(self.cube_data[15][1][0], self.cube_data[15][1][1], self.cube_data[15][1][2]))
        self.YR = compound([self.cube_data[16][0][0], self.cube_data[16][0][1]],
                           pos=vector(self.cube_data[16][1][0], self.cube_data[16][1][1], self.cube_data[16][1][2]))
        self.YB = compound([self.cube_data[17][0][0], self.cube_data[17][0][1]],
                           pos=vector(self.cube_data[17][1][0], self.cube_data[17][1][1], self.cube_data[17][1][2]))
        self.YO = compound([self.cube_data[18][0][0], self.cube_data[18][0][1]],
                           pos=vector(self.cube_data[18][1][0], self.cube_data[18][1][1], self.cube_data[18][1][2]))
        self.YG = compound([self.cube_data[19][0][0], self.cube_data[19][0][1]],
                           pos=vector(self.cube_data[19][1][0], self.cube_data[19][1][1], self.cube_data[19][1][2]))
        # centres#
        self.yellow_c = compound([self.Y], pos=vector(self.cube_data[20][1][0], self.cube_data[20][1][1],self.cube_data[20][1][2]))
        self.white_c = compound([self.W], pos=vector(self.cube_data[21][1][0], self.cube_data[21][1][1],self.cube_data[21][1][2]))
        self.green_c = compound([self.G], pos=vector(self.cube_data[22][1][0], self.cube_data[22][1][1],self.cube_data[22][1][2]))
        self.orange_c = compound([self.O], pos=vector(self.cube_data[23][1][0], self.cube_data[23][1][1],self.cube_data[23][1][2]))
        self.blue_c = compound([self.B], pos=vector(self.cube_data[24][1][0], self.cube_data[24][1][1],self.cube_data[24][1][2]))
        self.red_c = compound([self.R], pos=vector(self.cube_data[25][1][0], self.cube_data[25][1][1],self.cube_data[25][1][2]))

        self.cube = [
            self.WRG, self.WRB, self.WGO, self.WOB,
            self.YRG, self.YRB, self.YOG, self.YOB,
            self.WR, self.WB, self.WO, self.WG,
            self.RG, self.RB, self.OB, self.OG,
            self.YR, self.YB, self.YO, self.YG,
            self.white_c,self.yellow_c,self.green_c,
            self.orange_c,self.blue_c,self.red_c
        ]


        self.keys(self)



    def rotations(self, rotation):
        U_rotation = np.array([[round(cos(radians(90))), 0, round(sin(radians(90)))],
                               [0, 1, 0],
                               [round(-sin(radians(90))), 0, round(cos(radians(90)))]])

        R_rotation = np.array([[1, 0, 0],
                               [0, round(cos(radians(90))), round(-sin(radians(90)))],
                               [0, round(sin(radians(90))), round(cos(radians(90)))]])

        L_rotation = np.array([[1, 0, 0],
                               [0, round(cos(radians(-90))), round(-sin(radians(-90)))],
                               [0, round(sin(radians(-90))), round(cos(radians(-90)))]])

        F_rotation = np.array([[round(cos(radians(90))), round(-sin(radians(90))), 0],
                               [round(sin(radians(90))), round(cos(radians(90))), 0],
                               [0, 0, 1]])

        D_rotation = np.array([[round(cos(radians(-90))), 0, round(sin(radians(-90)))],
                               [0, 1, 0],
                               [round(-sin(radians(-90))), 0, round(cos(radians(-90)))]])

        B_rotation = np.array([[round(cos(radians(-90))), round(-sin(radians(-90))), 0],
                               [round(sin(radians(-90))), round(cos(radians(-90))), 0],
                               [0, 0, 1]])

        if rotation == 'u':
            self.rotate_face(self,1,1,U_rotation,vector(0,-1,0))
        elif rotation == 'd':
            self.rotate_face(self,1,-1,D_rotation,vector(0,1,0))
        elif rotation == 'l':
            self.rotate_face(self,0,-1,L_rotation,vector(1,0,0))
        elif rotation == 'r':
            self.rotate_face(self,0,1,R_rotation,vector(-1,0,0))
        elif rotation == 'f':
            self.rotate_face(self,2,1,F_rotation,vector(0,0,-1))
        elif rotation == 'b':
            self.rotate_face(self,2,-1,B_rotation,vector(0,0,1))
        elif rotation == 'U':
            self.rotate_face(self,1,1,D_rotation,vector(0,1,0))
        elif rotation == 'D':
            self.rotate_face(self,1,-1,U_rotation,vector(0,-1,0))
        elif rotation == 'L':
            self.rotate_face(self,0,-1,R_rotation,vector(-1,0,0))
        elif rotation == 'R':
            self.rotate_face(self,0,1,L_rotation,vector(1,0,0))
        elif rotation == 'F':
            self.rotate_face(self,2,1,B_rotation,vector(0,0,1))
        elif rotation == 'B':
            self.rotate_face(self,2,-1,F_rotation,vector(0,0,1))


    def rotate_cube(self, rot_axis, rotation_matrix):
        cube_arr = []

        for y in range(26):
            rotated_piece = np.dot(self.cube_data[y][1], rotation_matrix)
            self.cube_data[y][1] = rotated_piece
            cube_arr.append(self.cube[y])
        for x in range(26):
            cube_arr[x].rotate(angle=radians(90), origin=vector(0, 0, 0),axis=rot_axis)

    def rotate_slice(self,layer,coord,rotation_matrix, rot_axis):
        face = []
        for x in range (8,26):
            if self.cube_data[x][1][layer] == coord:
                rotated_piece = np.dot(self.cube_data[x][1], rotation_matrix)
                self.cube_data[x][1] = rotated_piece
                del rotated_piece
                face.append(self.cube[x])
        for y in range(8):
            face[y].rotate(angle=radians(90), origin=vector(0, 0, 0), axis=rot_axis)

    def rotate_face(self,layer,pos_neg_coord,rotation_matrix,rot_axis):
        side = []
        for x in range(26):
            if self.cube_data[x][1][layer] == pos_neg_coord:
                rotated_piece = np.dot(self.cube_data[x][1], rotation_matrix)
                self.cube_data[x][1] = rotated_piece
                del rotated_piece
                side.append(self.cube[x])
        for y in range(8):
            side[y].rotate(angle=radians(90), origin=vector(0, 0, 0), axis=rot_axis)
        del side[:]
        print(self.cube_str)

    def keys(self):
        while True:
            k = keysdown()
            if 'u' in k:
                self.cube_str.U()
                self.rotations(self, 'u')
                sleep(0.5)
            elif 'r' in k:
                self.cube_str.R()
                self.rotations(self, 'r')
                sleep(0.5)
            elif 'f' in k:
                self.cube_str.F()
                self.rotations(self, 'f')
                sleep(0.5)
            elif 'd' in k:
                self.cube_str.D()
                self.rotations(self, 'd')
                sleep(0.5)
            elif 'l' in k:
                self.cube_str.L()
                self.rotations(self, 'l')
                sleep(0.5)
            elif 'b' in k:
                self.cube_str.B()
                self.rotations(self, 'b')
                sleep(0.5)
            elif 'U' in k:
                self.cube_str.Ui()
                self.rotations(self, 'U')
                sleep(0.5)
            elif 'R' in k:
                self.cube_str.Ri()
                self.rotations(self, 'R')
                sleep(0.5)
            elif 'F' in k:
                self.cube_str.Fi()
                self.rotations(self, 'F')
                sleep(0.5)
            elif 'D' in k:
                self.cube_str.Di()
                self.rotations(self, 'D')
                sleep(0.5)
            elif 'L' in k:
                self.cube_str.Li()
                self.rotations(self, 'L')
                sleep(0.5)
            elif 'B' in k:
                self.cube_str.Bi()
                self.rotations(self, 'B')
                sleep(0.5)
            elif 'z' in k:
                break

    def solve(self):
        cube_string =(str(self.cube_str)).strip()
        cube_to_solve = cube_string.replace(' ', '')
        cube_to_solve1 = cube_to_solve.replace('\n','')

        test = cube_to_solve1[:9]+cube_to_solve1[15:18]+cube_to_solve1[27:30]+cube_to_solve1[39:42]+cube_to_solve1[12:15]+cube_to_solve1[24:27]+cube_to_solve1[36:39]+cube_to_solve1[45:54]+cube_to_solve1[9:12]+cube_to_solve1[21:24]+cube_to_solve1[33:36]+cube_to_solve1[18:21]+cube_to_solve1[30:33]+cube_to_solve1[42:45]
        replacement = ['U','L','F','R','B','D']
        to_replace = ['y','b','r','g','o','w']
        print(test)
        for x in range(6):
            test = test.replace(to_replace[x],replacement[x])
        print(test)
        print(len(test))
        print(kociemba.solve(test))




    def reset(self):
        for x in range (20):
            self.cube[x].visible = False
        self.cube_data =[
            # edge pieces
            [[up_7, front_1, left_3], np.array([-1, 1, 1])],
            [[up_9, front_3, right_1], np.array([1, 1, 1])],
            [[up_1, left_1, back_3], np.array([-1, 1, -1])],
            [[up_3, back_1, right_3], np.array([1, 1, -1])],
            [[down_1, front_7, left_9], np.array([-1, -1, 1])],
            [[down_3, front_9, right_7], np.array([1, -1, 1])],
            [[down_7, back_9, left_7], np.array([-1, -1, -1])],
            [[down_9, back_7, right_9], np.array([1, -1, -1])],
            # corner pieces
            [[up_8, front_2], np.array([0, 1, 1])],
            [[up_6, right_2], np.array([1, 1, 0])],
            [[up_2, back_2], np.array([0, 1, -1])],
            [[up_4, left_2], np.array([-1, 1, 0])],
            [[front_4, left_6], np.array([-1, 0, 1])],
            [[front_6, right_4], np.array([1, 0, 1])],
            [[back_4, right_6], np.array([1, 0, -1])],
            [[back_6, left_4], np.array([-1, 0, -1])],
            [[down_2, front_8], np.array([0, -1, 1])],
            [[down_6, right_8], np.array([1, -1, 0])],
            [[down_8, back_8], np.array([0, -1, -1])],
            [[down_4, left_8], np.array([-1, -1, 0])],
            # centres
            [up_piece, np.array([0, 1.25, 0])],
            [down_piece, np.array([0, -1.25, 0])],
            [left_piece, np.array([-1.25, 0, 0])],
            [back_piece, np.array([0, 0, -1.25])],
            [right_piece, np.array([1.25, 0, 0])],
            [front_piece, np.array([0, 0, 1.25])]
        ]

        self.__init__(self)

if __name__ == "__main__":
    root = Interface()
    root.attributes('-alpha', 0.9)
    root.mainloop()