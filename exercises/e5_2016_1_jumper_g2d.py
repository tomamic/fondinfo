#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d
from random import choice, randrange
from actor import Actor, Arena


class Turtle(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed = 4
        self._landed = False

    def move(self, arena):
        keys = arena.current_keys()
        if "w" in keys and self._landed:
            self._dy = -self._speed * 2
            self._landed = False

        if "a" in keys:
            self._dx = -self._speed
        elif "d" in keys:
            self._dx = +self._speed
        else:
            self._dx = 0

        arena_w, arena_h = arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h
            self._landed = True

        if not self._landed:
            self._dy += 0.3

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def collide(self, other, arena):
        pass

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20


def tick():
    arena.tick(g2d.current_keys())  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())

def main():
    global arena, turtle

    arena = Arena((320, 240))
    arena.spawn(Turtle((80, 80)))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
