#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Conteggio cifre
- Chiedere una riga di testo all'utente
- Contare il numero complessivo di cifre presenti (da '0' a '9')
- Valutare anche la somma di tutte le singole cifre trovate
'''

line = input("Text? ")

n, tot = 0, 0

for c in line:
    if '0' <= c <= '9':
        n += 1
        tot += int(c)

print("Number of digits:", n)
print("Sum of digits:", tot)
