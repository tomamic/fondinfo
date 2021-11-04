#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

def center(pos: (int, int), size: (int, int)) -> (int, int):
    x, y, w, h = pos + size
    return x + w / 2, y + h / 2

def htree(pos: (int, int), size: (int, int), level: int):
    x, y, w, h = pos + size
    if level == 0 or w < 3 or h < 3:
        return
    if level % 2 == 0:
        pos2 = x + w / 2, y
        size2 = w / 2, h
    else:
        pos2 = x, y + h / 2
        size2 = w, h / 2

    g2d.draw_line(center(pos, size2), center(pos2, size2))
    htree(pos, size2, level - 1)
    htree(pos2, size2, level - 1)

side = 600

g2d.init_canvas((side, side))

level = int(g2d.prompt('level? '))  ## -1 = infinite
htree((0, 0), (side, side), level)

g2d.main_loop()
