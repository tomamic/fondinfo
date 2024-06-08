#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

class QuadraticModel:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def predict(self, x: float) -> float:
        return self._a * x ** 2 + self._b * x + self._c

def main():
    a = float(input("a? "))
    b = float(input("b? "))
    c = float(input("c? "))
    model = QuadraticModel(a, b, c)

    line = input("x? ")
    while line != "":
        x = float(line)
        y = model.predict(x)
        print("y:", y)
        line = input("x? ")

if __name__ == "__main__":
    main()
