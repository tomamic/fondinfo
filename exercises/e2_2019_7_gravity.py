#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from random import randrange
canvas_w, canvas_h = 480, 360

class Ball:
    def __init__(self):
        self._w, self._h = 20, 20
        self._dx, self._dy = randrange(-5, 6), 0
        self._x = randrange(canvas_w - self._w)
        self._y = randrange(canvas_h - self._h)
        self._r, self._g, self._b = randrange(256), randrange(256), randrange(256)

    def move(self):
        if not (0 <= self._x + self._dx <= canvas_w - self._w):
            self._dx *= -1
        if not (0 <= self._y + self._dy <= canvas_h - self._h):
            self._dy *= -1
        else:
            self._dy += 0.4

        self._x += self._dx
        self._y += self._dy

    def color(self) -> (int, int, int):
        return self._r, self._g, self._b

    def position(self) -> (int, int):
        return self._x, int(self._y)

    def size(self) -> (int, int):
        return self._w, self._h


def tick():
    g2d.clear_canvas()
    for b in balls:
        b.move()
        g2d.set_color(b.color())
        g2d.fill_rect(b.position(), b.size())

balls = [Ball(), Ball(), Ball()]
g2d.init_canvas((canvas_w, canvas_h))
g2d.main_loop(tick)
