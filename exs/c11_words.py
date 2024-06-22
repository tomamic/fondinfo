#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def words(alphabet: str, n: int) -> list[str]:
    if n == 0:
        return [""]

    ws = words(alphabet, n - 1)
    #return [symbol + word for symbol in alphabet for word in words]

    result = []
    for symbol in alphabet:
        for word in ws:
            result.append(symbol + word)
    return result

print(words("ABC", 4))
