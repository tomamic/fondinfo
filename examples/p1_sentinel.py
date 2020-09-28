#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

count = 0
total = 0

val = int(input("Val? [-1 to end] "))
while val != -1:
    total += val  # total = total + val
    count += 1    # count = count + 1
    val = int(input("Val? [-1 to end] "))

if count != 0:
    print("The average is", total / count)
