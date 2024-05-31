#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

from time import time_ns

def xorshift32(n) -> int:
    n ^= (n << 13) & 0xffffffff
    n ^= (n >> 17)
    n ^= (n << 5) & 0xffffffff
    return n

n = time_ns() & 0xffffffff
for _ in range(10):
    n = xorshift32(n)
    print(n)
