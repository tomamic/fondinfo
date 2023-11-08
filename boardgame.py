#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def abstract():
    raise NotImplementedError("Abstract method")

class BoardGame:
    def play(self, x: int, y: int, action: str): abstract()
    def read(self, x: int, y: int) -> str: abstract()
    def size(self) -> tuple[int, int]: abstract()
    def finished(self) -> bool: abstract()
    def status(self) -> str: abstract()


def print_game(game: BoardGame):
    cols, rows = game.size()
    for y in range(rows):
        for x in range(cols):
            print(game.read(x, y) or "·", end="\t")
        print()
    print(game.status())

def console_play(game: BoardGame):
    print_game(game)

    while not game.finished():
        x, y, action = input("x y action?\n").split()
        game.play(int(x), int(y), action)
        print_game(game)
