def factors(n: int):
    result = []
    x = 2
    while x <= n:
        if n % x == 0:
            result.append(x)
            # to skip non-prime factors...
            while n % x == 0:
                n = n // x
        x += 1
    return result

if __name__ == '__main__':
    n = int(input('n? '))
    while n > 0:
        print(factors(n))
        n = int(input('n? '))
