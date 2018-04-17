#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d

palette = []
palette_file = open('palette.txt', 'r')
with palette_file:
    for line in palette_file:
        if len(line) > 0:
            vals = line.split()
            color = (int(vals[0]), int(vals[1]), int(vals[2]))
            palette.append(color)

n = int(input('squares? '))

side = 400.0
delta = side / n

g2d.init_canvas((int(side), int(side)))

for i in range(n):
    color = palette[i % len(palette)]
    g2d.draw_rect(color, (0, 0, int(side), int(side)))
    side -= delta

g2d.main_loop()
