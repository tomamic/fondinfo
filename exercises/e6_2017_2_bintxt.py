def bintxt(n):
    if n == 0:
        return ''
    return bintxt(n // 2) + str(n % 2)

def main():
    n = int(input("n? "))
    print(bintxt(n))

if __name__ == '__main__':
    main()
