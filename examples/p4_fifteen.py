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
        self._cols = cols
        self._rows = rows
        self._solution = list(range(1, cols * rows)) + [0]

        '''Sort the game, matching its solution'''
        self._board = list(self._solution)  # copy the list
        self._blx, self._bly = self._cols - 1, self._rows - 1

        '''Do a random walk of the blank cell'''
        while self.finished():
            for _ in range(len(self._board) ** 2):
                dx, dy = choice(((0, -1), (+1, 0), (0, +1), (-1, 0)))
                self.play_at(self._blx + dx, self._bly + dy)

    def cols(self) -> int:
        return self._cols

    def rows(self) -> int:
        return self._rows

    def finished(self) -> bool:
        '''Puzzle solved'''
        return self._board == self._solution

    def move_val(self, val: int):
        '''Search around the blank cell,
           if val is found in a cell,
           then swap it with the blank cell'''
        if val < 1 or val >= len(self._board):
            return
        x0, y0 = self._blank
        for dx, dy in self._DIRS:
            x, y = x0 + dx, y0 + dy
            if (self.get(x, y) == val):
                self._swap_blank_with(x, y)
                return

    def play_at(self, x: int, y: int):
        if (0 <= y < self._rows and 0 <= x < self._cols and
            abs(self._blx - x) + abs(self._bly - y) == 1):
            moved = y * self._cols + x
            blank = self._bly * self._cols + self._blx
            self._board[blank] = self._board[moved]
            self._board[moved] = 0
            self._blx, self._bly = x, y

    def get_val(self, x: int, y: int) -> str:
        if (0 <= y < self._rows and 0 <= x < self._cols and
            self._board[y * self._cols + x] > 0):
            return str(self._board[y * self._cols + x])
        return ""

    def message(self) -> str:
        return "Puzzle solved!"


def main():
    game = Fifteen(3, 2)
    ##return console_play(game)
    gui = BoardGameGui(game)
    gui.main_loop()

if __name__ == '__main__':
    main()
