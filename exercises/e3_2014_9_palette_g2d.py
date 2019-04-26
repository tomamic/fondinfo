#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d

with open("palette.txt", "w") as new_file:
    print('''180 120 60\n120 180 60\n120 60 180''', file=new_file);

palette = []
with open('palette.txt', 'r') as palette_file:
    for line in palette_file:
        if len(line) > 0:
            vals = line.split()
            color = (int(vals[0]), int(vals[1]), int(vals[2]))
            palette.append(color)

side = 400.0
g2d.init_canvas((int(side), int(side)))

n = int(g2d.prompt('squares? '))
delta = side / n

for i in range(n):
    g2d.set_color(palette[i % len(palette)])
    g2d.fill_rect((0, 0, int(side), int(side)))
    side -= delta

g2d.main_loop()
