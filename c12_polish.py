#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from typing import Iterable
from c12_expr import ops, Num, BinaryOp

def to_infix(tokens: Iterable) -> str:
    token = next(tokens)

    if token[0].isdigit():
        return token
    else:
        a = to_infix(tokens)
        b = to_infix(tokens)
        return f"({a} {token} {b})"

def evaluate(tokens: Iterable) -> float:
    token = next(tokens)

    if token[0].isdigit():
        return float(token)
    else:
        a = evaluate(tokens)
        b = evaluate(tokens)
        op = ops[token]
        return op(a, b)

def parse(tokens: Iterable) -> float:
    token = next(tokens)

    if token[0].isdigit():
        return Num(float(token))
    else:
        a = parse(tokens)
        b = parse(tokens)
        return BinaryOp(token, a, b)

def main():
    polish = "* 5 + * 3 2 4".split()

    infix = to_infix(iter(polish))
    value = evaluate(iter(polish))
    tree = parse(iter(polish))
    print(infix, "==", value)

    # (5 * ((3 * 2) + 4)) == 50.0

main()
