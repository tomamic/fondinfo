from sys import stdin
from arena import Character, Arena

class Passenger:
    @property
    def pos(self) -> (int, int):
        raise NotImplementedError('Abstract method')

    def shift(self, dx: int, dy: int):
        raise NotImplementedError('Abstract method')


class Frog(Character, Passenger):
    SYMBOL = '@'
    STAY, UP, LEFT, DOWN, RIGHT = (0, 0), (0, -1), (-1, 0), (0, 1), (1, 0)
    DIRS = (STAY, UP, LEFT, DOWN, RIGHT)

    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        self._dx, self._dy = Frog.STAY
        arena.add_character(self)

    def move(self):
        new_x = self._x + self._dx
        new_y = self._y + self._dy

        if ((self._dx, self._dy) != Frog.STAY
            and self._arena.is_inside(new_x, new_y)):
            what = self._arena.get(new_x, new_y)
            # touch everybody who's in the way
            if what != None:
                what.interact(self)
            # if the cell is free, move there
            if what == None or isinstance(what, Boat):
                self._x, self._y = new_x, new_y

    def set_direction(self, dx: int, dy):
        if (dx, dy) in Frog.DIRS:
            self._dx, self._dy = dx, dy

    def interact(self, other: Character):
        # the penguin dies as soon as it's touched by anybody
        self._arena.remove_character(self)

    def shift(self, dx: int, dy: int):
        self._x += dx
        self._y += dy
        if not self._arena.is_inside(self._x, self._y):
            self._arena.remove_character(self)

    def symbol_at(self, x: int, y: int) -> str:
        if self._x == x and self._y == y:
            return Frog.SYMBOL
        return Arena.EMPTY

    @property
    def pos(self) -> (int, int):
        return (self._x, self._y)


class Boat(Character):
    SYMBOL = 'O'
    DEF_SIZE, MARGIN = 3, 4
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        arena.add_character(self)
        self._turn = 0
        self._dx = 2 * (y % 2) - 1  # -1 if y is even, +1 if odd
        self._size = Boat.DEF_SIZE

    def move(self):
        WAIT = 2
        self._turn = (self._turn + 1) % WAIT
        if self._turn == 0:
            passengers = []
            x0, x1 = self._x, self._x + self._size
            for c in self._arena.characters:
                if (isinstance(c, Passenger)):
                    cx, cy = c.pos
                    if (self._y == c.pos[1] and x0 <= c.pos[0] < x1
                        and not c in passengers):
                        passengers.append(c)

            self._x += self._dx
            if self._x < -Boat.MARGIN: self._x = self._arena.width + Boat.MARGIN
            if self._x > self._arena.width + Boat.MARGIN: self._x = -Boat.MARGIN
            
            for a in passengers:
                try:
                    a.shift(self._x - x0, 0)
                except AttributeError:
                    pass

    def interact(self, other: Character):
        pass

    def symbol_at(self, x: int, y: int) -> str:
        if self._x <= x < self._x + self._size and y == self._y:
            return Boat.SYMBOL
        return Arena.EMPTY


class River(Character):
    SYMBOL = '~'
    def __init__(self, arena: Arena, y: int):
        self._y = y
        self._arena = arena
        arena.add_character(self)

    def move(self):
        pass

    def interact(self, other: Character):
        other.interact(self)

    def symbol_at(self, x: int, y: int) -> str:
        if y == self._y:
            return River.SYMBOL
        return Arena.EMPTY


class Truck(Character):
    SYMBOL = '='
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        arena.add_character(self)
        self._turn = 0
        self._dx = 2 * (y % 2) - 1  # -1 if y is even, +1 if odd
        self._size = 1

    def move(self):
        WAIT = 2
        self._turn += 1
        if self._turn % WAIT == 0:
            
            self._x += self._dx
            if self._x < 0: self._x = self._arena.width - 1
            if self._x >= self._arena.width: self._x = 0

            what = self._arena.get(self._x, self._y);
            if what != None and what != self:
                what.interact(self)

    def interact(self, other: Character):
        if isinstance(other, Frog):
            other.interact(self)

    def symbol_at(self, x: int, y: int) -> str:
        if self._x <= x < self._x + self._size and y == self._y:
            return Truck.SYMBOL
        return Arena.EMPTY


class FroggerArena(Arena):
    def __init__(self, width, height):
        super().__init__(width, height)

    @property
    def won(self) -> bool:
        for c in self._characters:
            if isinstance(c, Frog) and c.pos[1] == 0:
                return True
        return False

    @property
    def lost(self) -> bool:
        for c in self._characters:
            if isinstance(c, Frog):
                return False
        return True

    # possibly... override `get` for taking layers into account


if __name__ == '__main__':
    arena = FroggerArena(15, 7)

    frog = Frog(arena, 7, 6)
    Truck(arena, 3, 4);
    Truck(arena, 5, 4);
    Truck(arena, 9, 4);
    Truck(arena, 2, 5);
    Truck(arena, 4, 5);
    Truck(arena, 8, 5);
    Boat(arena, 2, 1)
    Boat(arena, 10, 1)
    Boat(arena, 2, 2)
    Boat(arena, 10, 2)
    River(arena, 1)
    River(arena, 2)  # objects with lower z: at the end of the list

    print(arena)

    COMMANDS = {'w': Frog.UP, 'a': Frog.LEFT,
                's': Frog.DOWN, 'd': Frog.RIGHT}
    while not arena.lost and not arena.won:
        line = input()
        direction = COMMANDS.get(line, Frog.STAY)
        frog.set_direction(*direction)

        arena.move_all()
        print(arena)

