#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randint

a = randint(1, 6)
b = randint(1, 6)
c = randint(1, 6)
smallest = 0
largest = 0

if a < b and a < c:
    smallest = a
elif b < c:
    smallest = b
else:
    smallest = c

if a > b and a > c:
    largest = a
elif b > c:
    largest = b
else:
    largest = c

print("Values:", a, b, c)
print("Min:", smallest)
print("Max:", largest)
