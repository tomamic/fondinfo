#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

from c12_stack import Stack
from typing import Iterable
from operator import add, sub, mul, truediv, neg
ops = {"+": add, "-": sub, "*": mul, "/": truediv, "~": neg}

def evaluate(tokens: Iterable) -> float:
    s = Stack()
    for token in tokens:
        if token[0].isdigit():
            s.push(float(token))
        else:
            a = s.pop()
            b = s.pop()
            op = ops[token]
            s.push(op(a, b))
    return s.pop()

def main():
    expr = "4 2 3 * + 5 *".split()
    v = evaluate(iter(expr))
    print(v)

if __name__ == "__main__":
    main()