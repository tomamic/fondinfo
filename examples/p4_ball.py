#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Ball:
    W, H = 20, 20
    ARENA_W, ARENA_H = 320, 240

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 5

    def move(self):
        if not (0 <= self._x + self._dx <= self.ARENA_W - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= self.ARENA_H - self.H):
            self._dy = -self._dy

        self._x += self._dx
        self._y += self._dy

    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self.W, self.H


def main():
    # Create two objects, instances of the Ball class
    b1 = Ball(40, 80)
    b2 = Ball(80, 40)
    print("Ball 1 @", b1.rect())
    print("Ball 2 @", b2.rect())

    while input() != "x":
        b1.move()
        b2.move()
        print("Ball 1 @", b1.rect())
        print("Ball 2 @", b2.rect())
        
if __name__ == "__main__":
    main()
