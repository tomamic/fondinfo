#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import logging, sys, time, functools


@functools.lru_cache()
def fibonacci1(n: int) -> int:
    if n <= 1:
        return n
    logging.debug('fib {}'.format(n))
    return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(n: int) -> int:
    if n < len(fibonacci2._lookup):
        return fibonacci2._lookup[n]
    logging.debug('fib {}'.format(n))
    result = fibonacci2(n - 1) + fibonacci2(n - 2)
    fibonacci2._lookup.append(result)
    return result

fibonacci2._lookup = [0, 1]
# lookup is a variable associated with the
# function itself, not a particular activation


def fibonacci3(n: int) -> int:
    val, nxt = 0, 1

    for i in range(n):
        logging.debug('fib {}'.format(i+1))
        val, nxt = nxt, val + nxt

    return val


def main():
##    logging.basicConfig(level=logging.DEBUG)
    for line in sys.stdin:
        n = int(line)

        start = time.clock()
        fib = fibonacci1(n)
        print('fib1:', fib, time.clock() - start)

        start = time.clock()
        fib = fibonacci2(n)
        print('fib2:', fib, time.clock() - start)

        start = time.clock()
        fib = fibonacci3(n)
        print('fib3:', fib, time.clock() - start)

main()
