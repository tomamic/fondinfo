#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame
from random import sample

FREE, ORC, GOLD, PIKD, OUT = range(5)

class Quest(BoardGame):
    def __init__(self, w: int, h: int, golds: int, orcs: int):
        if (free_cells := w * h - golds - orcs - 1) < 0:
            raise VaueError("Too many golds and orcs")
        bd = [GOLD] * golds + [ORC] * orcs + [FREE] * free_cells
        self._bd = [FREE] + sample(bd, len(bd))  # shuffled(bd)
        self._x = self._y = 0
        self._w, self._h = w, h
        self._golds, self._lost = golds, False

    def _get(self, x, y) -> int:
        bd, w, h = self._bd, self._w, self._h
        return bd[y * w + x] if 0 <= x < w and 0 <= y < h else OUT

    def play(self, x: int, y: int, action: str):
        v = self._get(x, y)
        if v != OUT and abs(x - self._x) + abs(y - self._y) == 1:
            if v == GOLD:
                self._bd[y * self._w + x] = PIKD
                self._golds -= 1
            self._lost = v == ORC
            self._x, self._y = x, y

    def read(self, x: int, y: int) -> str:
        v = self._get(x, y)
        return ("\U0001F479" if v==ORC and self.finished() else
                "\U0001F4B0" if v==PIKD or v==GOLD and self._lost else
                "\U0001F934" if (x, y) == (self._x, self._y) else "")

    def finished(self) -> bool:
        return self._lost or self._golds == 0

    def status(self) -> str:
        return ("Orc!" if self._lost else
                "All golds found!" if self._golds == 0 else
                f"{self._golds} golds to find.")

    def size(self) -> tuple[int, int]:
        return self._w, self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    gui_play(Quest(5, 5, 2, 2))
