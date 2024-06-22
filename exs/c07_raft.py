#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
from actor import Actor, Arena

class Raft(Actor):
    def __init__(self, x, y, dx):
        self._x, self._y = x, y
        self._w, self._h = 60, 20
        self._dx = dx

    def move(self, arena):
        aw, ah = arena.size()
        margin, width = aw // 2, aw * 2
        self._x += self._dx
        if self._x < -margin:
            self._x += width
        if self._x >= aw + margin:
            self._x -= width

    def speed(self):
        return self._dx

    def pos(self):
        return self._x, self._y

    def size(self):
        return 60, 20

    def sprite(self):
        return None


class Frog(Actor):
    def __init__(self, x, y):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._dx, self._dy, self._drift = 0, 0, 0
        self._count, self._steps = 0, 6
        self._speed = 4

    def move(self, arena):
        raft = False
        for other in arena.collisions():
            if isinstance(other, Raft) and self._count == 0:
                raft = True
                self._drift = other.speed()
                self._x += self._drift

        if self._count > 0:
            self._count -= 1
            self._x += self._dx + self._drift
            self._y += self._dy
        else:
            if not raft:
                self._drift = 0
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
    arena.spawn(Raft(360, 48, -4))
    arena.spawn(Raft(360, 72, 4))
    arena.spawn(Frog(240, 96))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
