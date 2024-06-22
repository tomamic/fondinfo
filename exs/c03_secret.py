#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randint

MAX_SECRET = 90
MAX_TRIES = 10
guess = 0
tries = 0
secret = randint(1, MAX_SECRET)

while secret != guess and tries < MAX_TRIES:
    guess = int(input("your guess? "))
    tries += 1

    if secret < guess:
        print("The secret is smaller than", guess)
    elif secret > guess:
        print("The secret is larger than", guess)

if secret == guess:
    print("Congratulations, you guessed in", tries, "tries");
else:
    print("No luck! The secret was", secret);
