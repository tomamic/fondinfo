#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from random import randrange

L = 500
g2d.init_canvas((L, L))

n = int(g2d.prompt("How many squares?"))
l = L / n
for i in range(n):
    g2d.set_color((randrange(256), randrange(256), randrange(256)))
    pos = i * l
    g2d.draw_rect((pos, pos), (l, l))

g2d.main_loop()
