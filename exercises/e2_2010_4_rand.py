import random

MAX_SECRET = 90
MAX_TRIES = 10

secret = random.randint(1, MAX_SECRET)
tries = 0
guess = 0
while secret != guess and tries < MAX_TRIES:
    guess = int(input())
    tries += 1

    if secret < guess:
        print("The secret is smaller than", guess)
    elif secret > guess:
        print("The secret is larger than", guess)
    else:
        print("Congratulations, you guessed in", tries, "tries");
