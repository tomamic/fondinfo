#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d
from random import choice, randrange
from actor import Actor, Arena

class Ball(Actor):
    W, H = 20, 20
    SPEED = 5

    def __init__(self, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = self.SPEED, self.SPEED

    def move(self, arena):
        arena_w, arena_h = arena.size()
        if not (0 <= self._x + self._dx <= arena_w - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= arena_h - self.H):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def collide(self, other, arena):
        if isinstance(other, Wall):
            bx, by, bw, bh = self.pos() + self.size()  # ball's rect
            wx, wy, ww, wh = other.pos() + other.size()  # wall's rect
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            dx, dy = min(borders_distance, key=lambda m: abs(sum(m)))
            self._x += dx
            self._y += dy

    def pos(self):
        return self._x, self._y

    def size(self):
        return self.W, self.H

    def sprite(self):
        return 0, 0


class Wall(Actor):

    def __init__(self, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h

    def move(self, arena):
        pass

    def collide(self, other, arena):
        pass

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0


def tick():
    arena.tick()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if isinstance(a, Wall):
            g2d.fill_rect(a.pos(), a.size())
        else:
            g2d.draw_image_clip("../examples/sprites.png", a.pos(), a.sprite(), a.size())

def main():
    global arena, sprites
    arena = Arena((320, 240))
    arena.spawn(Ball(40, 80))
    arena.spawn(Ball(85, 40))
    arena.spawn(Wall(115, 80, 100, 20))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
