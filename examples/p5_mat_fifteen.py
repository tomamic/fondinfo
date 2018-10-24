#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play
from boardgame_g2d import BoardGameGui
from random import choice

class Fifteen(BoardGame):

    def __init__(self, cols: int, rows: int):
        self._w, self._h = cols, rows
        self._x0, self._y0 = cols - 1, rows - 1  # blank
        
        # Start with sorted cells, then...
        # do a random walk of the blank cell
        self._board = list(range(1, cols * rows)) + [0]
        self._solution = list(self._board)
        while self.finished():
            for _ in range((cols * rows) ** 2):
                dx, dy = choice(((0, -1), (+1, 0), (0, +1), (-1, 0)))
                self.play_at(self._x0 + dx, self._y0 + dy)

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h

    def finished(self) -> bool:
        return self._board == self._solution

    def play_at(self, x: int, y: int):
        x0, y0, w, h = self._x0, self._y0, self._w, self._h
        if 0 <= y < h and 0 <= x < w and abs(x - x0) + abs(y - y0) == 1:
            board, i0, i1 = self._board, y0 * w + x0, y * w + x
            board[i0], board[i1] = board[i1], 0  # swap cell with blank
            self._x0, self._y0 = x, y

    def flag_at(self, x: int, y: int):
        pass

    def get_val(self, x: int, y: int) -> str:
        w, h, board = self._w, self._h, self._board
        if 0 <= y < h and 0 <= x < w and board[y * w + x] > 0:
            return str(board[y * w + x])
        return ""

    def message(self) -> str:
        return "Puzzle solved!"


def main():
    game = Fifteen(3, 3)
    ##return console_play(game)
    gui = BoardGameGui(game)
    gui.main_loop()

main()
