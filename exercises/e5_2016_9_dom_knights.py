#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys, time
sys.setrecursionlimit(15000)

delta = [(1, -2), (2, -1), (2, 1), (1, 2),
         (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

def find_moves(board: list, pos: int) -> list:
    '''find all cells covered by a knight in position `pos`.
       these cells include the position `pos` itself.
    '''
    moves = [pos]
    side = int(len(board) ** 0.5)
    x, y = pos % side, pos // side
    for dx, dy in delta:
        xm, ym = x + dx, y + dy
        m = ym * side + xm
        if 0 <= xm < side and 0 <= ym < side and board[m] == 0:
            moves.append(m)
    return moves

def set_knight(board: list, cover: list, pos: int, val: int) -> None:
    '''place a knight in position `pos`.
       if sign is -1, remove the knight.
    '''
    board[pos] += val
    for m in find_moves([0] * len(board), pos):
        cover[m] += val

def dominate(board: list, cover: list, n: int) -> bool:
    if n == 0:
        return 0 not in cover

    # try each cell, among those covering the first zero
    moves = find_moves(board, cover.index(0))
    
##    zeros = [i for i, val in enumerate(cover) if val == 0]
##    pos_zero = min(zeros, key=lambda i: len(find_moves(board, i)))
##    moves = find_moves(board, pos_zero)
##    moves.sort(key=lambda i: -len(find_moves(cover, i)))

    for m in moves:
        set_knight(board, cover, m, +1)
        if dominate(board, cover, n - 1):
            return True
        set_knight(board, cover, m, -1)
    return False

def print_board(board: list):
    side = int(len(board) ** 0.5)
    for y in range(side):
        for x in range(side):
            if board[y * side + x] == 1:
                print('|@', end='')
            else:
                print('| ', end='')
        print('|')

def main():
    knights = (0, 1, 4, 4, 4, 5, 8, 10, 12, 14, 16, 21, 24, 28, 32, 36, 40, 46, 52, 57, 62)

    side = int(input('board? '))
    n = knights[side]
    board = [0] * (side * side)
    cover = [0] * (side * side)

    start = time.time()
    if dominate(board, cover, n):
        print(time.time() - start)
        print_board(board)

if __name__ == '__main__':
    main()
