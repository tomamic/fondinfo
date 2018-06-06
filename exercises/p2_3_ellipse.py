#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from math import pi

def ellipse_area(a: float, b: float) -> float:
    return pi * a * b

def main():
    a0 = float(input("a? "))
    b0 = float(input("b? "))
    area = ellipse_area(a0, b0)
    print(area)

main()
