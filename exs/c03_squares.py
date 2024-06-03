#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import sys; sys.path.append("../")
import g2d

L, l, margin = 500, 200, 10
g2d.init_canvas((L, L))

n = int(g2d.prompt("How many squares?"))

pos_fst, pos_lst = margin, L - l - margin
pos_m = (pos_lst - pos_fst) / max(n - 1, 1)  # ⚠️ div by 0

red_fst, red_lst = 0, 255
red_m = (red_lst - red_fst) / max(n - 1, 1)  # ⚠️ div by 0

for i in range(n):
    red = red_m * i + red_fst
    g2d.set_color((red, 0, 0))

    pos = pos_m * i + pos_fst
    g2d.draw_rect((pos, pos), (l, l))

g2d.main_loop()
