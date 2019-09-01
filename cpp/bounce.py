#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy
cppyy.include("bounce.hpp")
from cppyy.gbl import Arena, Ball, Ghost, Turtle

import sys; sys.path.append('../examples/')
import g2d

def pt(x, y): p = cppyy.gbl.Point(); p.x, p.y = x, y; return p
cppyy.gbl.Point.__getitem__ = lambda self, key: getattr(self, "xy"[key])
cppyy.gbl.Rect.__getitem__ = lambda self, key: getattr(self, "xywh"[key])
cppyy.gbl.Color.__getitem__ = lambda self, key: getattr(self, "rgb"[key])

arena = Arena(pt(480, 360))
b1 = Ball(arena, pt(40, 80))
b2 = Ball(arena, pt(80, 40))
g = Ghost(arena, pt(120, 80))
turtle = Turtle(arena, pt(80, 80))
sprites = g2d.load_image("sprites.png")

def tick():
    if g2d.key_pressed("ArrowUp"):
        turtle.go_up()
    elif g2d.key_pressed("ArrowDown"):
        turtle.go_down()
    elif g2d.key_pressed("ArrowLeft"):
        turtle.go_left()
    elif g2d.key_pressed("ArrowRight"):
        turtle.go_right()
    elif (g2d.key_released("ArrowUp") or
          g2d.key_released("ArrowDown") or
          g2d.key_released("ArrowLeft") or
          g2d.key_released("ArrowRight")):
        turtle.stay()

    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_image_clip(sprites, a.symbol(), a.position())

def main():
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()
