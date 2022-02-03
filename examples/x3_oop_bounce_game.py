#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randrange
from p3_oop_bounce import Actor, Arena, Ball, Ghost, Turtle

def randpt(w: int, h: int) -> (int, int):
    x, y = randrange(w), randrange(h)
    while (x - w // 2) ** 2 + (y - h // 2) ** 2 < 100 ** 2:
        x, y = randrange(w), randrange(h)
    return x, y

class BounceGame:
    def __init__(self, size=(480, 360), nballs=3, nghosts=2, secs=120):
        self._arena = Arena(size)
        w, h = size[0] - 20, size[1] - 20
        self._arena.spawn(Turtle((w // 2, h // 2)))  # center
        for _ in range(nballs):
            self._arena.spawn(Ball(randpt(w, h)))
        for _ in range(nghosts):
            self._arena.spawn(Ghost(randpt(w, h)))
        self._time = secs * 30  # 120 seconds
        self._lives = 1

    def tick(self, keys=tuple()):
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
