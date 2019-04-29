#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play
from boardgame_g2d import gui_play
from random import choice

class Fifteen(BoardGame):

    def __init__(self, w: int, h: int):
        # start with sorted tiles, then...
        b = list(range(1, w * h)) + [0]  # [1 2 3 ... 14 15 0]
        self._board, self._solved = b, b[:]
        self._w, self._h = w, h
        self._x0, self._y0 = w - 1, h - 1  # blank
        a1, a2 = w - 1, (h - 1) * w
        # do a random walk of the blank tile, until all angle tiles change
        while (b[0] == 1 or b[a1] == a1 + 1 or b[a2] == a2 + 1):
            dx, dy = choice([(0, -1), (+1, 0), (0, +1), (-1, 0)])
            self.play_at(self._x0 + dx, self._y0 + dy)
            # https://docs.python.org/3/library/functions.html#any

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
            b, i0, i1 = self._board, y0 * w + x0, y * w + x
            b[i0], b[i1] = b[i1], 0  # swap tile with blank
            self._x0, self._y0 = x, y

    def flag_at(self, x: int, y: int):
        pass

    def finished(self) -> bool:
        return self._board == self._solved

def main():
    game = Fifteen(3, 3)
    gui_play(game)
    ##console_play(game)

main()
