#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import game2d as g2d

# Create canvas, width=600, height=400
g2d.init_canvas((600, 400))

# Yellow rectangle, left=150, top=100, w=250, h=200
# red=255 (max), green=255 (max), blue=0 (min)
g2d.draw_rect((255, 255, 0), (150, 100, 250, 200))

# Green diagonal
g2d.draw_line((0, 255, 0), (150, 100), (400, 300))

# Blue circle, center=(400, 300), radius=20
g2d.draw_circle((0, 0, 255), (400, 300), 20)

# Red text, pos=(150, 100), size=40
g2d.draw_text("Hello", (255, 0, 0), (150, 100), 40)

g2d.main_loop()
