counters = [0] * 26

text = input('text? ')

for c in text:
    if 'A' <= c <= 'Z':
        index = ord(c) - ord('A')
        counters[index] += 1

for i in range(26):
    print(chr(i + ord('A')), counters[i])
