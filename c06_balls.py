#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import g2d
from c06_ball import Ball, ARENA_W, ARENA_H

def tick():
    g2d.clear_canvas()
    for b in balls:
        g2d.draw_image("ball.png", b.pos())
        b.move()

def main():
    global balls
    balls = [Ball(40, 80), Ball(80, 40), Ball(120, 120)]
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
