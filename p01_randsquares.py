#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from random import randrange

W, H = 640, 480
SIDE = 100
size = (SIDE, SIDE)
g2d.init_canvas((W, H))

n = int(g2d.prompt("n? "))
for i in range(n):
    color = randrange(255), randrange(255), randrange(255)
    pos = randrange(W - SIDE), randrange(H - SIDE)
    g2d.set_color(color)
    g2d.draw_rect(pos, size)

g2d.main_loop()
