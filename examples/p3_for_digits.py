#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

line = input("Text? ")

n, tot = 0, 0

for c in line:
    if '0' <= c <= '9':
        n += 1
        tot += int(c)

print("Number of digits:", n)
print("Sum of digits:", tot)
