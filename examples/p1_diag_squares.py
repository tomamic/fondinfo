#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

g2d.init_canvas((400, 400))
n = int(g2d.prompt("N?"))

for i in range(n):
    c, p = 0, 0
    if n > 1:
        c = i * 255 // (n - 1)
        p = i * 300 // (n - 1)
    g2d.set_color((c, 0, 0))
    g2d.fill_rect((p, p, 100, 100))

g2d.main_loop()
