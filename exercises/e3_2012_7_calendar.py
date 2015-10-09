WEEK_DAYS = 7
MAX_WEEKS = 6

first = int(input('first (0-6)? '))
length = int(input('length (28-31)? '))

for i in range (WEEK_DAYS * MAX_WEEKS):
    day = i + 1 - first
    if 0 < day <= length:
        print('{:3}'.format(day), end='')
    else:
        print('   ', end='')
    if i % WEEK_DAYS == WEEK_DAYS - 1:
        print()
print()

for y in range(MAX_WEEKS):
    for x in range(WEEK_DAYS):
        day = y * WEEK_DAYS + x + 1 - first
        if 0 < day <= length:
            print('{:3}'.format(day), end='')
        else:
            print('   ', end='')
    print()
print()

for y in range(WEEK_DAYS):
    for x in range(MAX_WEEKS):
        day = y + x * WEEK_DAYS + 1 - first
        if 0 < day <= length:
            print('{:3}'.format(day), end='')
        else:
            print('   ', end='')
    print()
print()
