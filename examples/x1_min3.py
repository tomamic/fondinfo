#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randint

a = randint(1, 6)
b = randint(1, 6)
c = randint(1, 6)
vmin = 0
vmax = 0

if a < b and a < c:
    vmin = a
elif b < c:
    vmin = b
else:
    vmin = c

if a > b and a > c:
    vmax = a
elif b > c:
    vmax = b
else:
    vmax = c

print("Values:", a, b, c)
print("Min:", vmin)
print("Max:", vmax)
