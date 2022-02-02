#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import choice, randrange
from time import time
from actor import Actor, Arena

class Ball(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 4
        self._dx, self._dy = self._speed, self._speed

    def move(self, arena: Arena):
        arena_w, arena_h = arena.size()
        if self._x + self._dx < 0:
            self._dx = self._speed
        if  self._x + self._dx + self._w > arena_w:
            self._dx = -self._speed
        if self._y + self._dy < 0:
            self._dy = self._speed
        if  self._y + self._dy + self._h > arena_h:
            self._dy = -self._speed
        self._x += self._dx
        self._y += self._dy

    def collide(self, other: Actor, arena: Arena):
        if not isinstance(other, Ghost):
            x, y = other.pos()
            if x < self._x:
                self._dx = self._speed
            else:
                self._dx = -self._speed
            if y < self._y:
                self._dy = self._speed
            else:
                self._dy = -self._speed

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0


class Ghost(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._visible = True

    def move(self, arena: Arena):
        aw, ah = arena.size()
        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % aw
        self._y = (self._y + dy) % ah

        if randrange(100) == 0:
            self._visible = not self._visible

    def collide(self, other: Actor, arena: Arena):
        pass

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        if self._visible:
            return 20, 0
        return 20, 20

    def visible(self):
        return self._visible

class Turtle(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed = 2
        self._lives = 3
        self._blinking = 0

    def move(self, arena: Arena):
        keys = arena.current_keys()
        self._dx = self._dy = 0
        if "ArrowUp" in keys:
            self._dy = -self._speed
        elif "ArrowDown" in keys:
            self._dy = self._speed
        if "ArrowLeft" in keys:
            self._dx = -self._speed
        elif "ArrowRight" in keys:
            self._dx = self._speed
        self._x += self._dx
        self._y += self._dy

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)  # clamp
        self._y = min(max(self._y, 0), ah - self._h)  # clamp
        if self._blinking > 0:
            self._blinking -= 1

    def collide(self, other: Actor, arena: Arena):
        if self._blinking == 0:
            self._blinking = 60
            if isinstance(other, Ghost):
                if other.visible():
                    self._lives = 0
                else:
                    self._lives += 1
                    arena.spawn(Ball((self._x + 100, self._y + 100)))
            elif isinstance(other, Ball):
                self._lives -= 1
        if self._lives <= 0:
            arena.kill(self)

    def lives(self) -> int:
        return self._lives

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        if self._blinking > 0 and self._blinking % 4 <= 2:
            return None
        return 0, 20


def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.pos())


def main():
    arena = Arena((480, 360))
    arena.spawn(Ball((40, 80)))
    arena.spawn(Ball((80, 40)))
    arena.spawn(Ghost((120, 80)))

    for i in range(25):
        print_arena(arena)
        arena.move_all()

##main()  # call main to start the program


