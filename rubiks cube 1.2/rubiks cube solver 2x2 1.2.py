from vpython import *
import numpy as np

cube_interface = canvas(title="Rubik's cube solver", height=1000, width=800)

scene.ambient = color.gray(0.1)


class cube_net:
    def __init__(self, up, down, left, right, front, back):
        self


class pieces:
    # [cubelet color, coordinates]

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

    # White, green, orange, blue, red, yellow corners
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

    def rotations(self, rotation):
        U_rotation = np.array([[cos(radians(90)), 0, sin(radians(90))],
                               [0, 1, 0],
                               [-sin(radians(90)), 0, cos(radians(90))]])
        R_rotation = np.array([[1, 0, 0],
                               [0, cos(radians(90)), -sin(radians(90))],
                               [0, sin(radians(90)), cos(radians(90))]])
        L_rotation = np.array([[1, 0, 0],
                               [0, cos(radians(-90)), -sin(radians(-90))],
                               [0, sin(radians(-90)), cos(radians(-90))]])
        F_rotation = np.array([[cos(radians(90)), -sin(radians(90)), 0],
                               [sin(radians(90)), cos(radians(90)), 0],
                               [0, 0, 1]])
        D_rotation = np.array([[cos(radians(-90)), 0, sin(radians(-90))],
                               [0, 1, 0],
                               [-sin(radians(-90)), 0, cos(radians(-90))]])
        B_rotation = np.array([[cos(radians(-90)), -sin(radians(-90)), 0],
                               [sin(radians(-90)), cos(radians(-90)), 0],
                               [0, 0, 1]])

        if rotation == 'u':
            pos_neg_coord = 1
            rotation_matrix = U_rotation
            layer = 1
            rot_axis = vector(0, -1, 0)
        elif rotation == 'd':
            pos_neg_coord = -1
            rotation_matrix = D_rotation
            layer = 1
            rot_axis = vector(0, 1, 0)
        elif rotation == 'l':
            pos_neg_coord = -1
            rotation_matrix = L_rotation
            layer = 0
            rot_axis = vector(1, 0, 0)
        elif rotation == 'r':
            pos_neg_coord = 1
            rotation_matrix = R_rotation
            layer = 0
            rot_axis = vector(-1, 0, 0)
        elif rotation == 'f':
            pos_neg_coord = 1
            rotation_matrix = F_rotation
            layer = 2
            rot_axis = vector(0, 0, -1)
        elif rotation == 'b':
            pos_neg_coord = -1
            rotation_matrix = B_rotation
            layer = 2
            rot_axis = vector(0, 0, 1)

        side = []
        for x in range(8):
            if round(self.cube_data[x][1][layer]) == pos_neg_coord:
                rotated_piece = np.dot(self.cube_data[x][1], rotation_matrix)
                self.cube_data[x][1] = rotated_piece
                del rotated_piece
                side.append(self.cube[x])
        for y in range(4):
            side[y].rotate(angle=radians(90), origin=vector(0, 0, 0), axis=rot_axis)
        del side[:]

    def keys(self):
        while True:
            k = keysdown()
            if 'u' in k:
                self.rotations(self, 'u')
                sleep(0.1)
            elif 'r' in k:
                self.rotations(self, 'r')
                sleep(0.1)
            elif 'f' in k:
                self.rotations(self, 'f')
                sleep(0.1)
            elif 'd' in k:
                self.rotations(self, 'd')
                sleep(0.1)
            elif 'l' in k:
                self.rotations(self, 'l')
                sleep(0.1)
            elif 'b' in k:
                self.rotations(self, 'b')
                sleep(0.1)


pieces.keys(pieces)
