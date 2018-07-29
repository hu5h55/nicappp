#!/usr/bin/env python

import unicornhathd
import time
import random

""" same as unicornhathd.off()  """
unicornhathd.clear()
unicornhathd.set_all(0, 0, 0)
unicornhathd.show()

unicornhathd.rotation(0)

""" switch decices black or white pixel  """ 
switch=0

""" rotation changes each x for """
width = 15
rot=90
counter = 0

unicornhathd.rotation(180)

sleep = 0.5

while True:
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        
        for x in range(0, 16):
            for y in range(0, 16):
                    if x <= y:
                            unicornhathd.set_pixel(y,x,r,g,b)
                            unicornhathd.set_pixel(x,y,r,g,b)
                            if x != 0:
                                    unicornhathd.set_pixel(y,x-1,0,0,0)
                                    unicornhathd.set_pixel(x-1,y,0,0,0)
                                    unicornhathd.set_pixel(x-1,y-1,0,0,0)
                            if x == width:
                                    unicornhathd.set_pixel(width,width ,r,g,b)
                                    unicornhathd.show()
                                    time.sleep(random.uniform(sleep,sleep))
            else:
                unicornhathd.set_pixel(width,width,0,0,0)
                                    
            
            unicornhathd.show()
            time.sleep(random.uniform(0.05,0.0005))


        unicornhathd.rotation(rot)
        rot += 90
        if rot == 360:
                rot=0
                       
                
        
                


                
