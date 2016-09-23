#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import random

class Memory:
    JOLLY = '?'
    FIRST = 'A'

    def __init__(self, rows: int, cols: int):
        self._rows, self._cols = rows, cols
        self._move1 = self._move2 = -1
        self.sort()
        self.shuffle()

    def sort(self):
        # cards: list of ints, representing the cards
        # visible: list of bools, to keep track of guessed cards
        self._cards = [i // 2 for i in range(rows * cols)]
        self._visible = [False] * (rows * cols)

    def shuffle(self):
        random.shuffle(self._cards)

    def uncover(self, pos1: int, pos2: int):
        if (pos1 != pos2
            and 0 <= pos1 < len(self._cards)
            and 0 <= pos2 < len(self._cards)):
            self._move1, self._move2 = pos1, pos2
            if self._cards[pos1] == self._cards[pos2]:
                # mark the guessed couple as visible
                self._visible[pos1] = True
                self._visible[pos2] = True

    def is_finished(self):
        return not (False in self._visible)

    def __str__(self) -> str:
        result = []
        for i, c in enumerate(self._cards):
            if self._visible[i] or i in (self._move1, self._move2):
                result.append(chr(c + ord(Memory.FIRST)))
            else:
                result.append(Memory.JOLLY)
            if i % self._cols == self._cols - 1:
                result.append('\n')
        return ''.join(result)

if __name__ == '__main__':
    rows = cols = size = 1
    while size % 2 != 0:
        cols = int(input('Cols? '))
        rows = int(input('Rows? '))
        size = rows * cols

    memory = Memory(rows, cols)
    print(memory)

    while not memory.is_finished():
        a = int(input('1st card (1-{})? '.format(size)))
        b = int(input('2nd card (1-{})? '.format(size)))
        memory.uncover(a - 1, b - 1)
        print(memory)
