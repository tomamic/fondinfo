line = input()
for c in line:
    if not c.isdigit():  # if c < '0' or c > '9'...
        print(c, end='')
