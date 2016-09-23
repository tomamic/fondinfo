#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

palette_txt = '''180 120 60
120 180 60
120 60 180'''

palette = []
f = palette_txt.split('\n')
for line in f:
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
