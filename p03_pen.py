#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
import math

def next_pos(start: g2d.Point, length: float, angle: float) -> g2d.Point:
    x, y = start
    x1 = x + math.cos(angle) * length
    y1 = y + math.sin(angle) * length
    return (x1, y1)

def main():
    g2d.init_canvas((600, 600))

    n = 3  # triangle
    rot = 2 * math.pi / n  # ↻ 120°, exterior angle
    pos = pos0 = (200, 200)
    side, angle = 200, 0  # →

    for i in range(n - 1):
        nxt = next_pos(pos, side, angle)
        g2d.draw_line(pos, nxt)
        pos = nxt
        angle += rot

    g2d.draw_line(pos, pos0)  # otherwise, last point is slightly different

    g2d.main_loop()

if __name__ == "__main__":
    main()  # won't run automatically, if the script is imported elsewhere
