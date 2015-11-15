#!/usr/bin/python2

from random import choice
from sys import argv, stdin                          

class Game:
    
    def play_at(self, x, y):
        raise NotImplementedError("Abstract method")
    
    def get_val(self, x, y):
        raise NotImplementedError("Abstract method")
    
    def size(self):
        raise NotImplementedError("Abstract method")
    
    def is_finished(self):
        raise NotImplementedError("Abstract method")
    
    def get_message(self):
        raise NotImplementedError("Abstract method")
    

class Fifteen(Game):
    
    _DIRS = ((0, -1), (+1, 0), (0, +1), (-1, 0))  # dx, dy

    def __init__(self, cols, rows):
        self._cols = cols
        self._rows = rows
        self._SOLUTION = list(range(1, cols * rows)) + [0]
        self.new_game()

    def new_game(self):
        '''Sort the game, matching its solution'''
        self._board = list(self._SOLUTION)  # copy the list
        self._blank = (self._cols - 1, self._rows - 1)
        self._moved = self._blank

        '''Do a random walk of the blank cell'''
        for _ in range(len(self._board) ** 2):
            x0, y0 = self._blank
            dx, dy = choice(self._DIRS)
            x, y = x0 + dx, y0 + dy
            self._swap_blank_with(x, y)

    def size(self):
        return self._cols, self._rows

    def is_finished(self):
        '''Puzzle solved'''
        return self._board == self._SOLUTION

    def blank(self):
        '''Position of blank cell'''
        return self._blank

    def moved(self):
        '''Position of last moved cell'''
        return self._moved


    def move_val(self, val):
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

    def play_at(self, x, y):
        self.move_val(self.get(x, y))

    def get(self, x, y):
        '''Get the content of a cell,
           or -1 if (x, y) out of range'''
        if 0 <= y < self._rows and 0 <= x < self._cols:
            return self._board[y * self._cols + x]
        return -1

    def get_val(self, x, y):
        val = self.get(x, y)
        if val <= 0: return ""
        return str(val)

    def _swap_blank_with(self, x, y):
        '''Swap the blank cell with a neighbor cell'''
        x0, y0 = self._blank
        val = self.get(x, y)
        if val > 0:
            self._board[y * self._cols + x] = 0
            self._board[y0 * self._cols + x0] = val
            self._blank = x, y
            self._moved = x0, y0

    def get_message(self):
        return "Puzzle solved!"

    def __str__(self):
        '''Get a string representaion of the game'''
        result = ""
        for y in range(self._rows):
            for x in range(self._cols):
                result += ('{:3}'.format(self.get(x, y)))
            result += '\n'
        return result
        

def main():
    puzzle = Fifteen(4, 4)
    print(puzzle)
    
    for line in stdin:
        puzzle.move_val(int(line))
        print(puzzle)
        
        if puzzle.is_finished():
            print('Congatulations!')
            puzzle.new_game()
            print(puzzle)

if __name__ == '__main__':
    main()
