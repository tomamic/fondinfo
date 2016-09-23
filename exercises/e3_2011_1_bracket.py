#!/usr/bin/env python3
'''
3.1 File, parentesi
* Leggere da file un carattere alla volta
* Riscrivere il testo a console, ma...
* Escludere il testo tra parentesi '(', ')'
(Segnare in un bool se si è letta una quadra aperta, ma non ancora una quadra chiusa)
(Se necessario, provare prima a leggere i caratteri da console)

@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

text = ''
with open('e3_2011_1_bracket.py') as infile:
    text = infile.read()

inside = False

for c in text:
    if c == '(':
        inside = True
    elif c == ')' and inside:
        inside = False
    elif not inside:
        print(c, end='')
