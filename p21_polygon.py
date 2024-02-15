#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import g2d
from p21_polar import move_around

def draw_polygon(n: int, center: g2d.Point, radius: float):
    angle = 360 / n
    for i in range(n):
        pt1 = move_around(center, radius, i * angle)
        pt2 = move_around(center, radius, (i + 1) * angle)
        g2d.draw_line(pt1, pt2)

def main():
    g2d.init_canvas((600, 600))
    n = int(g2d.prompt("Sides?"))
    draw_polygon(n, (300, 300), 250)
    g2d.main_loop()

if __name__ == "__main__":
    main()
