dirs = [(+1, -2), (+2, -1), (+2, +1), (+1, +2), (-1, +2), (-2, +1), (-2, -1), (-1, -2)]

def print_matrix(m: list, w: int, h: int):
    for y in range(h):
        for x in range(w):
            print(f"{m[y * w + x]:3}", end="")
        print()

def find_moves(m: list, w, h, x, y) -> list:
    moves = []
    for dx, dy in dirs:
        x1, y1 = x + dx, y + dy
        if 0 <= x1 < w and 0 <= y1 < h and m[y1 * w + x1] == 0:
            moves.append((x1, y1))
    return moves

def main():
    w = int(input("w? "))
    h = int(input("h? "))
    n, count = w * h, 1
    last_x, last_y = 0, 0
    matrix = [0] * n
    matrix[0] = count

    while count < n:
        print_matrix(matrix, w, h)
        x = int(input("x? "))
        y = int(input("y? "))
        if (x, y) in find_moves(matrix, w, h, last_x, last_y):
            count += 1
            matrix[y * w + x] = count
            last_x, last_y = x, y
    print_matrix(matrix, w, h)

main()
