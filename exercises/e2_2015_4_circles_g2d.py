#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

n = int(input('Circles? '))

SIDE = 600
canvas = canvas_init((SIDE, SIDE))

center = SIDE // 2, SIDE // 2
delta_radius = SIDE / (2 * n)
delta_color = 0
if n > 1:
    delta_color = 255.0 / (n - 1)

for i in range(n):
    radius = int(SIDE // 2 - i * delta_radius)
    color = int(255.0 - i * delta_color)
    draw_circle(canvas, (color, 0, 0), center, radius)
