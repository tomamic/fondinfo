#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

W, H = 480, 360

class Vehicle:
    def __init__(self, pos: (int, int), dx: int):
        self._x = pos[0]
        self._y = pos[1]
        self._w, self._h = 20, 20
        self._dx = dx
        self._left, self._right = -100, W + 100

    def move(self):
        if self._x + self._dx < self._left:
            self._x = self._right
        if self._x + self._dx > self._right:
            self._x = self._left
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
    b = Vehicle((40, 40), 5)
    g2d.init_canvas((W, H))
    g2d.main_loop(tick)

##main()
