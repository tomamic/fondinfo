#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Cerchio
- Chiedere all'utente il valore del raggio r di un cerchio
- Mostrare il valore dell'area e della circonferenza
- Se r è negativo, però, mostrare un messaggio d'errore
'''

from math import pi

r = float(input("r? "))
if r < 0:
    print("error: negative r")
else:
    area = pi * r ** 2
    perimeter = 2 * pi * r
    print("area:", area)
    print("perimeter:", perimeter)
