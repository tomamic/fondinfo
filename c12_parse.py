#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
"""

from c12_expr import Expr, Num, BinaryOp

def parse(tokens: list) -> str:
    token = tokens.pop(0)

    if "0" <= token[-1] <= "9":
        return Num(float(token))
    else:
        a = parse(tokens)
        b = parse(tokens)

        if token in "+-*/":
            return BinaryOp(token, a, b)

def main():
    polish = "* 5 + 4 * 3 2".split()

    expr = parse(polish)
    print(expr.infix(), "==", expr.eval({}))

    # 5.0 * (4.0 + 3.0 * 2.0) == 50.0

main()
