#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys

calories = {}
with open('calories.txt', 'r') as f:
    for line in f:
        splitted = line.split('\t')
        food = splitted[0]
        val = splitted[1]
        calories[food] = float(val)

total = 0
for line in sys.stdin:
    food, weight = line.split('|')  # see `splitted`, above
    total += float(weight) * calories[food]
print(total)
