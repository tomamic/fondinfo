#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import sys; sys.path.append("../")
import g2d

L = 500
g2d.init_canvas((L, L))

n = int(g2d.prompt("N?"))
g = 255 / max(n - 1, 1)  # max, to avoid dividing by 0
l = L / max(n, 1)

for i in range(n):
    g2d.set_color((0, i * g, 0))
    g2d.draw_rect((0, i * l), (l, l))

g2d.main_loop()
