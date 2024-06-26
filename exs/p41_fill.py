#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

def fill(values: list[int], pos: int):
    if values[pos] == 0:
        values[pos] = 1
        for d in (-1, 1):
            pos1 = pos + d
            while pos1 < len(values) and values[pos1] == 0:
                values[pos1] = 1
                pos1 += d

data = [int(v) for v in "0022000000002000"]
fill(data, 9)
print(data)
