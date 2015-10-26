'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from io import StringIO

def board_str(board: list):
    output = StringIO()
    for row in board:
        for cell in row:
            if cell: output.write('|Q')
            else: output.write('| ')
        output.write('|\n')
    return output.getvalue()

def under_attack_(board: list, row: int, col: int) -> bool:
    # for each direction up-left, up, up-right (no queens below)...
    dy = -1
    for dx in [-1, 0, +1]:
        # walk till finding a queen, or border
        x, y = col + dx, row + dy
        while 0 <= y < len(board) and 0 <= x < len(board[y]):

            # if a queen is found, the square is under attack
            if board[y][x]: return True
            x, y = x + dx, y + dy
    return False

def place_queens_(board: list, row=0) -> bool:
    for col in range(len(board[row])):
        if not under_attack_(board, row, col):
            # square not attacked, place a queen
            board[row][col] = True

            # is this the last row?
            if row == len(board) - 1:
                return True

            # else, place queens in the following rows
            if place_queens_(board, row + 1):
                return True

            # no luck this way, remove the queen
            board[row][col] = False  # (backtracking)
    return False

def print_board(board: list):
    for y in range(len(board)):
        for x in range(len(board)):
            if x == board[y]: print('|Q', end='')
            else: print('| ', end='')
        print('|')

def under_attack(board: list, x: int, y: int) -> bool:
    for i in range(y):
        d = y - i
        # directions: ↖↑↗ (no queens below)
        if board[i] in (x - d, x, x + d):
            return True
    return False

def place_queens(board: list, y=0) -> bool:
    if y == len(board):
        return True  # all queens already placed
    for x in range(len(board)):
        if not under_attack(board, x, y):
            board[y] = x  # (x, y) is safe: place a queen

            # try and place queens in the following rows
            if place_queens(board, y + 1):
                return True

            board[y] = None  # no luck, backtrack
    return False

if __name__ == '__main__':
    side = int(input('side? '))
    board = [None] * side

    # solution: place queens starting from first row
    place_queens(board)
    print_board(board)
