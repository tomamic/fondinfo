#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Conteggio cifre
- Leggere un numero intero positivo
- Determinare di quante cifre è composto
- Quante volte riusciamo a dividerlo per 10, prima che si annulli?
'''

n = 0
while n <= 0:
    n = int(input("n? "))

count = 0
while n != 0:
    n = n // 10
    count += 1

print(count)
