#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play
from boardgamegui import gui_play
from random import randrange

class LightsOut(BoardGame):
    '''https://en.wikipedia.org/wiki/Lights_Out_(game)'''

    def __init__(self, w=5, h=5, level=4):
        self._w, self._h = w, h
        self._board = [False] * (w*h)
        for _ in range(level):
            self.play_at(randrange(w), randrange(h))

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h

    def finished(self) -> bool:
        # https://docs.python.org/3/library/functions.html#any
        return not any(self._board)

    def play_at(self, x: int, y: int):
        '''Place (or remove) a light at cell (x, y)'''
        w, h = self._w, self._h
        if 0 <= x < w and 0 <= y < h:
            for dx, dy in ((0, 0), (0, -1), (1, 0),
                           (0, 1), (-1, 0)):
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < w and 0 <= y1 < h:
                    self._board[y1*w+x1] = not self._board[y1*w+x1]

    def flag_at(self, x: int, y: int):
        pass

    def value_at(self, x: int, y: int) -> str:
        w, h = self._w, self._h
        if 0 <= x < w and 0 <= y < h and self._board[y*w+x]:
            return '@'
        return '-'

    def message(self) -> str:
        return "Puzzle solved!"


def main():
    game = LightsOut()
    gui_play(game)
    ##console_play(game)

main()
