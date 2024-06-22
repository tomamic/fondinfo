#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

class Linear2Model:
    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def predict(self, x: float, y: float) -> float:
        return self._a * x + self._b * y + self._c

def main():
    a = float(input("a? "))
    b = float(input("b? "))
    c = float(input("c? "))
    model = Linear2Model(a, b, c)

    line = input("x? ")
    while line != "":
        x = float(line)
        y = float(input("y? "))
        z = model.predict(x, y)
        print("z:", z)
        line = input("x? ")

if __name__ == "__main__":
    main()
