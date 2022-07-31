#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

FIRST = 32
LAST = 126
ROWS = 4
COLS = 24

for y in range(ROWS):
    for x in range(COLS):
        ##i = FIRST + x + y * COLS
        i = FIRST + y + x * ROWS
        if i <= LAST:
            print(chr(i), end="")
    print()
