from random import randint

DIE_SIDES = 6
NUM_RESULTS = 11

n = int(input('n? '))

results = [0] * NUM_RESULTS

for i in range(n):
    die1 = randint(1, DIE_SIDES)
    die2 = randint(1, DIE_SIDES)
    val = die1 + die2
    results[val - 2] += 1

for i in range(NUM_RESULTS):
    print('Result {} has come out {} times'.format(i + 2, results[i]))
