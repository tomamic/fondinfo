#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class BoardGame:
    
    def play_at(self, x: int, y: int):
        raise NotImplementedError("Abstract method")
    
    def get_val(self, x: int, y: int) -> str:
        raise NotImplementedError("Abstract method")
    
    def cols(self) -> int:
        raise NotImplementedError("Abstract method")
    
    def rows(self) -> int:
        raise NotImplementedError("Abstract method")
    
    def finished(self) -> bool:
        raise NotImplementedError("Abstract method")
    
    def message(self) -> str:
        raise NotImplementedError("Abstract method")
    

def print_game(game: BoardGame):
    for y in range(game.rows()):
        for x in range(game.cols()):
            print('{:3}'.format(game.get_val(x, y)), end='')
        print()

def console_play(game: BoardGame):
    print_game(game)
    
    while not game.finished():
        x, y = input().split()
        game.play_at(int(x), int(y))
        print_game(game)
        
    print(game.message())

