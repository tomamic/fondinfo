#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *
from random import choice, randrange
from actor import *


class Jumper(Actor):
    W, H = 20, 20
    SPEED = 4
    MAX_SPEED = 8
    GRAVITY = 0.4

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if not self._landed:
            self._dy += self.GRAVITY
            self._dy = min(self._dy, self.MAX_SPEED)

        self._landed = False

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self.W:
            self._x = arena_w - self.W

    def jump(self):
        if self._landed:
            self._dy = -self.MAX_SPEED
            self._landed = False
        
    def go_left(self):
        self._dx = -self.SPEED
        
    def go_right(self):
        self._dx = +self.SPEED

    def stay(self):
        self._dx = 0

    def collide(self, other):
        if isinstance(other, Wall):
            bx, by, bw, bh = self.rect()  # ball's pos
            wx, wy, ww, wh = other.rect() # wall's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))
            self._x += move[0]
            self._y += move[1]
            if move[1] != 0:
                self._dy = 1
            if move[1] < 0:
                self._landed = True
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 20


class Mario(Jumper):
    pass


class Goomba(Jumper):
    def move(self):
        r = randrange(30)
        if r == 0:
            self.go_left()
        elif r == 1:
            self.go_right()
        elif r == 2:
            self.jump()
        Jumper.move(self)

    def symbol(self):
        return 20, 0


class Wall(Actor):

    def __init__(self, arena, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0


def update():
    arena.move_all()  # Game logic

    canvas_fill(canvas, (255, 255, 255))
    for a in arena.actors():
        if isinstance(a, Wall):
            draw_rect(canvas, (127, 127, 127), a.rect())
        else:
            x, y, w, h = a.rect()
            xs, ys = a.symbol()
            image_blit(canvas, sprites, (x, y), area=(xs, ys, w, h))

def keydown(e):
    if e.code == "Space":
        mario.jump()
    elif e.code == "ArrowLeft":
        mario.go_left()
    elif e.code == "ArrowRight":
        mario.go_right()

def keyup(e):
    if e.code in ("ArrowLeft", "ArrowRight"):
        mario.stay()

arena = Arena(320, 240)
mario = Mario(arena, 80, 80)
Goomba(arena, 180, 80)
Goomba(arena, 150, 80)
Wall(arena, 200, 80, 80, 20)
Wall(arena, 120, 160, 80, 20)
Wall(arena, 0, 220, 320, 20)

canvas = canvas_init(arena.size())
sprites = image_load("sprites.png")

doc.onkeydown = keydown
doc.onkeyup = keyup
set_interval(update, 1000 // 30)  # millis
    
