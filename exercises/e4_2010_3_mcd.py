'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

4.3 Ricorsione, MCD
* Leggere due numeri
* Calcolare il loro Massimo Comun Divisore
* Visualizzare il risultato

(Provare ad usare sia l'iterazione che la ricorsione)
(Euclide: MCD(m, n) = MCD(n, m mod n), se n > 0; MCD(m, n) = m, se n = 0)
'''

import logging

def mcd1(m: int, n: int) -> int:
    logging.debug('mcd1 {} {}'.format(m, n))
    if n == 0:
        return m
    else:
        return mcd1(n, m % n)

def mcd2(m: int, n: int) -> int:
    logging.debug('mcd2 {} {}'.format(m, n))
    while n != 0:
        m, n = n, m % n
        logging.debug('mcd2 {} {}'.format(m, n))
    return m

if __name__ == '__main__':
    # m, n = 1071, 1029
    m = int(input())
    n = int(input())
    logging.basicConfig(level=logging.DEBUG)
    print(mcd1(m, n))
    print(mcd2(m, n))
