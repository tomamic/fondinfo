#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import math

def sqrt_bisection(x: float) -> float:
    low, high = 0, x
    if high < 1:
        high = 1
    y = (high + low) / 2
    delta = y ** 2 - x

    while not (-0.001 <= delta <= 0.001):
        if delta < 0:
            low = y
        else:
            high = y
        y = (high + low) / 2
        delta = y ** 2 - x
    return y

if __name__ == '__main__':
    x = float(input())
    print(sqrt_bisection(x))
    print(math.sqrt(x))
