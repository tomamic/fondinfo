#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

w = int(input("w? "))
h = int(input("h? "))

x0, y0 = 0, 0
for y in range(h):
    for x in range(w):
        d = abs(x - x0) + abs(y - y0)  # = x + y
        print(d, end="\t")
    print()
print()

x0, y0 = 0, h - 1
for y in range(h):
    for x in range(w):
        d = abs(x - x0) + abs(y - y0)  # = x + h - 1 - y
        print(d, end="\t")
    print()
print()

