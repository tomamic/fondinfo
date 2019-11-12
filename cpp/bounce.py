#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy
cppyy.include("bounce.hpp")
from cppyy.gbl import Arena, Ball, Ghost, Turtle, Point, Rect

import sys; sys.path.append('../examples/')
import g2d_pyg as g2d

def pt(x, y):
    p = Point()
    p.x, p.y = x, y
    return p
##cppyy.gbl.Point.__getitem__ = lambda self, key: getattr(self, "xy"[key])
##cppyy.gbl.Rect.__getitem__ = lambda self, key: getattr(self, "xywh"[key])

arena = Arena(pt(480, 360))
b1 = Ball(arena, pt(40, 80))
b2 = Ball(arena, pt(80, 40))
g = Ghost(arena, pt(120, 80))
turtle = Turtle(arena, pt(80, 80))
sprites = g2d.load_image("../examples/sprites.png")

def tick():
    if g2d.key_pressed("ArrowUp"):
        turtle.go_up(True)
    elif g2d.key_released("ArrowUp"):
        turtle.go_up(False)
    if g2d.key_pressed("ArrowRight"):
        turtle.go_right(True)
    elif g2d.key_released("ArrowRight"):
        turtle.go_right(False)
    if g2d.key_pressed("ArrowDown"):
        turtle.go_down(True)
    elif g2d.key_released("ArrowDown"):
        turtle.go_down(False)
    if g2d.key_pressed("ArrowLeft"):
        turtle.go_left(True)
    elif g2d.key_released("ArrowLeft"):
        turtle.go_left(False)

    arena.move_all()  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        sym, pos = a.symbol(), a.position()
        g2d.draw_image_clip(sprites, (sym.x, sym.y, sym.w, sym.h),
                            (pos.x, pos.y, pos.w, pos.h))

def main():
    size = arena.size()
    g2d.init_canvas((size.x, size.y))
    g2d.main_loop(tick)

main()
