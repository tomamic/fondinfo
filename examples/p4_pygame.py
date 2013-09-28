#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
from p4_arena import Character, Arena, Ball, Ghost

arena = Arena()
arena.add(Ball(4, 8))
arena.add(Ball(8, 4))
arena.add(Ball(12, 4))
arena.add(Ghost(12, 8))

TILE_SIDE = 20
SCREEN_SIZE = (arena.width * TILE_SIDE, arena.height * TILE_SIDE)
BACKGROUND = (255, 255, 255)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
images = {Ball.SYMBOL: pygame.image.load('ball.bmp'),
          Ghost.SYMBOL: pygame.image.load('ghost.bmp')}
# if img size ≠ 20x20: pygame.transform.scale

playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = False

    arena.move_all()  # Game logic
        
    screen.fill(BACKGROUND)
    for c in arena.characters:
        x, y = c.position
        p = (x * TILE_SIDE, y * TILE_SIDE)
        if c.symbol in images:
            i = images[c.symbol]
            screen.blit(i, p)
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

