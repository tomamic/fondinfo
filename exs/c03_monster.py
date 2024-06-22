#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

from random import randrange

W, H = 5, 5
player = (0, 0)

monster = (0, 0)
while monster == player:
    monster = (randrange(W), randrange(H))

gold = (0, 0)
while gold == player or gold == monster:
    gold = (randrange(W), randrange(H))

while player != monster and player != gold:
    direction = input(f"Position: {player}. Direction (w/a/s/d)? ")
    x, y = player  # unpacking
    if direction == "w" and y > 0:
        y -= 1
    elif direction == "a" and x > 0:
        x -= 1
    elif direction == "s" and y < H - 1:
        y += 1
    elif direction == "d" and x < W - 1:
        x += 1
    player = (x, y)

if player == gold:
    print(f"Position: {player}. Gold!")
else:
    print(f"Position: {player}. Monster!")
