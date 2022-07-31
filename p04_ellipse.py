#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import math

class Ellipse:
    def __init__(self, a0: float, b0: float):
        self._a = a0
        self._b = b0

    def area(self) -> float:
        return math.pi * self._a * self._b

    def focal_distance(self) -> float:
        return 2 * math.sqrt(abs(self._a ** 2 - self._b ** 2))

def main():
    val_a = float(input("a? "))
    val_b = float(input("b? "))
    e = Ellipse(val_a, val_b)
    area = e.area()
    dist = e.focal_distance()
    print(area, dist)

main()
