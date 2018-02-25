#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d

from actor import Arena, Actor
from random import randrange

class Ball(Actor):
    def __init__(self, arena):
        self._speed = 5
        self._g = 0.5
        self._w, self._h = 20, 20
        self._safety = 15
        arena_w, arena_h = arena.size()
        self._x = randrange(arena_w - self._w)
        self._y = randrange(arena_h - self._h)
        self._dx, self._dy = randrange(self._speed), 0
        self._count = 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x + self._dx <= arena_w - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= arena_h - self._h):
            self._dy = -self._dy
        else:
            self._dy += self._g
        self._x += self._dx
        self._y += self._dy

        if self._count > 0:
            self._count -= 1

    def collide(self, other):
        if self._count == 0:
            self._dx = -self._dx
            self._count = self._safety

    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0, self._w, self._h


def update():
    arena.move_all()  # Game logic

    g2d.fill_canvas((255, 255, 255))
    for a in arena.actors():
        g2d.draw_image_clip(sprites, a.rect(), a.symbol())

def keyup(code):
    print(code + " up")
    turtle.stay()

def main():
    global arena, turtle, sprites

    arena = Arena(320, 240)
    for i in range(5):
        Ball(arena)

    g2d.init_canvas(arena.size())
    sprites = g2d.load_image("sprites.png")
    g2d.main_loop(update, 1000//30)  # millis

main()
