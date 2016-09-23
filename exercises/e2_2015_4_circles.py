#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame

n = int(input('Circles? '))

SIDE = 600
pygame.init()
w = pygame.display.set_mode((SIDE, SIDE))

center = SIDE // 2, SIDE // 2
delta_radius = SIDE / (2 * n)
delta_color = 0
if n > 1:
    delta_color = 255.0 / (n - 1)

for i in range(n):
    radius = int(SIDE // 2 - i * delta_radius)
    color = int(255.0 - i * delta_color)
    pygame.draw.circle(w, (color, 0, 0), center, radius)

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
