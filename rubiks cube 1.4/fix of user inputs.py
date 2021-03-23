from vpython import *
from tkinter import *
import numpy as np
up_piece = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
left_piece = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), visible=False)
back_piece = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), visible=False)
right_piece = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), visible=False)
front_piece = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), visible=False)
down_piece = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), visible=False)

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

        self.test = Button(text='test', command=self.test_).grid(column=1, row=10)
        # self.start = Button(text='apply to cube', command=self.get_colour(0,0)).grid(column=7, row=2)

        self.options = ['White', 'Green', 'Orange', 'Blue', 'Red', 'Yellow']
        self.options_dict = {'White': up_piece, 'Green': left_piece, 'Orange': back_piece, 'Blue': right_piece, 'Red': front_piece, 'Yellow': down_piece}
        # self.option_var_up = [
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)]
        # ]
        #
        # self.option_var_left = [
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)]
        # ]
        #
        # self.option_var_front = [
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)]
        # ]
        #
        # self.option_var_right = [
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)]
        # ]
        #
        # self.option_var_back = [
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)]
        # ]
        #
        # self.option_var_down = [
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)],
        #     [StringVar(self), StringVar(self), StringVar(self)]
        # ]

        self.create_options()


        cube.__init__(cube)

    def create_options(self):
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

        U_1 = OptionMenu(self, self.option_var_up[0][0], self.option_var_up[0][0].set(self.options[0]), *self.options).grid(row=1, column=4)
        U_2 = OptionMenu(self, self.option_var_up[0][1], self.option_var_up[0][1].set(self.options[0]), *self.options).grid(row=1, column=5)
        U_3 = OptionMenu(self, self.option_var_up[0][2], self.option_var_up[0][2].set(self.options[0]), *self.options).grid(row=1, column=6)
        U_4 = OptionMenu(self, self.option_var_up[1][0], self.option_var_up[1][0].set(self.options[0]), *self.options).grid(row=2, column=4)
        U_6 = OptionMenu(self, self.option_var_up[1][2], self.option_var_up[1][2].set(self.options[0]), *self.options).grid(row=2, column=6)
        U_7 = OptionMenu(self, self.option_var_up[2][0], self.option_var_up[2][0].set(self.options[0]), *self.options).grid(row=3, column=4)
        U_8 = OptionMenu(self, self.option_var_up[2][1], self.option_var_up[2][1].set(self.options[0]), *self.options).grid(row=3, column=5)
        U_9 = OptionMenu(self, self.option_var_up[2][2], self.option_var_up[2][2].set(self.options[0]), *self.options).grid(row=3, column=6)

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

        D_1 = OptionMenu(self, self.option_var_down[0][0], self.option_var_down[0][0].set(self.options[5]), *self.options).grid(row=7, column=4)
        D_2 = OptionMenu(self, self.option_var_down[0][1], self.option_var_down[0][1].set(self.options[5]), *self.options).grid(row=7, column=5)
        D_3 = OptionMenu(self, self.option_var_down[0][2], self.option_var_down[0][2].set(self.options[5]), *self.options).grid(row=7, column=6)
        D_4 = OptionMenu(self, self.option_var_down[1][0], self.option_var_down[1][0].set(self.options[5]), *self.options).grid(row=8, column=4)
        D_6 = OptionMenu(self, self.option_var_down[1][2], self.option_var_down[1][2].set(self.options[5]), *self.options).grid(row=8, column=6)
        D_7 = OptionMenu(self, self.option_var_down[2][0], self.option_var_down[2][0].set(self.options[5]), *self.options).grid(row=9, column=4)
        D_8 = OptionMenu(self, self.option_var_down[2][1], self.option_var_down[2][1].set(self.options[5]), *self.options).grid(row=9, column=5)
        D_9 = OptionMenu(self, self.option_var_down[2][2], self.option_var_down[2][2].set(self.options[5]), *self.options).grid(row=9, column=6)

    def test_(self):
        # for x in range(4):
        #     cube.cube_data[x][0][0].color = color.red
        for x in range(3):
            for y in range(3):
                self.option_var_up[y][x] = up_layer[x+y].color
                print(self.option_var_up[y][x])
                print(up_layer[x+y].color)
        cube.__init__(cube)



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

    def __init__(self):
        # White, green, orange, blue, red, yellow corners
        self.W = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0),
                         visible=False)
        self.G = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), color=color.green,
                         visible=False)
        self.O = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), color=color.orange,
                         visible=False)
        self.B = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), color=color.blue,
                         visible=False)
        self.R = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), color=color.red,
                         visible=False)
        self.Y = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), color=color.yellow,
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
        self.centres = compound([self.W], pos=vector(self.cube_data[20][1][0], self.cube_data[20][1][1],
                                                     self.cube_data[20][1][2])), \
                       compound([self.Y], pos=vector(self.cube_data[21][1][0], self.cube_data[21][1][1],
                                                     self.cube_data[21][1][2])), \
                       compound([self.G], pos=vector(self.cube_data[22][1][0], self.cube_data[22][1][1],
                                                     self.cube_data[22][1][2])), \
                       compound([self.O], pos=vector(self.cube_data[23][1][0], self.cube_data[23][1][1],
                                                     self.cube_data[23][1][2])), \
                       compound([self.B], pos=vector(self.cube_data[24][1][0], self.cube_data[24][1][1],
                                                     self.cube_data[24][1][2])), \
                       compound([self.R], pos=vector(self.cube_data[25][1][0], self.cube_data[25][1][1],
                                                     self.cube_data[25][1][2]))

        self.cube = [
            self.WRG, self.WRB, self.WGO, self.WOB,
            self.YRG, self.YRB, self.YOG, self.YOB,
            self.WR, self.WB, self.WO, self.WG,
            self.RG, self.RB, self.OB, self.OG,
            self.YR, self.YB, self.YO, self.YG,
            self.centres
        ]


if __name__ == "__main__":
    root = Interface()
    root.attributes('-alpha', 0.6)
    root.mainloop()