#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play

class TicTacToe(BoardGame):
    '''https://en.wikipedia.org/wiki/Tic-tac-toe'''

    def __init__(self, l=3):
        self._l = l
        self._bd = [0] * l**2  # clean board
        self._turn = 1 # 1 is X, -1 is O
        self._won = self._full = False

    def _get(self, x, y) -> int:  # -2 if outside of board
        bd, l = self._bd, self._l
        return bd[x + y*l] if (0 <= x < l and 0 <= y < l) else -2

    def _line(self, x, y, dx, dy) -> int:
        return all(self._get(x + i*dx, y + i*dy) == self._turn
                   for i in range(self._l))

    def play(self, x: int, y: int, action: str):
        if self._get(x, y) == 0:
            self._bd[x + y*self._l] = self._turn
            self._won = (self._line(x, 0, 0, 1) or  # column x
                         self._line(0, y, 1, 0) or  # row y
                         self._line(0, 0, 1, 1) or  # diagonals
                         self._line(self._l - 1, 0, -1, 1))
            self._full = all(self._bd)
            if not self.finished():
                self._turn *= -1

    def _sign(self, v: int):
        return "X" if v == 1 else "O" if v == -1 else ""

    def read(self, x: int, y: int) -> str:
        return self._sign(self._get(x, y))

    def finished(self) -> bool:
        return self._won or self._full

    def status(self) -> str:
        won, full, p = self._won, self._full, self._sign(self._turn)
        return f"{p} has won" if won else "Tie game" if full else f"{p} turn"

    def size(self) -> tuple[int, int]:
        return self._l, self._l


if __name__ == "__main__":
    from boardgamegui import gui_play
    game = TicTacToe(3)
    gui_play(game)
