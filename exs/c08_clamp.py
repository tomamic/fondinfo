#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
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
