#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play
from random import choice

class Fifteen(BoardGame):
    def __init__(self, w: int, h: int):
        if w < 2 or h < 2:
            raise ValueError("Fifteen needs at least 2×2 cells")
        self._w, self._h = w, h
        # init game board with sorted tiles: [1 2 ... 14 15 0]
        self._bd = list(range(1, w * h)) + [0]
        self._solution = self._bd[:]
        self._x0, self._y0 = w - 1, h - 1  # blank
        # then, random walk of the blank tile, until most tiles change
        while self._bd[-1] != 1:
            dx, dy = choice([(0, -1), (1, 0), (0, 1), (-1, 0)])
            self.play(self._x0 + dx, self._y0 + dy, "")

    def _get(self, x, y) -> int:  # -1 if outside of board
        w, h = self.size()
        return self._bd[x + y*w] if (0<=x<w and 0<=y<h) else -1

    def play(self, x: int, y: int, action: str):
        v, x0, y0 = self._get(x, y), self._x0, self._y0
        if v > 0 and abs(x - x0) + abs(y - y0) == 1:
            self._bd[x0 + y0*self._w] = v
            self._bd[x + y*self._w] = 0
            self._x0, self._y0 = x, y  # tile @ (x, y) ⇆ blank

    def read(self, x: int, y: int) -> str:
        v = self._get(x, y)
        return str(v) if v > 0 else ""

    def finished(self) -> bool:
        return self._bd == self._solution

    def status(self) -> str:
        return "Puzzle solved!" if self.finished() else "Playing"

    def size(self) -> tuple[int, int]:
        return self._w, self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    game = Fifteen(3, 3)
    ##console_play(game)
    gui_play(game)
