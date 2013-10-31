import sys

calories = {}
with open('calories.txt', 'r') as f:
    for line in f:
        splitted = line.split('\t')
        food = splitted[0]
        val = splitted[1]
        calories[food] = float(val)

total = 0
for line in sys.stdin:
    food, weight = line.split('|')  # see `splitted`, above
    total += float(weight) * calories[food]
print(total)
