cols = 0
rows = 0
matrix = []
with open('matrix.dat', 'r') as f:
    for line in f:
        row = list(line)
        row.pop()  # remove newline
        rows += 1
        if cols == 0:
            cols = len(row)
        matrix += row  # list concatenation
        # 4.9: matrix.append(row)

print(cols, rows)

for y in range(rows):
    for x in range(cols):
        print(matrix[y * cols + x], end='')
        # 4.9: print(matrix[y][x], end='')
    print()
