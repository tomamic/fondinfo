#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import sample

w, h = 16, 6
n = 3
bishops = set(sample(range(w * h), n))

diags1, diags2 = set(), set()

for b in bishops:
    y, x = divmod(b, w)
    diags1.add(x + y)  # //
    diags2.add(x + h - 1 - y)  # \\

for y in range(h):
    for x in range(w):
        c = ("X" if y * w + x in bishops else
             "/" if x + y in diags1 else
             "\\" if x + h - 1 - y in diags2 else
             "·")
        print(c, end="")
    print()
