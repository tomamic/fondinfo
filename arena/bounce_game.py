#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
from arena import *
from bounce import *

arena = Arena(320, 240)
Ball(arena, 40, 80)
Ball(arena, 80, 40)
Ghost(arena, 120, 80)
turtle = Turtle(arena, 80, 80)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(arena.size())
background = (255, 255, 255)
images = {Ball: pygame.image.load('ball.png'),
          Ghost: pygame.image.load('ghost.png'),
          Turtle: pygame.image.load('turtle.png')}

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
    for a in arena.actors():
        x, y, w, h = a.rect()
        img = images[type(a)]
        screen.blit(img, (x, y))
        # use the following lines to cut a sprite from a larger image
        # xs, ys = a.symbol()
        # screen.blit(img, (x, y), area=(xs, ys, w, h))

    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()

