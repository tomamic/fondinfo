'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

3.5 Interpolazione
* Leggere da un file una serie di numeri reali e memorizzarli in un vettore
  * Es. dati dall'esercizio 3.2
* Suppore che i numeri rappresentino il valore di una certa funzione f(x), per valori interi di x
* Supporre f periodica, periodo = lunghezza del vettore
* Usare l'interpolazione (e la periodicità) per calcolare f(x) per qualsiasi x reale
'''

import math, sys

with open('sin.txt') as infile:
    function = [float(line) for line in infile]
period = len(function)

for line in sys.stdin:
    angle = float(line)
    x1 = math.floor(angle)
    fract = angle - x1

    x1 = x1 % period  # translate into the base range, considering periodicity
    x2 = (x1 + 1) % period  # x2 is the next integer, in the base range

    y1 = function[x1]
    y2 = function[x2]
    print(y1 + fract * (y2 - y1))
