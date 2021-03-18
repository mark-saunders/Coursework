from vpython import *
from vpython import rotate


class interface:
    scene = canvas(title='rubiks cube', height=1000)

class cube:
    ########################################################################################
    #                                    centres                                           #
    ########################################################################################
    whitec = box(pos=vector(0, 1.01, 0), size=vector(1, 1, 1))
    yellowc = box(pos=vector(0, -1.01, 0), size=vector(1, 1, 1), color=color.yellow)
    orangec = box(pos=vector(0, 0, 1.01), size=vector(1, 1, 1), color=color.orange)
    redc = box(pos=vector(0, 0, -1.01), size=vector(1, 1, 1), color=color.red)
    bluec = box(pos=vector(-1.01, 0, 0), size=vector(1, 1, 1), color=color.blue)
    greenc = box(pos=vector(1.01, 0, 0), size=vector(1, 1, 1), color=color.green)

    ########################################################################################
    #                                      edges                                           #
    ########################################################################################
    WG = pyramid(pos=vector(1.01, 1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
         pyramid(pos=vector(1.51, 1.01, 0), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                 color=color.green),

    WO = pyramid(pos=vector(0, 1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
         pyramid(pos=vector(0, 1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                 color=color.orange)

    WB = pyramid(pos=vector(-1.01, 1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
         pyramid(pos=vector(-1.51, 1.01, 0), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                 color=color.blue)

    WR = pyramid(pos=vector(0, 1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
         pyramid(pos=vector(0, 1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                 color=color.red),

    YG = pyramid(pos=vector(1.01, -1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                 color=color.yellow), \
         pyramid(pos=vector(1.51, -1.01, 0), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                 color=color.green),

    YO = pyramid(pos=vector(0, -1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                 color=color.yellow), \
         pyramid(pos=vector(0, -1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                 color=color.orange),

    YB = pyramid(pos=vector(-1.01, -1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                 color=color.yellow),\
         pyramid(pos=vector(-1.51, -1.01, 0), size=vector(0.5, 1, 1), axis=vector(0, 0, 0),
                 color=color.blue),

    YR = pyramid(pos=vector(0, -1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                 color=color.yellow), \
         pyramid(pos=vector(0, -1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                 color=color.red),

    GO = pyramid(pos=vector(1.01, 0, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                 color=color.orange), \
         pyramid(pos=vector(1.51, 0, 1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                 color=color.green)

    GB = pyramid(pos=vector(-1.01, 0, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                 color=color.orange), \
         pyramid(pos=vector(-1.51, 0, 1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                 color=color.blue)

    RB = pyramid(pos=vector(-1.01, 0, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                 color=color.red), \
         pyramid(pos=vector(-1.51, 0, -1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                 color=color.blue)

    RG = pyramid(pos=vector(1.01, 0, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                 color=color.red), \
         pyramid(pos=vector(1.51, 0, -1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                 color=color.green)

    ########################################################################################
    #                                      corners                                         #
    ########################################################################################
    WOG = pyramid(pos=vector(1.01, 1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
          pyramid(pos=vector(1.51, 1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                  color=color.green), \
          pyramid(pos=vector(1.01, 1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                  color=color.orange),

    WRG = pyramid(pos=vector(1.01, 1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
          pyramid(pos=vector(1.51, 1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                  color=color.green), \
          pyramid(pos=vector(1.01, 1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                  color=color.red)

    WOB = pyramid(pos=vector(-1.01, 1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
          pyramid(pos=vector(-1.01, 1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                  color=color.orange), \
          pyramid(pos=vector(-1.51, 1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                  color=color.blue)

    WRB = pyramid(pos=vector(-1.01, 1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
          pyramid(pos=vector(-1.01, 1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                  color=color.red), \
          pyramid(pos=vector(-1.51, 1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                  color=color.blue)

    YOG = pyramid(pos=vector(1.01, -1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                  color=color.yellow), \
          pyramid(pos=vector(1.51, -1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                  color=color.green), \
          pyramid(pos=vector(1.01, -1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                  color=color.orange)

    YRG = pyramid(pos=vector(1.01, -1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                  color=color.yellow), \
          pyramid(pos=vector(1.51, -1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                  color=color.green), \
          pyramid(pos=vector(1.01, -1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                  color=color.red)

    YOB = pyramid(pos=vector(-1.01, -1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                  color=color.yellow), \
          pyramid(pos=vector(-1.01, -1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                  color=color.orange), \
          pyramid(pos=vector(-1.51, -1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                  color=color.blue)

    YRB = pyramid(pos=vector(-1.01, -1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                  color=color.yellow), \
          pyramid(pos=vector(-1.01, -1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                  color=color.red), \
          pyramid(pos=vector(-1.51, -1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                  color=color.blue)


    def __init__(self):
        UP_B = button(bind=cube.__init__(), text='up')
        scene.append_to_caption('\n\n')

    def up(self):
        pass
        cube.WG.rotate(axis=vector(1,0,0), angle=0.5*2*pi/20)



