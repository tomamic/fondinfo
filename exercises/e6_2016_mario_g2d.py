#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from random import choice, randrange
from actor import Actor, Arena


class Jumper(Actor):
    def __init__(self, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed = 4
        self._max_speed = 8
        self._gravity = 0.4
        self._landed = False

    def move(self, arena):
        arena_w, arena_h = arena.size()
        self._y += self._dy
        if not self._landed:
            self._dy += self._gravity
            self._dy = min(self._dy, self._max_speed)

        self._landed = False

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def collide(self, other, arena):
        if isinstance(other, Wall):
            bx, by = self.pos()  # ball's pos
            bw, bh = self.size()
            wx, wy = other.pos() # wall's pos
            ww, wh = other.size()
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))
            self._x += move[0]
            self._y += move[1]
            if move[1] != 0:
                self._dy = 1
            if move[1] < 0:
                self._landed = True

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20


class Mario(Jumper):
    def move(self, arena):
        keys = arena.current_keys()
        if "w" in keys and self._landed:
            self._dy = -self._max_speed
            self._landed = False

        if "a" in keys:
            self._dx = -self._speed
        elif "d" in keys:
            self._dx = self._speed
        else:
            self._dx = 0

        Jumper.move(self, arena)


class CrazyGoomba(Jumper):
    def move(self, arena):
        # random move, just as an example
        # implement your desired behaviour here

        r = randrange(30)
        if r == 0:
            self._dx = -self._speed
        elif r == 1:
            self._dx = self._speed
        elif r == 2 and self._landed:
            self._dy = -self._max_speed
            self._landed = False
        Jumper.move(self, arena)

    def sprite(self):
        return 20, 0


class Wall(Actor):

    def __init__(self, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h

    def move(self, arena):
        pass

    def collide(self, other, arena):
        pass

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0


def tick():
    arena.tick(g2d.current_keys())  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if isinstance(a, Wall):
            g2d.fill_rect(a.pos(), a.size())
        else:
            g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())

arena = Arena((320, 240))
arena.spawn(Mario(80, 80))
arena.spawn(CrazyGoomba(180, 80))
arena.spawn(CrazyGoomba(150, 80))
arena.spawn(Wall(200, 80, 80, 20))
arena.spawn(Wall(120, 160, 80, 20))
arena.spawn(Wall(0, 220, 320, 20))

g2d.init_canvas(arena.size())
g2d.main_loop(tick)
