#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from boardgame import BoardGame, console_play

symbol = ["", "x", "o"]  # 0, 1, -1

class TicTacToe(BoardGame):
    """https://en.wikipedia.org/wiki/Tic-tac-toe"""

    def __init__(self, l=3):
        self._l = l
        self._bd = [0] * l**2  # clean board
        self._turn = 1  # 1 is `x`, -1 is `o`
        self._won = self._tie = False

    def _get(self, x, y) -> int:  # -2 if outside of board
        bd, l = self._bd, self._l
        return bd[x + y*l] if (0 <= x < l and 0 <= y < l) else -2

    def _line(self, x, y, dx, dy) -> bool:
        # whole line filled with current symbol?
        return all(self._get(x + i*dx, y + i*dy) == self._turn
                   for i in range(self._l))

    def play(self, x: int, y: int, action: str):
        if self._get(x, y) == 0:
            self._bd[x + y*self._l] = self._turn
            self._won = (self._line(x, 0, 0, 1) or  # column x
                         self._line(0, y, 1, 0) or  # row y
                         self._line(0, 0, 1, 1) or  # diagonals
                         self._line(self._l - 1, 0, -1, 1))
            self._tie = not self._won and all(self._bd)
            if not self.finished():
                self._turn *= -1

    def read(self, x: int, y: int) -> str:
        return symbol[self._get(x, y)]

    def finished(self) -> bool:
        return self._won or self._tie

    def status(self) -> str:
        p = "None" if self._tie else symbol[self._turn]
        return f"{p} wins" if self.finished() else f"{p} plays"

    def cols(self) -> int:
        return self._l

    def rows(self) -> int:
        return self._l


if __name__ == "__main__":
    from boardgamegui import gui_play
    gui_play(TicTacToe(3))
