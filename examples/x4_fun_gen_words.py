#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def gen_words(alphabet: str, n: int) -> [str]:
    if n == 0:
        return ['']

    words = gen_words(alphabet, n - 1)
    #return [symbol + word for symbol in alphabet for word in words]

    result = []
    for symbol in alphabet:
        for word in words:
            result.append(symbol + word)
    return result

print(gen_words("AEIOU", 3))
