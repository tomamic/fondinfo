#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from math import sqrt

def hypotenuse(leg1: float, leg2: float) -> float:
    """
    Return the hypotenuse of a right triangle,
    given both its legs (catheti).
    """
    return sqrt(leg1 ** 2 + leg2 ** 2)

def main():
    a = float(input("a? "))
    b = float(input("b? "))
    c = hypotenuse(a, b)
    print(c)

main()  # remove if importing as a module elsewhere
