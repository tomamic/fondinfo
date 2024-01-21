#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from math import pi, sin, cos, radians

g2d.init_canvas((400, 400))  # width, height

r = 100
x0, y0 = 200, 200  # center
for angle in (0, 15, 30, 45):
    x = x0 + r * cos(radians(angle))
    y = y0 + r * sin(radians(angle))
    g2d.draw_line((x0, y0), (x, y))

g2d.main_loop()  # manage the window/canvas
