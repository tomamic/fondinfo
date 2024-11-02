#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import sample

w, h = 12, 6
n = 3
bishops = set(sample(range(w * h), n))

# diagonals, see exercise c03_diags
diags1 = set()  # ╱ diagonals, counted from top-left corner
diags2 = set()  # ╲ diagonals, counted from bottom-left corner

for b in bishops:
    y, x = divmod(b, w)
    diags1.add(x + y)          # distance from left-top corner
    diags2.add(x + h - 1 - y)  # distance from bottom-left corner

for y in range(h):
    for x in range(w):
        d1 = x + y          # distance from left-top corner
        d2 = x + h - 1 - y  # distance from bottom-left corner
        c = ("O" if y * w + x in bishops else
             "╳" if d1 in diags1 and d2 in diags2 else
             "╱" if d1 in diags1 else
             "╲" if d2 in diags2 else
             "·")
        print(c, end="")
    print()
