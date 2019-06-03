#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena
from x3_oop_vehicle import Vehicle

class Frog(Actor):
    def __init__(self, arena, pos: (int, int)):
        self._x0, self._y0 = pos
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 0, 0
        self._speed, self._steps, self._count = 4, 8, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        if self._count > 0:
            self._count -= 1

            arena_w, arena_h = self._arena.size()
            self._y += self._dy
            if self._y < 0:
                self._y = 0
            elif self._y > arena_h - self._h:
                self._y = arena_h - self._h

            self._x += self._dx
            if self._x < 0:
                self._x = 0
            elif self._x > arena_w - self._w:
                self._x = arena_w - self._w

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0

    def collide(self, other):
        self._x, self._y = self._x0, self._y0

    def jump_left(self):
        if self._count == 0:
            self._count = self._steps
            self._dx, self._dy = -self._speed, 0

    def jump_right(self):
        if self._count == 0:
            self._count = self._steps
            self._dx, self._dy = +self._speed, 0

    def jump_up(self):
        if self._count == 0:
            self._count = self._steps
            self._dx, self._dy = 0, -self._speed

    def jump_down(self):
        if self._count == 0:
            self._count = self._steps
            self._dx, self._dy = 0, +self._speed

def tick():
    if g2d.key_pressed("ArrowUp"):
        frog.jump_up()
    elif g2d.key_pressed("ArrowRight"):
        frog.jump_right()
    elif g2d.key_pressed("ArrowDown"):
        frog.jump_down()
    elif g2d.key_pressed("ArrowLeft"):
        frog.jump_left()

    g2d.clear_canvas()
    arena.move_all()
    for a in arena.actors():
        g2d.fill_rect(a.position())

def main():
    global arena, frog
    arena = Arena((480, 360))
    frog = Frog(arena, (230, 340))
    Vehicle(arena, (40, 40), 5)
    Vehicle(arena, (80, 80), -5)
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
