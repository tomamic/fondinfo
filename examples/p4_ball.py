#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys

class Ball:
    ARENA_WIDTH = 16
    ARENA_HEIGHT = 12

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = +1
        self._dy = +1
        
    def move(self):
        if not (0 <= self._x + self._dx < Ball.ARENA_WIDTH):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy < Ball.ARENA_HEIGHT):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def position(self) -> (int, int):
        return (self._x, self._y)


if __name__ == '__main__':
    # Create two objects, instances of the Ball class
    b1 = Ball(4, 8)
    b2 = Ball(8, 4)
    print('Ball 1 @', b1.position())
    print('Ball 2 @', b2.position())

    for line in sys.stdin:
        b1.move()
        b2.move()
        print('Ball 1 @', b1.position())
        print('Ball 2 @', b2.position())
