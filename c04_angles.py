#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import g2d
from math import pi, sin, cos, radians

def draw_rays(x0: int, y0: int, r: int):
    for angle in [0, 15, 30, 45]:
        x = x0 + r * cos(radians(angle))
        y = y0 + r * sin(radians(angle))
        g2d.draw_line((x0, y0), (x, y))

g2d.init_canvas((400, 400))
draw_rays(200, 200, 100)
g2d.main_loop()
