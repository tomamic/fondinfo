EMPTY = -1

def empty(matrix: list, x: int, y: int) -> bool:
    if 0 <= y < len(matrix) and 0 <= x < len(matrix[y]):
        return (matrix[y][x] == EMPTY)
    return False

if __name__ == '__main__':
    rows = int(input('Rows? '))
    cols = int(input('Cols? '))
    matrix = [[EMPTY for x in range(cols)] for y in range(rows)]

    # initially: bottom-left cell, heading up
    x, y = 0, rows - 1
    dx, dy = 0, -1

    for i in range(rows * cols):
        matrix[y][x] = i
        # advance
        x += dx
        y += dy
        # bounce against border or visited cell?
        if not empty(matrix, x, y):
            # go one step back
            x -= dx
            y -= dy
            # turn clockwise
            dx, dy = -dy, dx
            x += dx
            y += dy

    for y in range(rows):
        for x in range(cols):
            print('{:4}'.format(matrix[y][x]), end='')
        print()
