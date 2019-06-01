#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from math import pi, sin, cos

R = 200

g2d.init_canvas((2*R, 2*R))
g2d.set_color((0, 0, 0))
i, angle, r = 0, 0.0, R - 20
while i < 12:
    angle = i * 2 * pi / 12
    pt1 = R + int(r*cos(angle)), R + int(r*sin(angle))
    pt2 = R + int(R*cos(angle)), R + int(R*sin(angle))
    g2d.draw_line(pt1, pt2)
    i += 1

i, angle, r = 0, 0.0, R - 5
while i < 60:
    angle = i * 2 * pi / 60
    pt1 = R + int(r*cos(angle)), R + int(r*sin(angle))
    pt2 = R + int(R*cos(angle)), R + int(R*sin(angle))
    g2d.draw_line(pt1, pt2)
    i += 1

g2d.main_loop()
