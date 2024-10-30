#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

class Fraction:
    """Always normalized fraction with positive denominator
    """
    def __init__(self, num: int, den: int):
        if den == 0:  # generate an error
            raise Exception("Invalid denominator")
        if den < 0:
            self._num = -num
            self._den = -den
        else:
            self._num = num
            self._den = den
        self._normalize()  # normalize

    def _normalize(self):
        import math
        gcg = math.gcd(self._num, self._den)
        self._num = self._num // gcg
        self._den = self._den // gcg

    def __str__(self):
        return f"({self._num}/{self._den})"

    def __add__(self, f: "Fraction") -> "Fraction":
        """ implements addition of fractions """
        num = self._num * f._den + f._num * self._den
        den = self._den * f._den
        return Fraction(num, den)

    def __sub__(self, f: "Fraction") -> "Fraction":
        """ implements subtraction between fractions """
        num = self._num * f._den - f._num * self._den
        den = self._den * f._den
        return Fraction(num, den)

    def __mul__(self, f: "Fraction") -> "Fraction":
        """ implements multiplication of fractions """
        num = self._num * f._num
        den = self._den * f._den
        return Fraction(num, den)

    def __truediv__(self, f: "Fraction") -> "Fraction":
        """ implements division between fractions """
        num = self._num * f._den
        den = self._den * f._num
        return Fraction(num, den)

def main():
    f1 = Fraction(10, 4)
    f2 = Fraction(-7, 8)
    print(f1 + f2)      # (13/8)
    print(f1 - f2)      # (27/8)
    print(f1 * f2)      # (-35/16)
    print(f1 / f2)      # (-20/7)


if __name__ == "__main__":
    main()
