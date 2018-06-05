#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d
from random import choice, randrange
from actor import Actor, Arena


class Jumper(Actor):
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed = 4
        self._max_speed = 8
        self._gravity = 0.4
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if not self._landed:
            self._dy += self._gravity
            self._dy = min(self._dy, self._max_speed)

        self._landed = False

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w

    def jump(self):
        if self._landed:
            self._dy = -self._max_speed
            self._landed = False

    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = +self._speed

    def stay(self):
        self._dx = 0

    def collide(self, other):
        if isinstance(other, Wall):
            bx, by, bw, bh = self.position()  # ball's pos
            wx, wy, ww, wh = other.position() # wall's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))
            self._x += move[0]
            self._y += move[1]
            if move[1] != 0:
                self._dy = 1
            if move[1] < 0:
                self._landed = True

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 20, self._w, self._h


class Mario(Jumper):
    pass


class CrazyGoomba(Jumper):
    def move(self):
        # random move, just as an example
        # implement your desired behaviour here

        r = randrange(30)
        if r == 0:
            self.go_left()
        elif r == 1:
            self.go_right()
        elif r == 2:
            self.jump()
        Jumper.move(self)

    def symbol(self):
        return 20, 0, self._w, self._h


class Wall(Actor):

    def __init__(self, arena, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0, self._w, self._h


def update():
    arena.move_all()  # Game logic

    g2d.fill_canvas((255, 255, 255))
    for a in arena.actors():
        if isinstance(a, Wall):
            g2d.draw_rect((127, 127, 127), a.position())
        else:
            g2d.draw_image_clip(sprites, a.position(), a.symbol())

def keydown(code):
    if code == "Space":
        mario.jump()
    elif code == "ArrowLeft":
        mario.go_left()
    elif code == "ArrowRight":
        mario.go_right()

def keyup(code):
    if code in ("ArrowLeft", "ArrowRight"):
        mario.stay()

arena = Arena(320, 240)
mario = Mario(arena, 80, 80)
CrazyGoomba(arena, 180, 80)
CrazyGoomba(arena, 150, 80)
Wall(arena, 200, 80, 80, 20)
Wall(arena, 120, 160, 80, 20)
Wall(arena, 0, 220, 320, 20)

g2d.init_canvas(arena.size())
sprites = g2d.load_image("sprites.png")

g2d.handle_keyboard(keydown, keyup)
g2d.main_loop(update, 1000 // 30)  # millis

