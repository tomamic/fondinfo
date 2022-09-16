#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

def sierpinski(pos: (int, int), size: (int, int), level):
    x, y, w, h = pos + size
    w2, h2 = w // 2, h // 2
    if w2 < 2 or h2 < 2 or level == 0:
        return
    g2d.draw_rect((x + w2, y), (w - w2, h2))
    sierpinski((x, y), (w2, h2), level - 1)
    sierpinski((x, y + h2), (w2, h - h2), level - 1)
    sierpinski((x + w2, y + h2), (w - w2, h - h2), level - 1)

def main():
    size = (600, 600)
    g2d.init_canvas(size)
    sierpinski((0, 0), size, 8)
    g2d.main_loop()

main()
