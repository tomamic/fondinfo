#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from actor import Actor, Arena

tile = 24

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
        self._speed = 4
        self._dx, self._dy = 0, 0
        self._dragging = 0
        self._count, self._steps = 0, 6

    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, Raft) and self._count == 0:
                self._dragging = other.speed()

        keys = arena.current_keys()
        u, l, d, r = "wasd"
        if self._count == 0:
            if u in keys:
                self._count = self._steps
                self._dx, self._dy = 0, -self._speed
            if d in keys:
                self._count = self._steps
                self._dx, self._dy = 0, +self._speed
            if l in keys:
                self._count = self._steps
                self._dx, self._dy = -self._speed, 0
            if r in keys:
                self._count = self._steps
                self._dx, self._dy = +self._speed, 0

        if self._count > 0:
            self._count -= 1
            self._y += self._dy
            self._x += self._dx
        self._x += self._dragging
        self._dragging = 0

        aw, ah = arena.size()
        self._x = min(max(0, self._x), (aw - self._w) // tile * tile)
        self._y = min(max(0, self._y), (ah - self._h) // tile * tile)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20

###


arena = Arena((20*tile, 15*tile))
arena.spawn(Raft(15*tile, 2*tile, -4))
arena.spawn(Raft(15*tile, 3*tile, 4))
arena.spawn(Frog(10*tile, 4*tile))

def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        if a.sprite():
            g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())
        else:
            g2d.draw_rect(a.pos(), a.size())

    arena.tick(g2d.current_keys())  # Game logic

def main():
    global sprites
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
