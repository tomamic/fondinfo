#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

WIDTH, HEIGHT = 600, 500
g2d.init_canvas((WIDTH, HEIGHT))
cols = int(g2d.prompt("Cols? "))
rows = int(g2d.prompt("Rows? "))

w, h = WIDTH / cols, HEIGHT / rows
delta_blue = 255 / max(cols - 1, 1)
delta_green = 255 / max(rows - 1, 1)

for y in range(rows):
    for x in range(cols):
        g2d.set_color((0, delta_green * y, delta_blue * x))
        g2d.draw_rect((w * x, h * y), (w - 1, h - 1))

g2d.main_loop()
