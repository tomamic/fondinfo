import sys

class TicTacToe:
    NONE = '.'
    PLR1 = 'X'
    PLR2 = 'O'
    DRAW = 'None'
    OUT = '!'

    def __init__(self, side=3):
        self._side = side
        self._matrix = [TicTacToe.NONE] * (self._side * self._side)
        self.clear()

    def clear(self):
        for i in range(len(self._matrix)):
            self._matrix[i] = TicTacToe.NONE
        self._turn = 0

    def play_at(self, x: int, y: int):
        if self.get(x, y) == TicTacToe.NONE:
            i = x + y * self._side
            if self._turn % 2 == 0:
                self._matrix[i] = TicTacToe.PLR1
            else:
                self._matrix[i] = TicTacToe.PLR2
            self._turn += 1

    def get(self, x: int, y: int) -> str:
        if 0 <= x < self._side and 0 <= y < self._side:
            return self._matrix[x + y * self._side]
        else:
            return TicTacToe.OUT

    def _check_line(self, x: int, y: int, dx: int, dy: int) -> bool:
        '''Check a single line, starting at (x, y) and
        advancing for `side` steps in direction (dx, dy).
        If a single player occupies all cells, he's won.'''
        player = self.get(x, y)
        if player == TicTacToe.NONE:
            return False
        for i in range(self._side):
            if self.get(x + dx * i, y + dy * i) != player:
                return False
        return True

    def winner(self) -> str:
        '''Check all rows, columns and diagonals.
        Otherwise, check if the game is tied.'''
        for x in range(self._side):
            if self._check_line(x, 0, 0, 1):
                return self.get(x, 0)
        for y in range(self._side):
            if self._check_line(0, y, 1, 0):
                return self.get(0, y)
        if self._check_line(0, 0, 1, 1):
            return self.get(0, 0)
        if self._check_line(self._side - 1, 0, -1, 1):
            return self.get(self._side - 1, 0)
        if self._turn == self._side * self._side:
            return TicTacToe.DRAW
        return TicTacToe.NONE

    def side(self) -> int:
        return self._side

    def __str__(self):
        out = ''  # Using a StringIO is more efficient
        for y in range(self._side):
            for x in range(self._side):
                out += self._matrix[y * self._side + x]
            out += '\n'
        return out

def main():
    game = TicTacToe(4)
    print(game)
    
    x = int(input('x? '))
    y = int(input('y? '))
    while x >= 0 and y >= 0:
        game.play_at(x, y)
        print(game)
        winner = game.winner()
        if winner != TicTacToe.NONE:
            print('Game finished.', winner, 'has won!')
            game.clear()
            print(game)
        x = int(input('x? '))
        y = int(input('y? '))

if __name__ == '__main__':
    main()
