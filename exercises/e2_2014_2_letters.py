N = 26
counters = [0] * N

text = input('text? ')

for c in text:
    if 'A' <= c <= 'Z':
        index = ord(c) - ord('A')
        counters[index] += 1

for i in range(N):
    code = i + ord('A')
    print(chr(code), counters[i])
