#!/usr/bin/env python3

import cppyy
cppyy.include("bounce.hpp")
from cppyy.gbl import Size, Point, Rect, Arena, Ball, Ghost, Turtle

import sys; sys.path.append('../../examples/')
import g2d

def make(typ, **attrs):
    obj = typ()
    for k, v in attrs.items():
        setattr(obj, k, v)
    return obj
    
def vals(obj, attrs=list("xywhrgb")):
    return tuple(getattr(obj, a) for a in attrs if hasattr(obj, a))

arena = Arena(make(Size, w=320, h=240))
b1 = Ball(arena, make(Point, x=40, y=80))
b2 = Ball(arena, make(Point, x=80, y=40))
g = Ghost(arena, make(Point, x=120, y=80))
turtle = Turtle(arena, make(Point, x=80, y=80))
sprites = g2d.load_image("sprites.png")

def update():
    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_image_clip(sprites, vals(a.symbol()), vals(a.position()))

def keydown(key):
    if key == "ArrowUp":
        turtle.go_up()
    elif key == "ArrowDown":
        turtle.go_down()
    elif key == "ArrowLeft":
        turtle.go_left()
    elif key == "ArrowRight":
        turtle.go_right()

def keyup(code):
    turtle.stay()

def main():
    g2d.init_canvas(vals(arena.size()))
    g2d.handle_events(update, keydown, keyup)
    g2d.main_loop()

main()
