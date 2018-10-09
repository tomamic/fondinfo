#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Array, precalcolo
- Riempire una lista con i valori di sin(x)
-- 360 elementi, indice x tra 0 e 359
- Poi, ciclicamente...
-- Chiedere un angolo all'utente
-- Visualizzare il corrispondente valore precalcolato
'''

from math import pi, sin

fast_sin = [0] * 360
for x in range(360):
    rad = x * pi / 180
    val = sin(rad)
    fast_sin[x] = val

# fast_sin = [sin(x * pi / 180) for x in range(360)]

angle = int(input("angle? "))
while 0 <= angle < 360:
    value = fast_sin[angle]
    print(f"sin({angle}) = {value:.2f}")
    angle = int(input("angle? "))
