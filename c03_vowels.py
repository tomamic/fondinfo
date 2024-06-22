#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

line = input("Text? ").lower()
digits, vowels = 0, 0

for c in line:
    if "0" <= c <= "9":
        digits += 1
    elif c in "aeiou":  # test membership
        vowels += 1

print(digits, vowels)
