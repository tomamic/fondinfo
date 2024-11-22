#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def eratosthenes(num: int) -> list[bool]:
    prime = [True] * (num + 1)
    p = 2
    while (p * p <= num):
        if (prime[p]):
            # all multiples of p are not prime
            for i in range(p * p, num + 1, p):  # start, stop, step
                prime[i] = False
        p += 1
    return prime

def main():
    NUM = 1000
    prime = eratosthenes(NUM)
    with open("_prime_twins.txt", "w") as pt:
        for n in range(2, NUM - 2):
            if prime[n] and prime[n + 2]:
                print(f"{n} {n + 2}", file=pt)
    
main()
