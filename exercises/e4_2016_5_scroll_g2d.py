#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *
from actor import Actor, Arena
    
class FallingBall(Actor):
    W, H = 20, 20

    def __init__(self, arena: Arena, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 0
        self._g = 0.3
        self._arena = arena
        arena.add(self)

    def move(self):
        aw, ah = arena.size()
        if not (0 <= self._x + self._dx <= aw - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ah - self.H):
            self._dy = -self._dy
        else:
            self._dy += self._g

        self._x += self._dx
        self._y += self._dy

    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self.W, self.H

    def collide(self, other: Actor):
        return

    def symbol(self) -> (int, int):
        return 0, 0


class Plane(Actor):
    W, H = 20, 20

    def __init__(self, arena, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._after_collision = 0
        self._arena = arena
        arena.add(self)

    def move(self):
        aw, ah = arena.size()
        self._x = (self._x + self._dx) % aw
        if self._after_collision > 0:
            self._after_collision -= 1

    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self.W, self.H

    def collide(self, other: Actor):
        if (isinstance(other, FallingBall)
            and self._after_collision == 0):
            self._dx = -self._dx
            self._after_collision = 60

    def symbol(self) -> (int, int):
        return 0, 0


def update():
    image_blit(canvas, background, (0, 0), area=(vx, vy, vw, vh))  # BG
    arena.move_all()
    for a in arena.actors():
        x, y, w, h = a.rect()
        draw_rect(canvas, (127, 127, 127),
                  (x - view_x, y - view_y, w, h))  # FG

def key_down(event):
    global view_x, view_y
    arena_w, arena_h = arena.size()
    code = event.code
    if code == "ArrowRight":
        view_x = min(view_x + 10, arena_w - view_w)
    elif code == "ArrowLeft":
        view_x = max(view_x - 10, 0)
    elif code == "ArrowDown":
        view_y = min(view_y + 10, arena_h - view_h)
    elif code == "ArrowUp":
        view_y = max(view_y - 10, 0)

arena = Arena(500, 250)
a1 = FallingBall(arena, 40, 80)
a2 = FallingBall(arena, 80, 40)
a3 = Plane(arena, 60, 60)

view_x, view_y, view_w, view_h = 0, 0, 300, 200
canvas = canvas_init((view_w, view_h))

background = image_load("viewport.png")

set_interval(update, 1000 // 30)  # Millis
doc.onkeydown = key_down
