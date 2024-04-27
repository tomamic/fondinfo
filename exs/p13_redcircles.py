#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import g2d

R = 250
g2d.init_canvas((2 * R, 2 * R))

n = int(g2d.prompt("Circles? "))
r = R / max(n, 1)  # radius: r_fst = r_m = r
c = 255 / max(n - 1, 1)  # color

for i in reversed(range(n)):
    g2d.set_color((c * i, 0, 0))
    g2d.draw_circle((R, R), r * i + r)

g2d.main_loop()
