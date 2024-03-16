from random import randrange

def shuffle(values: list):
    for i, v in enumerate(values):
        j = randrange(len(values))
        values[i], values[j] = values[j], values[i]

data = list(range(10))
shuffle(data)
print(data)