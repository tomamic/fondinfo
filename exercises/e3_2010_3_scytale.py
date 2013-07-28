infile = open('exer-3-2010-3-scytale.py')
text = infile.read()

with open('out.txt', 'w') as outfile:
    FILLER = ' '
    ROWS = 3
    COLS = 4

    matrix = [[' '] * COLS for y in range(ROWS)]
    i = 0
    while i < len(text):
        for y in range(ROWS):
            for x in range(COLS):
                if i < len(text):
                    matrix[y][x] = text[i]
                    i += 1
                else:
                    matrix[y][x] = FILLER

        for x in range(COLS):
            for y in range(ROWS):
                print(matrix[y][x], end='', file=outfile)
