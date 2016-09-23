#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

for y in range(1, 13):
    for x in range(1, 13):
        val = '{:4}'.format(x * y)
        print(val, end='')
    print()
