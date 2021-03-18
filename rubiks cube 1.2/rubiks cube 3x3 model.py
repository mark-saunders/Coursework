from vpython import *
import numpy as np

cube_interface = canvas(title="Rubik's cube solver", height=500, width=500)

scene.ambient = color.gray(0.1)

solved_state = [
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
    ['YG', np.array([-1, -1, 0])]
]


class pieces:
    def __init__(self):
        # [cubelet color, coordinates]

        self.cube_data = [
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

        self.WRG = compound([self.W, self.R, self.G],
                            pos=vector(self.cube_data[0][1][0], self.cube_data[0][1][1], self.cube_data[0][1][2]))
        self.WRB = compound([self.W, self.R, self.B],
                            pos=vector(self.cube_data[1][1][0], self.cube_data[1][1][1], self.cube_data[1][1][2]))
        self.WGO = compound([self.W, self.G, self.O],
                            pos=vector(self.cube_data[2][1][0], self.cube_data[2][1][1], self.cube_data[2][1][2]))
        self.WOB = compound([self.W, self.O, self.B],
                            pos=vector(self.cube_data[3][1][0], self.cube_data[3][1][1], self.cube_data[3][1][2]))
        self.YRG = compound([self.Y, self.R, self.G],
                            pos=vector(self.cube_data[4][1][0], self.cube_data[4][1][1], self.cube_data[4][1][2]))
        self.YRB = compound([self.Y, self.R, self.B],
                            pos=vector(self.cube_data[5][1][0], self.cube_data[5][1][1], self.cube_data[5][1][2]))
        self.YOG = compound([self.Y, self.O, self.G],
                            pos=vector(self.cube_data[6][1][0], self.cube_data[6][1][1], self.cube_data[6][1][2]))
        self.YOB = compound([self.Y, self.O, self.B],
                            pos=vector(self.cube_data[7][1][0], self.cube_data[7][1][1], self.cube_data[7][1][2]))
        # edge pieces#
        self.WR = compound([self.W, self.R],
                           pos=vector(self.cube_data[8][1][0], self.cube_data[8][1][1], self.cube_data[8][1][2]))
        self.WB = compound([self.W, self.B],
                           pos=vector(self.cube_data[9][1][0], self.cube_data[9][1][1], self.cube_data[9][1][2]))
        self.WO = compound([self.W, self.O],
                           pos=vector(self.cube_data[10][1][0], self.cube_data[10][1][1], self.cube_data[10][1][2]))
        self.WG = compound([self.W, self.G],
                           pos=vector(self.cube_data[11][1][0], self.cube_data[11][1][1], self.cube_data[11][1][2]))
        self.RG = compound([self.R, self.G],
                           pos=vector(self.cube_data[12][1][0], self.cube_data[12][1][1], self.cube_data[12][1][2]))
        self.RB = compound([self.R, self.B],
                           pos=vector(self.cube_data[13][1][0], self.cube_data[13][1][1], self.cube_data[13][1][2]))
        self.OB = compound([self.O, self.B],
                           pos=vector(self.cube_data[14][1][0], self.cube_data[14][1][1], self.cube_data[14][1][2]))
        self.OG = compound([self.O, self.G],
                           pos=vector(self.cube_data[15][1][0], self.cube_data[15][1][1], self.cube_data[15][1][2]))
        self.YR = compound([self.Y, self.R],
                           pos=vector(self.cube_data[16][1][0], self.cube_data[16][1][1], self.cube_data[16][1][2]))
        self.YB = compound([self.Y, self.B],
                           pos=vector(self.cube_data[17][1][0], self.cube_data[17][1][1], self.cube_data[17][1][2]))
        self.YO = compound([self.Y, self.O],
                           pos=vector(self.cube_data[18][1][0], self.cube_data[18][1][1], self.cube_data[18][1][2]))
        self.YG = compound([self.Y, self.G],
                           pos=vector(self.cube_data[19][1][0], self.cube_data[19][1][1], self.cube_data[19][1][2]))
        # centres#
        self.centres = compound([self.W], pos=vector(self.cube_data[20][1][0], self.cube_data[20][1][1], self.cube_data[20][1][2])), \
                       compound([self.Y], pos=vector(self.cube_data[21][1][0], self.cube_data[21][1][1], self.cube_data[21][1][2])), \
                       compound([self.G], pos=vector(self.cube_data[22][1][0], self.cube_data[22][1][1], self.cube_data[22][1][2])), \
                       compound([self.O], pos=vector(self.cube_data[23][1][0], self.cube_data[23][1][1], self.cube_data[23][1][2])), \
                       compound([self.B], pos=vector(self.cube_data[24][1][0], self.cube_data[24][1][1], self.cube_data[24][1][2])), \
                       compound([self.R], pos=vector(self.cube_data[25][1][0], self.cube_data[25][1][1], self.cube_data[25][1][2]))

        self.cube = [
            self.WRG, self.WRB, self.WGO, self.WOB,
            self.YRG, self.YRB, self.YOG, self.YOB,
            self.WR, self.WB, self.WO, self.WG,
            self.RG, self.RB, self.OB, self.OG,
            self.YR, self.YB, self.YO, self.YG,
            self.centres
        ]

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
        elif rotation == 'U':
            pos_neg_coord = 1
            rotation_matrix = D_rotation
            layer = 1
            rot_axis = vector(0, 1, 0)
        elif rotation == 'D':
            pos_neg_coord = -1
            rotation_matrix = U_rotation
            layer = 1
            rot_axis = vector(0, -1, 0)
        elif rotation == 'L':
            pos_neg_coord = -1
            rotation_matrix = R_rotation
            layer = 0
            rot_axis = vector(-1, 0, 0)
        elif rotation == 'R':
            pos_neg_coord = 1
            rotation_matrix = L_rotation
            layer = 0
            rot_axis = vector(1, 0, 0)
        elif rotation == 'F':
            pos_neg_coord = 1
            rotation_matrix = B_rotation
            layer = 2
            rot_axis = vector(0, 0, 1)
        elif rotation == 'B':
            pos_neg_coord = -1
            rotation_matrix = F_rotation
            layer = 2
            rot_axis = vector(0, 0, -1)
        elif rotation == 'k':
            for x in range(20):
                self.cube[x].rotate(angle=radians(90), origin=(0,0,0), axis=1)

        side = []
        for x in range(20):
            if self.cube_data[x][1][layer] == pos_neg_coord:
                rotated_piece = np.dot(self.cube_data[x][1], rotation_matrix)
                self.cube_data[x][1] = rotated_piece
                del rotated_piece
                side.append(self.cube[x])
                print(x)
        for y in range(8):
            side[y].rotate(angle=radians(90), origin=vector(0, 0, 0), axis=rot_axis)
            print(y)
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
            elif 'U' in k:
                self.rotations(self, 'U')
                sleep(0.1)
            elif 'R' in k:
                self.rotations(self, 'R')
                sleep(0.1)
            elif 'F' in k:
                self.rotations(self, 'F')
                sleep(0.1)
            elif 'D' in k:
                self.rotations(self, 'D')
                sleep(0.1)
            elif 'L' in k:
                self.rotations(self, 'L')
                sleep(0.1)
            elif 'B' in k:
                self.rotations(self, 'B')
                sleep(0.1)
            elif 'k' in k:
                self.rotations(self, 'k')
                sleep(0.1)

            elif 'z' in k:

                for x in range(20):
                    self.cube[x].visible = False
                self.cube_data = solved_state
                pieces.__init__(self)


pieces.__init__(pieces)
pieces.keys(pieces)
