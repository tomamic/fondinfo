#!/usr/bin/env python3
'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d

game2d.canvas_init((300, 300))

i = 0
while i < 5:
    x = i * 40
    y = i * 40
    red = i * 60
    game2d.draw_rect((red, 0, 0), (x, y, 140, 140))
    i += 1
