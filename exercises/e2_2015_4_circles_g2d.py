#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d

n = int(input('Circles? '))

SIDE = 600
g2d.canvas_init((SIDE, SIDE))

center = SIDE // 2, SIDE // 2
delta_radius = SIDE / (2 * n)
delta_color = 0
if n > 1:
    delta_color = 255.0 / (n - 1)

for i in range(n):
    radius = int(SIDE // 2 - i * delta_radius)
    color = int(255.0 - i * delta_color)
    g2d.draw_circle((color, 0, 0), center, radius)
