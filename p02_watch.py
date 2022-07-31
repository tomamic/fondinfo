#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from math import pi, sin, cos

R = 200

g2d.init_canvas((2*R, 2*R))
g2d.set_color((0, 0, 0))

for i in range(60):
    r = R - 5
    if i % 5 == 0:
        r = R - 20
    angle = i * (2*pi / 60)
    pt1 = R + r*cos(angle), R + r*sin(angle)
    pt2 = R + R*cos(angle), R + R*sin(angle)
    g2d.draw_line(pt1, pt2)

g2d.main_loop()
