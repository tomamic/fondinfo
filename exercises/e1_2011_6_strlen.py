#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

lines = 0
chars = 0
line = input()
while line != 'end':
    lines += 1
    chars += len(line)
    line = input()
if lines > 0:
    print(chars / lines)
