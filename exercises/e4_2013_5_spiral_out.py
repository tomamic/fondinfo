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

    obliged = abs(h - w)  # initial straight row
    x = y = min(w, h) // 2
    if h >= w:
        dx, dy = 0, 1
        if w % 2 == 0:
            y, dy = y + h - w, -1
    else:
        obliged -= 1
        dx, dy = 1, 0
        if h % 2 == 1:
            x, dx = x + w - h, -1

    for i in range(h * w):
        m[y][x] = i + 1
        if i > obliged:
            # if initial row completed, look at left (90° CCW)
            dx1, dy1 = dy, -dx
            if empty(m, x + dx1, y + dy1):
                # if empty @ left, turn left
                dx, dy = dx1, dy1
        x, y = x + dx, y + dy
    return m


if __name__ == '__main__':
    w = int(input('w? '))
    h = int(input('h? '))
    while w > 0 and h > 0:
        m = spiral(w, h)
        for y in range(h):
            for x in range(w):
                print('{:3}'.format(m[y][x]), end='', sep='')
            print()
        print()
        w = int(input('w? '))
        h = int(input('h? '))

