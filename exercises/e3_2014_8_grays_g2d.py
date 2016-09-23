#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

grays = []
val = int(input('gray? '))
while 0 <= val < 256:
    grays.append(val)
    val = int(input('gray? '))

m = int(input('repetitions? '))

side = 400.0
delta = side / (len(grays) * m)

canvas = canvas_init((int(side), int(side)))

for i in range(m):
    for val in grays:
        draw_rect(canvas, (val, val, val),
                  (0, 0, int(side), int(side)))
        side -= delta
