#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys; sys.path.append('../examples/')
import g2d
from actor import Actor, Arena

class FallingBall(Actor):
    W, H = 20, 20

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 0
        self._g = 0.3

    def act(self, arena: Arena):
        aw, ah = arena.size()
        if not (0 <= self._x + self._dx <= aw - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ah - self.H):
            self._dy = -self._dy
        else:
            self._dy += self._g

        self._x += self._dx
        self._y += self._dy

    def collide(self, other: Actor, arena: Arena):
        return

    def pos(self) -> (int, int):
        return self._x, self._y

    def size(self) -> (int, int):
        return self.W, self.H

    def sprite(self) -> (int, int):
        return 0, 0


class Plane(Actor):
    W, H = 20, 20

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._after_collision = 0

    def act(self, arena: Arena):
        aw, ah = arena.size()
        self._x = (self._x + self._dx) % aw
        if self._after_collision > 0:
            self._after_collision -= 1

    def collide(self, other: Actor, arena: Arena):
        if (isinstance(other, FallingBall)
            and self._after_collision == 0):
            self._dx = -self._dx
            self._after_collision = 60

    def pos(self) -> (int, int):
        return self._x, self._y

    def size(self) -> (int, int):
        return self.W, self.H

    def sprite(self) -> (int, int):
        return 0, 0


def tick():
    global view_x, view_y
    arena_w, arena_h = arena.size()
    keys = g2d.current_keys()
    if "ArrowUp" in keys:
        view_y = max(view_y - 10, 0)
    elif "ArrowRight" in keys:
        view_x = min(view_x + 10, arena_w - view_w)
    elif "ArrowDown" in keys:
        view_y = min(view_y + 10, arena_h - view_h)
    elif "ArrowLeft" in keys:
        view_x = max(view_x - 10, 0)

    g2d.draw_image_clip(background, (0, 0),
                        (view_x, view_y), (view_w, view_h))  # BG
    arena.tick()
    for a in arena.actors():
        x, y = a.pos()
        g2d.fill_rect((x - view_x, y - view_y), a.size())  # FG

def main():
    global arena, view_x, view_y, view_w, view_h, background

    arena = Arena((500, 250))
    arena.spawn(FallingBall(40, 80))
    arena.spawn(FallingBall(80, 40))
    arena.spawn(Plane(60, 60))

    view_x, view_y, view_w, view_h = 0, 0, 300, 200
    g2d.init_canvas((view_w, view_h))

    background = g2d.load_image("https://raw.githubusercontent.com/tomamic/tomamic.github.io/master/images/oop/viewport.png")

    g2d.main_loop(tick)

main()
