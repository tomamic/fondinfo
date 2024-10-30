#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from functools import lru_cache
from time import time

## @lru_cache()
def fibonacci1(n: int) -> int:
    if n < 2:
        return n
    return fibonacci1(n - 1) + fibonacci1(n - 2)

def fibonacci2(n: int, _cache=[0, 1]) -> int:
    if n < len(_cache):
        return _cache[n]
    result = fibonacci2(n - 1) + fibonacci2(n - 2)
    _cache.append(result)
    return result

def fibonacci3(n: int) -> tuple[int, int]:
    if n == 0:
        return 0, 1
    prv, val = fibonacci3(n - 1)
    return val, val + prv

def fibonacci4(n: int) -> int:
    val, nxt = 0, 1
    for i in range(n):
        val, nxt = nxt, val + nxt
    return val


def main():
    n = int(input("n? "))

    start = time()
    fib = fibonacci1(n)
    print("fib1:", fib, time() - start)

    start = time()
    fib = fibonacci2(n)
    print("fib2:", fib, time() - start)

    start = time()
    fib, nxt = fibonacci3(n)
    print("fib3:", fib, time() - start)

    start = time()
    fib = fibonacci4(n)
    print("fib4:", fib, time() - start)

main()
