from vpython import *
from rotations import *
import cube
import scrambled_cube


class display:
    scene = canvas(title='rubiks cube', width=500, height=500)

    def __init__(self):
        cube.cube()
        #test = button(text='solve scrambled cube', bind=rotations.up())
        self.test = button(text='solve scrambled cube', bind=self.testt())

        while True:
            key = scene.waitfor('click')
            if key.event == 'click':
                rate(30)


    def testt(self):
        print('yes')

    def scrambled_faces(self):
        R = color.red
        G = color.green
        B = color.blue
        O = color.orange
        W = color.white
        Y = color.yellow

display()





