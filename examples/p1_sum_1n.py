#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

# Sum of the numbers from 1 to n
n = int(input("n? "))
total = 0
count = 1

while count <= n:
    total = total + count
    count = count + 1

print("The sum is", total)
