#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

text = input("Text? ")
counters = [0] * 10

for c in text:
    if "0" <= c <= "9":
        counters[int(c)] += 1

for i in range(len(counters)):
    print(i, "=" * counters[i])
