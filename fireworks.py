#!/usr/bin/env python

import unicornhathd
import time
import random

""" same as unicornhathd.off()  """
unicornhathd.clear()
unicornhathd.set_all(0, 0, 0)
unicornhathd.show()

unicornhathd.rotation(0)


unicornhathd.rotation(180)

sleep = 0.5
rot = 0


def matrixprint(x_start,width,y_start,height,r,g,b):
        for x in range(x_start,min(x_start+width,16)):
            for y in range(y_start,min(y_start+height,16)):
                    unicornhathd.set_pixel(x,y,r,g,b)
                                




while True:
        sleeptime = 0.075
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        x_start = random.randint(0,15)
        y_start = random.randint(9,15)
        x_len = 1
        y_len = 1

        for y in range(y_start):
                unicornhathd.set_pixel(x_start,y,255,255,255)
                unicornhathd.show()

        matrixprint(max(x_start,0),x_len,max(y_start,0),y_len,r,g,b)
        unicornhathd.show()
        time.sleep(sleeptime)

        
        for x in range(4):
                
                new_x_start = x_start -1
                new_y_start = y_start -1
                if new_x_start < 0:
                        new_x_len = x_len +2 -abs(new_x_start)
                else:
                        new_x_len = x_len +2
                if new_y_start < 0:
                        new_y_len = y_len +2 -abs(new_y_start)
                else:
                        new_y_len = y_len +2

        
                matrixprint(max(new_x_start,0),new_x_len,max(new_y_start,0),new_y_len,r,g,b)
                matrixprint(max(x_start,0),x_len,max(y_start,0),y_len,0,0,0)
        
                unicornhathd.show()
                time.sleep(sleeptime)
                sleeptime += 0.05

                x_start = new_x_start
                y_start = new_y_start
                x_len = new_x_len
                y_len = new_y_len

        unicornhathd.off()
                
        
        

                       
                
        
                


                
