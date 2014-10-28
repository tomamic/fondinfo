'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

4.3 Ricorsione, MCD
* Leggere due numeri
* Calcolare il loro Massimo Comun Divisore
* Visualizzare il risultato

(Provare ad usare sia l'iterazione che la ricorsione)
(Euclide: MCD(a, b) = MCD(b, a mod b), se b > 0; MCD(a, b) = a, se b = 0)
'''

import logging

def mcd1(a: int, b: int) -> int:
    logging.debug('mcd1 {} {}'.format(a, b))
    if b == 0:
        return a
    else:
        return mcd1(b, a % b)

def mcd2(a: int, b: int) -> int:
    logging.debug('mcd2 {} {}'.format(a, b))
    while b != 0:
        a, b = b, a % b
        logging.debug('mcd2 {} {}'.format(a, b))
    return a

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    # a, b = 1071, 1029
    a = int(input())
    b = int(input())
    print(mcd1(a, b))
    print(mcd2(a, b))
