#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from random import randrange

W, H = 480, 360
g2d.init_canvas((W, H))
g2d.set_color((0, 0, 0))

n = int(g2d.prompt("How many segments? "))
for _ in range(n):
    src = (randrange(W), randrange(H))
    dst = (randrange(W), randrange(H))
    g2d.draw_line(src, dst)

g2d.main_loop()

