#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p03_polar import move_around
from math import pi

W, H, N = 500, 500, 256
v = 4 * pi / N  # angular velocity
i = 0

def tick():
    global i
    pos = move_around((W / 2, H / 2), 25 + i * 0.4, i * v)
    g2d.clear_canvas()
    g2d.set_color((255 - i, 0, i))
    g2d.draw_circle(pos, i * 0.4)
    i = (i + 1) % N

def main():
    g2d.init_canvas((W, H))
    g2d.main_loop(tick)

main()
