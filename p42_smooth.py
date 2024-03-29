#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

def avg(matrix: list, cols: int, rows: int, x0: int, y0: int) -> float:
    dirs = ((0, 0), (0, -1), (1, 0), (0, 1), (-1, 0))
    count, total = 0, 0
    for dx, dy in dirs:
        x1, y1 = x0 + dx, y0 + dy
        if 0 <= x1 < cols and 0 <= y1 < rows:
            count += 1
            total += matrix[x1 + y1 * cols]
    return total / count

def smooth(matrix: list[float], cols: int, rows: int) -> list[float]:
##    return [avg(matrix, cols, rows, x, y) for y in range(rows) for x in range(cols)]
    result = []
    for y in range(rows):
        for x in range(cols):
            val = avg(matrix, cols, rows, x, y)
            result.append(val)
    return result

def main():
    from p42_csv import read_csv
    matrix, cols, rows = read_csv("_matrix.csv")

    print(f"{cols}×{rows}")
    print(matrix, "\n")
    smoothed = smooth(matrix, cols, rows)
    print(smoothed)

if __name__ == "__main__":
    main()
