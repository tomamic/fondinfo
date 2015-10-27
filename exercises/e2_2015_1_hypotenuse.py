def hypotenuse(side1: float, side2: float) -> float:
    result = (side1 ** 2 + side2 ** 2) ** 0.5
    return result

def main():
    a = float(input('a? '))
    b = float(input('b? '))

    c = hypotenuse(a, b)

    print(c)

if __name__ == '__main__':
    main()

