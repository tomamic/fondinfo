#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
from arena import Character, Arena
from ball import Ball, Ghost

arena = Arena(16, 12)
Ball(arena, 4, 8)
Ball(arena, 8, 4)
Ghost(arena, 12, 8)

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
    for y in range(arena.height):
        for x in range(arena.width):
            symbol = arena.get_symbol(x, y)
            if symbol in images:
                i = images[symbol]
                screen.blit(i, (x * TILE_SIDE, y * TILE_SIDE))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

