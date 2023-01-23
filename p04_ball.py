#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20

class Ball:
    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._dx, self._dy = 5, 5

    def move(self):
        if not 0 <= self._x + self._dx <= ARENA_W - BALL_W:
            self._dx = -self._dx
        if not 0 <= self._y + self._dy <= ARENA_H - BALL_H:
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def pos(self) -> (int, int):
        return self._x, self._y


def console_run():
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)

    b1.move()
    b2.move()

    print("b1 @", b1.pos())
    print("b2 @", b2.pos())

def tick():
    g2d.clear_canvas()  # BG
    g2d.draw_image("ball.png", b1.pos())  # FG
    g2d.draw_image("ball.png", b2.pos())  # FG
    b1.move()
    b2.move()

def main():
    global b1, b2, g2d
    import g2d  # Ball does not depend on g2d
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)

    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

##main()
