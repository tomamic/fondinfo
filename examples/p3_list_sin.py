#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from math import pi, sin

fast_sin = [0] * 360
for x in range(360):
    rad = x * pi / 180
    val = sin(rad)
    fast_sin[x] = val

# fast_sin = [sin(x * pi / 180) for x in range(360)]

angle = int(input("angle? "))
while 0 <= angle < 360:
    value = fast_sin[angle]
    print(f"sin({angle}) = {value:.2f}")
    angle = int(input("angle? "))
