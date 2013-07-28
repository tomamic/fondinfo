#!/usr/bin/python3

from random import randrange
from io import StringIO
from sys import argv, stdin                          

class FifteenPuzzle:
    _DIRS = ((0, -1), (+1, 0), (0, +1), (-1, 0)) # dx, dy

    def __init__(self, cols: int, rows: int):
        self._cols = int(cols)
        self._rows = int(rows)
        self._SOLUTION = list(range(1, cols * rows))
        self._SOLUTION.append(0)
        self.sort()
        self.shuffle()

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def finished(self) -> bool:
        return self._board == self._SOLUTION


    def sort(self):
        self._board = list(self._SOLUTION)
        self._blank = (self._cols - 1, self._rows - 1)

    def shuffle(self):
        for _ in range(len(self._board)**2):
            d = randrange(4)
            dx, dy = self._DIRS[d]
            self._move_blank(dx, dy)

    def move_val(self, val: int):
        x, y = self._blank
        for dx, dy in self._DIRS:
            if (self.get(x + dx, y + dy) == val):
                self._move_blank(dx, dy)
                return

    def move_position(self, x: int, y: int):
        self.move_val(self.get(x, y))

    def get(self, x: int, y: int) -> int:
        val = -1
        if 0 <= y < self._rows and 0 <= x < self._cols:
            val = self._board[y * self._cols + x]
        return val

    def _set(self, x: int, y: int, value: int):
        self._board[y * self._cols + x] = int(value)

    def _move_blank(self, dx: int, dy: int):
        x, y = self._blank
        val = self.get(x + dx, y + dy)
        if val > 0:
            self._set(x, y, val)
            self._set(x + dx, y + dy, 0)
            self._blank = (x + dx, y + dy)

    def __str__(self):
        result = StringIO()
        for y in range(self._rows):
            for x in range(self._cols):
                result.write(str(self.get(x, y)).rjust(3))
            result.write('\n')
        return result.getvalue()
        

def main():
    puzzle = FifteenPuzzle(4, 4)
    print(puzzle)
    
    for line in stdin:
        puzzle.move_val(int(line))
        print(puzzle)
        
        if puzzle.finished:
            print('Congatulations!')
            puzzle.shuffle()
            print(puzzle)

if __name__ == '__main__':
    main()
