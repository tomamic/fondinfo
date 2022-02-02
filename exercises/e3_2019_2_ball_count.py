#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d
from random import randrange
ARENA_W, ARENA_H = 480, 360
BALL_W, BALL_H = 20, 20

class TurningBall:
    def __init__(self):
        self._w, self._h = 20, 20
        self._dx, self._dy = 5, 0
        self._count = 0
        self._x = randrange(ARENA_W - BALL_W - 50)
        self._y = randrange(ARENA_H - BALL_H - 50)
    def move(self):
        self._x += self._dx
        self._y += self._dy

        self._count += 1
        if self._count == 10:
            self._dx, self._dy = -self._dy, self._dx  # rot 90°
            self._count = 0
    def pos(self) -> (int, int):
        return self._x, self._y

def tick():
    g2d.clear_canvas()
    b1.move()
    b2.move()
    g2d.draw_image("../examples/ball.png", b1.pos())
    g2d.draw_image("../examples/ball.png", b2.pos())

b1, b2 = TurningBall(), TurningBall()
g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(tick)
