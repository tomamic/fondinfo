#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy, time
cppyy.include("integral.cpp")
from cppyy.gbl import integral

def py_f(x: float) -> float:
    return x * x + x

def py_integral(a: float, b: float, n: int) -> float:
    """
    Estimate the area beneath the curve py_f, between the
    abscissas a and b; the region is approximated as n rectangles.
    """
    total = 0.0
    dx = (b - a) / n
    for i in range(n):
        total += dx * py_f(a + dx * i)
    return total

def main():
    t0 = time.time()
    i = integral(1, 10, 100_000_000)
    t = time.time() - t0
    print(f"C++\t{i:10.4f}\t{t:10.4f}")

    t0 = time.time()
    i = py_integral(1, 10, 100_000_000)
    t = time.time() - t0
    print(f"Python\t{i:10.4f}\t{t:10.4f}")

main()
