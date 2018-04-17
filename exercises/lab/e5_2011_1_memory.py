#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import random

class Memory:

    def __init__(self, rows: int, cols: int):
        self._rows, self._cols = rows, cols
        self._pos1 = self._pos2 = -1
        n = self._rows * self._cols

        self._cards = [chr(i // 2 + ord('A')) for i in range(n)]
        self._visible = [False for i in range(n)]

        random.shuffle(self._cards)
##        cards = self._cards
##        for i in range(n):
##            j = random.randrange(n)
##            cards[i], cards[j] = cards[j], cards[i]

    def uncover(self, pos1: int, pos2: int):
        cards = self._cards
        n = len(cards)
        if pos1 != pos2 and 0 <= pos1 < n and 0 <= pos2 < n:
            self._pos1, self._pos2 = pos1, pos2
            if cards[pos1] == cards[pos2]:
                # mark the guessed couple as visible
                self._visible[pos1] = True
                self._visible[pos2] = True

    def solved(self) -> bool:
        return not (False in self._visible)

    def __str__(self) -> str:
        result = ""    # StringIO is more efficient
        for y in range(self._rows):
            for x in range(self._cols):
                i = y * self._cols + x
                if self._visible[i] or i == self._pos1 or i == self._pos2:
                    result += self._cards[i]
                else:
                    result += '?'
            result += '\n'
        return result


def main():
    rows = cols = size = 1
    while size % 2 != 0:
        cols = int(input('Cols? '))
        rows = int(input('Rows? '))
        size = rows * cols

    memory = Memory(rows, cols)
    print(memory)

    while not memory.solved():
        a = int(input('1st card (1-{})? '.format(size)))
        b = int(input('2nd card (1-{})? '.format(size)))
        memory.uncover(a - 1, b - 1)
        print(memory)

if __name__ == '__main__':
    main()
