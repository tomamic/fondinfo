#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

def clamp(values: list[int], a: int, b: int):
    for i, v in enumerate(values):
        if v < a:
            values[i] = a
        if v > b:
            values[i] = b

data = [3, 4, 6, 7, 3, 5, 6, 12, 4]
clamp(data, 5, 10)
print(data)
