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

r = 0
g = 0
b = 0

while True:
        if switch == 1:
                
                r=0
                g=0
                b=0

        for x in range(0, 16):
                r += 1
                g += 1
                b += 1
                for y in range(0, 16):
                        unicornhathd.set_pixel(x,y,r,g,b)

                unicornhathd.show()

        if switch == 0:
                switch=1
        else:
                switch=0

        unicornhathd.rotation(rot)
        rot += 90
        if rot == 360:
                rot=0
                


                
