#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

from boardgame import BoardGame, console_play
from random import choice

class Fifteen(BoardGame):
    def __init__(self, w: int, h: int):
        self._w, self._h = w, h
        self._won = True  # sorted board tiles: [1 2 ... 14 15 0]
        self._bd = bd = list(range(1, w * h)) + [0]
        self._x0, self._y0 = w - 1, h - 1  # blank
        while w * h > 1 and bd[-1] != 1: # random walk of blank tile
            dx, dy = choice([(0, -1), (1, 0), (0, 1), (-1, 0)])
            self.play(self._x0 + dx, self._y0 + dy, "")

    def play(self, x: int, y: int, action: str):
        w, h, bd, x0, y0 = self._w, self._h, self._bd, self._x0, self._y0
        if 0<=x<w and 0<=y<h and abs(x-x0) + abs(y-y0) == 1:
            bd[y0*w + x0], bd[y*w + x] = bd[y*w + x], 0  # swap tiles
            self._x0, self._y0 = x, y  # blank
            self._won = all(v in (0, i+1) for i, v in enumerate(bd))

    def read(self, x: int, y: int) -> str:
        w, h, bd = self._w, self._h, self._bd
        return str(bd[y*w + x]) if 0<=x<w and 0<=y<h and bd[y*w + x] else ""

    def finished(self) -> bool:
        return self._won

    def status(self) -> str:
        return "Puzzle solved!" if self._won else "Playing"

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    game = Fifteen(2, 2)
    ##console_play(game)
    gui_play(game)
