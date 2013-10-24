import random

n = int(input('n? '))

results = [0] * 11
for i in range(n):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    val = die1 + die2
    results[val - 2] += 1

for i in range(11):
    print('Result {} has come out {} times'.format(i + 2, results[i]))
