#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Numero segreto
- Generare un intero “segreto” a caso tra 1 e 90
- Chiedere ripetutamente all'utente di immettere un numero, finché non indovina quello generato
- Ad ogni tentativo, dire se il numero immesso è maggiore o minore del numero segreto
'''

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
    else:
        print("Congratulations, you guessed in", tries, "tries");
