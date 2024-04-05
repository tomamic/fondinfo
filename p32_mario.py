#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import g2d
from actor import Actor, Arena
from math import hypot

class Mario(Actor):
    def __init__(self):
        self._x, self._y = 0, 240
        self._w, self._h = 20, 20
        self._dx, self._dy = 0, 0
        self._speed, self._jump = 2, -8
        self._gravity = 0.25

    def move(self, arena):
        self._dx = 0
        if "ArrowRight" in arena.current_keys():
             self._dx = self._speed
        elif "ArrowLeft" in arena.current_keys():
             self._dx = -self._speed
        for other in arena.collisions():
            wall_x, wall_y = other.pos()
            wall_w, wall_h = other.size()
            if self._y < wall_y and self._dy >= 0:
                self._y = wall_y - self._h  # ⤓ landed
                self._dy = 0
                if "ArrowUp" in arena.current_keys():
                    self._dy = self._jump  # jump
            elif self._y + self._h > wall_y + wall_h and self._dy <= 0:
                self._y = wall_y + wall_h + 1  # ⤒
                self._dy = 0
            elif self._x < wall_x and self._dx >= 0:
                self._x = wall_x - self._w  # ⇥
                self._dx = 0
            elif self._x + self._w > wall_x + wall_w and self._dx <= 0:
                self._x = wall_x + wall_w  # ⇤
                self._dx = 0

        arena_w, arena_h = arena.size()
        self._x = (self._x + self._dx) % arena_w
        self._y += self._dy
        self._dy += self._gravity

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return None


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
arena.spawn(Mario())

g2d.init_canvas(arena.size())
g2d.main_loop(tick)
