#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def max_min(filename: str) -> (int, int):
    with open(filename, 'r') as f:
        first = f.readline()
        max_val = min_val = float(first)
        for line in f:
            val = float(line)
            if val > max_val:
                max_val = val
            if val < min_val:
                min_val = val
    return max_val, min_val

if __name__ == '__main__':
    fn = input('filename? ')
    mx, mn = max_min(fn)
    print(mx, mn)
