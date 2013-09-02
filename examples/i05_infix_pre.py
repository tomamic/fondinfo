from i05_infix_eval import expr, term, factor, Tokenizer, regex

class Actions:
    def add(self, x, y): return "+ {} {}".format(x, y)
    def sub(self, x, y): return "- {} {}".format(x, y)
    def mul(self, x, y): return "* {} {}".format(x, y)
    def div(self, x, y): return "/ {} {}".format(x, y)
    def opp(self, x): return "~{}".format(x)
    def num(self, x): return x
    def var(self, x): return x


# Wrapper function
def parse_simple_expr(text):
    tok = Tokenizer(text, regex)
    act = Actions()
    result = expr(tok, act)
    tok.end()
    return result


# Tests.
if __name__ == '__main__':
    assert parse_simple_expr('(((1.5)))') == "1.5"
    assert parse_simple_expr('w * -z') == "* w ~z"
    assert parse_simple_expr('x / z * -y') == "* / x z ~y"
    assert parse_simple_expr('x / 0.5 * --y') == "* / x 0.5 ~~y"
    assert parse_simple_expr('w') == "w"
    assert parse_simple_expr('(x + w) * (x + y) * (y - z)') == "* * + x w + x y - y z"
