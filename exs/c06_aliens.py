#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d

W, H = 480, 360

class Alien:
    def __init__(self, pos: (int, int)):
        self._x, self._y = pos
        # TODO: give each alien its own moving space, e.g. 150px
        # self._xmin, self._xmax = ...
        self._dx, self._dy = 5, 5

    def move(self):
        # TODO: use the alien’s own limits
        if 0 <= self._x + self._dx <= W - 20:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy

    def pos(self):
        return self._x, self._y


def tick():
    g2d.clear_canvas()
    for a in aliens:
        g2d.draw_image("ball.png", a.pos())
        a.move()

def main():
    global aliens, W, H
    aliens = [Alien((40, 40)), Alien((80, 40)), Alien((60, 80))]
    g2d.init_canvas((W, H))
    g2d.main_loop(tick, 10)

if __name__ == "__main__":
    main()
