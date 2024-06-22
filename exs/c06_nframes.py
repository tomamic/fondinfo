#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from random import choice, randrange

ARENA_W, ARENA_H, BALL_W, BALL_H = 400, 400, 20, 20

class Ghost:
    def __init__(self):
        self._x, self._y = ARENA_W // 2, ARENA_H // 2
        self._dx, self._dy = 0, 0
        self._count = 0

    def move(self):
        if self._count > 0:
            self._x = (self._x + self._dx) % ARENA_W
            self._y = (self._y + self._dy) % ARENA_H
            self._count -= 1
        elif randrange(100) == 0:
            self._count = 10
            self._dx = choice([-4, 0, 4])
            self._dy = choice([-4, 0, 4])

    def pos(self) -> tuple[int, int]:
        return self._x, self._y

    def sprite(self) -> tuple[int, int]:
        if self._count > 0:
            return 20, 20  # transparent, while moving
        return 20, 0  # visible

    def size(self) -> tuple[int, int]:
        return 20, 20


def tick():
    g2d.clear_canvas()
    g2d.draw_image("sprites.png", g1.pos(), g1.sprite(), g1.size())
    g1.move()

def main():
    global g1
    g1 = Ghost()
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
