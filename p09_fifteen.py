#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play
from random import choice

class Fifteen(BoardGame):
    def __init__(self, w: int, h: int):
        if w * h < 2:
            raise ValueError("Fifteen needs at least two cells")
        self._w, self._h = w, h
        # start with sorted tiles: [1 2 ... 14 15 0]
        self._board = list(range(1, w * h)) + [0]  # game board
        self._solved = self._board[:]
        self._x0, self._y0 = w - 1, h - 1  # blank
        # then, random walk of the blank tile, until most tiles change
        # while any(a == b for a, b in zip(self._board, self._solved)):
        while self._board[-1] != 1:
            dx, dy = choice([(0, -1), (+1, 0), (0, +1), (-1, 0)])
            self.play(self._x0 + dx, self._y0 + dy, "")
        self._finished = False

    def _get(self, x, y) -> int:
        bd, w, h = self._board, self._w, self._h
        return bd[y * w + x] if (0 <= x < w and 0 <= y < h) else -1

    def play(self, x: int, y: int, action: str):
        v, x0, y0 = self._get(x, y), self._x0, self._y0
        if v > 0 and abs(x - x0) + abs(y - y0) == 1:
            self._board[y0 * self._w + x0] = v
            self._board[y * self._w + x] = 0
            self._x0, self._y0 = x, y  # swap tile with blank
        self._finished = self._board == self._solved

    def read(self, x: int, y: int) -> str:
        v = self._get(x, y)
        return str(v) if v > 0 else ""

    def finished(self) -> bool:
        return self._finished

    def status(self) -> str:
        return "Puzzle solved!" if self._finished else "Playing"

    def size(self) -> tuple[int, int]:
        return self._w, self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    game = Fifteen(3, 3)
    ##console_play(game)
    gui_play(game)
