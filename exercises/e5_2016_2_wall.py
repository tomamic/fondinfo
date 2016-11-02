#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *
from random import choice, randrange
from actor import *

class Ball(Actor):
    W, H = 20, 20
    SPEED = 5

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = self.SPEED, self.SPEED
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x + self._dx <= arena_w - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= arena_h - self.H):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def collide(self, other):
        if isinstance(other, Wall):
            x, y, w, h = other.rect()
            
            border_left, border_right = x - self.W, x + w
            border_top, border_bottom = y - self.H, y + h
            # now set either self._x or self._y, to the nearest border
            
            if abs(border_left - self._x) < abs(border_right - self._x):
                nearest_x = border_left
            else:
                nearest_x = border_right
            
            if abs(border_top - self._y) < abs(border_bottom - self._y):
                nearest_y = border_top
            else:
                nearest_y = border_bottom

            if abs(nearest_x - self._x) < abs(nearest_y - self._y):
                self._x = nearest_x
            else:
                self._y = nearest_y
            
##            move_x = min(x - self.W - self._x, x + w - self._x, key=abs)
##            move_y = min(y - self.H - self._y, y + h - self._y, key=abs)
##            if abs(move_x) < abs(move_y):
##                self._x += move_x
##            else:
##                self._y += move_y

    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 0


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
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 0, 0

  
def update():
    arena.move_all()  # Game logic

    canvas_fill(canvas, (255, 255, 255))
    for a in arena.actors():
        if isinstance(a, Wall):
            draw_rect(canvas, (127, 127, 127), a.rect())
        else:
            x, y, w, h = a.rect()
            xs, ys = a.symbol()
            image_blit(canvas, sprites, (x, y), area=(xs, ys, w, h))

arena = Arena(320, 240)
Ball(arena, 40, 80)
Ball(arena, 80, 40)
Wall(arena, 120, 80, 100, 20)

canvas = canvas_init(arena.size())
sprites = image_load("sprites.png")

set_interval(update, 1000//30)  # millis
    
