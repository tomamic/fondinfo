#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def empty(m: list, x: int, y: int) -> bool:
    w, h = len(m[0]), len(m)
    return 0 <= x < w and 0 <= y < h and m[y][x] == 0

def spiral(w: int, h: int) -> list:
    m = [[0 for x in range(w)] for y in range(h)]

    # initially: bottom-left cell, heading up
    x, y = 0, h - 1
    dx, dy = 0, -1

    for i in range(h * w):
        m[y][x] = i + 1
        # bounce against border or visited cell?
        if not empty(m, x + dx, y + dy):
            # turn 90° clockwise, raster: (x', y') = (-y, x)
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return m

if __name__ == '__main__':
    w = int(input('w? '))
    h = int(input('h? '))
    m = spiral(w, h)
    for y in range(h):
        for x in range(w):
            print('{:3}'.format(m[y][x]), end='', sep='')
        print()
    print()
