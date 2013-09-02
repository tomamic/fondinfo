from sys import stdin
from arena import Piece, Character, Arena

class Frog(Character):
    STAY, UP, LEFT, DOWN, RIGHT = (0, 0), (0, -1), (-1, 0), (0, 1), (1, 0)
    
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y = x, y
        self._arena = arena
        self._dx, self._dy = Frog.STAY
        arena.add_actor(self)

    def move(self):
        new_x = self._x + self._dx
        new_y = self._y + self._dy

        if ((self._dx, self._dy) != Frog.STAY
            and self._arena.is_inside(new_x, new_y)):
            piece = self._arena.get(new_x, new_y)
            # touch everybody who's in the way
            if piece != None:
                piece.actor.interact(self)
            # if the cell is free, move there
            if piece == None or isinstance(piece.actor, Boat):
                self._x, self._y = new_x, new_y

    def set_direction(self, dx: int, dy):
        self._dx, self._dy = dx, dy

    def interact(self, other: Character):
        # the penguin dies as soon as it's touched by anybody
        self._arena.remove_actor(self)

    def shift(self, dx: int, dy: int):
        self._x += dx
        self._y += dy
        if not self._arena.is_inside(self._x, self._y):
            self._arena.remove_actor(self)

    @property
    def pieces(self):
        return [Piece(self._x, self._y, 10, '@', self)]


class Boat(Character):
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y, self._z = x, y, -5
        self._arena = arena
        arena.add_actor(self)
        self._turn = 0
        self._dx = 2 * (y % 2) - 1
        self._size = 3

    def move(self):
        WAIT = 2
        self._turn += 1
        if self._turn % WAIT == 0:
            passengers = []
            x0, x1 = self._x, self._x + self._size
            for p in self._arena.pieces:
                if (self._y == p. y and x0 <= p.x < x1
                    and p.z > self._z and not p.actor in passengers):
                    passengers.append(p.actor)

            self._x += self._dx
            if self._x < -5: self._x = self._arena.width + 4
            if self._x > self._arena.width + 4: self._x = -4
            
            for a in passengers:
                try:
                    a.shift(self._x - x0, 0)
                except AttributeError:
                    pass

    def interact(self, other: Character):
        pass

    @property
    def pieces(self):
        return [Piece(self._x + d, self._y, self._z, 'O', self)
                for d in range(self._size)]


class River(Character):
    def __init__(self, arena: Arena, y: int):
        self._x, self._y, self._z = 0, y, -10
        self._arena = arena
        arena.add_actor(self)
        self._size = arena.width

    def move(self):
        pass

    def interact(self, other: Character):
        other.interact(self)

    @property
    def pieces(self):
        return [Piece(self._x + d, self._y, self._z, '~', self)
                for d in range(self._size)]

class Truck(Character):
    def __init__(self, arena: Arena, x: int, y: int):
        self._x, self._y, self._z = x, y, 0
        self._arena = arena
        arena.add_actor(self)
        self._turn = 0
        self._dx = 2 * (y % 2) - 1
        self._size = 1

    def move(self):
        WAIT = 2
        self._turn += 1
        if self._turn % WAIT == 0:
            
            self._x += self._dx
            if self._x < 0: self._x = self._arena.width - 1
            if self._x >= self._arena.width: self._x = 0

            piece = self._arena.get(self._x, self._y);
            if piece != None:
                piece.actor.interact(self)

    def interact(self, other: Character):
        if isinstance(other, Frog):
            other.interact(self)

    @property
    def pieces(self):
        return [Piece(self._x + d, self._y, self._z, '=', self)
                for d in range(self._size)]


class FroggerArena(Arena):
    def __init__(self, width, height):
        super().__init__(width, height)

    @property
    def won(self) -> bool:
        for p in self.pieces:
            if p.y == 0 and isinstance(p.actor, Frog):
                return True
        return False

    @property
    def lost(self) -> bool:
        for a in self._actors:
            if isinstance(a, Frog):
                return False
        return True


if __name__ == '__main__':
    arena = FroggerArena(15, 7)

    River(arena, 1)
    River(arena, 2)
    Boat(arena, 2, 1)
    Boat(arena, 10, 1)
    Boat(arena, 2, 2)
    Boat(arena, 10, 2)
    Truck(arena, 3, 4);
    Truck(arena, 5, 4);
    Truck(arena, 9, 4);
    Truck(arena, 2, 5);
    Truck(arena, 4, 5);
    Truck(arena, 8, 5);
    frog = Frog(arena, 7, 6)

    print(arena)

    COMMANDS = {'w': Frog.UP, 'a': Frog.LEFT,
                's': Frog.DOWN, 'd': Frog.RIGHT}
    for line in stdin:
        direction = COMMANDS.get(line.strip(), Frog.STAY)
        frog.set_direction(*direction)

        arena.move_all()
        print(arena)
        if arena.lost or arena.won:
            break
