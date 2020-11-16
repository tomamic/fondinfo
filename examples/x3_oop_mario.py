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
        self._x, self._y, self._w, self._h = pos
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
            wall_x, wall_y, wall_w, wall_h = other.position()
            x, y, w, h = self.position()
            previous_x, previous_y = x - self._dx, y - self._dy

            if previous_x + w <= wall_x:
                self._x = wall_x - w
            elif previous_x >= wall_x + wall_w:
                self._x = wall_x + wall_w
            elif previous_y + h <= wall_y:
                self._y, self._dy = wall_y - h, 1
                self._landed = True
            #elif previous_y >= wall_y + wall_h:
            #    self._y, self._dy = wall_y + wall_h, 1

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 20, self._w, self._h


arena = Arena((480, 360))
w1 = Wall(arena, (300, 300, 100, 20))
w2 = Wall(arena, (80, 240, 100, 20))
w2 = Wall(arena, (380, 220, 20, 80))
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
