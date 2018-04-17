#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

line = input()
for c in line:
    if not c.isdigit():  # if c < '0' or c > '9'...
        print(c, end='')
