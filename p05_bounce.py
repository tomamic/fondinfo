#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import choice, randrange
from actor import Actor, Arena

class Ball(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 4
        self._dx, self._dy = self._speed, self._speed

    def move(self, arena: Arena):
        for other in arena.collisions():
            if not isinstance(other, Ghost):
                x, y = other.pos()
                if x < self._x:
                    self._dx = self._speed
                else:
                    self._dx = -self._speed
                if y < self._y:
                    self._dy = self._speed
                else:
                    self._dy = -self._speed

        arena_w, arena_h = arena.size()
        if self._x + self._dx < 0:
            self._dx = self._speed
        elif self._x + self._dx > arena_w - self._w:
            self._dx = -self._speed
        if self._y + self._dy < 0:
            self._dy = self._speed
        elif self._y + self._dy > arena_h - self._h:
            self._dy = -self._speed
        self._x += self._dx
        self._y += self._dy

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 0


class Ghost(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._visible = True

    def move(self, arena: Arena):
        aw, ah = arena.size()
        dx = choice([-4, 0, 4])
        dy = choice([-4, 0, 4])
        self._x = (self._x + dx) % aw
        self._y = (self._y + dy) % ah

        if randrange(100) == 0:
            self._visible = not self._visible
        if randrange(1000) == 0:
            arena.spawn(Ball(self.pos()))

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        if self._visible:
            return 20, 0
        return 20, 20

    def visible(self):
        return self._visible

class Turtle(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._dx, self._dy = 0, 0
        self._w, self._h = 20, 20
        self._speed = 2

    def move(self, arena: Arena):
        for other in arena.collisions():
            if isinstance(other, Ball):
                self.hit(arena)

        keys = arena.current_keys()
        self._dx = self._dy = 0
        if "ArrowUp" in keys:
            self._dy = -self._speed
        elif "ArrowDown" in keys:
            self._dy = self._speed
        if "ArrowLeft" in keys:
            self._dx = -self._speed
        elif "ArrowRight" in keys:
            self._dx = self._speed
        self._x += self._dx
        self._y += self._dy

        aw, ah = arena.size()
        self._x = min(max(self._x, 0), aw - self._w)  # clamp
        self._y = min(max(self._y, 0), ah - self._h)  # clamp

    def hit(self, arena: Arena):
        arena.kill(self)

    def pos(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def sprite(self):
        return 0, 20


def tick():
    g2d.clear_canvas()
    for a in arena.actors():
        if a.sprite() != None:
            g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())
        else:
            pass  # g2d.draw_rect(a.pos(), a.size())

    arena.tick(g2d.current_keys())  # Game logic


def main():
    global g2d, arena
    import g2d  # game classes do not depend on g2d

    arena = Arena((480, 360))
    arena.spawn(Ball((40, 80)))
    arena.spawn(Ball((80, 40)))
    arena.spawn(Ghost((120, 80)))
    arena.spawn(Turtle((80, 80)))

    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

if __name__ == "__main__":
    main()  # call main to start the program
