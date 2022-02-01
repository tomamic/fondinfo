#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p3_oop_bounce import Arena, Ball, Ghost, Turtle

arena = Arena((480, 360))
arena.spawn(Ball((40, 80)))
arena.spawn(Ball((80, 40)))
arena.spawn(Ghost((120, 80)))
arena.spawn(Turtle((80, 80)))

def tick():
    arena.tick(g2d.current_keys())  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if a.sprite() != None:
            g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())
        else:
            pass  # g2d.fill_rect(a.pos(), a.size())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
