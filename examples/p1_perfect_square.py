#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

n = int(input("n? "))

i = 1
while i * i < n:
    i += 1

if i * i == n:
    print(i)
else:
    print("No")
