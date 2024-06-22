#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from math import pi

RMAX = 200
CX, CY = 250, 250
TY, TH = 25, 50  # text pos and size

g2d.init_canvas((CX * 2, CY * 2))
r = float(g2d.prompt("Radius? "))

if 0 <= r <= RMAX:
    g2d.draw_circle((CX, CY), r)
    area = round(pi * r ** 2, 2)
    perimeter = round(2 * pi * r, 2)
    g2d.draw_text("Area: " + str(area),
                  (CX, CY - r - TY), TH)
    g2d.draw_text("Perimeter: " + str(perimeter),
                  (CX, CY + r + TY), TH)
else:
    g2d.alert("Error: out of range")

g2d.main_loop()
