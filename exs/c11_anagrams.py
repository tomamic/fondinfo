#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

def anagrams(text: str) -> [str]:
    if len(text) == 0:
        return [""]

    result = []
    for i, char in enumerate(text):
        rest = text[:i] + text[i + 1:]
        for partial in anagrams(rest):
            result.append(char + partial)
    return result

print(anagrams("RAMO"))
