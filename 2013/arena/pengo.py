from sys import stdin
from random import choice
from arena import Character, Arena

class Penguin(Character):
    SYMBOL = '&'
    STAY, UP, LEFT, DOWN, RIGHT = (0, 0), (0, -1), (-1, 0), (0, 1), (1, 0)
    DIRS = (STAY, UP, LEFT, DOWN, RIGHT)
    
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        self._dx, self._dy = 0, 0
        arena.add_character(self)

    def set_direction(self, dx: int, dy: int):
        if (dx, dy) in Penguin.DIRS:
            self._dx, self._dy = dx, dy

    def move(self):
        new_x = self._x + self._dx
        new_y = self._y + self._dy

        if ((self._dx, self._dy) != Penguin.STAY
            and self._arena.is_inside(new_x, new_y)):
            # touch everybody who's in the way
            what = self._arena.get(new_x, new_y)
            if what != None:
                what.interact(self)
            # if the cell is free, move there
            if self._arena.get(new_x, new_y) == None:
                self._x, self._y = new_x, new_y

    def interact(self, other: Character):
        # the penguin dies as soon as it's touched by anybody
        self._arena.remove_character(self)

    def symbol_at(self, x: int, y: int) -> str:
        if self._x == x and self._y == y:
            return Penguin.SYMBOL
        return Arena.EMPTY

    @property
    def pos(self) -> (int, int):
        return (self._x, self._y)


class Ghost(Character):
    SYMBOL = '^'
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        arena.add_character(self)
        self._turn = 0

    def move(self):
        dx, dy = choice([(0, -1), (+1, 0), (0, +1), (-1, 0)])
        new_x, new_y = self._x + dx, self._y + dy
        WAIT = 3
        self._turn += 1
        if (self._turn % WAIT == 0
            and self._arena.is_inside(new_x, new_y)):
            # don't touch anybody... but players
            what = self._arena.get(new_x, new_y)
            if what != None and isinstance(what, Penguin):
                what.interact(self)
            # if the cell is free, move there
            if self._arena.get(new_x, new_y) == None:
                self._x, self._y = new_x, new_y

    def interact(self, other: Character):
        # if a player touches a ghost, the player dies
        # otherwise, the ghost dies
        if isinstance(other, Penguin):
            other.interact(self)
        else:
            self._arena.remove_character(self)

    def symbol_at(self, x: int, y: int) -> str:
        if self._x == x and self._y == y:
            return Ghost.SYMBOL
        return Arena.EMPTY


class Ice(Character):
    SYMBOL = '#'
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add_character(self)

    def move(self):
        new_x = self._x + self._dx
        new_y = self._y + self._dy
        if ((self._dx != 0 or self._dy != 0)
            and self._arena.is_inside(new_x, new_y)):
            # touch everybody who's in the way
            what = self._arena.get(new_x, new_y)
            if what != None:
                what.interact(self)
            # if the cell is free, eventually, move there
            if self._arena.get(new_x, new_y) == None:
                self._x, self._y = new_x, new_y
            else:
                self._dx, self._dy = 0, 0

    def interact(self, other: Character):
        # if touched by a player
        if isinstance(other, Penguin):
            # find the direction opposite to the player
            self._dx = self._x - other.pos[0]
            self._dy = self._y - other.pos[1]
            new_x = self._x + self._dx
            new_y = self._y + self._dy

            # if the ice-block is pushed against the border,
            # or against another ice-block,
            # the ice-block dies
            if not self._arena.is_inside(new_x, new_y):
                self._arena.remove_character(self)
            else:
                what = self._arena.get(new_x, new_y)
                if what != None and isinstance(what, Ice):
                    self._arena.remove_character(self)

    def symbol_at(self, x: int, y: int) -> str:
        if self._x == x and self._y == y:
            return Ice.SYMBOL
        return Arena.EMPTY


class PengoArena(Arena):
    def __init__(self, width, height):
        super().__init__(width, height)

    @property
    def won(self) -> bool:
        for a in self._characters:
            if isinstance(a, Ghost):
                return False
        return True

    @property
    def lost(self) -> bool:
        for a in self._characters:
            if isinstance(a, Penguin):
                return False
        return True


if __name__ == '__main__':
    arena = PengoArena(7, 7)
    Ice(arena, 2, 1)
    Ice(arena, 2, 2)
    Ice(arena, 4, 4)
    Ice(arena, 4, 5)
    Ghost(arena, 0, 3)
    Ghost(arena, 5, 2)
    penguin = Penguin(arena, 3, 3)
    print(arena)

    COMMANDS = {'w': Penguin.UP, 'a': Penguin.LEFT,
                's': Penguin.DOWN, 'd': Penguin.RIGHT}
    while not arena.lost and not arena.won:
        line = input()
        direction = COMMANDS.get(line, Penguin.STAY)
        penguin.set_direction(*direction)

        arena.move_all()
        print(arena)

