#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

total = 0
total_inv = 0

val = float(input("Value? "))
while val > 0:
    total += val
    total_inv += 1 / val
    val = float(input("Value? "))

if total_inv > 0:
    print(total, 1 / total_inv)
