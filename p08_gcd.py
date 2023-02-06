#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def gcd(a: int, b: int) -> int:
    if b != 0:
        return gcd(b, a % b)  # tail recursion
    return a

def gcd_it(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a, b = 1071, 1029
    # a = int(input("a? "))
    # b = int(input("b? "))
    result = gcd(a, b)
    print(result)

main()
