#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

W, H, MARGIN = 480, 360, 100

class Ball:
    def __init__(self, x0: int, y0: int):
        self._x, self._y = x0, y0
        self._w, self._h = 20, 20
        self._dx = 5

    def move(self):
        if self._x + self._dx < -MARGIN:
            self._x = W + MARGIN
        if self._x + self._dx > W + MARGIN:
            self._x = -MARGIN
        self._x += self._dx

    def uturn(self):
        self._dx *= -1

    def position(self):
        return self._x, self._y, self._w, self._h


def tick():
    if g2d.key_pressed("Enter"):
        b.uturn()
    g2d.clear_canvas()
    b.move()
    g2d.fill_rect(b.position())

def main():
    global b
    b = Ball(40, 40)
    g2d.init_canvas((W, H))
    g2d.main_loop(tick)

main()
