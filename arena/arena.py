from io import StringIO

class Character:
    
    def move(self):
        raise NotImplementedError('Abstract method')

    def interact(self, other: 'Character'):
        raise NotImplementedError('Abstract method')

    def symbol_at(self, x: int, y: int) -> str:
        raise NotImplementedError('Abstract method')


class Arena:
    
    EMPTY = '.'
    
    def __init__(self, width: int, height: int):
        self._width, self._height = width, height
        self._characters = []

    def add_character(self, c: Character):
        self._characters.append(c)

    def remove_character(self, c: Character):
        self._characters.remove(c)

    def move_all(self):
        for c in self._characters:
            c.move()

    def get(self, x: int, y: int) -> Character:
        for c in self._characters:
            if c.symbol_at(x, y) != None:
                return c;
        return None;

    def get_symbol(self, x: int, y: int) -> str:
        for c in self._characters:
            symbol = c.symbol_at(x, y)
            if symbol != None:
                return symbol;
        return Arena.EMPTY;

    def __str__(self):
        output = StringIO()
        for y in range(self._height):
            for x in range(self._width):
                output.write(self.get_symbol(x, y))
            output.write('\n')
        return output.getvalue()

    def is_inside(self, x: int, y: int) -> bool:
        return 0 <= x < self._width and 0 <= y < self._height

    @property
    def characters(self) -> list:
        return list(self._characters)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

