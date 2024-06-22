#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import g2d
from c04_polar import move_around

def draw_tree(pos, length, angle):
    nxt = move_around(pos, length, angle)
    if length < 5:
        g2d.set_color((0, 255, 0))
        g2d.draw_line(pos, nxt)
    else:
        g2d.set_color((128, 64, 0))
        g2d.draw_line(pos, nxt, length / 5)
        draw_tree(nxt, length * 0.8, angle + 30)
        draw_tree(nxt, length * 0.8, angle - 30)

def main():
    W, H = 480, 360
    g2d.init_canvas((W, H))
    draw_tree((W // 2, H), 72, -90)
    g2d.main_loop()

main()
