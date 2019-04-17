#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import randrange

W, H = 320, 240
SIDE = 100

n = int(g2d.prompt("n? "))  # like input
dx, dc = 0, 0
if n > 1:
    dx = (W - SIDE) / (n - 1)
    dy = (H - SIDE) / (n - 1)
    dc = 255.0 / (n - 1)

g2d.init_canvas((W, H))

i = 0
while i < n:
    g2d.set_color((i * dc, 0, 0))
    g2d.fill_rect((i * dx, i * dy, SIDE, SIDE))
    i += 1

g2d.main_loop()
