#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

CANVAS, SIDE = 300, 100
g2d.init_canvas((CANVAS, CANVAS))
n = int(g2d.prompt("N?"))

for i in range(n):
    red = i * 255 // max(n - 1, 1)
    x = y = i * (CANVAS - SIDE) // max(n - 1, 1)
    g2d.set_color((red, 0, 0))
    g2d.fill_rect((x, y), (SIDE, SIDE))

g2d.main_loop()
