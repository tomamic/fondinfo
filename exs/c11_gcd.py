#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)  # tail recursion

def gcd_it(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a, b = 1071, 1029
    # a = int(input("a? "))
    # b = int(input("b? "))
    result = gcd(a, b)
    print(result)

if __name__ == "__main__":
    main()
