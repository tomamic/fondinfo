#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import randrange

W, H = 5, 5

player = 0, 0
monster = 0, 0
while monster == player:
    monster = randrange(W), randrange(H)
gold = 0, 0
while gold == player or gold == monster:
    gold = randrange(W), randrange(H)

#print('Monster:', monster)
#print('Gold:', gold)
print('Player:', player)

while player != monster and player != gold:
    direction = input('wasd? ')
    x, y = player
    if direction == 'w' and y > 0:
        player = x, y - 1
    elif direction == 'a' and x > 0:
        player = x - 1, y
    elif direction == 's' and y < H - 1:
        player = x, y + 1
    elif direction == 'd' and x < W - 1:
        player = x + 1, y
    print('Player:', player)

if player == gold:
    print('Gold!')
else:
    print('Monster!')
