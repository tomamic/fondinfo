#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena


class Wall(Actor):
    def __init__(self, pos, size):
        self._pos = pos
        self._size = size

    def move(self, arena):
        return

    def pos(self):
        return self._pos

    def size(self):
        return self._size

    def sprite(self):
        return None


class Mario(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed, self._max_speed, self._gravity = 2, 4, 0.1

    def move(self, arena):
        keys = arena.current_keys()
        for other in arena.collisions():
            if isinstance(other, Wall):
                sx, sy, sw, sh = self.pos() + self.size()  # self's pos
                ox, oy, ow, oh = other.pos() + other.size()  # other's pos

                # move to the nearest border: left, right, top or bottom
                dx = min(ox - sx - sw, ox + ow - sx, key=abs)
                dy = min(oy - sy - sh, oy + oh - sy, key=abs)
                if abs(dx) < abs(dy):
                    self._x += dx
                else:
                    if dy != 0:
                        self._y += dy
                        self._dy = 0
                    if sy < oy and "w" in keys:  # if on top, can jump
                        self._dy = -self._max_speed

        if "a" in keys:
            self._dx = -self._speed
        elif "d" in keys:
            self._dx = self._speed
        else:
            self._dx = 0

        self._x += self._dx
        self._y += self._dy

        self._dy = min(self._dy + self._gravity, self._max_speed)

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)  # clamp

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20


def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        if a.sprite():
            g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())
        else:
            g2d.draw_rect(a.pos(), a.size())

    arena.tick(g2d.current_keys())  # Game logic

arena = Arena((320, 240))
arena.spawn(Mario((80, 80)))
arena.spawn(Wall((200, 80), (80, 20)))
arena.spawn(Wall((120, 160), (80, 20)))
arena.spawn(Wall((0, 220), (320, 20)))

g2d.init_canvas(arena.size())
g2d.main_loop(tick, 60)
