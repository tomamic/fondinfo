#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randint

ROLLS, SIDES, COUNTERS = 100, 6, 11

results = [0] * COUNTERS

for r in range(ROLLS):
    die1 = randint(1, SIDES)
    die2 = randint(1, SIDES)
    val = die1 + die2
    results[val - 2] += 1

for i in range(len(results)):
    if i + 2 < 10:
        print(end=" ")
    print(i + 2, "=" * results[i])  # or, f"{i+2:2}"
