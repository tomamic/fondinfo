#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

from p42_connect4 import Connect4, gui_play
from copy import deepcopy
from math import inf
from random import sample, shuffle, random

class Connect4AI(Connect4):
    def _value(self):
        count = self._winner * (10000 + 100 * self._board.count(0))
        for y in range(self._h):
            count += (1 + y) * self._get(self._w // 2, y)  # pieces in middle column
            for x in range(self._w):
                for v in (1, -1):
                    if self._get(x, y) == 0 and self._around(x, y, v) >= 3:
                        count += v * (1 + y)
        return count

    def _negamax(self, depth, alpha=-inf, beta=+inf):
        if depth == 0 or self.finished():
            return self._turn * self._value(), self._move[0]
        value, move = -inf, inf
        children = []
        for x in range(self._w):
            if self._get(x, 0) == 0:
                child = deepcopy(self)
                child.play(x, 0)
                children.append((self._turn * child._value(), random(), child))
        for _, _, child in reversed(sorted(children)):
            v, _ = child._negamax(depth - 1, -beta, -alpha)
            value, move = max((value, move), (-v, child._move[0]))
            alpha = max(alpha, value)
            if alpha >= beta:
                break # α-β cutoff
        return value, move

    def play(self, x: int, y: int, command=""):
        if command == "flag":
            _, x = self._negamax(6)
        super().play(x, y)

if __name__ == "__main__":
    gui_play(Connect4AI(7, 6))
