#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def abstract():
    raise NotImplementedError("Abstract method")

class BoardGame:
    def play(self, x: int, y: int, action: str): abstract()
    def read(self, x: int, y: int) -> str: abstract()
    def cols(self) -> int: abstract()
    def rows(self) -> int: abstract()
    def finished(self) -> bool: abstract()
    def status(self) -> str: abstract()


def print_game(game: BoardGame):
    for y in range(game.rows()):
        for x in range(game.cols()):
            print(game.read(x, y) or "·", end="\t")
        print()
    print(game.status())

def console_play(game: BoardGame):
    print_game(game)

    while not game.finished():
        x, y, action = input("x y action?\n").split()
        game.play(int(x), int(y), action)
        print_game(game)
