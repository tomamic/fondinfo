#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import sys; sys.path.append("../")
import g2d
from p21_polygon import draw_polygon

i, n = 0, 0
ARENA_W, ARENA_H, R = 600, 600, 250

def tick():
    global i
    g2d.clear_canvas()
    draw_polygon(n, (ARENA_W/2, ARENA_H/2), R, i)
    i += 1

def main():
    global n
    g2d.init_canvas((ARENA_W, ARENA_H))
    n = int(g2d.prompt("Sides?"))
    g2d.main_loop(tick)

main()
