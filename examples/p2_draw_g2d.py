#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d

game2d.canvas_init((400, 400))

game2d.draw_rect((165, 0, 255), (100, 100, 250, 250))
game2d.draw_circle((255, 0, 0), (100, 100), 20)

game2d.draw_text("Hello", (0, 255, 0), (0, 0), 60)
