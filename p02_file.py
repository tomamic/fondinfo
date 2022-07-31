total = 0
total_inv = 0

with open("resistors.txt") as file:
    for line in file:
        val = float(line)
        if val > 0:
            total += val
            total_inv += 1 / val

if total > 0:
    print(total, 1 / total_inv)
