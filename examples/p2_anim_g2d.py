#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

def update():
    global x
    canvas_fill(canvas, (255, 255, 255))  # Draw background        
    image_blit(canvas, image, (x, 50))    # Draw foreground
    x = (x + dx) % 320                     # Update ball's position

def keydown(e):
    global dx
    if e.code == "Space":
        dx = -dx

canvas = canvas_init((320, 240))
image = image_load("ball.png")
x = 50
dx = 5

set_interval(update, 1000 // 30)    # Call update 30 times/second
doc.onkeydown = keydown
