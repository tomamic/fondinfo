#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

class Expression:
    def eval(self) -> float:
        raise NotImplementedError()
    def prefix(self) -> str:
        raise NotImplementedError()


class Literal:
    def __init__(self, val):
        self._val = val

    def eval(self):
        return self._val

    def prefix(self):
        return str(self._val)


class Product:
    def __init__(self, op1, op2):
        self._op1 = op1
        self._op2 = op2

    def eval(self):
        return self._op1.eval() * self._op2.eval()

    def prefix(self):
        return "* " + self._op1.prefix() + " " + self._op2.prefix()


class Sum:
    def __init__(self, op1, op2):
        self._op1 = op1
        self._op2 = op2

    def eval(self):
        return self._op1.eval() + self._op2.eval()

    def prefix(self):
        return "+ " + self._op1.prefix() + " " + self._op2.prefix()


def main():
                                              #   *  (prod2)
    prod1 = Product(Literal(3), Literal(2))   #  / \
    sum1 = Sum(Literal(4), prod1)             # 5   +  (sum1)
    prod2 = Product(Literal(5), sum1)         #    / \
    print(prod2.eval())                       #   4   *  (prod1)
    print(prod2.prefix())                     #      / \
                                              #     3   2

if __name__ == "__main__":
    main()
