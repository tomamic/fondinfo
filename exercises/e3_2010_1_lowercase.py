text = "Hey!! It's 2010, yet"
dash = False

for c in text:
    if c.isupper():
        print(c.lower(), end='')
        dash = False
    elif c.isdigit() or c.islower():
        print(c, end='')
        dash = False
    elif not dash:
        print('-', end='')
        dash = True
