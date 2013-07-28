'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

3.5 Sottostringhe
* Leggere da tastiera un testo generico
* Estrarre le parti comprese tra '<' e '>'
* Riprodurre in output, ciascuna su una riga, le parti selezionate
(Es. “Scrivete a < john@example.com > per informazioni” → “john@example.com”)
'''

text = 'Scrivete a <john@example.com> o <tom@example.com> per informazioni'
match = []
inside = False
for c in text:
    if c == '<':
        inside = True
    elif c == '>' and inside:
        print(''.join(match))
        match = []
        inside = False
    elif inside:
        match.append(c)
