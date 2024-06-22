#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

def count_am_nz(text: str) -> tuple[int, int]:
    count_am, count_nz = 0, 0
    for c in text.lower():
        if "a" <= c <= "m":
            count_am += 1
        elif "n" <= c <= "z":
            count_nz += 1
    return count_am, count_nz

def main():
    t = input("Text? ")
    c1, c2 = count_am_nz(t)
    print(c1, c2)

main()
