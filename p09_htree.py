#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

def htree(pos: (int, int), size: (int, int), level: int):
    x, y, w, h = pos + size
    if level == 0 or w < 10 or h < 10:
        return

    x1, x2, x3 = x + 1*w//4, x + 2*w//4, x + 3*w//4
    y1, y2, y3 = y + 1*h//4, y + 2*h//4, y + 3*h//4
    g2d.draw_line((x1, y1), (x1, y3))
    g2d.draw_line((x3, y1), (x3, y3))
    g2d.draw_line((x1, y2), (x3, y2))

    for pt in ((x, y), (x2, y), (x, y2), (x2, y2)):
        htree(pt, (w//2, h//2), level-1)

def main():
    size = 600, 600
    g2d.init_canvas(size)
    level = int(g2d.prompt('level? '))  ## -1 = infinite
    htree((0, 0), size, level)
    g2d.main_loop()

main()
