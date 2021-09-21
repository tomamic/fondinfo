#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def primes(n: int) -> list:
    nums = []
    is_prime = [True] * (n + 1)
    for x in range(2, n + 1):
        if is_prime[x]:
            nums.append(x)
            for i in range(x * x, n + 1, x):
                is_prime[i] = False
    return nums

def main():
    n = int(input('n? '))
    result = primes(n)
    print(result)
    print(len(result), 'primes found')

main()

'''
import time

def primes_slow(n: int) -> list:
    nums = list(range(2, n + 1))
    j = 0
    while j < len(nums):
        x = nums[j]
        for i in range(x, n // x + 1):
            try:  # if x * i in nums
                nums.remove(x * i)
            except:
                pass
        j += 1
    return nums

def test():
    n = int(input('n? '))
    t0 = time.clock()
    res1 = primes(n)
    t1 = time.clock()
    res2 = primes_slow(n)
    t2 = time.clock()
    print(res1)
    print('A.', len(res1), 'primes found in', t1 - t0, 'seconds')
    print('B.', len(res2), 'primes found in', t2 - t1, 'seconds')
'''
