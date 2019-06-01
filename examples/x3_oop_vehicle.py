#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena

class Vehicle(Actor):
    def __init__(self, arena, pos: (int, int), dx: int):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._margin = 100
        self._dx = dx
        self._arena = arena
        arena.add(self)

    def move(self):
        aw, ah = self._arena.size()
        if self._x + self._dx < -self._margin:
            self._x = aw + self._margin
        if self._x + self._dx > aw + self._margin:
            self._x = -self._margin
        self._x += self._dx

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0

    def collide(self, other):
        pass

def tick():
    g2d.clear_canvas()
    arena.move_all()
    for a in arena.actors():
        g2d.fill_rect(a.position())

def main():
    global arena
    arena = Arena((480, 360))
    Vehicle(arena, (40, 40), 5)
    Vehicle(arena, (80, 80), -5)
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
