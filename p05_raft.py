#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from actor import Actor, Arena


class Raft(Actor):
    def __init__(self, x, y, dx):
        self._x, self._y = x, y
        self._w, self._h = 60, 20
        self._dx = dx

    def move(self, arena):
        arena_w, arena_h = arena.size()
        margin, width = arena_w // 2, arena_w * 2
        self._x += self._dx
        if self._x < -margin:
            self._x += width
        if self._x >= arena_w + margin:
            self._x -= width

    def speed(self):
        return self._dx

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0


class Frog(Actor):
    def __init__(self, x, y):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._speed = 4
        self._dx, self._dy = 0, 0
        self._dragging = 0
        self._count, self._steps = 0, 5

    def move(self, arena):
        for other in arena.collisions(self):
            if isinstance(other, Raft) and self._count == 0:
                self._dragging = other.speed()

        keys = arena.current_keys()
        u, d, l, r = "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"
        #u, d, l, r = "w", "s", "a", "d"
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
            self._y += self._dy
            self._x += self._dx
            self._count -= 1
        self._x += self._dragging
        self._dragging = 0

        arena_w, arena_h = arena.size()
        self._x = min(max(0, self._x), arena_w - self._w)
        self._y = min(max(0, self._y), arena_h - self._h)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20

###


arena = Arena((320, 240))
arena.spawn(Raft(40, 60, 5))
arena.spawn(Raft(80, 40, -5))
arena.spawn(Frog(80, 80))

def tick():
    arena.tick(g2d.current_keys())  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if a.size() != (20, 20):
            g2d.draw_rect(a.pos(), a.size())
        else:
            g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())

def main():
    global sprites
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
