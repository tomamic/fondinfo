#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p2_oop_ball import Ball, ARENA_W, ARENA_H

def tick():
    g2d.clear_canvas()  # BG
    for b in balls:
        b.move()
        g2d.fill_rect(b.position())  # FG

def main():
    global balls
    balls = [Ball((40, 80)), Ball((80, 40)), Ball((120, 120))]
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
