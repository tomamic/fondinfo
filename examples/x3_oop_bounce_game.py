#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from p3_oop_bounce import Actor, Arena, Ball, Ghost, Turtle


class BounceGame:
    def __init__(self):
        self._arena = Arena((480, 360))
        self._arena.spawn(Ball((40, 80)))
        self._arena.spawn(Ball((80, 40)))
        self._arena.spawn(Ghost((120, 80)))
        self._arena.spawn(Turtle((80, 80)))
        self._time = 120 * 30  # 120 seconds

    def tick(self, keys=tuple()):
        self._arena.tick(keys)
        self._time -= 1

    def size(self) -> (int, int):
        return self._arena.size()

    def actors(self) -> [Actor]:
        return self._arena.actors()

    def game_over(self) -> bool:
        return self.lives() <= 0

    def game_won(self) -> bool:
        return self._time <= 0

    def lives(self) -> int:
        lives = 0
        for a in self._arena.actors():
            if isinstance(a, Turtle):
                lives = a.lives()
        return lives

    def time(self) -> int:
        return self._time // 30
