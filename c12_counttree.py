#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

T = int | list["T"]

def count_tree(t: T) -> int:
    count = 0
    if isinstance(t, int):
        count += 1
    else:
        for v in t:
            count += count_tree(v)
    return count

tree = [[1, 2, [3, 4], [5]], 6]
print(count_tree(tree))
