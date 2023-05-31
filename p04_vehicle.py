#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

ARENA_W, ARENA_H = 480, 360

class Vehicle:
    def __init__(self, pos: (int, int), dx: int):
        self._x, self._y = pos
        self._dx = dx
        self._left, self._right = -100, ARENA_W + 100

    def move(self):
        if self._x + self._dx < self._left:
            self._x = self._right
        if self._x + self._dx > self._right:
            self._x = self._left
        self._x += self._dx

    def uturn(self):
        self._dx *= -1

    def pos(self):
        return self._x, self._y

    def size(self):
        return 20, 20

    def sprite(self):
        return 20, 0


def tick():
    g2d.clear_canvas()
    g2d.draw_image("ball.png", v.pos())
    if g2d.mouse_clicked():
        v.uturn()
    v.move()

def main():
    global g2d, v
    import g2d  # Vehicle does not depend on g2d

    v = Vehicle((40, 40), 5)
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
