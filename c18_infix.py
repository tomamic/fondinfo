#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import re
from math import isclose
from c12_expr import Expr, BinaryOp, UnaryOp, Var, Num

class Tokenizer:
    def __init__(self, text):
        regex = r"\s*([\w\.]+|.?)"
        self._tokens = re.finditer(regex, text.rstrip())
        self._next = next(self._tokens)

    def peek(self) -> str:
        return self._next.group(1)

    def consume(self, x):
        if self.peek() != x:
            raise SyntaxError("Expected " + x)
        self._next = next(self._tokens)

    def end(self):
        if self.peek():
            raise SyntaxError("Extra tokens")


# expr = term {( "+" | "-" ) term}
# term = factor {( "*" | "/" ) factor}
# factor = "-" factor | "(" expr ")" | identifier | number
# (identifiers start with a letter, numbers are float)

# expr = term {( "+" | "-" ) term}
def expr(tok: Tokenizer) -> Expr:
    x = term(tok)
    while tok.peek() in ("+", "-"):
        op = tok.peek()
        tok.consume(op)
        y = term(tok)
        x = BinaryOp(op, x, y)
    return x

# term = factor {( "*" | "/" ) factor}
def term(tok: Tokenizer) -> Expr:
    x = factor(tok)
    while tok.peek() in ("*", "/"):
        op = tok.peek()
        tok.consume(op)
        y = factor(tok)
        x = BinaryOp(op, x, y)
    return x

# factor = "-" factor | "(" expr ")" | identifier | number
def factor(tok: Tokenizer) -> Expr:
    nxt = tok.peek()
    if nxt == "-":
        tok.consume("-")
        x = factor(tok)
        return UnaryOp("~", x)
    elif nxt == "(":
        tok.consume("(")
        x = expr(tok)
        tok.consume(")")
        return x
    elif nxt[0].isalpha():
        tok.consume(nxt)
        return Var(nxt)
    else:
        tok.consume(nxt)
        return Num(float(nxt))


# Tests
def main():
    ctx = {"w": 0.0, "x": 1.0, "y": 1.5, "z": 0.5}

    tests = [("(((1.5)))", "1.5", 1.5),
             ("w * -z", "* w ~z", 0.0),
             ("x / z * -y", "* / x z ~y", -3.0),
             ("x / 0.5 * --y", "* / x 0.5 ~~y", 3.0),
             ("w", "w", 0.0),
             ("(x + w) * (x + y)", "* + x w + x y", 2.5)]

    for infix, prefix, val in tests:
        tok = Tokenizer(infix)
        ast = expr(tok)
        tok.end()
        assert ast.prefix() == prefix
        assert isclose(ast.eval(ctx), val)

if __name__ == "__main__":
    main()
