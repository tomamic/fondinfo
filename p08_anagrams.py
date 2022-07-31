#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def anagrams(text: str) -> [str]:
    if len(text) == 0:
        return ['']

    result = []
    for i, char in enumerate(text):
        rest = text[:i] + text[i + 1:]
        for partial in anagrams(rest):
            result.append(char + partial)
    return result

print(anagrams("RAMO"))
