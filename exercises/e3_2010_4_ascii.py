FIRST = 32
LAST = 126
ROWS = 10
COLS = 10

for y in range(ROWS):
    for x in range(COLS):
        i = FIRST + y + x * ROWS
        if i <= LAST:
            print('{:3} {} '.format(i, chr(i)), end='')
    print()
