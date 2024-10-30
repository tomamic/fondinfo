#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

import g2d

g2d.init_canvas((400, 400))  # width, height

r = int(g2d.prompt("Radius? [50-99]"))

if 50 <= r <= 99:
    g2d.set_color((0, 0, 255))
    g2d.draw_circle((200, 200), r)
else:
    g2d.alert("Out of range!")

g2d.set_color((255, 255, 0))
g2d.draw_circle((200, 200), 25)

g2d.main_loop()  # manage the window/canvas
