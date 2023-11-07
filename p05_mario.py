#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena

class Jumpy(Actor):
    def __init__(self):
        self._x, self._y = 0, 240
        self._w, self._h = 20, 20
        self._dx, self._dy = 4, 0
        self._jump = -16

    def move(self, arena):
        for other in arena.collisions():
            other_x, other_y = other.pos()
            if self._dy >= 0 and self._y < other_y:
                self._y = other_y - self._h
                self._dy = 0
                if "ArrowUp" in arena.current_keys():
                    self._dy = self._jump  # jump

        arena_w, arena_h = arena.size()
        self._x = (self._x + self._dx) % arena_w
        self._y = self._y + self._dy
        self._dy += 1  # gravity

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20


class Wall(Actor):
    def __init__(self, pos, size):
        self._pos = pos
        self._size = size

    def move(self, arena):
        return

    def pos(self):
        return self._pos

    def size(self):
        return self._size

    def sprite(self):
        return None


def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_rect(a.pos(), a.size())

    arena.tick(g2d.current_keys())


arena = Arena((640, 480))
arena.spawn(Wall((240, 350), (100, 40)))
arena.spawn(Wall((420, 250), (100, 40)))
arena.spawn(Wall((0, 460), (640, 20)))
arena.spawn(Jumpy())

g2d.init_canvas(arena.size())
g2d.main_loop(tick)
