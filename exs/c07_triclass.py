#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from math import isclose

class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
    def get_coord(self):
        return (self._x,self._y)
    def distance(self, p: "Point") -> float:
        return ((self._x - p._x) ** 2 + (self._y - p._y) ** 2) ** 0.5

class LineSegment:
    def __init__(self, a: Point, b: Point):
        self._a = a
        self._b = b
    def length(self) -> float:
        return self._a.distance(self._b)

R = 5 

A = Point(300,400)
B = Point(300,10)
C = Point(400,10)
a = LineSegment(A,B).length()
b = LineSegment(B,C).length()
c = LineSegment(C,A).length()


g2d.init_canvas((500, 500))
g2d.set_color((255,0,0))
g2d.draw_circle((A.get_coord()), R)
g2d.set_color((0,255,0))
g2d.draw_circle((B.get_coord()), R)
g2d.set_color((0,0,255))
g2d.draw_circle((C.get_coord()), R)

g2d.set_color((0,0,0))
g2d.draw_line(A.get_coord(),B.get_coord())
g2d.draw_line(B.get_coord(),C.get_coord())
g2d.draw_line(C.get_coord(),A.get_coord())

if a + b != c and a + c != b and b + c != a:
	if a == b == c:
	   g2d.alert("equilateral triangle")
	elif a != b and a != c and b != c:
	   g2d.alert("scalene triangle")
	else:
	   g2d.alert("isosceles triangle")

	if isclose(a**2,b**2 + c**2) or isclose(b**2,a**2 + c**2) or isclose(c**2, b**2 + a**2):
	   g2d.alert("righ triangle")

g2d.main_loop()
