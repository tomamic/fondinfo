def to_infix(tokens: list) -> list:
    token = tokens.pop(0)

    try:
        value = float(token)
        return [token]
    except:
        result = ['(']
        result += to_infix(tokens)
        result += [' ', token, ' ']
        result += to_infix(tokens)
        result += [')']
        return result

def evaluate(tokens: list) -> float:
    token = tokens.pop(0)

    try:
        value = float(token)
        return value
    except:
        a = evaluate(tokens)
        b = evaluate(tokens)

        if token == '+': return a + b
        elif token == '-': return a - b
        elif token == '*': return a * b
        elif token == '/': return a / b;
        elif token == 'div': return int(a) // int(b)
        elif token == 'mod': return int(a) % int(b)

if __name__ == '__main__':
    polish = 'mod + * + 1 2 + 2 3 4 5'.split()

    infix = to_infix(polish[:])
    value = evaluate(polish[:])
    print(''.join(infix), '==', value)

    # ((((1 + 2) * (2 + 3)) + 4) mod 5) == 4
