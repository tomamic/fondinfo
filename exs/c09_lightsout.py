#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
from boardgame import BoardGame, console_play
from random import sample

class LightsOut(BoardGame):
    """https://en.wikipedia.org/wiki/Lights_Out_(game)"""

    def __init__(self, w=5, h=5, level=4):
        self._w, self._h = w, h
        self._board = [False] * (w * h)
        for i in sample(range(w * h), level):
            self.play(i % w, i // w, "")
        self._solved = False
        # TODO: count available moves (= level)

    def _get(self, x, y) -> bool | None:
        if 0 <= x < self._w and 0 <= y < self._h:
            return self._board[y * self._w + x]  # if outside, None

    def play(self, x: int, y: int, action: str):
        if self._get(x, y) != None:  # is the cell within the board?
            for dx, dy in [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]:
                x1, y1 = x + dx, y + dy
                v = self._get(x1, y1)
                if v != None:  # is this neighbor cell in the board?
                    self._board[x1 + y1 * self._w] = not v
            self._solved = not any(self._board)

    def read(self, x: int, y: int) -> str:
        return "@" if self._get(x, y) else "-"

    def finished(self) -> bool:
        return self._solved

    def status(self) -> str:
        return "Puzzle solved!" if self._solved else "Playing"

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h


if __name__ == "__main__":
    from boardgamegui import gui_play
    game = LightsOut()
    gui_play(game)
