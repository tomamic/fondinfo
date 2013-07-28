import types

def f3(x: float) -> float:
    return x ** 3 - x - 1

def find_zero(f: types.FunctionType,
              low: float, high: float, err: float) -> float:
    x = (low + high) / 2
    y = f(x)
    if not (-err <= y <= err):
        if y * f(low) < 0:
            x = find_zero(f, low, x, err)
        else:
            x = find_zero(f, x, high, err)
    return x

if __name__ == '__main__':
    x = find_zero(f3, 1, 2, 1e-6)
    print(x)
