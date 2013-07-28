a = int(input())
b = int(input())
c = int(input())

print("Min:")
if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

print("Max:")
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

