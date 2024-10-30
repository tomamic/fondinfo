#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

with open("_squares.txt", "w") as squares:
    for x in range(10):
        print(x, x ** 2, file=squares)

