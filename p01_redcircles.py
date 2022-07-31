#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

RADIUS, radius, red = 300, 300, 255
g2d.init_canvas((RADIUS * 2, RADIUS * 2))

n = int(g2d.prompt("Circles? "))
for i in reversed(range(n)):
    red = i * 255 // max(n - 1, 1)
    radius = (i + 1) * RADIUS // n
    g2d.set_color((red, 0, 0))
    g2d.fill_circle((RADIUS, RADIUS), radius)

g2d.main_loop()
