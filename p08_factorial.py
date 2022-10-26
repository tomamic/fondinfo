#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def factorial(n: int) -> int:
    result = 1
    if n > 0:
        result = n * factorial(n - 1)
    return result

def main():
    v = factorial(3)
    print(v)

main()
