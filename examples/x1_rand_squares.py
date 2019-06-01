#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

Quadrati casuali
- Chiedere all'utente un numero n
- Disegnare n quadrati
-- Tutti con lato di 100 pixel
-- Ciascuno in posizione casuale
-- Ciascuno con un colore casuale
'''

import g2d
from random import randrange

W, H = 640, 480
SIDE = 100
g2d.init_canvas((W, H))

n = int(g2d.prompt("n? "))
i = 0
while i < n:
    color = randrange(255), randrange(255), randrange(255)
    rect = randrange(W - SIDE), randrange(H - SIDE), SIDE, SIDE
    g2d.set_color(color)
    g2d.fill_rect(rect)
    i += 1

g2d.main_loop()
