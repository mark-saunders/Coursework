from vpython import *
from tkinter import *
import numpy as np

W = pyramid(pos=vector(1, 1.5, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0), visible=False)
G = pyramid(pos=vector(0.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(1, 0, 0), color=color.green, visible=False)
O = pyramid(pos=vector(1, 1, 0.5), size=vector(0.5, 1, 1), axis=vector(0, 0, 1), color=color.orange, visible=False)
B = pyramid(pos=vector(1.5, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0), color=color.blue, visible=False)
R = pyramid(pos=vector(1, 1, 1.5), size=vector(0.5, 1, 1), axis=vector(0, 0, -1), color=color.red, visible=False)
Y = pyramid(pos=vector(1, 0.5, 1), size=vector(0.5, 1, 1), axis=vector(0, 1, 0), color=color.yellow, visible=False)

class Interface(Tk):

    def __init__(self):
        super().__init__()
        self.geometry('500x400')
        self.title('rubiks cube solver input screen')

        self.test = Button(text='test',command=self.append_to_data).grid(column=7,row=1)
        #self.start = Button(text='apply to cube', command=self.get_colour(0,0)).grid(column=7, row=2)

        self.options = ['White','Green','Orange','Blue','Red','Yellow']
        self.options_dict = {'White': W, 'Green': G, 'Orange': O, 'Blue': B, 'Red': R, 'Yellow': Y}
        self.option_var = [
            [StringVar(self),StringVar(self),StringVar(self)],
            [StringVar(self),StringVar(self),StringVar(self)],
            [StringVar(self),StringVar(self),StringVar(self)]
        ]

        self.create_options()

    def create_options(self):
        W_1 = OptionMenu(self, self.option_var[0][0], self.option_var[0][0].set(self.options[0]), *self.options).grid(row=3, column=4)
        W_2 = OptionMenu(self, self.option_var[0][1], self.option_var[0][1].set(self.options[0]), *self.options).grid(row=3, column=5)
        W_3 = OptionMenu(self, self.option_var[0][2], self.option_var[0][2].set(self.options[0]), *self.options).grid(row=3, column=6)
        W_4 = OptionMenu(self, self.option_var[1][0], self.option_var[1][0].set(self.options[0]), *self.options).grid(row=4, column=4)
        W_5 = OptionMenu(self, self.option_var[1][2], self.option_var[1][2].set(self.options[0]), *self.options).grid(row=4, column=6)
        W_6 = OptionMenu(self, self.option_var[2][0], self.option_var[2][0].set(self.options[0]), *self.options).grid(row=5, column=4)
        W_7 = OptionMenu(self, self.option_var[2][1], self.option_var[2][1].set(self.options[0]), *self.options).grid(row=5, column=5)
        W_8 = OptionMenu(self, self.option_var[2][2], self.option_var[2][2].set(self.options[0]), *self.options).grid(row=5, column=6)

    def test_(self):
        for x in range(3):
            for y in range(3):
                #for i in (-1,0,1):
                #sticker = compound([self.options_dict.get(self.option_var[x][y].get())],pos=vector(i,x,y))
                print(self.options_dict.get(self.option_var[x][y].get()))

    def append_to_data(self):
        
        for x in range(3):
            #cube.cube_data.insert([x][0][0],self.options_dict.get(self.option_var[x][0].get()))
            temp = self.options_dict.get(self.option_var[x][0].get())
            cube.cube_data[x][0][0] = temp
            print(cube.cube_data[x][0][0])
        cube.__init__(cube)

class cube:
    cube_data = [
        # edge pieces
        [[W,R,G], np.array([-1, 1, 1])],
        [[W,R,B], np.array([1, 1, 1])],
        [[W,G,O], np.array([-1, 1, -1])],
        [[W,O,B], np.array([1, 1, -1])],
        [[Y,R,G], np.array([-1, -1, 1])],
        [[Y,R,B], np.array([1, -1, 1])],
        [[Y,O,G], np.array([-1, -1, -1])],
        [[Y,O,B], np.array([1, -1, -1])],
        # corner pieces
        [[W,R], np.array([0, 1, 1])],
        [[W,B], np.array([1, 1, 0])],
        [[W,O], np.array([0, 1, -1])],
        [[W,G], np.array([-1, 1, 0])],
        [[R,G], np.array([-1, 0, 1])],
        [[R,B], np.array([1, 0, 1])],
        [[O,B], np.array([1, 0, -1])],
        [[O,G], np.array([-1, 0, -1])],
        [[Y,R], np.array([0, -1, 1])],
        [[Y,B], np.array([1, -1, 0])],
        [[Y,O], np.array([0, -1, -1])],
        [[Y,G], np.array([-1, -1, 0])],
        # centres
        [W, np.array([0, 1.25, 0])],
        [Y, np.array([0, -1.25, 0])],
        [G, np.array([-1.25, 0, 0])],
        [O, np.array([0, 0, -1.25])],
        [B, np.array([1.25, 0, 0])],
        [R, np.array([0, 0, 1.25])]
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

        self.WRG = compound([self.cube_data[0][0][0], self.cube_data[0][0][1], self.cube_data[0][0][2]],pos=vector(self.cube_data[0][1][0], self.cube_data[0][1][1], self.cube_data[0][1][2]))
        self.WRB = compound([self.cube_data[1][0][0], self.cube_data[1][0][1], self.cube_data[1][0][2]],pos=vector(self.cube_data[1][1][0], self.cube_data[1][1][1], self.cube_data[1][1][2]))
        self.WGO = compound([self.cube_data[2][0][0], self.cube_data[2][0][1], self.cube_data[2][0][2]],pos=vector(self.cube_data[2][1][0], self.cube_data[2][1][1], self.cube_data[2][1][2]))
        self.WOB = compound([self.cube_data[3][0][0], self.cube_data[3][0][1], self.cube_data[3][0][2]],pos=vector(self.cube_data[3][1][0], self.cube_data[3][1][1], self.cube_data[3][1][2]))
        self.YRG = compound([self.cube_data[4][0][0], self.cube_data[4][0][1], self.cube_data[4][0][2]],pos=vector(self.cube_data[4][1][0], self.cube_data[4][1][1], self.cube_data[4][1][2]))
        self.YRB = compound([self.cube_data[5][0][0], self.cube_data[5][0][1], self.cube_data[5][0][2]],pos=vector(self.cube_data[5][1][0], self.cube_data[5][1][1], self.cube_data[5][1][2]))
        self.YOG = compound([self.cube_data[6][0][0], self.cube_data[6][0][1], self.cube_data[6][0][2]],pos=vector(self.cube_data[6][1][0], self.cube_data[6][1][1], self.cube_data[6][1][2]))
        self.YOB = compound([self.cube_data[7][0][0], self.cube_data[7][0][1], self.cube_data[7][0][2]],pos=vector(self.cube_data[7][1][0], self.cube_data[7][1][1], self.cube_data[7][1][2]))
        # edge pieces#
        self.WR = compound([self.cube_data[8][0][0],  self.cube_data[8][0][1]], pos=vector(self.cube_data[8][1][0],  self.cube_data[8][1][1],  self.cube_data[8][1][2]))
        self.WB = compound([self.cube_data[9][0][0],  self.cube_data[9][0][1]], pos=vector(self.cube_data[9][1][0],  self.cube_data[9][1][1],  self.cube_data[9][1][2]))
        self.WO = compound([self.cube_data[10][0][0], self.cube_data[10][0][1]],pos=vector(self.cube_data[10][1][0], self.cube_data[10][1][1], self.cube_data[10][1][2]))
        self.WG = compound([self.cube_data[11][0][0], self.cube_data[11][0][1]],pos=vector(self.cube_data[11][1][0], self.cube_data[11][1][1], self.cube_data[11][1][2]))
        self.RG = compound([self.cube_data[12][0][0], self.cube_data[12][0][1]],pos=vector(self.cube_data[12][1][0], self.cube_data[12][1][1], self.cube_data[12][1][2]))
        self.RB = compound([self.cube_data[13][0][0], self.cube_data[13][0][1]],pos=vector(self.cube_data[13][1][0], self.cube_data[13][1][1], self.cube_data[13][1][2]))
        self.OB = compound([self.cube_data[14][0][0], self.cube_data[14][0][1]],pos=vector(self.cube_data[14][1][0], self.cube_data[14][1][1], self.cube_data[14][1][2]))
        self.OG = compound([self.cube_data[15][0][0], self.cube_data[15][0][1]],pos=vector(self.cube_data[15][1][0], self.cube_data[15][1][1], self.cube_data[15][1][2]))
        self.YR = compound([self.cube_data[16][0][0], self.cube_data[16][0][1]],pos=vector(self.cube_data[16][1][0], self.cube_data[16][1][1], self.cube_data[16][1][2]))
        self.YB = compound([self.cube_data[17][0][0], self.cube_data[17][0][1]],pos=vector(self.cube_data[17][1][0], self.cube_data[17][1][1], self.cube_data[17][1][2]))
        self.YO = compound([self.cube_data[18][0][0], self.cube_data[18][0][1]],pos=vector(self.cube_data[18][1][0], self.cube_data[18][1][1], self.cube_data[18][1][2]))
        self.YG = compound([self.cube_data[19][0][0], self.cube_data[19][0][1]],pos=vector(self.cube_data[19][1][0], self.cube_data[19][1][1], self.cube_data[19][1][2]))
        # centres#
        self.centres = compound([self.W],pos=vector(self.cube_data[20][1][0], self.cube_data[20][1][1],self.cube_data[20][1][2])), \
                       compound([self.Y], pos=vector(self.cube_data[21][1][0], self.cube_data[21][1][1],self.cube_data[21][1][2])), \
                       compound([self.G], pos=vector(self.cube_data[22][1][0], self.cube_data[22][1][1],self.cube_data[22][1][2])), \
                       compound([self.O], pos=vector(self.cube_data[23][1][0], self.cube_data[23][1][1],self.cube_data[23][1][2])), \
                       compound([self.B], pos=vector(self.cube_data[24][1][0], self.cube_data[24][1][1],self.cube_data[24][1][2])), \
                       compound([self.R], pos=vector(self.cube_data[25][1][0], self.cube_data[25][1][1],self.cube_data[25][1][2]))

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
    root.attributes('-alpha', 0.2)
    root.mainloop()


###################################
# with this model of changing the colours on the face of the cube this uses the pyramid variables W,R,B,O,G,Y
# the pyramids have a set orientation therefore when a different colour is selected the orientation of the pyramids are wrong