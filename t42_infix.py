#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

import re
from math import isclose
from operator import add, sub, mul, truediv, neg
ops = {"+": add, "-": sub, "*": mul, "/": truediv, "~": neg}

# expr = term {( "+" | "-" ) term}
# term = factor {( "*" | "/" ) factor}
# factor = "-" factor | "(" expr ")" | identifier | number
# (identifiers start with a letter, numbers are float)

# expr = term {( "+" | "-" ) term}
def expr(tok: "Tokenizer") -> "Expr":
    x = term(tok)
    while (nxt := tok.peek()) in ("+", "-"):
        tok.consume(nxt)
        y = term(tok)
        x = BinaryOp(nxt, x, y)
    return x

# term = factor {( "*" | "/" ) factor}
def term(tok: "Tokenizer") -> "Expr":
    x = factor(tok)
    while (nxt := tok.peek()) in ("*", "/"):
        tok.consume(nxt)
        y = factor(tok)
        x = BinaryOp(nxt, x, y)
    return x

# factor = "-" factor | "(" expr ")" | identifier | number
def factor(tok: "Tokenizer") -> "Expr":
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
    elif nxt.isalpha():
        tok.consume(nxt)
        return Var(nxt)
    else:
        tok.consume(nxt)
        return Num(float(nxt))


class Tokenizer:
    def __init__(self, text):
        regex = r"\s*([A-Za-z0-9\.]+|.?)"
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


class Expr:
    def to_prefix(self) -> str:
        raise NotImplementedError("Abstract method")

    def eval(self, context: dict[str, float]) -> float:
        raise NotImplementedError("Abstract method")

class BinaryOp(Expr):
    def __init__(self, op: str, x: Expr, y: Expr):
        self._op, self._x, self._y = op, x, y

    def to_prefix(self):
        x = self._x.to_prefix()
        y = self._y.to_prefix()
        return f"{self._op} {x} {y}"

    def eval(self, ctx):
        x = self._x.eval(ctx)
        y = self._y.eval(ctx)
        op = ops[self._op]
        return op(x, y)


class UnaryOp(Expr):
    def __init__(self, op, x: Expr):
        self._op, self._x = op, x

    def to_prefix(self):
        x = self._x.to_prefix()
        return f"{self._op}{x}"

    def eval(self, ctx):
        x = self._x.eval(ctx)
        op = ops[self._op]
        return op(x)

class Var(Expr):
    def __init__(self, name: str):
        self._name = name

    def to_prefix(self):
        return f"{self._name}"

    def eval(self, ctx):
        return ctx.get(self._name, 0)

class Num(Expr):
    def __init__(self, val: float):
        self._val = val

    def to_prefix(self):
        return f"{self._val}"

    def eval(self, ctx):
        return self._val


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
        assert ast.to_prefix() == prefix
        assert isclose(ast.eval(ctx), val)

if __name__ == "__main__":
    main()
