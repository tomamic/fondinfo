#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from time import time
from p3_oop_bounce import Actor, Arena, Ball, Ghost, Turtle


class BounceGame:
    def __init__(self):
        self._arena = Arena((480, 360))
        Ball(self._arena, (40, 80))
        Ball(self._arena, (80, 40))
        Ghost(self._arena, (120, 80))
        self._hero = Turtle(self._arena, (80, 80))
        self._playtime = 120  # seconds

    def arena(self) -> Arena:
        return self._arena

    def hero(self) -> Turtle:
        return self._hero

    def game_over(self) -> bool:
        return self._hero.lives() <= 0

    def game_won(self) -> bool:
        return self.remaining_time() <= 0

    def remaining_time(self) -> int:
        return (self._playtime - self._arena.count() // 30)
