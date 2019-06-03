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
sprites = g2d.load_image("sprites.png")

def tick():
    if g2d.key_pressed("ArrowUp"):
        turtle.go_up()
    elif g2d.key_pressed("ArrowRight"):
        turtle.go_right()
    elif g2d.key_pressed("ArrowDown"):
        turtle.go_down()
    elif g2d.key_pressed("ArrowLeft"):
        turtle.go_left()
    elif (g2d.key_released("ArrowUp") or
          g2d.key_released("ArrowRight") or
          g2d.key_released("ArrowDown") or
          g2d.key_released("ArrowLeft")):
        turtle.stay()

    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        if a.symbol != (0, 0, 0, 0):
            g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
