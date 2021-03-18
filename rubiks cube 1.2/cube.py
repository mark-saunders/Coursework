from vpython import *

cube_interface = canvas(title='Rubiks cube solver', height=1000, width=800)
Face = shapes.rectangle(width=10, height=10)

####################
#   centres        #
####################
cube_centre = box(pos=vector(0, 0, 0), size=vector(10, 10, 10))

red_centre = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(0, 0, 15.5), color=color.red)

green_centre = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, 0, 0),
                         color=color.green, axis=vector(0, 0, 1))
Blue_centre = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, 0, 0), color=color.blue,
                        axis=vector(0, 0, 1))
orange_centre = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(0, 0, -15.5),
                          color=color.orange)
white_centre = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(0, 15.5, 0))

yellow_centre = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(0, -15.5, 0),
                          color=color.yellow)

####################
#    edges         #
####################

WR_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(0, 15.5, 10.5))
WR_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(0, 10.5, 15.5), color=color.red)

WG_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(-10.5, 15.5, 0))
WG_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, 10.5, 0),
                 color=color.green, axis=vector(0, 0, 1))

WB_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(10.5, 15.5, 0))
WB_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, 10.5, 0), color=color.blue,
                 axis=vector(0, 0, 1))

WO_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(0, 15.5, -10.5))
WO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(0, 10.5, -15.5),
                 color=color.orange)

RG_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-10.5, 0, 15.5), color=color.red)
RG_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, 0, 10.5),
                 color=color.green, axis=vector(0, 0, 1))

GO_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, 0, -10.5),
                 color=color.green, axis=vector(0, 0, 1))
GO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-10.5, 0, -15.5),
                 color=color.orange)

BO_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, 0, -10.5), color=color.blue,
                 axis=vector(0, 0, 1))
BO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(10.5, 0, -15.5),
                 color=color.orange)

RB_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(10.5, 0, 15.5), color=color.red)
RB_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, 0, 10.5), color=color.blue,
                 axis=vector(0, 0, 1))

YR_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(0, -15.5, 10.5),
                 color=color.yellow)
YR_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(0, -10.5, 15.5), color=color.red)

YG_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(-10.5, -15.5, 0),
                 color=color.yellow)
YG_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, -10.5, 0),
                 color=color.green, axis=vector(0, 0, 1))

YB_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(10.5, -15.5, 0),
                 color=color.yellow)
YB_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, -10.5, 0), color=color.blue,
                 axis=vector(0, 0, 1))

YO_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(0, -15.5, -10.5),
                 color=color.yellow)
YO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(0, -10.5, -15.5),
                 color=color.orange)
#####################
#   corners         #
#####################
WRG_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(-10.5, 15.5, 10.5))
WRG_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-10.5, 10.5, 15.5),
                  color=color.red)
WRG_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, 10.5, 10.5),
                  color=color.green, axis=vector(0, 0, 1))
WGO_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(-10.5, 15.5, -10.5))

WGO_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, 10.5, -10.5),
                  color=color.green, axis=vector(0, 0, 1))
WGO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-10.5, 10.5, -15.5),
                  color=color.orange)
WBO_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(10.5, 15.5, -10.5))
WBO_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, 10.5, -10.5),
                  color=color.blue, axis=vector(0, 0, 1))
WBO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(10.5, 10.5, -15.5),
                  color=color.orange)
WRB_W = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(10.5, 15.5, 10.5))
WRB_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(10.5, 10.5, 15.5),
                  color=color.red)
WRB_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, 10.5, 10.5),
                  color=color.blue, axis=vector(0, 0, 1))
YRG_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(-10.5, -15.5, 10.5),
                  color=color.yellow)
YRG_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-10.5, -10.5, 15.5),
                  color=color.red)
YRG_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, -10.5, 10.5),
                  color=color.green, axis=vector(0, 0, 1))
YGO_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(-10.5, -15.5, -10.5),
                  color=color.yellow)
YGO_G = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-15.5, -10.5, -10.5),
                  color=color.green, axis=vector(0, 0, 1))
YGO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(-10.5, -10.5, -15.5),
                  color=color.orange)
YBO_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(10.5, -15.5, -10.5),
                  color=color.yellow)
YBO_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, -10.5, -10.5),
                  color=color.blue, axis=vector(0, 0, 1))
YBO_O = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(10.5, -10.5, -15.5),
                  color=color.orange)
YRB_Y = extrusion(path=[vector(0, 0, 0), vector(0, 1, 0)], shape=Face, pos=vector(10.5, -15.5, 10.5),
                  color=color.yellow)
YRB_R = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(10.5, -10.5, 15.5),
                  color=color.red)
YRB_B = extrusion(path=[vector(0, 0, 0), vector(0, 0, 1)], shape=Face, pos=vector(15.5, -10.5, 10.5),
                  color=color.blue, axis=vector(0, 0, 1))

# [left/Right,top,front/back] with red facing forward and white up
up_layer = [[[WGO_G, WGO_W, WGO_O], [WO_W, WO_O], [WBO_B, WBO_W, WBO_O]],
            [[WG_W, WG_G], [white_centre], [WB_B, WB_W]],
            [[WRG_G, WRG_W, WRG_R], [WR_W, WR_R], [WRB_B, WRB_W, WRB_R]]]

front_layer = [[[WRG_G, WRG_W, WRG_R], [WR_W, WR_R], [WRB_B, WRB_W, WRB_R]],
               [[RG_G, RG_R], [red_centre], [RB_R, RB_B]],
               [[YRG_G, YRG_R, YRG_Y], [YR_R, YR_Y], [YRB_B, YRB_R, YRB_Y]]]

cube_layout =
[[[YGO_O, YO_O, YBO_O]


def up():  # up rotation
    for i in range(0, 30):
        white_centre.rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))
        for x in range(0, 3):  # corner rotation
            up_layer[0][0][x].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))
            up_layer[0][2][x].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))
            up_layer[2][0][x].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))
            up_layer[2][2][x].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))

        for y in range(0, 2):
            up_layer[0][1][y].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))
            up_layer[1][0][y].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))
            up_layer[1][2][y].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))
            up_layer[2][1][y].rotate(axis=vector(0, 1, 0), angle=radians(3), origin=vector(0, 0, 0))

        sleep(0.000001)
    # corner rotations
    up_layer[0][0], up_layer[0][1], up_layer[0][2], \
    up_layer[1][0], up_layer[1][1], up_layer[1][2], \
    up_layer[2][0], up_layer[2][1], up_layer[2][2] \
        = \
        up_layer[0][2], up_layer[1][2], up_layer[2][2], \
        up_layer[0][1], up_layer[1][1], up_layer[2][1], \
        up_layer[0][0], up_layer[1][0], up_layer[2][0]

    #up_layer[0][0], up_layer[1][0], up_layer[2][0] = front_layer[0][0], front_layer[0][1], front_layer[0][2]


def front():
    for i in range(0, 30):
        red_centre.rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
        for x in range(0, 3):  # corner rotation
            front_layer[0][0][x].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
            front_layer[0][2][x].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
            front_layer[2][0][x].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
            front_layer[2][2][x].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))

        for y in range(0, 2):
            front_layer[0][1][y].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
            front_layer[1][0][y].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
            front_layer[1][2][y].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
            front_layer[2][1][y].rotate(axis=vector(0, 0, -1), angle=radians(3), origin=vector(0, 0, 0))
        sleep(0.000001)

    front_layer[0][0], front_layer[0][1], front_layer[0][2], \
    front_layer[1][0], front_layer[1][1], front_layer[1][2], \
    front_layer[2][0], front_layer[2][1], front_layer[2][2] \
        = \
        front_layer[2][0], front_layer[1][0], front_layer[0][0], \
        front_layer[2][1], front_layer[1][1], front_layer[0][1], \
        front_layer[2][2], front_layer[1][2], front_layer[0][2]

    #front_layer[2][2], front_layer[2][1], front_layer[2][0] = up_layer[2][0], up_layer[2][1], up_layer[2][2]

while True:
    k = keysdown()
    if 'u' in k:
        up()
    elif 'f' in k:
        front()


