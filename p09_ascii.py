#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

FIRST, LAST = 32, 126
COLS, ROWS = 24, 4

for y in range(ROWS):
    for x in range(COLS):
        ##i = FIRST + y * COLS + x
        i = FIRST + y + x * ROWS
        if i <= LAST:
            print(chr(i), end="")
    print()
