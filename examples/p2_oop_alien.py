#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

class Alien:
    def __init__(self, x0: int, y0: int):
        self._x, self._y = x0, y0
        self._w, self._h = 20, 20
        self._xmin, self._xmax = x0, x0 + 150
        self._dx, self._dy = 5, 5

    def move(self):
        if self._xmin <= self._x + self._dx <= self._xmax:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self._dy

    def position(self):
        return self._x, self._y, self._w, self._h

def update():
    g2d.fill_canvas((255, 255, 255))
    a.move()
    g2d.draw_rect((127, 127, 127), a.position())

def main():
    global a
    a = Alien(40, 40)
    g2d.init_canvas((320, 240))
    g2d.main_loop(update, 1000 // 30)

##main()  # call main to start the program
