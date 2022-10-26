#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

def sierpinski(x, y, w, h, level):
    w2, h2 = w // 2, h // 2
    if w2 < 2 or h2 < 2 or level == 0:
        return
    g2d.draw_rect((x, y), (w2, h2))
    sierpinski(x + w2, y, w2, h2, level - 1)
    sierpinski(x, y + h2, w2, h2, level - 1)
    sierpinski(x + w2, y + h2, w2, h2, level - 1)

def main():
    w, h = 512, 512
    g2d.init_canvas((w, h))

    g2d.set_color((0, 0, 0))
    g2d.draw_rect((0, 0), (w, h))
    g2d.set_color((255, 255, 255))

    sierpinski(0, 0, w, h, 6)
    g2d.main_loop()

main()
