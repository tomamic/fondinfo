#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
pygame.init()                     # Prepare pygame
screen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()       # To set game speed

x = 50; playing = True
while playing:
    for e in pygame.event.get():  # Handle events: mouse, keyb etc.
        if e.type == pygame.QUIT: playing = False
    screen.fill((255, 255, 255))  # Draw background, and then foreground
    pygame.draw.rect(screen, (127, 127, 127), (x, 50, 20, 20))
    x = (x + 5) % 320             # Update ball's position
    pygame.display.flip()         # Surface ready, show it!
    clock.tick(30)                # Wait 1/30 seconds
pygame.quit()                     # Close the window
