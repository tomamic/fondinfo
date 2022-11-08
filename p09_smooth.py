#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def avg(matrix: list, rows: int, cols: int, x0: int, y0: int) -> int:
    dirs = ((0, 0), (0, -1), (+1, 0), (0, +1), (-1, 0))
    count, total = 0, 0
    for dx, dy in dirs:
        x1, y1 = x0 + dx, y0 + dy
        if 0 <= x1 < cols and 0 <= y1 < rows:
            count += 1
            total += matrix[y1 * cols + x1]
    return total / count

def smooth(matrix: list, rows: int, cols: int) -> list:
##    return [avg(matrix, rows, cols, x, y) for y in range(rows) for x in range(cols)]
    result = []
    for y in range(rows):
        for x in range(cols):
            val = avg(matrix, rows, cols, x, y)
            result.append(val)
    return result

def main():
    matrix = []
    cols, rows = 0, 0

    with open('matrix.csv', 'r') as file1:
        for line in file1:
            splitted = line.split(',')
            vals = [int(i) for i in splitted]
            matrix += vals
            cols = len(vals)
            rows += 1

    print(cols, 'x', rows)
    print(matrix)
    print()
    smoothed = smooth(matrix, rows, cols)
    print(smoothed)

if __name__ == '__main__':
    main()
