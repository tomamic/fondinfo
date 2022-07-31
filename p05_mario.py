#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from random import choice, randrange
from actor import Actor, Arena


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


class Mario(Actor):

    def __init__(self, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed, self._max_speed, self._gravity = 4, 8, 0.4
        self._landed = False

    def move(self, arena):
        keys = arena.current_keys()
        if self._landed and "w" in keys and "w" not in arena.previous_keys():
            self._dy = -self._max_speed
            self._landed = False

        if "a" in keys:
            self._dx = -self._speed
        elif "d" in keys:
            self._dx = self._speed
        else:
            self._dx = 0

        self._x += self._dx
        self._y += self._dy

        if not self._landed:
            self._dy = min(self._dy + self._gravity, self._max_speed)
        self._landed = False

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)  # clamp
        self._y = min(max(self._y, 0), ah - self._h)  # clamp

    def collide(self, other, arena):
        if isinstance(other, Wall):
            sx, sy, sw, sh = self.pos() + self.size()  # self's pos
            ox, oy, ow, oh = other.pos() + other.size()  # other's pos

            # move to the nearest border: left, right, top or bottom
            dx = min(ox - sx - sw, ox + ow - sx, key=abs)
            dy = min(oy - sy - sh, oy + oh - sy, key=abs)
            if abs(dx) < abs(dy):
                self._x += dx
            else:
                self._y += dy
                self._dy = 1
                self._landed = dy < 0

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20


def tick():
    arena.tick(g2d.current_keys())  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if isinstance(a, Wall):
            g2d.draw_rect(a.pos(), a.size())
        else:
            g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())

arena = Arena((320, 240))
arena.spawn(Mario(80, 80))
arena.spawn(Wall(200, 80, 80, 20))
arena.spawn(Wall(120, 160, 80, 20))
arena.spawn(Wall(0, 220, 320, 20))

g2d.init_canvas(arena.size())
g2d.main_loop(tick)
