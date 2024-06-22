#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def merge(a: list, b: list) -> list:
    ia, ib = 0, 0
    result = []
    while ia < len(a) or ib < len(b):
        if ia < len(a) and (ib == len(b) or a[ia] <= b[ib]):
            result.append(a[ia])
            ia += 1  # one elem “consumed” from a
        else:
            result.append(b[ib])
            ib += 1  # one elem “consumed” from b
    return result

def main():
    data1 = [1, 4, 5, 7]
    data2 = [2, 3, 6, 8, 9, 10]
    merged = merge(data1, data2)
    print(data1, data2, merged)

main()
