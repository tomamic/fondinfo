#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from c04_polar import move_around

def draw_polygon(n: int, center: g2d.Point, radius: float,
                 rot: float=0):
    angle = 360 / n
    for i in range(n):
        pt1 = move_around(center, radius, i * angle + rot)
        pt2 = move_around(center, radius, (i + 1) * angle + rot)
        g2d.draw_line(pt1, pt2)

def main():
    g2d.init_canvas((600, 600))
    n = int(g2d.prompt("Sides?"))
    draw_polygon(n, (300, 300), 250)
    g2d.main_loop()

if __name__ == "__main__":
    main()
