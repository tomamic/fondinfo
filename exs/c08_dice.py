#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randint

rolls = int(input("Rolls? "))
results = [0] * 11

for r in range(rolls):
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    val = die1 + die2
    results[val - 2] += 1

for i, v in enumerate(results):
    print(i + 2, v, "=" * v, sep="\t")
