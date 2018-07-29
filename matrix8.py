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
rot=90
counter = 0

unicornhathd.rotation(180)

sleep = 0.5



def matrixprint(x_start,width,y_start,height,r,g,b):
        for x in range(x_start,width):
            for y in range(y_start,height):
                    if x <= y:
                            unicornhathd.set_pixel(y,x,r,g,b)
                            unicornhathd.set_pixel(x,y,r,g,b)
                            if x != 0:
                                    unicornhathd.set_pixel(y,x-1,0,0,0)
                                    unicornhathd.set_pixel(x-1,y,0,0,0)
                                    unicornhathd.set_pixel(x-1,y-1,0,0,0)
                            if x == width-1:
                                    unicornhathd.set_pixel(width-1,height-1 ,r,g,b)
                                    unicornhathd.show()
                                
            else:
                unicornhathd.set_pixel(width-1,height-1,0,0,0)
                                    
            
            unicornhathd.show()
            time.sleep(random.uniform(0.1,0.1))

            
while True:
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        width = 16
        height = 16
        x_start = 9
        y_start = 9

        matrixprint(x_start,width,y_start,height,r,g,b)
        unicornhathd.rotation(rot)
        rot += 90
        if rot == 360:
                rot=0
                
        
        

                       
                
        
                


                
