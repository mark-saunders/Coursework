from vpython import *
#from interface import display


class cube:

    def __init__(self):
        self.scene = canvas(title='rubiks cube', width=800, height=800)
        self.corners = corners
        self.edges = edges
        self.centres = centres
        centres.__init__(centres)
        edges.__init__(edges)
        corners.__init__(corners)

    def up_rotation(self):
        rotations.up(rotations)


class centres:
    def __init__(self):
        centre = self.centre = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=color.black, scene=canvas)
        whitec =self.whitec = box(pos=vector(0, 1.01, 0), size=vector(1, 1, 1))
        yellowc = self.yellowc = box(pos=vector(0, -1.01, 0), size=vector(1, 1, 1), color=color.yellow)
        orangec = self.orangec = box(pos=vector(0, 0, 1.01), size=vector(1, 1, 1), color=color.orange)
        redc = self.redc = box(pos=vector(0, 0, -1.01), size=vector(1, 1, 1), color=color.red)
        bluec = self.bluec = box(pos=vector(-1.01, 0, 0), size=vector(1, 1, 1), color=color.blue)
        greenc = self.greenc = box(pos=vector(1.01, 0, 0), size=vector(1, 1, 1), color=color.green)


class edges:
    def __init__(self):
        WG = self.WG = pyramid(pos=vector(1.01, 1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                       pyramid(pos=vector(1.51, 1.01, 0), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                               color=color.green), \

        WO = self.WO = pyramid(pos=vector(0, 1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                       pyramid(pos=vector(0, 1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                               color=color.orange), \

        WB = self.WB = pyramid(pos=vector(-1.01, 1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                       pyramid(pos=vector(-1.51, 1.01, 0), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                               color=color.blue), \

        WR = self.WR = pyramid(pos=vector(0, 1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                       pyramid(pos=vector(0, 1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                               color=color.red), \

        YG = self.YG = pyramid(pos=vector(1.01, -1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                               color=color.yellow), \
                       pyramid(pos=vector(1.51, -1.01, 0), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                               color=color.green), \

        YO = self.YO = pyramid(pos=vector(0, -1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                               color=color.yellow), \
                       pyramid(pos=vector(0, -1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                               color=color.orange), \

        YB = self.YB = pyramid(pos=vector(-1.01, -1.51, 0), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                               color=color.yellow), \
                       pyramid(pos=vector(-1.51, -1.01, 0), size=vector(0.5, 1, 1), axis=vector(0, 0, 0),
                               color=color.blue), \

        YR = self.YR = pyramid(pos=vector(0, -1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                               color=color.yellow), \
                       pyramid(pos=vector(0, -1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                              color=color.red), \

        GO = self.GO = pyramid(pos=vector(1.01, 0, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                               color=color.orange), \
                       pyramid(pos=vector(1.51, 0, 1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                               color=color.green)

        GB = self.GB = pyramid(pos=vector(-1.01, 0, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                               color=color.orange), \
                       pyramid(pos=vector(-1.51, 0, 1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                               color=color.blue)

        RB = self.RB = pyramid(pos=vector(-1.01, 0, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                               color=color.red), \
                       pyramid(pos=vector(-1.51, 0, -1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                               color=color.blue)

        RG = self.RG = pyramid(pos=vector(1.01, 0, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                               color=color.red), \
                       pyramid(pos=vector(1.51, 0, -1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                               color=color.green)

class corners:
    def __init__(self):
        WOG = self.WOG = pyramid(pos=vector(1.01, 1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                         pyramid(pos=vector(1.51, 1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                                 color=color.green), \
                         pyramid(pos=vector(1.01, 1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                                 color=color.orange), \

        WRG = self.WRG = pyramid(pos=vector(1.01, 1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                         pyramid(pos=vector(1.51, 1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                                 color=color.green), \
                         pyramid(pos=vector(1.01, 1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                                 color=color.red)

        WOB = self.WOB = pyramid(pos=vector(-1.01, 1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                         pyramid(pos=vector(-1.01, 1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                                 color=color.orange), \
                         pyramid(pos=vector(-1.51, 1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                                 color=color.blue)

        WRB = self.WRB = pyramid(pos=vector(-1.01, 1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
                         pyramid(pos=vector(-1.01, 1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                                 color=color.red), \
                         pyramid(pos=vector(-1.51, 1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                                 color=color.blue)

        YOG = self.YOG = pyramid(pos=vector(1.01, -1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                                 color=color.yellow), \
                         pyramid(pos=vector(1.51, -1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                                 color=color.green), \
                         pyramid(pos=vector(1.01, -1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                                 color=color.orange)

        YRG = self.YRG = pyramid(pos=vector(1.01, -1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                                 color=color.yellow), \
                         pyramid(pos=vector(1.51, -1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
                                 color=color.green), \
                         pyramid(pos=vector(1.01, -1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                                 color=color.red)

        YOB = self.YOB = pyramid(pos=vector(-1.01, -1.51, 1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                                 color=color.yellow), \
                         pyramid(pos=vector(-1.01, -1.01, 1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
                                 color=color.orange), \
                         pyramid(pos=vector(-1.51, -1.01, 1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                                 color=color.blue)

        YRB = self.YRB = pyramid(pos=vector(-1.01, -1.51, -1.01), size=vector(0.5, 1, 1), axis=vector(0, 1, 0),
                                 color=color.yellow), \
                         pyramid(pos=vector(-1.01, -1.01, -1.51), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
                                 color=color.red), \
                         pyramid(pos=vector(-1.51, -1.01, -1.01), size=vector(0.5, 1, 1), axis=vector(1, 0, 0),
                                 color=color.blue)

class rotations:


    def __init__(self):
        up = self.up()
        up_prime = self.up_prime()
        down = self.down()
        down_prime = self.down_prime()
        right = self.right()
        right_prime = self.right_prime()
        left = self.left()
        left_prime= self.left_prime()
        front = self.front()
        front_prime =  self.front_prime()
        back = self.back()
        back_prime = self.back_prime()

    def up(self):
        centres.whitec.rotate(angle=pi)

    def up_prime(self):
        pass

    def down(self):
        pass

    def down_prime(self):
        pass

    def right(self):
        pass

    def right_prime(self):
        pass

    def left(self):
        pass

    def left_prime(self):
        pass

    def front(self):
        pass

    def front_prime(self):
        pass

    def back(self):
        pass

    def back_prime(self):
        pass

cube()

WOG = pyramid(pos=vector(1, 1, 1), size=vector(0.5, 1, 1), axis=vector(0, -1, 0)), \
      pyramid(pos=vector(1, 1, 1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
              color=color.green), \
      pyramid(pos=vector(1, 1, 1), size=vector(0.5, 1, 1), axis=vector(0, 0, -1),
              color=color.orange),

WRG = pyramid(pos=vector(1, 1, -1), size=vector(0.5, 1, 1),
              axis=vector(0, -1, 0)), \
      pyramid(pos=vector(1, 1, -1), size=vector(0.5, 1, 1), axis=vector(-1, 0, 0),
              color=color.green), \
      pyramid(pos=vector(1, 1, -1), size=vector(0.5, 1, 1), axis=vector(0, 0, 1),
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
