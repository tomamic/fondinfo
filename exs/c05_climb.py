#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from random import randint

ARENA_W, ARENA_H = 480, 320
START = ARENA_H - 10
TOP = 0
climb_a = climb_b = START  # start
win_a = win_b = False      # winner
x_a = ARENA_W / 4          # climbing a route
x_b = ARENA_W - x_a        # climbing b route
end_game = False

def tick():
    global end_game, climb_a, climb_b
    if end_game:
        return
    
    win_a = climb_a == TOP
    win_b = climb_b == TOP
    if win_a and win_b:
        g2d.draw_text ("Both climbers win", (ARENA_W/2, 20), 15)
        #print("both winners")
        end_game = True
    elif win_a:
        g2d.draw_text ("Climber a wins the race", (ARENA_W/2, 20), 15)
        #print("the climber a wins the race")
        end_game = True
    elif win_b:
        g2d.draw_text ("Climber b wins the race", (ARENA_W/2, 20), 15)
        #print("the climber b wins the race")
        end_game = True
    else:
        # move
        climb_a = move(climb_a)
        climb_b = move(climb_b)
        # Draw background
        g2d.clear_canvas()
        # Draw foreground
        g2d.draw_image("climbing.png", (x_a, climb_a))
        g2d.draw_image("climbing.png", (x_b, climb_b))

def move(pos: int) -> int:
    return max(min(pos - randint(-1, 3), START), TOP)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()

