#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import sys; sys.path.append("../")
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
        return None


class Frog(Actor):
    def __init__(self, pos: (int, int)):
        self._x0, self._y0 = pos
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 0, 0
        self._speed, self._steps, self._count = 4, 6, 0

    def move(self, arena):
        if arena.collisions():
            self._x, self._y = self._x0, self._y0
            self._count = 0

        if self._count > 0:
            self._count -= 1
            self._x += self._dx
            self._y += self._dy
        else:
            length = self._speed * self._steps  # total jump length
            arena_w, arena_h = arena.size()
            keys = arena.current_keys()
            u, l, d, r = "wasd"
            if l in keys and self._x - length >= 0:
                self._count = self._steps
                self._dx, self._dy = -self._speed, 0
            elif r in keys and self._x + length <= arena_w - self._w:
                self._count = self._steps
                self._dx, self._dy = self._speed, 0
            elif u in keys and self._y - length >= 0:
                self._count = self._steps
                self._dx, self._dy = 0, -self._speed
            elif d in keys and self._y + length <= arena_h - self._h:
                self._count = self._steps
                self._dx, self._dy = 0, self._speed

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20


def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        if a.sprite():
            g2d.draw_image("sprites.png", a.pos(), a.sprite(), a.size())
        else:
            g2d.draw_rect(a.pos(), a.size())
    arena.tick(g2d.current_keys())

def main():
    global g2d, arena
    import g2d
    arena = Arena((480, 360))
    arena.spawn(Frog((240, 120)))
    arena.spawn(Vehicle((48, 48), 4))
    arena.spawn(Vehicle((72, 72), -4))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
