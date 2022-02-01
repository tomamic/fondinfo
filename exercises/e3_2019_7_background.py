#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from actor import Actor, Arena

class Background(Actor):
    def __init__(self, y, h, ys, speed):
        self._x, self._y, self._ys = 0, y, ys
        self._w, self._h = 512, h
        self._speed = speed

    def act(self, arena):
        self._x -= self._speed
        if self._x + self._w < 0:
            self._x += self._w

    def collide(self, other, arena):
        pass

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, self._ys


arena = Arena((480, 360))
arena.spawn(Background(120, 128, 256, 2))
bg = "https://raw.githubusercontent.com/tomamic/tomamic.github.io/master/images/sprites/moon-patrol-bg.png"

def tick():
    arena.tick()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if isinstance(a, Background):
            ax, ay = a.pos()
            aw, ah = a.size()
            g2d.draw_image_clip(bg, (ax, ay), a.sprite(), a.size())
            g2d.draw_image_clip(bg, (ax+aw, ay), a.sprite(), a.size())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
