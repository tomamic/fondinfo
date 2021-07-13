#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d
from random import randrange
canvas_w, canvas_h, ball_w, ball_h = 480, 360, 20, 20

class Ball:
    def __init__(self):
        self._dx, self._dy = 5, 0
        self._x = randrange(canvas_w - ball_w)
        self._y = randrange(canvas_h - ball_h)

    def move(self):
        if self._x + self._dx > canvas_w - ball_w:
            self._x = canvas_w - ball_w
            self._dx, self._dy = 0, 5
        elif self._x + self._dx < 0:
            self._x = 0
            self._dx, self._dy = 0, -5
        elif self._y + self._dy > canvas_h - ball_h:
            self._y = canvas_h - ball_h
            self._dx, self._dy = -5, 0
        elif self._y + self._dy < 0:
            self._y = 0
            self._dx, self._dy = 5, 0
        self._x += self._dx
        self._y += self._dy

    def position(self) -> (int, int):
        return self._x, self._y

def tick():
    b.move()
    g2d.clear_canvas()
    g2d.draw_image("ball.png", b.position())

b = Ball()
g2d.init_canvas((canvas_w, canvas_h))
g2d.main_loop(tick)
