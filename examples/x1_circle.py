#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from math import pi

r = float(input("r? "))
if 0 <= r <= 200:
    area = pi * r ** 2
    perimeter = 2 * pi * r
    print("area:", area)
    print("perimeter:", perimeter)
else:
    print("error: out of range")
