#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

# matrix as a simple list
def avg(matrix: list[float], cols: int, rows: int, x0: int, y0: int) -> float:
    dirs = ((0, 0), (0, -1), (1, 0), (0, 1), (-1, 0))
    count, total = 0, 0
    for dx, dy in dirs:
        x1, y1 = x0 + dx, y0 + dy
        if 0 <= x1 < cols and 0 <= y1 < rows:
            count += 1
            total += matrix[x1 + y1 * cols]
    return total / count

# matrix as a simple list
def smooth(matrix: list[float], cols: int, rows: int) -> list[float]:
    ## return [avg(matrix, cols, rows, x, y) for y in range(rows) for x in range(cols)]
    result = []
    for y in range(rows):
        for x in range(cols):
            val = avg(matrix, cols, rows, x, y)
            result.append(val)
    return result

# matrix as a list of lists
def avg2(matrix: list[list[float]], x0: int, y0: int) -> float:
    dirs = ((0, 0), (0, -1), (1, 0), (0, 1), (-1, 0))
    rows, cols = len(matrix), len(matrix[0])
    count, total = 0, 0
    for dx, dy in dirs:
        x1, y1 = x0 + dx, y0 + dy
        if 0 <= x1 < cols and 0 <= y1 < rows:
            count += 1
            total += matrix[y1][x1]
    return total / count

# matrix as a list of lists
def smooth2(matrix: list[list[float]]) -> list[list[float]]:
    rows, cols = len(matrix), len(matrix[0])
    ## return [[avg2(matrix, x, y) for x in range(cols)] for y in range(rows)]
    result = []
    for y in range(rows):
        row = []
        for x in range(cols):
            val = avg2(matrix, x, y)
            row.append(val)
        result.append(row)
    return result


def main():
    matrix = [10,  7,  6,  8,
               8,  1, 11,  4,
               6,  7,  8,  2]
    cols, rows = 4, 3

    smoothed = smooth(matrix, cols, rows)
    print(smoothed)

if __name__ == "__main__":
    main()
