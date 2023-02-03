#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import math

filename = input("filename? ")
minval, maxval = math.inf, -math.inf
with open(filename) as f:
    for line in f:
        val = float(line)
        if val < minval:
            minval = val
        if val > maxval:
            maxval = val
print(minval, maxval)
