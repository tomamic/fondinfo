#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

canvas = canvas_init((400, 400))

draw_rect(canvas, (165, 0, 255), (100, 100, 250, 250))
draw_circle(canvas, (255, 0, 0), (100, 100), 20)

draw_text(canvas, "Hello", (0, 255, 0), (0, 0), 60)
