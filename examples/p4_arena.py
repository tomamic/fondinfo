#!/usr/bin/env python3
# @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
# @license This software is free - http://www.gnu.org/licenses/gpl.html

import io, random, sys

class Character:
    def move(self):
        raise NotImplementedError('Abstract method')

    @property
    def position(self) -> (int, int):
        raise NotImplementedError('Abstract method')

    @property
    def symbol(self) -> str:
        raise NotImplementedError('Abstract method')


class Arena:
    EMPTY = '-'
    def __init__(self, w=16, h=12):
        self._w, self._h = w, h
        self._characters = []

    def add(self, c: Character):
        self._characters.append(c)

    def move_all(self):
        for c in self._characters:
            c.move()

    def get_symbol(self, x: int, y: int) -> str:
        for c in self._characters:
            if c.position == (x, y):
                return c.symbol
        return Arena.EMPTY

    def __str__(self):
        output = io.StringIO()
        for y in range(self._h):
            for x in range(self._w):
                output.write(self.get_symbol(x, y))
            output.write('\n')
        return output.getvalue()

    @property
    def width(self) -> int:
        return self._w

    @property
    def height(self) -> int:
        return self._h

    @property
    def characters(self) -> list:
        return list(self._characters)


class Ball(Character):
    SYMBOL = '*'
    def __init__(self, x: int, y: int, dx=1, dy=1, w=16, h=12):
        self._x, self._y = x, y
        self._dx, self._dy = dx, dy
        self._w, self._h = w, h

    def move(self):
        new_x = self._x + self._dx
        if not (0 <= new_x < self._w):
            self._dx = -self._dx
        new_y = self._y + self._dy
        if not (0 <= new_y < self._h):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    @property
    def symbol(self):
        return Ball.SYMBOL

    @property
    def position(self):
        return (self._x, self._y)


class Ghost(Character):
    SYMBOL = '?'
    def __init__(self, x: int, y: int, w=16, h=12):
        self._x, self._y = x, y
        self._w, self._h = w, h

    def move(self):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self._x = (self._x + dx) % self._w
        self._y = (self._y + dy) % self._h

    @property
    def symbol(self):
        return Ghost.SYMBOL

    @property
    def position(self):
        return (self._x, self._y)


if __name__ == '__main__':
    arena = Arena(16, 12)
    arena.add(Ball(4, 8))
    arena.add(Ball(8, 4))
    arena.add(Ghost(12, 8))
    print(arena)

    for line in sys.stdin:
        arena.move_all()
        print(arena)
