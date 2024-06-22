#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import math

class Ellipse:
    def __init__(self, a0: float, b0: float):
        self._a = a0
        self._b = b0

    def area(self) -> float:
        return math.pi * self._a * self._b

    def focus(self) -> float:
        return math.sqrt(abs(self._a ** 2 - self._b ** 2))

def main():
    val_a = float(input("a? "))
    val_b = float(input("b? "))
    e = Ellipse(val_a, val_b)
    area = e.area()
    focus = e.focus()
    print(area, focus)

main()
