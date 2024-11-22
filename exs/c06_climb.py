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

class Climber:
    def __init__(self, y, x, top):
        self._y = y  # upright position
        self._x = x  # route
        self._start = y
        self._top = top

    def win(self):
        return self._y == self._top
    
    def move(self):
        self._y = max(min(self._y - randint(-1, 3), self._start), self._top)
    
    def pos(self):
        return (self._x,self._y)

x_a = ARENA_W / 4    # climbing a route
x_b = ARENA_W - x_a  # climbing b route
end_game = False

a = Climber(START, x_a, TOP)
b = Climber(START, x_b, TOP)

def tick():
    global end_game
    if end_game:
        return
    if a.win() and b.win():
        g2d.draw_text ("Both climbers win", (ARENA_W/2,20),15)
        #print("both winners")
        end_game = True
    elif a.win():
        g2d.draw_text ("Climber a wins the race", (ARENA_W/2, 20), 15)
        #print("the climber a wins the race")
        end_game = True
    elif b.win():
        g2d.draw_text ("Climber b wins the race", (ARENA_W/2, 20), 15)
        #print("the climber b wins the race")
        end_game = True
    else:
        # move
        a.move()
        b.move()
        # Draw background
        g2d.clear_canvas()
        # Draw foreground
        g2d.draw_image("climbing.png", a.pos())
        g2d.draw_image("climbing.png", b.pos())

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()

