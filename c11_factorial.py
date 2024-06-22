#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def factorial(n: int) -> int:
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result

def main():
    v = factorial(3)
    print(v)

main()
