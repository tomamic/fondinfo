#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d

L = 500
g2d.init_canvas((L, L))

n = int(g2d.prompt("N?"))
b = 255 / max(n - 1, 1)  # max, to avoid dividing by 0
r = L / max(2 * n, 1)

for i in range(n):
    g2d.set_color((0, 0, i * b))
    g2d.draw_circle((r + i * r * 2, r), r)

g2d.main_loop()
