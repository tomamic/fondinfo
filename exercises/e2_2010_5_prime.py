'''Proof. Since n is composite, n = d*e for some natural numbers d and e
(both >= 2, d <= e). If d > sqrt(n) ==> n = d*e > sqrt(n)*sqrt(n) = n,
i.e. n>n (contraddiction!). So d <= sqrt(n).'''

n = int(input());
d = 2

# while d < n // 2 and n % d != 0: d += 1 ...

if n % d != 0:  # if odd
    d = 3
    while d * d <= n and n % d != 0:
        d += 2

if n % d == 0 and n != d:
    print("The number is divisible by", d)
else:
    print("The number is prime")
