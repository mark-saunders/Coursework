from vpython import *
import numpy as np

cube_interface = canvas(title='Rubiks cube solver', height=1000, width=800)
Face = shapes.rectangle(width=1, height=1)


class pieces:
    # [cubelet color, coordinates, orientation]

    cube_data = [
        ['WRG', np.array([-1, 1, 1])],
        ['WRB', np.array([1, 1, 1])],
        ['WGO', np.array([-1, 1, -1])],
        ['WOB', np.array([1, 1, -1])],
        ['YRG', np.array([-1, -1, 1])],
        ['YRB', np.array([1, -1, 1])],
        ['YOG', np.array([-1, -1, -1])],
        ['YOB', np.array([1, -1, -1])]
    ]

    # White, orange, green corner
    W = pyramid(pos=vector(1, 2, 1), size=vector(1, 2, 2), axis=vector(0, -1, 0), visible=False)
    G = pyramid(pos=vector(0, 1, 1), size=vector(1, 2, 2), axis=vector(1, 0, 0), color=color.green, visible=False)
    O = pyramid(pos=vector(1, 1, 0), size=vector(1, 2, 2), axis=vector(0, 0, 1), color=color.orange, visible=False)
    B = pyramid(pos=vector(2, 1, 1), size=vector(1, 2, 2), axis=vector(-1, 0, 0), color=color.blue, visible=False)
    R = pyramid(pos=vector(1, 1, 2), size=vector(1, 2, 2), axis=vector(0, 0, -1), color=color.red, visible=False)
    Y = pyramid(pos=vector(1, 0, 1), size=vector(1, 2, 2), axis=vector(0, 1, 0), color=color.yellow, visible=False)

    WRG = compound([W, R, G], pos=vector(cube_data[0][1][0], cube_data[0][1][1], cube_data[0][1][2]))
    WRB = compound([W, R, B], pos=vector(cube_data[1][1][0], cube_data[1][1][1], cube_data[1][1][2]))
    WGO = compound([W, G, O], pos=vector(cube_data[2][1][0], cube_data[2][1][1], cube_data[2][1][2]))
    WOB = compound([W, O, B], pos=vector(cube_data[3][1][0], cube_data[3][1][1], cube_data[3][1][2]))
    YRG = compound([Y, R, G], pos=vector(cube_data[4][1][0], cube_data[4][1][1], cube_data[4][1][2]))
    YRB = compound([Y, R, B], pos=vector(cube_data[5][1][0], cube_data[5][1][1], cube_data[5][1][2]))
    YOG = compound([Y, O, G], pos=vector(cube_data[6][1][0], cube_data[6][1][1], cube_data[6][1][2]))
    YOB = compound([Y, O, B], pos=vector(cube_data[7][1][0], cube_data[7][1][1], cube_data[7][1][2]))

    cube = [WRG, WRB, WGO, WOB, YRG, YRB, YOG, YOB]

    def up_rotation(self):
        U_rotation = np.array([[cos(radians(90)), 0, sin(radians(90))],
                               [0, 1, 0],
                               [-sin(radians(90)), 0, cos(radians(90))]])

        side = []
        for x in range(0, 8):
            if self.cube_data[x][1][1] == 1:
                self.cube_data[x][1] = self.cube_data[x][1].dot(U_rotation)
                side.append(self.cube[x])
        for y in range(0, 4):
            side[y].rotate(angle=radians(90), origin=vector(0, 0, 0), axis=vector(0, -1, 0))
            sleep(0.0001)
        del side[:]
        print(side)


    def right_rotation(self):
        R_rotation = np.array([[1, 0, 0],
                               [0, cos(radians(90)), -sin(radians(90))],
                               [0, sin(radians(90)), cos(radians(90))]])
        side_r = []
        for y in range(0, 8):
            print(self.cube_data[y])
            if self.cube_data[y][1][0] == 1:
                self.cube_data[y][1] = self.cube_data[y][1].dot(R_rotation)
                side_r.append(self.cube[y])
        for i in range(8):
            print(self.cube_data[i])
        for x in range(4):
            side_r[x].rotate(angle=radians(90), origin=vector(0, 0, 0), axis=vector(1, 0, 0))
            sleep(0.0001)
        del side_r[:]


    def rotations(self):
        U_rotation = np.array([[cos(radians(90)), 0, sin(radians(90))],
                               [0, 1, 0],
                               [-sin(radians(90)), 0, cos(radians(90))]])

        R_rotation = np.array([[1, 0, 0],
                               [0, cos(radians(90)), -sin(radians(90))],
                               [0, sin(radians(90)), cos(radians(90))]])

    def keys(self):
        while True:
            k = keysdown()
            if 'u' in k:
                self.up_rotation(self)
            elif 'r' in k:
                self.right_rotation(self)



pieces.__init__(pieces)
pieces.keys(pieces)
