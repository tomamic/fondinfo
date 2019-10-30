#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena

class Background(Actor):
    def __init__(self, arena, y, h, ys, speed):
        self._x, self._y, self._ys = 0, y, ys
        self._w, self._h = 512, h
        self._speed = speed
        self._arena = arena
        arena.add(self)

    def move(self):
        self._x -= self._speed
        if self._x + self._w < 0:
            self._x += self._w

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, self._ys, self._w, self._h

arena = Arena((480, 360))
back = Background(arena, 120, 128, 256, 2)
sprites = g2d.load_image("moon-patrol.png")
bg = g2d.load_image("moon-patrol-bg.png")

def tick():
    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if isinstance(a, Background):
            ax, ay, aw, ah = a.position()
            g2d.draw_image_clip(bg, a.symbol(), (ax, ay, aw, ah))
            g2d.draw_image_clip(bg, a.symbol(), (ax+aw, ay, aw, ah))
        elif a.symbol() != (0, 0, 0, 0):
            g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
