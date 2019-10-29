#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def anagram(text: str) -> [str]:
    if len(text) == 0:
        return ['']

    result = []
    for i in range(len(text)):
        c = text[i]
        rest = text[:i] + text[i + 1:]
        for p in anagram(rest):
            result.append(c + p)
    return result

print(anagram("RAMO"))
