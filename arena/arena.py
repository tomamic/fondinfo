from collections import namedtuple

Piece = namedtuple('Piece', 'x y z symbol character')


class Character:
    
    def move(self):
        raise NotImplementedError('Abstract method')

    def interact(self, other: 'Character'):
        raise NotImplementedError('Abstract method')

    @property
    def pieces(self) -> list:
        raise NotImplementedError('Abstract method')


class Arena:
    
    EMPTY = '.'
    
    def __init__(self, width: int, height: int):
        self._width, self._height = width, height
        self._characters = []
        self._pieces = []

    def add_character(self, c: Character):
        self._characters.append(c)

    def remove_character(self, c: Character):
        self._characters.remove(c)

    def move_all(self):
        for c in self._characters:
            c.move()
            self.update()
            
    def get(self, x: int, y: int) -> Piece:
        for p in reversed(self._pieces):
            if x == p.x and y == p.y:
                return p
        return None
    
    def is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self._width and 0 <= y < self._height

    def __str__(self):
        map = [[Arena.EMPTY] * self._width for y in range(self._height)]
        for p in self._pieces:
            if self.is_inside(p.x, p.y):
                map[p.y][p.x] = p.symbol
        rows = [''.join(row) for row in map]
        return '\n'.join(rows)

    def update(self):
        self._pieces = []
        for c in self._characters:
            self._pieces += c.pieces
        self._pieces.sort(key=lambda val: val.z)

    @property
    def pieces(self) -> list:
        return self._pieces

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

