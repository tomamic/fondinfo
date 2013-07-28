def zigzag(matrix: list):
    rows = len(matrix)
    cols = len(matrix[0])

    # initially: bottom-left cell, heading down-right
    x, y = 0, rows - 1
    dx, dy = +1, +1

    for i in range(rows * cols):
        matrix[y][x] = i

        x += dx
        y += dy

        # if out of bounds...
        if not (0 <= y < rows and 0 <= x < cols):
            # invert direction and go one step back
            dx, dy = -dx, -dy
            x += dx
            y += dy

            # shift along the border by one
            if x == cols - 1: y -= 1
            elif y == rows - 1: x += 1
            elif y == 0: x += 1
            elif x == 0: y -= 1

if __name__ == '__main__':
    rows = cols = 0
    while rows <= 0 or cols <= 0:
        rows = int(input('Rows? '))
        cols = int(input('Cols? '))

    matrix = [[0] * cols for y in range(rows)]
    zigzag(matrix)

    for y in range(rows):
        for x in range(cols):
            print('{:4}'.format(matrix[y][x]), end='')
        print()
