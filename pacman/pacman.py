'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import choice
from arena import *

# The following two functions may me adapted to be part of a subclass
# of Arena, specialized for the Pac-Man game

def rect_in_wall(arena: Arena, rect: (int, int, int, int)) -> bool:
    for other in arena.actors():
        if isinstance(other, Wall):
            x1, y1, w1, h1 = rect
            x2, y2, w2, h2 = other.rect()
            if (y2 < y1 + h1 and y1 < y2 + h2 and
                x2 < x1 + w1 and x1 < x2 + w2):
                return True
        else:
            return False  # walls must be the first actors in the list!


def going_to_wall(arena: Arena, actor: Actor, dx: int, dy: int) -> bool:
    x, y, w, h = actor.rect()
    return rect_in_wall(arena, (x + dx, y + dy, w, h))


##class PacManArena(Arena):
##    pass


# Size and position hints for Pac-Man characters
# Everything needs yet to be fixed!

class Wall(Actor):  # ...

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



class Cookie(Actor):  # ...
    W, H = 4, 4

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 166, 54


class Power(Actor):  # ...
    W, H = 8, 8

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 180, 52


class Ghost(Actor):  # ...
    W, H = 16, 16
    SPEED = 2

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        if self._x % 8 == 0 and self._y %8 == 0:
            moves = [(0, -self.SPEED),
                     (self.SPEED, 0),
                     (0, self.SPEED),
                     (-self.SPEED, 0)]
            opposite = (-self._dx, -self._dy)
            dx, dy = choice(moves)
            while ((dx, dy) == opposite or
                   going_to_wall(self._arena, self, dx, dy)):
                moves.remove((dx, dy))  # don't try it again!
                dx, dy = choice(moves)
            self._dx, self._dy = dx, dy
            
        self._y += self._dy
        self._x += self._dx

    def collide(self, other):
        pass

    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 64


class PacMan(Actor):  # ...
    W, H = 16, 16
    SPEED = 2

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._user_dx, self._user_dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        if self._x % 8 == 0 and self._y %8 == 0:
            if not going_to_wall(self._arena, self,
                              self._user_dx, self._user_dy):
                self._dx = self._user_dx
                self._dy = self._user_dy
            
        self._y += self._dy
        self._x += self._dx

    def go_left(self):
        self._user_dx, self._user_dy = -self.SPEED, 0
        
    def go_right(self):
        self._user_dx, self._user_dy = +self.SPEED, 0

    def go_up(self):
        self._user_dx, self._user_dy = 0, -self.SPEED
        
    def go_down(self):
        self._user_dx, self._user_dy = 0, +self.SPEED

    def collide(self, other):
        if isinstance(other, Wall):
            self._x -= self._dx
            self._y -= self._dy
            self._dx, self._dy = 0, 0
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 0


