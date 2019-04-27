#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def bintxt(n):
    if n == 0:
        return ''
    return bintxt(n // 2) + str(n % 2)

def main():
    n = int(input("n? "))
    print(bintxt(n))

main()
