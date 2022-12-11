#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d_pyodide as g2d
from boardgame import BoardGame
from boardgamegui import gui_play
from random import choice

class Fifteen(BoardGame):

    def __init__(self, w: int, h: int):
        self._w, self._h = w, h
        self._x0, self._y0 = w - 1, h - 1  # blank
        # start with sorted tiles: [1 2 ... 14 15 0]
        self._board = list(range(1, w * h)) + [0]
        self._solved = self._board[:]
        # then, random walk of the blank tile, until most tiles change
        # https://docs.python.org/3/library/functions.html#any
        # while any(map(eq, self._board, self._solved)):
        while self._board[-1] != 1:
            dx, dy = choice([(0, -1), (+1, 0), (0, +1), (-1, 0)])
            self.play_at(self._x0 + dx, self._y0 + dy)

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h

    def message(self) -> str:
        return "Puzzle solved!"

    def value_at(self, x: int, y: int) -> str:
        b, w, h = self._board, self._w, self._h
        if 0 <= y < h and 0 <= x < w and b[y * w + x] > 0:
            return str(b[y * w + x])
        return ""

    def play_at(self, x: int, y: int):
        x0, y0, w, h = self._x0, self._y0, self._w, self._h
        if 0 <= y < h and 0 <= x < w and abs(x - x0) + abs(y - y0) == 1:
            b, i, i0 = self._board, y * w + x, y0 * w + x0
            b[i0], b[i] = b[i], 0  # swap tile with blank
            self._x0, self._y0 = x, y

    def flag_at(self, x: int, y: int):
        return

    def finished(self) -> bool:
        return self._board == self._solved


gui_play(Fifteen(3, 3))
