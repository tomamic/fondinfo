#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d, math
from p03_polar import move_around

W, H = 500, 500

class Spiral:
    def __init__(self, center):
        self._center = center
        self._n, self._i = 256, 0
        self._v = 4 * math.pi / self._n  # angular velocity

    def move(self):
        self._i = (self._i + 1) % self._n

    def pos(self):
        i, v, center = self._i, self._v, self._center
        return move_around(center, 25 + i * 0.4, i * v)

    def radius(self):
        return self._i * 0.4

    def color(self):
        return (255 - self._i, 0, self._i)

def tick():
    g2d.clear_canvas()
    g2d.set_color(a.color())
    g2d.draw_circle(a.pos(), a.radius())
    a.move()

def main():
    global a
    a = Spiral((W / 2, H / 2))
    g2d.init_canvas((W, H))
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()
