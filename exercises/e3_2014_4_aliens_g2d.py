#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d

class Alien:
    SPEED = 5
    W, H = 20, 20
    PATH_W = 150

    def __init__(self, x0: int, y0: int):
        self._x = x0
        self._y = y0
        self._xmin = x0
        self._dx = self.SPEED

    def move(self):
        xmax = self._xmin + self.PATH_W - self.W
        if self._xmin <= self._x + self._dx <= xmax:
            self._x += self._dx
        else:
            self._dx = -self._dx
            self._y += self.SPEED

    def rect(self):
        return self._x, self._y, self.W, self.H


def update():
    game2d.canvas_fill((255, 255, 255))  # Draw background 

    for a in aliens:
        a.move()                # Apply game logic
                                # Draw foreground
        game2d.draw_rect((127, 127, 127), a.rect())

aliens = [Alien(40, 40), Alien(80, 80), Alien(120, 40)]
game2d.canvas_init((320, 240))
game2d.set_interval(update, 1000 // 30)  # Millis
