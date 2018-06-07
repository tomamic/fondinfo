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

import game2d as g2d
from random import randrange

W, H = 640, 480
SIDE = 100

n = int(input("n? "))

g2d.init_canvas((W, H))

i = 0
while i < n:
    color = randrange(255), randrange(255), randrange(255)
    x, y = randrange(W - SIDE), randrange(H - SIDE)
    g2d.draw_rect(color, (x, y, SIDE, SIDE))
    i += 1

g2d.main_loop()
