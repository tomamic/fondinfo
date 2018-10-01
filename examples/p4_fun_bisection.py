#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

##from types import Callable  # f: Callable[[float], float]

def f3(x: float) -> float:
    return x ** 3 - x - 1

def find_zero(f, low: float, high: float, err: float) -> float:
    x = (low + high) / 2
    y = f(x)
    if abs(y) > err:
        if y * f(low) < 0:
            x = find_zero(f, low, x, err)
        else:
            x = find_zero(f, x, high, err)
    return x

def main():
    x = find_zero(f3, 1, 2, 1e-6)
    print(x)

main()
