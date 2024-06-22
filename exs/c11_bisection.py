#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

##from types import Callable  # f: Callable[[float], float]

def f3(x: float) -> float:
    return x ** 3 - x - 1

def find_zero(f, x1: float, x2: float, err: float) -> float:
    y1, y2 = f(x1), f(x2)
    if y1 * y2 > 0:
        raise ValueError("f(x1) and f(x2) must have opposite sign")
    x = (x1 + x2) / 2
    y = f(x)
    if abs(y) <= err:
        return x
    x1, x2 = (x1, x) if y1 * y < 0 else (x, x2)
    return find_zero(f, x1, x2, err)

def main():
    sol = find_zero(f3, 1, 2, 1e-6)
    print(sol)

if __name__ == "__main__":
    main()
