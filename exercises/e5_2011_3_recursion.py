import math

def sqrt_recursion(x: float, low: float, high: float) -> float:
    y = (high + low) / 2
    delta = y ** 2 - x

    if not (-0.001 <= delta <= 0.001):
        if delta < 0:
            y = sqrt_recursion(x, y, high)
        else:
            y = sqrt_recursion(x, low, y)
    return y

if __name__ == '__main__':
    x= float(input())
    
    low, high = 0, x
    if (high < 1):
        high = 1

    print(sqrt_recursion(x, low, high))
    print(math.sqrt(x))
