#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

##from types import Callable  # f: Callable[[float], float]

def f3(x: float) -> float:
    return x ** 3 - x - 1

def find_zero(f, xmin: float, xmax: float, err: float) -> float:
    if f(xmin) * f(xmax) > 0:
        raise ValueError("Cannot find a solution in the range")
    x = (xmin + xmax) / 2
    y = f(x)
    if abs(y) > err:
        if y * f(xmin) < 0:
            x = find_zero(f, xmin, x, err)
        else:
            x = find_zero(f, x, xmax, err)
    return x

def main():
    x = find_zero(f3, 1, 2, 1e-6)
    print(x)

main()
