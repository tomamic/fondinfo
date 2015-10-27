n = int(input('n? '))
result = 0

i = 1
while i * i <= n:
    if i * i == n:
        result = i
    i += 1

if result == 0:
    print('no')
else:
    print(result)
