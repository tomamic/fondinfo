#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import randrange

W, H = 240, 320
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
    color = (i * dc, 0, 0)
    rect = (i * dx, i * dy, SIDE, SIDE)
    g2d.draw_rect(color, rect)
    i += 1

g2d.main_loop()
