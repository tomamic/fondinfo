#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

total = 0
total_inv = 0

val = float(input("val? "))
while val > 0:
    total += val
    total_inv += 1 / val
    val = float(input("val? "))

if total_inv > 0:
    print(total, 1 / total_inv)
