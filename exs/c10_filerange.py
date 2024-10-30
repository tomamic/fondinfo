#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import math

filename = input("filename? ")
minval, maxval = math.inf, -math.inf
with open(filename) as f:
    for line in f:
        val = float(line)
        if val < minval:
            minval = val
        if val > maxval:
            maxval = val
print(minval, maxval)
