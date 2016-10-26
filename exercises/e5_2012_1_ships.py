#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import random

class Sea:
    DIRS = 4
    DX = ( 0, +1,  0, -1)
    DY = (-1,  0, +1,  0)

    def __init__(self, rows: int, cols: int):
        self._rows, self._cols = rows, cols
        self._matrix = [[False for x in range(cols)] for y in range(rows)]

    def place(self, x: int, y: int, dx: int, dy: int, size: int) -> bool:
        if not (0 <= y < self._rows
                and 0 <= x < self._cols
                and not self._matrix[y][x]):
            return False

        if size > 1 and not self.place(x + dx, y + dy, dx, dy, size - 1):
            return False

        self._matrix[y][x] = True
        return True

    def __str__(self) -> str:
        result = []
        for y in range(self._rows):
            for x in range(self._cols):
                if self._matrix[y][x]: result.append('@')
                else: result.append('-')
            result.append('\n')
        return ''.join(result)

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

if __name__ == '__main__':
    sea = Sea(8, 12)
    size = int(input('size? '))
    while size > 0:
        x = random.randrange(sea.cols)
        y = random.randrange(sea.rows)
        d = random.randrange(Sea.DIRS)
        if not sea.place(x, y, Sea.DX[d], Sea.DY[d], size):
            print('error @ {}, {}, {}'.format(x, y, d))
        print(sea)
        size = int(input('size? '))
