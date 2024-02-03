#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p03_polar import move_around

def draw_watch(center: g2d.Point, radius: int):
    angle = 360 / 60       # 6° rotation for each minute
    for i in range(60):    # 60 minutes
        l = radius * 0.05  # line length: 5% of radius
        if i % 5 == 0:     # each 5 mins, line is 4-fold longer
            l *= 4
        pt1 = move_around(center, radius, i * angle)
        pt2 = move_around(center, radius - l, i * angle)
        g2d.draw_line(pt1, pt2)  # external pt → internal pt

R = 200
g2d.init_canvas((2 * R, 2 * R))
draw_watch((R, R), R)
g2d.main_loop()
