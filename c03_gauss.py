#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

n = int(input("n? "))
total = 0
for i in range(1, n + 1):
    total += i

print("The sum is", total)
print("Gauss’ formula is", total == n * (n + 1) / 2)
