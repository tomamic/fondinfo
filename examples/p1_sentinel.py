count = 0
total = 0

val = int(input("Val? [0 to end] "))
while val != 0:
    total += val  # total = total + val
    count += 1    # count = count + 1
    val = int(input("Val? [0 to end] "))

if count != 0:
    print("The average is", total / count)
