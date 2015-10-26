def hypotenuse(side1: float, side2: float) -> float:
    hyp = (side1 ** 2 + side2 ** 2) ** 0.5
    print(a)
    return hyp

def main():
    a = float(input('a? '))
    b = float(input('b? '))

    c = hypotenuse(a, b)

    print(c)

if __name__ == '__main__':
    main()

