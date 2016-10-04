#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

canvas = canvas_init((300, 300))

for i in range(5):
    x = i * 40
    y = i * 40
    red = i * 60
    draw_rect(canvas, (red, 0, 0), (x, y, 140, 140))
