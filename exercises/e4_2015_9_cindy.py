#!/usr/bin/env python3
'''
- You have some number `n` of black marbles and the same number of white marbles
- You have a playing board which consists simply of a line of `2n+1` spaces to put the marbles in
- Start with the black marbles all at one end (say, the left), the white marbles all at the other end, and a free space in between
- The *goal* is to reverse the positions of the marbles
- The black marbles can only move to the right, and the white marbles can only move to the left (no backing up)
- At each move, a marble can either:
    - Move one space ahead, if that space is clear, or
    - Jump ahead over exactly one marble of the opposite color, if the space just beyond that marble is clear

@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def get_move(board: list, x: int) -> int:
    if board[x:x+2] == ['b', '_']:
        return 1
    elif board[x:x+3] == ['b', 'w', '_']:
        return 2
    elif board[x-1:x+1] == ['_', 'w']:
        return -1
    elif board[x-2:x+1] == ['_', 'b', 'w']:
        return -2
    return 0

def solve(board, solution, level=0) -> bool:
    print('  ' * level + ''.join(board))  # just for debug
    if board == solution:
        return True

    for x in range(len(board)):
        m = get_move(board, x)
        if m != 0:
            board[x], board[x + m] = board[x + m], board[x]
            
            if solve(board, solution, level + 1):
                return True
            
            # no luck: backtrack
            board[x], board[x + m] = board[x + m], board[x]
                
    return False

n = int(input('n? '))
board = ['b'] * n + ['_'] + ['w'] * n
solution = ['w'] * n + ['_'] + ['b'] * n
print(solve(board, solution))
