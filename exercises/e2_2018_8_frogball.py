#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d


ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class FrogBall:
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx = 5
        self._dy = 5
        self._count = 0

    def move(self):
        if self._count > 0:
            self._x = (self._x + self._dx) % ARENA_W
            self._y = (self._y + self._dy) % ARENA_H
            self._count -= 1

    def position(self) -> (int, int, int, int):
        return self._x, self._y, BALL_W, BALL_H

    def go(self):
        if self._count == 0:
            self._count = 5

b1 = FrogBall((40, 80))
b2 = FrogBall((80, 40))

def tick():
    if g2d.key_pressed("1"):
        b1.go()
    elif g2d.key_pressed("2"):
        b2.go()
    g2d.clear_canvas()  # BG
    b1.move()
    b2.move()
    g2d.draw_image("../examples/ball.png", b1.position())  # FG
    g2d.draw_image("../examples/ball.png", b2.position())  # FG

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick, 10)

main()
