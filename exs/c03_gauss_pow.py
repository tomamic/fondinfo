#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

n = int(input("n? "))
total = 0
for i in range(n):
    total += 2 ** i

print("The sum is", total)
print("Gauss’ formula is", total == 2 ** n - 1)
