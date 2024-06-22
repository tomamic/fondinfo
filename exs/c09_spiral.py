#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def available(m: list, w: int, h: int, x: int, y: int) -> bool:
    return 0 <= x < w and 0 <= y < h and m[x + y * w] == 0

def spiral(w: int, h: int) -> list:
    m = [0] * (w * h)

    # initially: bottom-left cell, heading up
    x, y = 0, h - 1
    dx, dy = 0, -1

    for i in range(h * w):
        m[x + y * w] = i + 1
        # against border or visited cell?
        if not available(m, w, h, x + dx, y + dy):
            # turn 90° clockwise, raster: (x’, y’) = (-y, x)
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return m

def main():
    w = int(input("w? "))
    h = int(input("h? "))
    m = spiral(w, h)
    for y in range(h):
        for x in range(w):
            print(m[x + y * w], end="\t")
        print()
    print()

main()
