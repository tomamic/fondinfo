'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

3.4 Matrice, coppie
* Allocare una matrice, dimensione rows×cols
  * rows e cols scelti dall'utente, ma celle in numero pari
  * Matrice o pseudo-matrice
* Inserire in ordine le prime lettere dell'alfabeto, ciascuna ripetuta due volte
* Ripetutamente, scegliere due celle a caso e scambiarne il contenuto
* Mostrare la matrice risultante
'''

import random

FIRST = ord('A')
rows = cols = size = 1

while size % 2 != 0:
    rows = int(input('Rows? '))
    cols = int(input('Cols? '))
    size = rows * cols

matrix = [chr(FIRST + i // 2) for i in range(size)]

for i in range(size):
    print(matrix[i], end='')
    if i % cols == cols - 1:
        print()
print()

random.shuffle(matrix)
## for i in range(size):
##     j = random.randrange(size)
##     matrix[i], matrix[j] = matrix[j], matrix[i]

for i in range(size):
    print(matrix[i], end='')
    if i % cols == cols - 1:
        print()

