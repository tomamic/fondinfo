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
    
    def size(self) -> (int, int):
        raise NotImplementedError("Abstract method")
    
    def finished(self) -> bool:
        raise NotImplementedError("Abstract method")
    
    def message(self) -> str:
        raise NotImplementedError("Abstract method")
    

class Knights(BoardGame):
    
    def __init__(self, cols: int, rows: int, n: int):
        self._cols = cols
        self._rows = rows
        self._n = n
        self._dirs = ((-1, -2), (+1, -2), (+2, -1), (+2, +1),
                      (+1, +2), (-1, +2), (-2, +1), (-2, -1))  # dx, dy
        self._board = [[False for x in range(cols)] for y in range(rows)]

    def size(self) -> (int, int):
        return self._cols, self._rows

    def _covered(self, x: int, y: int) -> bool:
        for dx, dy in self._dirs:
            if (0 <= x + dx < self._cols and
                0 <= y + dy < self._rows and
                self._board[y + dy][x + dx]):
                return True
        return False

    def finished(self) -> bool:
        '''Puzzle solved?'''
        knights = 0
        for y in range(self._rows):
            for x in range(self._cols):
                if self._board[y][x]:
                    knights += 1
                elif not self._covered(x, y):
                    return False
        return self._n == knights

    def play_at(self, x: int, y: int):
        if 0 <= x < self._cols and 0 <= y < self._rows:
            self._board[y][x] = not self._board[y][x]

    def get_val(self, x: int, y: int) -> str:
        if not (0 <= x < self._cols and 0 <= y < self._rows):
            return  '!'
        if self._board[y][x]:
            return 'K'
        return '-'

    def message(self) -> str:
        return "Puzzle solved!"

    def __str__(self):
        '''Get a string representaion of the game'''
        result = []
        for y in range(self._rows):
            for x in range(self._cols):
                result.append(self.get_val(x, y))
            result.append('\n')
        return "".join(result)
        

def console_play(game: BoardGame):
    print(game)
    
    while not game.finished():
        x, y = input().split()
        game.play_at(int(x), int(y))
        print(game)
        
    print(puzzle.message())

def main():
    # solutions = (0, 1, 4, 4, 4, 5, 8, 10, 12, 14, 16, 21, 24, 28, 32, 36, 40, 46, 52, 57, 62)

    game = Knights(6, 6, 8)
    console_play(game)

if __name__ == '__main__':
    main()
