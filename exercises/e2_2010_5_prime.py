'''Proof. Since n is composite, n = d*e for some natural numbers
d and e which are not zero and not units. If both of them are
greater than sqrt(n), then n = d*e > sqrt(n)*sqrt(n) = n, so
n>n, contradiction. So d or e is <= sqrt(n).'''

n = int(input());
d = 2

# while d < n // 2 && n % d != 0: d += 1 ...

if n % d != 0:
    d = 3
    while d * d <= n and n % d != 0:
        d += 2

if n % d == 0 and n != d:
    print("The number is divisible by", d)
else:
    print("The number is prime")
