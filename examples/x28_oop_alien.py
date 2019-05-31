#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

class Alien:
    def __init__(self, pos: (int, int)):
        self._x = pos[0]
        self._y = pos[1]
        self._w, self._h = 20, 20
        self._xmin, self._xmax = self._x, self._x + 150
        self._dx, self._dy = 5, 5

    def move(self):
        if self._xmin <= self._x + self._dx <= self._xmax:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy

    def position(self):
        return self._x, self._y, self._w, self._h

def tick():
    g2d.clear_canvas()
    a.move()
    g2d.fill_rect(a.position())

def main():
    global a
    a = Alien((40, 40))
    g2d.init_canvas((480, 360))
    g2d.main_loop(tick, 10)

main()  # call main to start the program
