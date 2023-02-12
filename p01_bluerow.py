#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

L = 500
g2d.init_canvas((L, L))

n = int(g2d.prompt("N?"))
d_blue = 255 / max(n - 1, 1)
d = L / max(n, 1)
r = d / 2

for i in range(n):
    x = r + i * d
    blue = i * d_blue
    g2d.set_color((0, 0, blue))
    g2d.draw_circle((x, r), r)

g2d.main_loop()
