#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def print_board(board: list):
    for y in range(len(board)):
        for x in range(len(board)):
            if x == board[y]: print('|♛', end='')
            else: print('| ', end='')
        print('|')

def under_attack(board: list, x: int, y: int) -> bool:
    for d in range(1, y + 1):  # for all rows above y
        # directions: ↖↑↗ (no queens below)
        if board[y - d] in (x - d, x, x + d):
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

def main():
    side = int(input('side? '))
    board = [None] * side

    # solution: place queens starting from first row
    place_queens(board)
    print_board(board)

main()
