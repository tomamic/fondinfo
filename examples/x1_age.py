birth_year = int(input("Birth year? "))
birth_month = int(input("Birth month? "))
birth_day = int(input("Birth day? "))
current_year = int(input("Current year? "))
current_month = int(input("Current month? "))
current_day = int(input("Current day? "))

age = current_year - birth_year
if current_month < birth_month or (current_month == birth_month and
        current_day < birth_day):
    age = age - 1

print("Your age is", age)
