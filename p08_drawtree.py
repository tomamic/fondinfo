#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d, math
from p03_polar import move_around

def draw_tree(pos, length, angle):
    nxt = move_around(pos, length, angle)
    if length < 5:
        g2d.set_color((0, 255, 0))
        g2d.draw_line(pos, nxt)
    else:
        g2d.set_color((128, 64, 0))
        g2d.draw_line(pos, nxt, length / 5)
        draw_tree(nxt, length * 0.8, angle + math.pi / 6)
        draw_tree(nxt, length * 0.8, angle - math.pi / 6)

def main():
    W, H = 480, 360
    g2d.init_canvas((W, H))
    draw_tree((W // 2, H), 72, -math.pi / 2)
    g2d.main_loop()

main()
