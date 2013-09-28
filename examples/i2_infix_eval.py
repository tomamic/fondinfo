# expr = term {( '+' | '-' ) term}
# term = factor {( '*' | '/' ) factor}
# factor = '-' factor | '(' expr ')' | val
# val = 'x' | 'y' | 'z'

import re


def expr(tok, act):
    x = term(tok, act)
    next = tok.peek()
    while next in ('+', '-'):
        tok.consume(next)
        y = term(tok, act)
        if next == '+': x = act.add(x, y)
        else: x = act.sub(x, y)
        next = tok.peek()
    return x

def term(tok, act):
    x = factor(tok, act)
    next = tok.peek()
    while next in ('*', '/'):
        tok.consume(next)
        y = factor(tok, act)
        if next == '*': x = act.mul(x, y)
        else: x = act.div(x, y)
        next = tok.peek()
    return x

def factor(tok, act):
    next = tok.peek()
    if next == '-':
        tok.consume('-')
        x = factor(tok, act)
        return act.opp(x)
    elif next == '(':
        tok.consume('(')
        x = expr(tok, act)
        tok.consume(')')
        return x
    elif next.isalpha():
        tok.consume(next)
        x = act.var(next)
        return x
    else:
        tok.consume(next)
        x = act.num(next)
        return x


class Actions:
    def __init__(self, values):
        self._values = values
    def add(self, x, y): return x + y
    def sub(self, x, y): return x - y
    def mul(self, x, y): return x * y
    def div(self, x, y): return x / y
    def opp(self, x): return -x
    def num(self, x): return float(x)
    def var(self, x): return self._values[x]


class Tokenizer:
    def __init__(self, text, regex):
        self._text = text.rstrip()
        self._point = 0
        self._token_re = re.compile(regex)

    def peek(self):
        return self._token_re.match(self._text, self._point).group(1)

    def consume(self, x):
        m = self._token_re.match(self._text, self._point)
        if m.group(1) != x:
            raise SyntaxError("expected " + x)
        self._point = m.end()

    def end(self):
        if self._point < len(self._text):
            raise SyntaxError("Extra stuff after expression")


regex = r'\s*([A-Za-z0-9\.]+|.?)'


# Wrapper function
def parse_expr(text, act):
    tok = Tokenizer(text, regex)
    result = expr(tok, act)
    tok.end()
    return result


# Tests
values = {'w': 0.0, 'x': 1.0, 'y': 1.5, 'z': 0.5}
act = Actions(values)

if __name__ == '__main__':
    assert parse_expr('(((1.5)))', act) == 1.5
    assert parse_expr('w * -z', act) == 0
    assert parse_expr('x / z * -y', act) == -3
    assert parse_expr('x / 0.5 * --y', act) == 3
    assert parse_expr('w', act) == 0
    assert parse_expr('(x + w) * (x + y) * (y - z)', act) == 2.5
