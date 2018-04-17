#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Resistenze, ciclo (*)
- Leggere, attraverso un ciclo, una sequenza di valori di resistenze elettriche
- La sequenza termina quando l'utente immette il valore 0
- Alla fine, visualizzare la resistenza equivalente, sia nel caso di resistenze disposte in serie, che in parallelo
'''

total = 0
total_inv = 0

val = float(input("val? "))
while val > 0:
    total += val
    total_inv += 1 / val
    val = float(input("val? "))

if total > 0:
    print(total, 1 / total_inv)
