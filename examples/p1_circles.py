#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

SIDE = 600
g2d.init_canvas((SIDE, SIDE))

n = int(g2d.prompt("Circles? "))

center = SIDE // 2, SIDE // 2
delta_radius = SIDE * 0.5 / n
delta_color = 0
if n > 1:
    delta_color = 255.0 / (n - 1)

for i in range(n):
    radius = int(SIDE // 2 - i * delta_radius)
    g2d.set_color((int(255.0 - i * delta_color), 0, 0))
    g2d.fill_circle(center, radius)

g2d.main_loop()
