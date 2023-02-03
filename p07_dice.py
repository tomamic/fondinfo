#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

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
