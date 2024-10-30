#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def reset(data: list[int]):
    data.clear()
    #data = []

def main():
    nums = [1, 2, 3]
    reset(nums)
    print(nums)

main()
