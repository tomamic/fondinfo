#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d
import math

i, n = 0, 256

def update():
    global i
    x = int(300 + i * math.cos(i * math.pi / 32))
    y = int(300 + i * math.sin(i * math.pi / 32))
    g2d.fill_canvas((255, 255, 255))
    g2d.draw_circle((255 - i, 0, i), (x, y), int(i / 2))
    i = (i + 1) % n

def main():
    g2d.init_canvas((600, 600))
    g2d.main_loop(update, 1000 / 30)

main()
