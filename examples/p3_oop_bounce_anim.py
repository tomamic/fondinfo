#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p3_oop_bounce import Arena, Ball, Ghost, Turtle

arena = Arena((480, 360))
b1 = Ball(arena, (40, 80))
b2 = Ball(arena, (80, 40))
g = Ghost(arena, (120, 80))
turtle = Turtle(arena, (80, 80))

def tick():
    turtle.control(g2d.current_keys())
    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if a.symbol() != None:
            g2d.draw_image_clip("sprites.png", a.symbol(), a.size(), a.position())
        else:
            g2d.fill_rect(a.position(), a.size())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
