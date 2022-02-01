#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import cppyy
cppyy.include("bounce.hpp")
from cppyy.gbl import Arena, Ball, Ghost, Turtle, Point

import sys; sys.path.append('../examples/')
import g2d

arena = Arena((480, 360))
arena.spawn(b1:=Ball((40, 80)))
arena.spawn(b2:=Ball((80, 40)))
arena.spawn(g:=Ghost((120, 80)))
arena.spawn(t:=Turtle((80, 80)))
sprites = g2d.load_image("../examples/sprites.png")

def tick():
    arena.tick(g2d.current_keys())  # Game logic

    g2d.clear_canvas()
    for a in arena.actors():
        g2d.draw_image_clip(sprites, a.pos(), a.sprite(), a.size())

def main():
    size = arena.size()
    g2d.init_canvas((size.x, size.y))
    g2d.main_loop(tick)

main()
