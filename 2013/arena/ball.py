from sys import stdin
from random import choice
from arena import Character, Arena

class Ball(Character):
    SYMBOL = '*'
    def __init__(self, arena: Arena, x: int, y: int, dx=1, dy=1, w=16, h=12):
        self._x, self._y = x, y
        self._dx, self._dy = dx, dy
        self._w, self._h = w, h
        self._arena = arena
        arena.add_character(self)

    def move(self):
        new_x = self._x + self._dx
        if not (0 <= new_x < self._w):
            self._dx = -self._dx
        new_y = self._y + self._dy
        if not (0 <= new_y < self._h):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def interact(self, other: Character):
        pass
        
    def symbol_at(self, x: int, y: int) -> str:
        if self._x == x and self._y == y:
            return Ball.SYMBOL
        return Arena.EMPTY


class Ghost(Character):
    SYMBOL = '?'
    def __init__(self, arena: Arena, x: int, y: int, w=16, h=12):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._arena = arena
        arena.add_character(self)

    def move(self):
        dx = choice([-1, 0, 1])
        dy = choice([-1, 0, 1])
        self._x = (self._x + dx) % self._w
        self._y = (self._y + dy) % self._h

    def interact(self, other: Character):
        pass
        
    def symbol_at(self, x: int, y: int) -> str:
        if self._x == x and self._y == y:
            return Ghost.SYMBOL
        return Arena.EMPTY


if __name__ == '__main__':
    arena = Arena(16, 12)
    Ball(arena, 4, 8)
    Ball(arena, 8, 4)
    Ghost(arena, 12, 8)
    print(arena)

    for line in stdin:
        arena.move_all()
        print(arena)
