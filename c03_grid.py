#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import g2d

CANVAS_W, CANVAS_H = 600, 500
g2d.init_canvas((CANVAS_W, CANVAS_H))
cols = int(g2d.prompt("Cols? "))
rows = int(g2d.prompt("Rows? "))

w, h = CANVAS_W / max(cols, 1), CANVAS_H / max(rows, 1)
g, b = 255 / max(rows - 1, 1), 255 / max(cols - 1, 1)

for y in range(rows):
    for x in range(cols):
        g2d.set_color((0, g * y, b * x))
        g2d.draw_rect((w * x, h * y), (w, h))

g2d.main_loop()
