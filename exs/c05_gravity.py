#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d

ARENA_W, ARENA_H = 480, 360
BALL_W, BALL_H = 20, 20
x, y, dx, dy, g = 50, 50, 5, 0, 0.5

def tick():
    global x, y, dx, dy
    g2d.clear_canvas()
    g2d.draw_image("ball.png", (x, y))
    if not 0 <= x + dx <= ARENA_W - BALL_W:
        dx = -dx
    if y + dy > ARENA_H - BALL_H:
        dy = -dy
    else:
        dy += g
    x += dx
    y += dy

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
