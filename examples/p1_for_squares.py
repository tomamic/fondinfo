#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

CANVAS_SIZE = 300
g2d.init_canvas((CANVAS_SIZE, CANVAS_SIZE))

n = 5           ## int(g2d.prompt("N?"))
step_pos = 50   ## CANVAS_SIZE // (n + 1)
step_red = 60   ## 255 // max(n - 1, 1)
side = step_pos * 2

for i in range(n):
    pos = i * step_pos
    red = i * step_red
    g2d.set_color((red, 0, 0))
    g2d.fill_rect((pos, pos), (side, side))

g2d.main_loop()
