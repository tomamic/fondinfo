#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

ARENA_W, ARENA_H = 480, 360
BALL_W, BALL_H = 20, 20

class Ball:
    def __init__(self, pos: (int, int)):
        self._x = pos[0]
        self._y = pos[1]
        self._dx = 5
        self._dy = 5

    def move(self):
        if not (0 <= self._x + self._dx <= ARENA_W - BALL_W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_H - BALL_H):
            self._dy = -self._dy

        self._x += self._dx
        self._y += self._dy

    def position(self) -> (int, int, int, int):
        return self._x, self._y, BALL_W, BALL_H


def main():
    # Create two objects, instances of the Ball class
    b1 = Ball((140, 180))
    b2 = Ball((180, 140))

    for i in range(25):
        print("b1 @", b1.position(), "b2 @", b2.position())
        b1.move()
        b2.move()

##main()  # call main to start the program
