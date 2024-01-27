#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from math import radians
from p03_polar import move_around

def draw_watch(center: g2d.Point, radius: int):
    for i in range(60):  # 60 minutes
        radius2 = radius * 0.95  # internal radius is 5% smaller
        if i % 5 == 0:
            radius2 = radius * 0.80  # or 20% smaller, each 5 minutes
        angle = radians(i * 360 / 60)  # 6° rotation for each minute
        pt1 = move_around(center, radius, angle)   # external point
        pt2 = move_around(center, radius2, angle)  # internal point
        g2d.draw_line(pt1, pt2)

R = 200
g2d.init_canvas((2 * R, 2 * R))
draw_watch((R, R), R)
g2d.main_loop()
