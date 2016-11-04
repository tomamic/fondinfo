#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *
from random import choice, randrange
from actor import *


class Turtle(Actor):
    W, H = 20, 20
    SPEED = 4

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self.H:
            self._y = arena_h - self.H
            self._landed = True

        if not self._landed:
            self._dy += 0.3

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self.W:
            self._x = arena_w - self.W

    def jump(self):
        if self._landed:
            self._dy = -self.SPEED * 2
            self._landed = False
        
    def go_left(self):
        self._dx = -self.SPEED
        
    def go_right(self):
        self._dx = +self.SPEED

    def stay(self):
        self._dx = 0

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 20

  
def update():
    arena.move_all()  # Game logic

    canvas_fill(canvas, (255, 255, 255))
    for a in arena.actors():
        x, y, w, h = a.rect()
        xs, ys = a.symbol()
        image_blit(canvas, sprites, (x, y), area=(xs, ys, w, h))

def keydown(e):
    if e.code == "Space":
        turtle.jump()
    elif e.code == "ArrowLeft":
        turtle.go_left()
    elif e.code == "ArrowRight":
        turtle.go_right()

def keyup(e):
    if e.code in ("ArrowLeft", "ArrowRight"):
        turtle.stay()

arena = Arena(320, 240)
turtle = Turtle(arena, 80, 80)

canvas = canvas_init(arena.size())
sprites = image_load("sprites.png")

doc.onkeydown = keydown
doc.onkeyup = keyup
set_interval(update, 1000//30)  # millis
    
