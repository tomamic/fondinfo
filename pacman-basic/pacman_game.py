#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
from arena import *
from pacman import *
from pacman_map import *

arena = Arena(232, 256)

for x, y, w, h in walls_pos:
    Wall(arena, x, y, w, h)
for x, y in cookies_pos:
    Cookie(arena, x, y)
for x, y in powers_pos:
    Power(arena, x, y)

pacman = PacMan(arena, 112, 184)
Ghost(arena, 112, 88)
Ghost(arena, 112, 88)
Ghost(arena, 112, 88)
Ghost(arena, 112, 88)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(arena.size())
background = pygame.image.load('pacman_background.png')
sprites = pygame.image.load('pacman_sprites.png')

playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                pacman.go_up()
            elif e.key == pygame.K_DOWN:
                pacman.go_down()
            elif e.key == pygame.K_LEFT:
                pacman.go_left()
            elif e.key == pygame.K_RIGHT:
                pacman.go_right()

    arena.move_all()  # Game logic

    screen.blit(background, (0, 0))
    for a in arena.actors():
        if not isinstance(a, Wall):
            x, y, w, h = a.rect()
            xs, ys = a.symbol()
            screen.blit(sprites, (x, y), area=(xs, ys, w, h))

    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()

