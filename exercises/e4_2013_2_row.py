def advance(row: list, dx: int, dy: int):
    head_x, head_y = row[-1]
    row.append((head_x + dx, head_y + dy))
    row.pop(0)
    
def show(row: list, cols: int, rows: int):
    for y in range(rows):
        for x in range(cols):
            if (x, y) in row:
                print('*', end='')
            else:
                print('-', end='')
        print()

def main():
    COLS, ROWS = 16, 12
    row  = [(1, 1), (2, 1), (3, 1), (4, 1)]
    show(row, COLS, ROWS)
    dx = int(input('dx? '))
    dy = int(input('dy? '))
    while dx in [-1, 0, 1] and dy in [-1, 0, 1]:
        advance(row, dx, dy)
        show(row, COLS, ROWS)
        dx = int(input('dx? '))
        dy = int(input('dy? '))

if __name__ == '__main__':
    main()
