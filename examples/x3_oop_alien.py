#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d, random
from actor import Actor, Arena

class Alien(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._xmin, self._xmax = self._x, self._x + 150
        self._dx, self._dy = 5, 5

    def act(self, arena):
        if self._xmin <= self._x + self._dx <= self._xmax:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0

    def collide(self, other, arena):
        if isinstance(other, Bullet):
            arena.kill(self)


class Bullet(Actor):
    def __init__(self, x0: int):
        self._w, self._h = 5, 10
        self._x, self._y = x0, arena.size()[1] - self._h
        self._dy = -5

    def act(self, arena):
        self._y += self._dy
        if self._y < 0:
            arena.kill(self)

    def collide(self, other, arena):
        if isinstance(other, Alien):
            arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0


def tick():
    g2d.clear_canvas()
    if random.randrange(50) == 0:
        arena.spawn(Bullet(random.randrange(arena.size()[0])))
    arena.tick()
    for a in arena.actors():
        g2d.fill_rect(a.pos(), a.size())

def main():
    global arena
    arena = Arena((320, 240))
    arena.spawn(Alien((40, 40)))
    arena.spawn(Alien((80, 80)))
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
