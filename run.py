#!/usr/bin/env python

import unicornhathd
import time
import random

unicornhathd.clear()

unicornhathd.set_all(0, 0, 0)

unicornhathd.show()

unicornhathd.rotation(0)

""" switch decices black or white pixel  """ 
switch=0

""" rotation changes each x for """
rot=90

negpixmap = [[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def blackify():
        for y in range (0,16):
                for x in range (0,16):
                        if negpixmap[x][y] != 0:
                                unicornhathd.set_pixel(x,y,255-negpixmap[x][y]*255,255-negpixmap[x][y]*255,255-negpixmap[x][y]*255)

while True:
        if switch == 0:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
        else:
                r=0
                g=0
                b=0

        for x in range(0, 16):
            for y in range(0, 16):
                unicornhathd.set_pixel(x,y,r,g,b)
                time.sleep(random.uniform(0.001,0.0000001))
                unicornhathd.show()

        if switch == 0:
                switch=1
        else:
                switch=0

        unicornhathd.rotation(rot)
        rot += 90
        if rot == 360:
                rot=0
                


                
