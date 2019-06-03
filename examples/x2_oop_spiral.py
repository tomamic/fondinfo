#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d, math

ARENA_W, ARENA_H = 600, 600

class Spiral:
    def __init__(self):
        self._w = math.pi / 32  # angular velocity
        self._i = 0
        self._n = 256

    def move(self):
        self._i = (self._i + 1) % self._n

    def center(self):
        x = int(ARENA_W // 2 + self._i * math.cos(self._i * self._w))
        y = int(ARENA_H // 2 + self._i * math.sin(self._i * self._w))
        return x, y

    def radius(self):
        return self._i // 2

    def color(self):
        return (255 - self._i, 0, self._i)

def tick():
    g2d.clear_canvas()
    a.move()
    g2d.set_color(a.color())
    g2d.fill_circle(a.center(), a.radius())

def main():
    global a
    a = Spiral()
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
