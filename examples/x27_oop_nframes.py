#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self, pos: (int, int)):
        self._x = pos[0]
        self._y = pos[1]
        self._dx = 5
        self._dy = 5
        self._count = 0

    def move(self):
        if self._count > 0:
            if not (0 <= self._x + self._dx <= ARENA_W - BALL_W):
                self._dx = -self._dx
            if not (0 <= self._y + self._dy <= ARENA_H - BALL_H):
                self._dy = -self._dy

            self._x += self._dx
            self._y += self._dy
            self._count -= 1

    def start(self):
        self._count = 5

    def position(self) -> (int, int, int, int):
        return self._x, self._y, BALL_W, BALL_H

def tick():
    if g2d.key_pressed("1"):
        b1.start()
    if g2d.key_pressed("2"):
        b2.start()
    g2d.clear_canvas()  # BG
    b1.move()
    b2.move()
    g2d.fill_rect(b1.position())  # FG
    g2d.fill_rect(b2.position())  # FG

def main():
    global b1, b2
    b1 = Ball((40, 80))
    b2 = Ball((80, 40))
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
