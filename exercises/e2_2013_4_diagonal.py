import sys

n = int(input('n? '))
matrix = []

for i in range(n * n):
    val = int(input('val? '))
    matrix.append(val)

for line in sys.stdin:
    k = int(line)
    count = 0
    diagonal = 0
    for i in range(n * n):
        if matrix[i] == k:
            count += 1
            x, y = i % n, i // n
            if x == y or n - x - 1 == y:
                diagonal += 1
    print(count, diagonal)
