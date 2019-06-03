#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from actor import Actor, Arena
from random import choice, randrange

class Wall(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 100, 20
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0, 0, 0


class Mario(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed, self._g = 5, 0.5
        self._dx, self._dy = 0, 0
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
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
        self._dy += self._g

    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = +self._speed

    def jump(self):
        if self._landed:
            self._dy = -2 * self._speed
            self._landed = False

    def stay(self):
        self._dx = 0

    def collide(self, other):
        if isinstance(other, Wall):
            x1, y1, w1, h1 = self.position()  # self's pos
            x2, y2, w2, h2 = other.position() # wall's pos
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0),
                       (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
            move = min(borders)  # find nearest border: ← → ↑ ↓
            self._x += move[1] * move[0]  ## sign_dx * distance
            self._y += move[2] * move[0]  ## sign_dy * distance
            if move[2] < 0:
                self._landed = True
            if move[2] != 0:
                self._dy = 1

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 20, self._w, self._h


arena = Arena((480, 360))
w1 = Wall(arena, (300, 300))
w2 = Wall(arena, (80, 240))
hero = Mario(arena, (230, 170))
sprites = g2d.load_image("sprites.png")

def tick():
    if g2d.key_pressed("ArrowUp"):
        hero.jump()
    elif g2d.key_pressed("ArrowRight"):
        hero.go_right()
    elif g2d.key_pressed("ArrowLeft"):
        hero.go_left()
    elif (g2d.key_released("ArrowLeft") or
          g2d.key_released("ArrowRight")):
        hero.stay()

    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if a.symbol() != (0, 0, 0, 0):
            g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
