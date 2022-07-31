#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

filename = input("filename? ")
minval, maxval = None, None
with open(filename) as f:
    for line in f:
        val = float(line)
        if minval == None or val < minval:
            minval = val
        if maxval == None or val > maxval:
            maxval = val
print(minval, maxval)
