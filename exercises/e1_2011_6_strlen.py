lines = 0
chars = 0
line = input()
while line != 'end':
    lines += 1
    chars += len(line)
    line = input()
if lines > 0:
    print(chars / lines)
