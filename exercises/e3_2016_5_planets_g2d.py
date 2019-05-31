#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d
import math
import random

class Planet:

    def __init__(self, orbit):
        self._orbit = orbit
        self._theta = random.uniform(0, math.pi * 2)
        self._omega = random.uniform(0.01, 0.04)
        self._diameter = random.randint(10, 20)
        self._color = (random.randrange(256),
                       random.randrange(256),
                       random.randrange(256))

    def pos(self):
        x = self._orbit * math.cos(self._theta)
        y = self._orbit * math.sin(self._theta)
        return int(x), int(y)

    def move(self):
        self._theta += self._omega

    def diameter(self):
        return self._diameter

    def color(self):
        return self._color


def tick():
    center_x, center_y = canvas_w // 2, canvas_h // 2
    g2d.clear_canvas()
    g2d.set_color((255, 255, 0))
    g2d.fill_circle((center_x, center_y), 30)
    for p in planets:
        p.move()
        x, y = p.pos()
        radius = p.diameter() // 2
        g2d.set_color(p.color())
        g2d.fill_circle((center_x + x, center_y + y), radius)

def main():
    global planets, canvas_w, canvas_h

    planets = []  # ex.: try to use a list comprehension
    for i in range(5):
        p = Planet(100 + i * 40)
        planets.append(p)

    canvas_w, canvas_h = 600, 600
    g2d.init_canvas((canvas_w, canvas_h))
    g2d.main_loop(tick)

main()
