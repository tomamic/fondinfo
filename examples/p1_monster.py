#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html

La stanza del mostro
- Il giocatore si muove su una scacchiera di 5x5 celle, partendo da un angolo
-- Le righe e le colonne sono numerate da 0 a 4
- Un tesoro ed un mostro sono nascosti in due posizioni casuali, all'inizio del gioco
- Ad ogni turno, il giocatore:
-- Sceglie una direzione verso cui spostarsi (alto, basso, sinistra, destra)
-- Se capita sulla cella del tesoro, ha vinto
-- Se capita sulla cella del mostro, ha perso
'''

from random import randrange

W, H = 5, 5

player_x = 0  # try and use a tuple: player = 0, 0
player_y = 0
monster_x = player_x  # try and use a tuple: monster = 0, 0
monster_y = player_y
while monster_x == player_x and monster_y == player_y:
    monster_x = randrange(W)
    monster_y = randrange(H)
gold_x = player_x  # try and use a tuple: gold = 0, 0
gold_y = player_y
while (gold_x == player_x and gold_y == player_y) or (gold_x == monster_x and gold_y == monster_y):
    gold_x = randrange(W)
    gold_y = randrange(H)

#print("Monster:", monster_x, monster_y)
#print("Gold:", gold_x, gold_y)
print("Player:", player_x, player_y)

while (player_x != monster_x or player_y != monster_y) and (player_x != gold_x or player_y != gold_y):
    direction = input("wasd? ")
    if direction == "w" and player_y > 0:
        player_y -= 1
    elif direction == "a" and player_x > 0:
        player_x -= 1
    elif direction == "s" and player_y < H - 1:
        player_y += 1
    elif direction == "d" and player_x < W - 1:
        player_x += 1
    print("Player:", player_x, player_y)

if player_x == gold_x and player_y == gold_y:
    print("Gold!")
else:
    print("Monster!")
