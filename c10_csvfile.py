#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randint

def read_csv(filename: str) -> tuple[list[int], int, int]:
    data, rows = [], 0
    with open(filename) as f:
        for line in f:
            row = [int(v) for v in line.split(",")]
            data += row
            rows += 1
    return data, len(data) // (rows or 1), rows

def write_csv(filename: str, data: list, cols: int, rows: int) -> None:
    with open(filename, "w") as f:
        for y in range(rows):
            for x in range(cols):
                sep = "\n" if x == cols - 1 else ","
                print(data[x + y * cols], end=sep, file=f)

def read_csv_2(filename: str) -> list[list[int]]:
    data = []
    with open(filename) as f:
        for line in f:
            row = [int(v) for v in line.split(",")]
            data.append(row)
    return data

def write_csv_2(filename: str, data: list[list]) -> None:
    with open(filename, "w") as f:
        rows, cols = len(data), len(data[0] if data else 0)
        for y in range(rows):
            for x in range(cols):
                sep = "\n" if x == cols - 1 else ","
                print(data[y][x], end=sep, file=f)

def main():
    write_csv("_data.csv", [randint(1, 12) for i in range(20)], 4, 5)

    data1, cols, rows = read_csv("_data.csv")
    write_csv("_data1.csv", data1, cols, rows)
    
    data2 = read_csv_2("_data.csv")
    write_csv_2("_data2.csv", data2)

if __name__ == "__main__":
    main()
