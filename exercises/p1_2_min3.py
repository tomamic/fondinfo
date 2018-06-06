#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Minore e maggiore
- Generare e stampare tre numeri interi casuali: a, b, c
- Ciascuno compreso tra 1 e 6
- Determinare e mostrare qual è il minore dei tre
'''

from random import randint

a = randint(1, 6)
b = randint(1, 6)
c = randint(1, 6)
min_ = 0
max_ = 0

if a < b and a < c:
    min_ = a
elif b < c:
    min_ = b
else:
    min_ = c

if a > b and a > c:
    max_ = a
elif b > c:
    max_ = b
else:
    max_ = c

print("Values:", a, b, c)
print("Min:", min_)
print("Max:", max_)
