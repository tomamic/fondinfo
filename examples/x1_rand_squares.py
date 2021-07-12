#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import randrange

W, H = 640, 480
SIDE = 100
g2d.init_canvas((W, H))

n = int(g2d.prompt("n? "))
for i in range(n):
    r = randrange(255)
    g = randrange(255)
    b = randrange(255)
    x = randrange(W - SIDE)
    y = randrange(H - SIDE)
    g2d.set_color((r, g, b))
    g2d.fill_rect((x, y), (SIDE, SIDE))

g2d.main_loop()
