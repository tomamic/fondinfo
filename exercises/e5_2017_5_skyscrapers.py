#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def count_tops(values: list) -> int:
    maxx = -1
    count = 0
    for val in values:
        if val > maxx:
            count += 1
            maxx = val
    return count

def transposed(matrix: list) -> list:
    rows, cols = len(matrix), len(matrix[0])
##    return [[matrix[y][x] for y in range(rows)] for x in range(cols)]

    result = []
    for x in range(cols):
        row = []
        for y in range(rows):
            row.append(matrix[y][x])
        result.append(row)
    return result

def main():
    matrix = []
    cols, rows = 0, 0

    with open('matrix.csv', 'r') as file1:
        for line in file1:
            splitted = line.split(',')
            vals = [int(i) for i in splitted]
            matrix.append(vals)
            ## matrix += vals  # for a simple list (ex. 4.5)

            if cols == 0:
                cols = len(vals)
            rows += 1

    print(cols, 'x', rows)
    print(matrix)
    print()

    for row in matrix:
        print(count_tops(row), count_tops(reversed(row)))

    for row in transposed(matrix):
        print(count_tops(row), count_tops(reversed(row)))

main()
