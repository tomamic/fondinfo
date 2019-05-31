n = int(input("How many values? "))
count = 0
total = 0

while count < n:
    val = int(input("Val? "))
    total += val  # total = total + val
    count += 1    # count = count + 1

if count != 0:
    print("The average is", total / count)
