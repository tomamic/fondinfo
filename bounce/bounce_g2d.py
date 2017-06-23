#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *

from bounce import Arena, Ball, Ghost, Turtle


def update():
    arena.move_all()  # Game logic

    canvas_fill((255, 255, 255))
    for a in arena.actors():
        x, y, w, h = a.rect()
        # use the following lines to cut a sprite from a larger image
        xs, ys = a.symbol()
        image_blit(sprites, (x, y), area=(xs, ys, w, h))    

def keydown(code):
    print(code + " dn")
    if code == "ArrowUp":
        turtle.go_up()
    elif code == "ArrowDown":
        turtle.go_down()
    elif code == "ArrowLeft":
        turtle.go_left()
    elif code == "ArrowRight":
        turtle.go_right()

def keyup(code):
    print(code + " up")
    turtle.stay()

arena = Arena(320, 240)
Ball(arena, 40, 80)
Ball(arena, 80, 40)
Ghost(arena, 120, 80)
turtle = Turtle(arena, 80, 80)

canvas_init(arena.size())
sprites = image_load("sprites.png")

handle_keyboard(keydown, keyup)
set_interval(update, 1000//30)  # millis
