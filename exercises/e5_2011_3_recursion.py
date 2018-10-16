#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import math

def sqrt_recursion(x: float, low: float, high: float) -> float:
    y = (high + low) / 2
    delta = y ** 2 - x

    if abs(delta) > 0.001:
        if delta < 0:
            y = sqrt_recursion(x, y, high)
        else:
            y = sqrt_recursion(x, low, y)
    return y

def main():
    x = float(input())

    low, high = 0, x
    if (high < 1):
        high = 1  # in this case, sqrt(x) > x

    print(sqrt_recursion(x, low, high))
    print(math.sqrt(x))

main()
