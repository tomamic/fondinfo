#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame
from random import sample

FREE, TRAP, GOLD, SACK, OUT = 0, 1, 2, 3, -1

class Monster(BoardGame):
    def __init__(self, w: int, h: int, golds: int, traps: int):
        if (frees := w * h - golds - traps - 1)< 0:
            raise VaueError("Too many treasures and monsters")
        bd = [GOLD] * golds + [TRAP] * traps + [FREE] * frees
        self._bd = [FREE] + sample(bd, len(bd))
        self._w, self._h = w, h
        self._x = self._y = 0
        self._lost = self._won = False

    def _get(self, x, y) -> int:
        bd, w, h = self._bd, self._w, self._h
        return bd[y * w + x] if 0 <= x < w and 0 <= y < h else OUT

    def play(self, x: int, y: int, action: str):
        v = self._get(x, y)
        if v != OUT and abs(x - self._x) + abs(y - self._y) == 1:
            if v == GOLD:
                self._bd[y * self._w + x] = SACK
            elif v == TRAP:
                self._lost = True
            self._x, self._y = x, y
            self._won = not self._lost and GOLD not in self._bd

    def read(self, x: int, y: int) -> str:
        v = self._get(x, y)
        return ("👹" if v == TRAP and self.finished() else
                "💰" if v == SACK or v == GOLD and self.finished() else
                "X" if (x, y) == (self._x, self._y) else "")

    def finished(self) -> bool:
        return self._lost or self._won

    def status(self) -> str:
        return ("Monster!" if self._lost else
                "All treasures found!" if self._won else
                str(self._bd.count(GOLD)) + " treasures to find.")

    def size(self) -> tuple[int, int]:
        return self._w, self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    gui_play(Monster(5, 5, 2, 2))

