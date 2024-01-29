#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from math import sqrt

def hypotenuse(leg1: float, leg2: float) -> float:
    '''
    Return the hypotenuse of a right triangle,
    given both its legs (catheti).
    '''
    return sqrt(leg1 ** 2 + leg2 ** 2)

def main():
    a = float(input('a? '))
    b = float(input('b? '))
    c = hypotenuse(a, b)
    print(c)

main()  # remove if importing the module elsewhere
