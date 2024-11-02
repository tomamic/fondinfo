#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d
from random import randint

class Climber:
    def __init__(self, y, x, top):
        self._y = y    # upright position
        self._x = x    # route
        self._start = y
        self._top = top
    
    def win(self):
        return self._y == 0

    def move(self):
        raise NotImplementedError("Abstract method")
    
    def pos(self):
        return (self._x,self._y)
        
class RiskyClimber(Climber):
    def move(self):
        fall = randint(0, 80)
        if fall == 0:
            self._y = self._start
        else:
            jump = randint(0, 4)
            self._y = max(self._y - jump, self._top)
            
class SteadyClimber(Climber):
    def move(self):
        self._y = max(min(self._y - randint(-1, 4), self._start), self._top)
        
class MindfulClimber(Climber):
    def move(self):
        jump = randint(-5, 5)
        if jump > 0:
            self._y = max(self._y - jump, self._top)

ARENA_W, ARENA_H = 480, 320
START = ARENA_H - 10
TOP = 0

x_a = ARENA_W / 4    # climbing a route
x_b = ARENA_W - x_a  # climbing b route
end_game = False

climb_num = 9
climbers = []
route_space = ARENA_W / (climb_num + 1)
for i in range(climb_num):
    route = route_space * i + route_space - 16  # img is 32 px wide
    if i % 3 == 0:
        climbers.append(RiskyClimber(START, route, TOP))
    elif i % 3 == 1:
        climbers.append(SteadyClimber(START, route, TOP))
    else:
        climbers.append(MindfulClimber(START, route, TOP))

def tick():
    global end_game
    if end_game:
        return

    g2d.clear_canvas()
    for c in climbers:
        c.move()
        g2d.draw_image("climbing.png", c.pos())
    end_game = any(c.win() for c in climbers)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()

