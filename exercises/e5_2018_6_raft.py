#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append("../examples")
import g2d
from actor import Actor, Arena


class Ball(Actor):
    def __init__(self, arena, x, y, dx):
        self._x, self._y = x, y
        self._w, self._h = 60, 20
        self._dx = dx
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        margin, width = arena_w // 2, arena_w * 2
        self._x += self._dx
        if self._x < -margin:
            self._x += width
        if self._x >= arena_w + margin:
            self._x -= width

    def collide(self, other):
        pass

    def speed(self):
        return self._dx

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 0


class Turtle(Actor):
    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._w, self._h = 20, 20
        self._speed = 4
        self._dx, self._dy = 0, 0
        self._raft = None
        self._count = 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if self._count > 0:
            self._y += self._dy
            if self._y < 0:
                self._y = 0
            elif self._y > arena_h - self._h:
                self._y = arena_h - self._h

            self._x += self._dx
            if self._x < 0:
                self._x = 0
            elif self._x > arena_w - self._w:
                self._x = arena_w - self._w
            self._count -= 1
        elif self._raft != None:
            self._x += self._raft.speed()
        self._raft = None

    def control(self, pressed):
        u, d, l, r = "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"
        #u, d, l, r = "w", "s", "a", "d"
        if self._count == 0:
            if u in pressed:
                self._count = 5
                self._dx, self._dy = 0, -self._speed
            if d in pressed:
                self._count = 5
                self._dx, self._dy = 0, +self._speed
            if l in pressed:
                self._count = 5
                self._dx, self._dy = -self._speed, 0
            if r in pressed:
                self._count = 5
                self._dx, self._dy = +self._speed, 0

    def collide(self, other):
        if isinstance(other, Ball) and self._count == 0:
            self._raft = other

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 0, 20

###


arena = Arena((320, 240))
b1 = Ball(arena, 40, 60, 5)
b2 = Ball(arena, 80, 40, -5)
turtle = Turtle(arena, 80, 80)

def tick():
    turtle.control(g2d.pressed_keys())

    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if a.size() != (20, 20):
            g2d.fill_rect(a.position(), a.size())
        else:
            g2d.draw_image_clip(sprites, a.symbol(), a.size(), a.position())

def main():
    global sprites
    g2d.init_canvas(arena.size())
    sprites = g2d.load_image("../examples/sprites.png")
    g2d.main_loop(tick)

main()
