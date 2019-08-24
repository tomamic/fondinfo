#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def combine(alphabet: str, n: int) -> [str]:
    if n == 0:
        return ['']

    combinations = combine(alphabet, n - 1)
    #return [symbol + comb for symbol in alphabet for comb in combinations]

    result = []
    for symbol in alphabet:
        for comb in combinations:
            result.append(symbol + comb)
    return result

print(combine("AEIOU", 3))
