#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

L = 500
g2d.init_canvas((L, L))

n = int(g2d.prompt("N?"))
m_blue = 255 / max(n - 1, 1)
diameter = L / max(n, 1)
radius = diameter / 2

for i in range(n):
    x = radius + i * diameter
    blue = i * m_blue
    g2d.set_color((0, 0, blue))
    g2d.draw_circle((x, radius), radius)

g2d.main_loop()
