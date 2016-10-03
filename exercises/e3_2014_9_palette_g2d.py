#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

palette = []
palette_file = open('palette.txt', 'r')
with palette_file:
    print(locals())
    for line in palette_file:
        if len(line) > 0:
            vals = line.split()
            color = (int(vals[0]), int(vals[1]), int(vals[2]))
            palette.append(color)

n = int(input('squares? '))

side = 400.0
delta = side / n

canvas = canvas_init((int(side), int(side)))

for i in range(n):
    color = palette[i % len(palette)]
    draw_rect(canvas, color, (0, 0, int(side), int(side)))
    side -= delta
