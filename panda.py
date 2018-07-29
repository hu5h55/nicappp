#!/usr/bin/env python

import signal
import time
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

import unicornhathd


print("""Unicorn HAT HD: Show a PNG image!

This basic example shows use of the Python Pillow library:

The tiny 16x16 bosses in lofi.png are from Oddball:
http://forums.tigsource.com/index.php?topic=8834.0

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0
Unported License.

Press Ctrl+C to exit!

""")

unicornhathd.rotation(90)
unicornhathd.brightness(0.5)
unicornhathd.set_all(10,10,10)

width, height = unicornhathd.get_shape()

img = Image.open('pandaheart16.png')




negpixmap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1],
             [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1]]


def blackify():
    for y in range (0,16):
        for x in range (0,16):
            if negpixmap[x][y] != 0:
                unicornhathd.set_pixel(x,y,255-negpixmap[x][y]*255,255-negpixmap[x][y]*255,255-negpixmap[x][y]*255)

try:
    while True:
        for o_x in range(int(img.size[0]/width)):
            for o_y in range(int(img.size[1]/height)):

                valid = False
                for x in range(width):
                    for y in range(height):
                        pixel = img.getpixel(((o_x*width)+y,(o_y*height)+x))
                        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                        if r or g or b:
                            valid = True
                        unicornhathd.set_pixel(x, y, r, g, b)
                        blackify()
                if valid:
                    unicornhathd.show()


except KeyboardInterrupt:
    unicornhathd.off()

