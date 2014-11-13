import sys
sys.setrecursionlimit(15000)

delta = [(1, -2), (2, -1), (2, 1), (1, 2),
         (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

def find_moves(board, x0, y0) -> list:
    w, h = len(board[0]), len(board)
    moves = []
    for d in delta:
        x, y = x0 + d[0], y0 + d[1]
        if (0 <= x < w and 0 <= y < h and board[y][x] == 0):
            moves.append((x, y))
    return moves

def border_distance(x, y, w, h):
    dist_x = min(x, w - x)
    dist_y = min(y, h - y)
    # return dist_x + dist_y
    return sorted((dist_x, dist_y))

def knight_tour(board, x, y, n) -> bool:
    board[y][x] = n
    # is this the last move?
    w, h = len(board[0]), len(board)
    if n == w * h: return True

    moves = find_moves(board, x, y)
##    moves.sort(key=lambda m: border_distance(m[0], m[1], w, h))
##    moves.sort(key=lambda m: len(find_moves(board, m[0], m[1])))

    # try each possible move (recursively)
    for (xm, ym) in moves:
        if knight_tour(board, xm, ym, n + 1): return True

    # no luck this way, go back (backtracking)
    board[y][x] = 0
    return False

if __name__ == '__main__':
    w = h = int(input('size? '))
    board = [[0 for x in range(w)] for y in range(h)]

    print(knight_tour(board, 0, 0, 1))

    for y in range(h):
        for x in range(w):
            print(("{:5}").format(board[y][x]), end='')
        print()
