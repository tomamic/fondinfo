#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import random, logging

N = 1000
DIE_FACES = 6
ATTACK_DICE = 3
DEFENCE_DICE = 2

def roll_dice(dice: list):
    for i in range(len(dice)):
        dice[i] = random.randint(1, DIE_FACES)
    dice.sort()
    dice.reverse()

def attack_result(a: list, d: list) -> int:
    attack = 0
    # compare the best attack dice with the best defence dice
    for i in range(min(len(a), len(d))):
        if a[i] > d[i]:
            attack += 1
    return attack

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    attack = [0] * ATTACK_DICE
    defence = [0] * DEFENCE_DICE

    # associate a possible attack result (0, 1, 2, ...)
    # with its actually counted occurrences
    result_occurrences = [0] * (min(ATTACK_DICE, DEFENCE_DICE) + 1)

    for x in range(N):
        roll_dice(attack)
        logging.debug('a: {}'.format(attack))
        roll_dice(defence)
        logging.debug('d: {}'.format(defence))
        result = attack_result(attack, defence)
        logging.debug('result: {}\n'.format(result))
        result_occurrences[result] += 1

    for j, r in enumerate(result_occurrences):
        print(j, 100.0 * r / N)
