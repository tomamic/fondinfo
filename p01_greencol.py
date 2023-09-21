#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

L = 500
g2d.init_canvas((L, L))

n = int(g2d.prompt("N?"))
m_green = 255 / max(n - 1, 1)
l = L / max(n, 1)

for i in range(n):
    y = i * l
    green = i * m_green
    g2d.set_color((0, green, 0))
    g2d.draw_rect((0, y), (l, l))

g2d.main_loop()
