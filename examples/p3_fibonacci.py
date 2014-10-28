'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import logging, sys, time, functools

# @functools.lru_cache()
def fibonacci1(n: int) -> int:
    result = 1
    if n >= 2:
        logging.debug('fib {}'.format(n))
        result = fibonacci1(n-1) + fibonacci1(n-2)
    return result

def fibonacci2(n: int) -> int:
    result = 1
    if n < len(fibonacci2._lookup):
        result = fibonacci2._lookup[n]
    else:
        logging.debug('fib {}'.format(n))
        result = fibonacci2(n - 1) + fibonacci2(n - 2)
        fibonacci2._lookup.append(result)
    return result

fibonacci2._lookup = [1, 1]
# lookup is a variable associated with the
# function itself, not a particular activation

def fibonacci3(n: int) -> int:

    result = 1
    fib2 = 1  # result @ 2 steps before

    for i in range(2, n + 1):
        logging.debug('fib {}'.format(i))
        result += fib2

        # store previous result, for next step
        fib2 = result - fib2
    return result;

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
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


