#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from math import pi

r = float(input("r? "))
if r < 0:
    print("error: negative r")
else:
    area = pi * r ** 2
    perimeter = 2 * pi * r
    print("area:", area)
    print("perimeter:", perimeter)
