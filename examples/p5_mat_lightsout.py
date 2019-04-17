#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play
from boardgame_g2d import gui_play
from random import randrange

class LightsOut(BoardGame):
    '''https://en.wikipedia.org/wiki/Lights_Out_(game)'''

    def __init__(self, side=5, level=4):
        self._cols, self._rows = side, side
        self._board = [[False for x in range(side)] for y in range(side)]
        for _ in range(level):
            self.play_at(randrange(side), randrange(side))

    def cols(self) -> int:
        return self._cols

    def rows(self) -> int:
        return self._rows

    def finished(self) -> bool:
        for y in range(self._rows):
            for x in range(self._cols):
                if self._board[y][x]:
                    return False
        return True

    def play_at(self, x: int, y: int):
        '''Place (or remove) a light at cell (x, y)'''
        if 0 <= x < self._cols and 0 <= y < self._rows:
            for dx, dy in ((0, 0), (0, -1), (1, 0),
                           (0, 1), (-1, 0)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < self._cols and 0 <= y1 < self._rows:
                    self._board[y1][x1] = not self._board[y1][x1]

    def flag_at(self, x: int, y: int):
        pass

    def value_at(self, x: int, y: int) -> str:
        if (0 <= x < self._cols and 0 <= y < self._rows and
            self._board[y][x]):
            return '@'
        return '-'

    def message(self) -> str:
        return "Puzzle solved!"


def main():
    game = LightsOut()
    gui_play(game)
    ##console_play(game)

main()
