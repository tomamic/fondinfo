#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

FIRST, LAST = 32, 126

cols, rows = 16, 8

for y in range(rows):
    for x in range(cols):
        i = FIRST + y * cols + x
        if i <= LAST:
            print(chr(i), end=" ")
    print()
print()

cols, rows = 8, 16

for y in range(rows):
    for x in range(cols):
        i = FIRST + x * rows + y
        if i <= LAST:
            print(chr(i), end=" ")
    print()

