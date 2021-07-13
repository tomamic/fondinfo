#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from random import randrange
canvas_w, canvas_h, ball_w, ball_h = 480, 360, 20, 20

class TurningBall:
    def __init__(self):
        self._dx, self._dy = 5, 0
        self._count = 0
        self._x = randrange(canvas_w - ball_w)
        self._y = randrange(canvas_h - ball_h)

    def move(self):
        self._x += self._dx
        self._y += self._dy
        self._count += 1
        if self._count == 10:
            self._dx, self._dy = self._dy, -self._dx  # rot 90°
            self._count = 0

    def position(self) -> (int, int):
        return self._x, self._y

def tick():
    b.move()
    g2d.clear_canvas()
    g2d.draw_image("ball.png", b.position())

b = TurningBall()
g2d.init_canvas((canvas_w, canvas_h))
g2d.main_loop(tick)
