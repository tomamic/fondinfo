#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

total = 0
total_inv = 0

with open("resistors.txt") as file:
    for line in file:
        val = float(line)
        total += val
        total_inv += 1 / val

if total_inv > 0:
    print(total, 1 / total_inv)
