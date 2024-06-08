#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
    def distance(self, p: "Point") -> float:
        return ((self._x - p._x) ** 2 + (self._y - p._y) ** 2) ** 0.5

class LineSegment:
    def __init__(self, a: Point, b: Point):
        self._a = a
        self._b = b
    def length(self) -> float:
        return self._a.distance(self._b)

def main():
    Point a(3,4)
    Point b(6,5)
    Segmant s(a,b)
    print(s.length()

main()
