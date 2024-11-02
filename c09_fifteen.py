#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from boardgame import BoardGame, console_play
from random import choice

class Fifteen(BoardGame):
    def __init__(self, w: int, h: int):
        # init board with sorted tiles: [1 2 ... 14 15 0]
        self._bd = list(range(1, w * h)) + [0]
        self._x0, self._y0 = w - 1, h - 1  # blank
        self._won = True
        self._w, self._h = w, h

        # then, random walk of the blank tile, until most tiles change
        while w * h > 1 and self._bd[-1] != 1:
            dx, dy = choice([(0, -1), (1, 0), (0, 1), (-1, 0)])
            self.play(self._x0 + dx, self._y0 + dy, "")

    def play(self, x: int, y: int, action: str):
        w, h, bd, x0, y0 = self._w, self._h, self._bd, self._x0, self._y0
        if 0 <= x < w and 0 <= y < h and abs(x-x0) + abs(y-y0) == 1:
            bd[y0 * w + x0] = bd[y * w + x]  # swap tiles
            bd[y * w + x] = 0
            self._x0, self._y0 = x, y  # blank
            self._won = self._sorted()  # hint: use `all`, instead

    def _sorted(self) -> bool:
        for i in range(self._w * self._h - 1):
            if self._bd[i] != i + 1:
                return False
        return True

    def read(self, x: int, y: int) -> str:
        w, h, bd = self._w, self._h, self._bd
        if 0 <= x < w and 0 <= y < h and bd[y * w + x]:
            return str(bd[y*w + x])
        return ""

    def finished(self) -> bool:
        return self._won

    def status(self) -> str:
        if self._won:
            return "Puzzle solved!"
        return "Playing"

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    game = Fifteen(4, 4)
    ##console_play(game)
    gui_play(game)
