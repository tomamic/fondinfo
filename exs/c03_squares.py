#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d

L, margin = 500, 10
g2d.init_canvas((L, L))

n = int(g2d.prompt("How many squares?"))
l = 2 * L / (n + 1)

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
