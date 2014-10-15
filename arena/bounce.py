from sys import stdin
from random import choice
from arena import Character, Arena

class Ball(Character):
    W, H = 20, 20

    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._dx, self._dy = 5, 5
        self._arena = arena
        arena.add(self)

    def move(self):
        self._x += self._dx
        self._y += self._dy
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x < arena_w - self.W):
            self._dx = -self._dx
        if not (0 <= self._y < arena_h - self.H):
            self._dy = -self._dy

    def hit(self, other: Character):
        pass
        
    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self.W, self.H

    def symbol(self) -> int:
        return 0


class Ghost(Character):
    W, H = 20, 20

    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        arena.add(self)

    def move(self):
        dx = choice([-5, 0, 5])
        dy = choice([-5, 0, 5])
        arena_w, arena_h = self._arena.size()
        self._x = (self._x + dx) % arena_w
        self._y = (self._y + dy) % arena_h

    def hit(self, other: Character):
        pass
        
    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self.W, self.H

    def symbol(self) -> int:
        return 0


class Turtle(Character):
    W, H = 20, 20
    SPEED = 2

    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - Turtle.H:
            self._y = arena_h - Turtle.H

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - Turtle.W:
            self._x = arena_w - Turtle.W

    def go_left(self):
        self._dx, self._dy = -Turtle.SPEED, 0
        
    def go_right(self):
        self._dx, self._dy = +Turtle.SPEED, 0

    def go_up(self):
        self._dx, self._dy = 0, -Turtle.SPEED
        
    def go_down(self):
        self._dx, self._dy = 0, +Turtle.SPEED

    def stay(self):
        self._dx, self._dy = 0, 0

    def hit(self, other: Character):
        pass
        
    def rect(self) -> (int, int, int, int):
        return self._x, self._y, self.W, self.H

    def symbol(self) -> int:
        return 0


if __name__ == '__main__':
    arena = Arena(320, 240)
    Ball(arena, 40, 80)
    Ball(arena, 80, 40)
    Ghost(arena, 120, 80)
    print(arena)

    for line in stdin:
        arena.move_all()
        print(arena)
