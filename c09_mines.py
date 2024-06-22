#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from boardgame import BoardGame
from random import sample

MINE, FREE, TFLAG, FFLAG, OUT = 9, 10, 11, 12, 13  # true/false flag
dirs = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]

class Mines(BoardGame):
    def __init__(self, w: int, h: int, n: int):
        self._w, self._h = w, h
        self._bd = sample([MINE] * n + [FREE] * (w*h - n), w*h)
        self._lost = self._won = False

    def _get(self, x, y) -> int:  # OUT if outside of board
        w, h = self.cols(), self.rows()
        return self._bd[x + y*w] if 0 <= x < w and 0 <= y < h else OUT

    def play(self, x: int, y: int, action: str):
        v = self._get(x, y)
        if v != OUT and action == "flag":
            rot = {MINE: TFLAG, TFLAG: MINE, FREE: FFLAG, FFLAG: FREE}
            self._bd[x + y*self._w] = rot.get(v, v)
        elif v == MINE:
            self._lost = True
        elif v == FREE:
            v = sum(1 for dx, dy in dirs
                    if self._get(x + dx, y + dy) in (MINE, TFLAG))
            self._bd[x + y*self._w] = v
            if v == 0:  # uncover all cells around
                for dx, dy in dirs:
                    self.play(x + dx, y + dy, "")
        self._won = not any(v in (FREE, FFLAG) for v in self._bd)

    def read(self, x: int, y: int) -> str:
        v = self._get(x, y)
        return ("💣" if v == MINE and self.finished() else
                "⚑" if v in (TFLAG, FFLAG) else
                str(v) if 1 <= v <= 8 else
                "" if v == 0 else "·")

    def finished(self) -> bool:
        return self._lost or self._won

    def status(self) -> str:
        return "Mine!" if self._lost else "Solved!" if self._won else ""

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    gui_play(Mines(10, 10, 5))
