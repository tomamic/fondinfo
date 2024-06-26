#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

def perf_square(n: int) -> tuple[bool, int]:
    i = 1
    while i * i < n:
        i += 1

    if i * i == n:
        return (True, i)
    return (False, 0)

def main():
    n = int(input("n? "))
    perf, root = perf_square(n)

    if perf:
        print("Perfect square of", root)
    else:
        print("Not a perfect square")

if __name__ == "__main__":
    main()