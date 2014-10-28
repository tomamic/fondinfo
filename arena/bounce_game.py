#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
from arena import Character, Arena
from bounce import Ball, Ghost, Turtle

arena = Arena(320, 240)
Ball(arena, 40, 80)
Ball(arena, 80, 40)
Ghost(arena, 120, 80)
turtle = Turtle(arena, 80, 80)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(arena.size())
background = (255, 255, 255)
images = {Ball: pygame.image.load('ball.bmp'),
          Ghost: pygame.image.load('ghost.bmp'),
          Turtle: pygame.image.load('turtle.bmp')}

playing = True
while playing:
    for e in pygame.event.get():
        # print(e)
        if e.type == pygame.QUIT:
            playing = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                turtle.go_up()
            elif e.key == pygame.K_DOWN:
                turtle.go_down()
            elif e.key == pygame.K_LEFT:
                turtle.go_left()
            elif e.key == pygame.K_RIGHT:
                turtle.go_right()
        elif e.type == pygame.KEYUP:
            turtle.stay()

    arena.move_all()  # Game logic

    screen.fill(background)
    for c in arena.characters():
        x, y, w, h = c.rect()
        img = images[type(c)]
        screen.blit(img, (x, y))

    pygame.display.flip()
    clock.tick(30)

