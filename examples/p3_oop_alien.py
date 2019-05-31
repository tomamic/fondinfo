#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena

class Alien(Actor):
    def __init__(self, arena, pos: (int, int)):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._xmin, self._xmax = x0, x0 + 150
        self._dx, self._dy = 5, 5
        self._arena = arena
        arena.add(self)

    def move(self):
        if self._xmin <= self._x + self._dx <= self._xmax:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy

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
    arena = Arena((320, 240))
    Alien(arena, (40, 40))
    Alien(arena, (80, 80))
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
