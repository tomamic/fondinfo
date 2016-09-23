#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''DELTA = ord('a') - ord('A')
DASH = '-'

text = ''
with open("e2_2011_6_dash.py") as infile:
    text = infile.read()

dash = False

for c in text:
    if 'a' <= c <= 'z':
        code = ord(c) - DELTA
        print(chr(code), end='')
        dash = False
    elif ('A' <= c <= 'Z') or ('0' <= c <= '9'):
        print(c, end='')
        dash = False
    elif not dash:
        print(DASH, end='')
        dash = True
