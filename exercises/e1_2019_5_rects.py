#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d

size = 500
g2d.init_canvas((size, size))

n = int((g2d.prompt("n?")))
dsize = size // n
dcolor = 255
if n > 1:
    dcolor = 255 // (n - 1)
for i in range(n):
    g2d.set_color((0, i * dcolor, 0))
    g2d.fill_rect((0, 0), (size - i * dsize, size - i * dsize))

g2d.main_loop()
