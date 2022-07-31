#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena

class Vehicle(Actor):
    def __init__(self, pos: (int, int), dx: int):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx = dx

    def move(self, arena):
        arena_w, arena_h = arena.size()
        margin, width = arena_w // 2, arena_w * 2
        self._x += self._dx
        if self._x < -margin:
            self._x += width
        if self._x >= arena_w + margin:
            self._x -= width

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0

    def collide(self, other, arena):
        pass

class Frog(Actor):
    def __init__(self, pos: (int, int)):
        self._x0, self._y0 = pos
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 0, 0
        self._speed, self._steps, self._count = 2, 10, 0

    def move(self, arena):
        keys = arena.current_keys()
        if "a" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = -self._speed, 0
        elif "d" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = +self._speed, 0
        elif "w" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = 0, -self._speed
        elif "s" in keys and self._count == 0:
            self._count = self._steps
            self._dx, self._dy = 0, +self._speed

        if self._count > 0:
            self._count -= 1

            x = self._x + self._dx
            y = self._y + self._dy
            
        arena_w, arena_h = arena.size()
        self._x = min(max(x, 0), arena_w - self._w)
        self._y = min(max(y, 0), arena_h - self._h)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0

    def collide(self, other, arena):
        self._x, self._y = self._x0, self._y0


def tick():
    arena.tick(g2d.current_keys())
    g2d.clear_canvas()
    for a in arena.actors():
        g2d.fill_rect(a.pos(), a.size())

def main():
    global arena, frog
    arena = Arena((480, 360))
    arena.spawn(Frog((230, 340)))
    arena.spawn(Vehicle((40, 40), 5))
    arena.spawn(Vehicle((80, 80), -5))
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
