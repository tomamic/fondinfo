#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import functools, time

@functools.lru_cache()
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

def fibonacci3(n: int) -> int:
    val, nxt = 0, 1
    for i in range(n):
        val, nxt = nxt, val + nxt
    return val


def main():
    n = int(input("n? "))

    start = time.time()
    fib = fibonacci1(n)
    print("fib1:", fib, time.time() - start)

    start = time.time()
    fib = fibonacci2(n)
    print("fib2:", fib, time.time() - start)

    start = time.time()
    fib = fibonacci3(n)
    print('fib3:', fib, time.time() - start)

main()
