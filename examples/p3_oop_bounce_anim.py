#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p3_oop_bounce import Arena, Ball, Ghost, Turtle

arena = Arena(320, 240)
b1 = Ball(arena, 40, 80)
b2 = Ball(arena, 80, 40)
g = Ghost(arena, 120, 80)
turtle = Turtle(arena, 80, 80)
sprites = g2d.load_image("sprites.png")

def update():
    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_image_clip(sprites, a.symbol(), a.position())

def keydown(key):
    #print(key + " dn")
    if key == "ArrowUp":
        turtle.go_up()
    elif key == "ArrowDown":
        turtle.go_down()
    elif key == "ArrowLeft":
        turtle.go_left()
    elif key == "ArrowRight":
        turtle.go_right()

def keyup(key):
    #print(key + " up")
    turtle.stay()

def main():
    g2d.init_canvas(arena.size())
    g2d.handle_events(update, keydown, keyup)
    g2d.main_loop()

main()
