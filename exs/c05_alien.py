#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d

ARENA_W, ARENA_H = 480, 360
BALL_W, BALL_H = 20, 20
x, y, dx, dy = 50, 50, 5, 5

def tick():
    global x, y, dx
    g2d.clear_canvas()
    g2d.draw_image("sprites.png", (x, y), (20, 0), (20, 20))
    if 0 <= x + dx <= ARENA_W - BALL_W:
        x += dx
    else:
        y += dy
        dx = -dx

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
