#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def troll(text: str) -> str:
    output = ''
    trolling = False
    for c in text:
        if c == '*':
            trolling = not trolling
        elif 'a' <= c <= 'z' and trolling:
            output += c.upper()
        else:
            output += c
    return output

with open('troll.out.txt', 'w') as out:
    with open('troll.txt', 'r') as f:
        for line in f:
            res = troll(line)
            print(res, file=out, end='')
