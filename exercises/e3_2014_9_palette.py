#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame

palette = []
with open('palette.txt', 'r') as f:
    for line in f:
        vals = line.split()
        color = (int(vals[0]), int(vals[1]), int(vals[2]))
        palette.append(color)

n = int(input('squares? '))

side = 400.0
delta = side / n

pygame.init()
w = pygame.display.set_mode((int(side), int(side)))

for i in range(n):
    color = palette[i % len(palette)]
    pygame.draw.rect(w, color, (0, 0, int(side), int(side)))
    side -= delta

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
