#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

* Chiedere all'utente tre numeri interi: a, b, c
* Determinare qual è il minore dei tre

Controllare prima di tutto se a è minore degli altri due,
altrimenti controllare quale è il minore tra b e c
'''

a = int(input())
b = int(input())
c = int(input())

print("Min:")
if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

print("Max:")
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

