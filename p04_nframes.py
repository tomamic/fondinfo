#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self, pos: (int, int)):
        self._x, self._y = pos
        self._dx, self._dy = 2, 2
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
        if self._count == 0:
            self._count = 10

    def pos(self) -> (int, int):
        return self._x, self._y

def tick():
    g2d.clear_canvas()  # BG
    g2d.draw_image("ball.png", b1.pos())  # FG
    g2d.draw_image("ball.png", b2.pos())  # FG

    if "1" in g2d.current_keys():
        b1.start()
    if "2" in g2d.current_keys():
        b2.start()
    b1.move()
    b2.move()

def main():
    global b1, b2
    b1 = Ball((40, 80))
    b2 = Ball((80, 40))
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
