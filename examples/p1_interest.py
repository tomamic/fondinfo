#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Interesse composto
- Dati dall'utente: capitale iniziale, tasso d'interesse, durata investimento
- Calcolare il capitale dopo ogni anno
'''

capital = float(input("Capital? "))
rate = float(input("Rate? "))
years = int(input("Years? "))

y = 0
while y <= years:
    print("Year {:2}: {:6.2f}".format(y, capital))
    capital += capital * rate / 100
    y += 1
