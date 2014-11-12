import sys
sys.setrecursionlimit(15000)

delta = [(1, -2), (2, -1), (2, 1), (1, 2),
         (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

def find_moves(board, x, y) -> list:
    moves = []
    for d in delta:
        xm = x + d[0]
        ym = y + d[1]
        if (0 <= xm < len(board[0]) and
            0 <= ym < len(board) and
            board[ym][xm] == 0):
            moves.append((xm, ym))
    return moves

def distance_from_border(x, y, w, h):
    dist_x = min(x, w - x)
    dist_y = min(y, h - y)
    return dist_x + dist_y

def knight_tour(board, x, y, n) -> bool:
    board[y][x] = n
    # is this the last move?
    w, h = len(board[0]), len(board)
    if n == w * h: return True

    moves = find_moves(board, x, y)
##    moves.sort(key=lambda elem:
##            distance_from_border(elem[0], elem[1], w, h))
##    moves.sort(key=lambda elem:
##               len(find_moves(board, elem[0], elem[1])))

    for (xm, ym) in moves:
            # move the knight this way
            if knight_tour(board, xm, ym, n + 1): return True

    # no luck this way, go back (backtracking)
    board[y][x] = 0
    return False

if __name__ == '__main__':
    size = int(input('size? '))
    w, h = size, size
    board = [[0 for x in range(w)] for y in range(h)]

    print(knight_tour(board, 0, 0, 1))

    for y in range(h):
        for x in range(w):
            print(("{:5}").format(board[y][x]), end='')
        print()
