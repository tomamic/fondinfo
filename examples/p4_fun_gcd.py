#!/usr/bin/env python3
'''
4.3 Ricorsione, MCD
* Leggere due numeri
* Calcolare il loro Massimo Comun Divisore
* Visualizzare il risultato

(Provare ad usare sia l'iterazione che la ricorsione)
(Euclide: MCD(a, b) = MCD(b, a mod b), se b > 0; MCD(a, b) = a, se b = 0)

@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import logging

def gcd1(a: int, b: int) -> int:
    logging.debug(f"gcd1 {a} {b}")
    if b == 0:
        return a
    return gcd1(b, a % b)

def gcd2(a: int, b: int) -> int:
    logging.debug(f"gcd2 {a} {b}")
    while b != 0:
        a, b = b, a % b
        logging.debug(f"gcd2 {a} {b}")
    return a

def main():
##    logging.basicConfig(level=logging.DEBUG)
##    a, b = 1071, 1029
    a = int(input("a? "))
    b = int(input("b? "))
    print(gcd1(a, b))
    print(gcd2(a, b))

main()
