matrix = []
cols, rows = 0, 0

with open('matrix.csv', 'r') as file1:
    for line in file1:
        splitted = line.split(',')
        vals = [int(i) for i in splitted]
        if cols == 0: cols = len(vals)
        matrix.append(vals)
        ## matrix += vals  # for a simple list (ex. 4.5)
        rows += 1

print(cols, 'x', rows)
print(matrix)

total = 0
x, y = cols - 1, rows - 1
while x >= 0 and y >= 0:
    total += matrix[y][x]
    ## total += matrix[y * cols + x]  # for a simple list (ex. 4.5)
    x -= 1
    y -= 1
print(total)
