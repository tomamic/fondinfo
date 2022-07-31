#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from math import pi

g2d.init_canvas((400, 400))
r = float(g2d.prompt("Radius? "))

if 0 <= r <= 200:
    g2d.draw_circle((200, 200), r)
    area = pi * r ** 2
    perimeter = 2 * pi * r
    g2d.alert("Area: " + str(area))
    g2d.alert("Perimeter: " + str(perimeter))
else:
    g2d.alert("Error: out of range")

g2d.main_loop()
