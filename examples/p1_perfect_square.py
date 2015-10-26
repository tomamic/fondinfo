i = 1
n = int(input('n ? '))
found = False

while i * i <= n:
    if i * i == n:
        print(i)
        found = True
    i += 1

if not found:
    print('no')
