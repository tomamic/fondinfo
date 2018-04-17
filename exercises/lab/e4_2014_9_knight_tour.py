#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import sys
sys.setrecursionlimit(15000)


delta = [(1, -2), (2, -1), (2, 1), (1, 2),
         (-1, 2), (-2, 1), (-2, -1), (-1, -2)]


def find_moves(board, x0, y0) -> list:
    w, h = len(board[0]), len(board)
    moves = []
    for dx, dy in delta:
        x, y = x0 + dx, y0 + dy
        if (0 <= x < w and 0 <= y < h and board[y][x] == 0):
            moves.append((x, y))
    return moves


def border_distance(x, y, w, h):
    dist_x = min(x, w - x)
    dist_y = min(y, h - y)
    # return dist_x + dist_y
    return sorted((dist_x, dist_y))


def knight_tour(board, x, y) -> bool:
    w, h = len(board[0]), len(board)
    n = board[y][x]
    if n == w * h: return True

    moves = find_moves(board, x, y)
##    moves.sort(key=lambda m: border_distance(m[0], m[1], w, h))
##    moves.sort(key=lambda m: len(find_moves(board, m[0], m[1])))

    # try each possible move (recursively)
    for xm, ym in moves:
        board[ym][xm] = n + 1

        if knight_tour(board, xm, ym): return True

        # no luck this way, go back (backtracking)
        board[ym][xm] = 0
    return False


def main():
    w = h = int(input('size? '))
    board = [[0 for x in range(w)] for y in range(h)]
    board[0][0] = 1

    print(knight_tour(board, 0, 0))

    for y in range(h):
        for x in range(w):
            print(("{:5}").format(board[y][x]), end='')
        print()

if __name__ == '__main__':
    main()
