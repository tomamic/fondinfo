#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

text = input("text? ")

inside = False

for c in text:
    if c == '(':
        inside = True
    elif c == ')' and inside:
        inside = False
    elif not inside:
        print(c, end="")
