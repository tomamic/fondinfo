#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

def sierpinski(x0, y0, w0, h0, level, canvas):
    w1 = w0 // 3
    h1 = h0 // 3
    if level == 0 or w1 == 0 or h1 == 0:
        return
    for y in range(3):
        for x in range(3):
            x1 = x0 + x * w1
            y1 = y0 + y * h1
            if x == 1 and y == 1:
                draw_rect(canvas, (255, 255, 255), (x1, y1, w1, h1))
            else:
                sierpinski(x1, y1, w1, h1, level - 1, canvas)

level = int(input('level? '))  ## -1 = infinite
side = 600

canvas = canvas_init((side, side))
canvas_fill(canvas, (0, 0, 0))
sierpinski(0, 0, side, side, level, canvas)
