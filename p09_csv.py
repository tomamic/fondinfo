#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randint

def read_csv(filename: str) -> (list, int, int):
    data, rows = [], 0
    with open(filename, "r") as f:
        for line in f:
            for v in line.split(","):
                data.append(int(v))
            rows += 1
    return data, rows, len(data) // max(rows, 1)

def write_csv(filename: str, data: list, rows: int, cols: int):
    with open(filename, "w") as f:
        for y in range(rows):
            for x in range(cols):
                sep = "\n" if x == cols - 1 else ","
                print(data[y * cols + x], end=sep, file=f)

def main():
    ##write_csv("_data.csv", [randint(1, 12) for i in range(20)], 4, 5)

    data, rows, cols = read_csv("_data.csv")

    for i in range(min(rows, cols)):
        x, y = cols - 1 - i, rows - 1 - i
        data[y * cols + x] **= 2  # n = n ** 2

    write_csv("_data2.csv", data, rows, cols)

main()
