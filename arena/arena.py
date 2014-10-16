from io import StringIO

class Character:
    
    def move(self):
        raise NotImplementedError('Abstract method')

    def hit(self, other: 'Character'):
        raise NotImplementedError('Abstract method')

    def symbol(self) -> int:
        '''return 0, or the index of current image'''
        raise NotImplementedError('Abstract method')

    def rect(self) -> (int, int, int, int):
        '''return (left, top, width, height)'''
        raise NotImplementedError('Abstract method')


class Arena:

    def __init__(self, width: int, height: int):
        self._w, self._h = width, height
        self._characters = []

    def add(self, c: Character):
        self._characters.append(c)

    def remove(self, c: Character):
        self._characters.remove(c)

    def move_all(self):
        for c in self.characters():
            c.move()
            for other in self._characters:
                if self.check_collision(c, other):
                    c.hit(other)
                    other.hit(c)

    def check_collision(self, c1: Character, c2: Character) -> bool:
        x1, y1, w1, h1 = c1.rect()
        x2, y2, w2, h2 = c2.rect()
        return (c1 is not c2
            and y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2)

    def first_colliding(self, c: Character) -> Character:
        for other in reversed(self._characters):
            if self.check_collision(c, other):
                return other
        return None;

    def characters(self) -> list:
        return list(self._characters)

    def size(self) -> (int, int):
        return (self._w, self._h)

    def inside(self, c: Character) -> bool:
        x, y, w, h = c.rect()
        return 0 <= y <= self._h - h and 0 <= x <= self._w - w

    def __str__(self):
        output = StringIO()
        for c in self._characters:
            print(type(c).__name__, '@', c.rect(), file=output)
        return output.getvalue()
