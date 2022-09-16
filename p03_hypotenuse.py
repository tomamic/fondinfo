#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def hypotenuse(leg1: float, leg2: float) -> float:
    '''
    Return the hypotenuse of a right triangle,
    given both its legs (catheti).
    '''
    return (leg1 ** 2 + leg2 ** 2) ** 0.5

def main():
    a = float(input('a? '))
    b = float(input('b? '))
    c = hypotenuse(a, b)
    print(c)

main()  # remove if importing the module elsewhere

