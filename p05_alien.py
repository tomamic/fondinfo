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
        # TODO: give each alien its own moving space, e.g. 150px
        # self._xmin, self._xmax = ...
        self._dx, self._dy = 5, 5

    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, Bullet):
                arena.kill(self)
        # TODO: use the alien's own limits
        aw, ah = arena.size()
        if 0 <= self._x + self._dx <= aw:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy

    def pos(self):
        return self._x, self._y

    def size(self):
        return 20, 20

    def sprite(self):
        return 0, 0


class Bullet(Actor):
    def __init__(self, pos: "tuple[int, int]"):
        self._x, self._y = pos
        # ...

    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, Alien):
                arena.kill(self)

        self._y -= 5
        if self._y < 0:
            arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return 5, 10

    def sprite(self):
        return 0, 0


def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_rect(a.pos(), a.size())
    if arena.count() % 40 == 0:
        aw, ah = arena.size()
        arena.spawn(Bullet((aw / 2, ah)))
    arena.tick()

def main():
    global arena
    arena = Arena((320, 240))
    arena.spawn(Alien((40, 40)))
    arena.spawn(Alien((80, 80)))
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
