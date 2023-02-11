#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame
from random import shuffle

FREE, ORC, GOLD, FOUND, OUT = range(5)  # 5 constants

class Quest(BoardGame):
    def __init__(self, w: int, h: int, golds: int, orcs: int):
        rest = w*h - golds - orcs - 1
        if rest < 0:
            raise VaueError("Too many golds and orcs")
        bd = [GOLD]*golds + [ORC]*orcs + [FREE]*rest
        shuffle(bd)
        self._bd, self._w, self._h = [FREE] + bd, w, h
        self._x = self._y = 0
        self._n, self._dead = golds, False

    def _get(self, x, y) -> int:  # OUT if outside of board
        bd, w, h = self._bd, self._w, self._h
        return bd[x + y*w] if (0 <= x < w and 0 <= y < h) else OUT

    def play(self, x: int, y: int, action: str):
        v = self._get(x, y)  # TODO : optionally allow diagonal moves
        if v != OUT and abs(x - self._x) + abs(y - self._y) == 1:
            if v == GOLD:
                self._bd[x + y*self._w] = FOUND
                self._n -= 1
            self._dead = v == ORC
            self._x, self._y = x, y

    def read(self, x: int, y: int) -> str:
        v, fin = self._get(x, y), self.finished()
        return ("\U0001F479" if v == ORC and fin else
                "\U0001F4B0" if v == FOUND or v == GOLD and fin else
                "\U0001F934" if (x, y) == (self._x, self._y) else "")

    def finished(self) -> bool:
        return self._dead or self._n == 0

    def status(self) -> str:  # TODO : refine messages
        return "Orc!" if self._dead else f"{self._n} golds to find"

    def size(self) -> tuple[int, int]:
        return self._w, self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    gui_play(Quest(5, 5, 2, 2))
