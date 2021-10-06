#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena
from random import choice, randrange

class Wall(Actor):
    def __init__(self, arena, rect):
        self._x, self._y, self._w, self._h = rect
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 0


class Mario(Actor):
    def __init__(self, arena, pos, delta=(0, 0)):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed, self._g = 5, 0.5
        self._dx, self._dy = delta
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        self._landed = False
        arena_w, arena_h = self._arena.size()
        self._dy += self._g

        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h
            self._landed = True

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def control(self, keys: set):
        if "w" in keys and self._landed:
            self._dy = -2 * self._speed
            self._landed = False

        if "a" in keys:
            self._dx = -self._speed
        elif "d" in keys:
            self._dx = +self._speed
        else:
            self._dx = 0

    def collide(self, other):
        if isinstance(other, Wall):
            wall_x, wall_y = other.position()
            wall_w, wall_h = other.size()
            x, y = self.position()
            w, h = self.size()
            previous_x, previous_y = x - self._dx, y - self._dy

            if previous_x + w <= wall_x:
                self._x = wall_x - w
            elif previous_x >= wall_x + wall_w:
                self._x = wall_x + wall_w
            elif previous_y + h <= wall_y:
                self._y, self._dy = wall_y - h, 1
                self._landed = True
            elif previous_y >= wall_y + wall_h:
                self._y, self._dy = wall_y + wall_h, 1

    def position(self):
        return self._x, int(self._y)

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 20


arena = Arena((480, 360))
w1 = Wall(arena, (300, 300, 100, 20))
w2 = Wall(arena, (80, 240, 100, 20))
w2 = Wall(arena, (380, 220, 20, 80))
hero = Mario(arena, (230, 170))
sprites = g2d.load_image("sprites.png")

def tick():
    hero.control(g2d.current_keys())
    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if not isinstance(a, Wall):
            g2d.draw_image_clip(sprites, a.symbol(), a.size(), a.position())
        else:
            g2d.fill_rect(a.position(), a.size())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
