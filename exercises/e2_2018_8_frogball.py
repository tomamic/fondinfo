#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d

ARENA_W, ARENA_H = 320, 240
BALL_W, BALL_H = 20, 20

class FrogBall:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
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


def update():
    g2d.clear_canvas()  # BG
    b1.move()
    b2.move()
    g2d.draw_image(img, b1.position())  # FG
    g2d.draw_image(img, b2.position())  # FG

def keydn(code: str):
    if code == "ArrowLeft":
        b1.go()
    elif code == "ArrowRight":
        b2.go()

def main():
    global b1, b2, img
    b1 = FrogBall(40, 80)
    b2 = FrogBall(80, 40)
    g2d.init_canvas((ARENA_W, ARENA_H))
    img = g2d.load_image("ball.png")
    g2d.handle_events(update, keydn, None)
    g2d.main_loop(5)

main()
