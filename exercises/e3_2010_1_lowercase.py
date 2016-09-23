#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

text = "Hey!! It's 2010, yet"
dash = False

for c in text:
    if c.isupper():
        print(c.lower(), end='')
        dash = False
    elif c.isdigit() or c.islower():
        print(c, end='')
        dash = False
    else:
        print('-', end='')
        dash = True
