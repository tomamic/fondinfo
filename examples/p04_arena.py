#!/usr/bin/env python3
# @author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
# @license This software is free - http://www.gnu.org/licenses/gpl.html

import random, sys

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
    def __init__(self, width: int, height: int):
        self._width, self._height = width, height
        self._characters = []

    def add_character(self, c: Character):
        self._characters.append(c)
                    
    def move_all(self):
        for c in self._characters:
            c.move()
            
    def __str__(self):
        # create an empty matrix
        map = [[Arena.EMPTY] * self._width for y in range(self._height)]
        # for each character, place its symbol in the matrix
        for c in self._characters:
            x, y = c.position
            if 0 <= x < self._width and 0 <= y < self._height:
                map[y][x] = c.symbol
        # join the matrix into a string
        rows = [''.join(row) for row in map]
        return '\n'.join(rows)

    @property
    def width(self) -> int: 
        return self._width

    @property
    def height(self) -> int: 
        return self._height

    @property
    def characters(self) -> list: 
        return list(self._characters)
        
class Ball(Character):
    SYMBOL = '*'
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._dx, self._dy = 1, 1
        self._arena = arena
        arena.add_character(self)
        
    def move(self):
        new_x = self._x + self._dx
        if not (0 <= new_x < self._arena.width):
            self._dx = -self._dx
        new_y = self._y + self._dy
        if not (0 <= new_y < self._arena.height):
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
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        arena.add_character(self)

    def move(self):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self._x = (self._x + dx) % self._arena.width
        self._y = (self._y + dy) % self._arena.height

    @property
    def symbol(self):
        return Ghost.SYMBOL
    
    @property
    def position(self):
        return (self._x, self._y)    
    
if __name__ == '__main__':
    arena = Arena(16, 12)
    b1 = Ball(arena, 4, 8)
    b2 = Ball(arena, 8, 4)
    g = Ghost(arena, 12, 8)
    print(arena)

    for line in sys.stdin:
        arena.move_all()
        print(arena)
