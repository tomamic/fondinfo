#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
import math

i, n = 0, 256

def tick():
    global i
    x = int(300 + i * math.cos(i * math.pi / 32))
    y = int(300 + i * math.sin(i * math.pi / 32))
    g2d.clear_canvas()
    g2d.set_color((255 - i, 0, i))
    g2d.fill_circle((x, y), i // 2)
    i = (i + 1) % n

def main():
    g2d.init_canvas((600, 600))
    g2d.main_loop(tick)

main()
