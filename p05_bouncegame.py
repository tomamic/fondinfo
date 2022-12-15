#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randrange
from p05_bounce import Actor, Arena, Ball, Ghost, Turtle

def randpt(w: int, h: int) -> (int, int):
    x, y = randrange(w - 20), randrange(h - 20)
    while (x - w // 2) ** 2 + (y - h // 2) ** 2 < 100 ** 2:
        x, y = randrange(w - 20), randrange(h - 20)
    return x, y

class TurtleHero(Turtle):
    def __init__(self, pos):
        super().__init__(pos)
        self._lives = 3
        self._blinking = 0

    def move(self, arena: Arena):
        super().move(arena)
        if self._blinking > 0:
            self._blinking -= 1

    def collide(self, other: Actor, arena: Arena):
        if self._blinking == 0:
            self._blinking = 60
            if isinstance(other, Ball):
                self._lives -= 1
        if self._lives <= 0:
            arena.kill(self)

    def lives(self) -> int:
        return self._lives

    def sprite(self):
        if self._blinking > 0 and self._blinking % 4 < 2:
            return None
        return super().sprite()


class BounceGame:
    def __init__(self, size=(480, 360), nballs=3, nghosts=2, secs=120):
        self._arena = Arena(size)
        w, h = size
        self._arena.spawn(TurtleHero((w // 2, h // 2)))  # center
        for _ in range(nballs):
            self._arena.spawn(Ball(randpt(w, h)))
        for _ in range(nghosts):
            self._arena.spawn(Ghost(randpt(w, h)))
        self._time = secs * 30  # 120 seconds
        self._lives = 1

    def tick(self, keys=[]):
        self._arena.tick(keys)
        self._time -= 1
        self._lives = 0
        for a in self._arena.actors():
            if isinstance(a, Turtle):
                self._lives = a.lives()

    def size(self) -> (int, int):
        return self._arena.size()

    def actors(self) -> [Actor]:
        return self._arena.actors()

    def game_over(self) -> bool:
        return self._lives <= 0

    def game_won(self) -> bool:
        return self._time <= 0

    def lives(self) -> int:
        return self._lives

    def time(self) -> int:
        return self._time // 30