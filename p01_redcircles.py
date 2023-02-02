#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

R = 300
g2d.init_canvas((R * 2, R * 2))

n = int(g2d.prompt("Circles? "))
for i in reversed(range(n)):
    red = i * 255 / max(n - 1, 1)
    radius = (i + 1) * R / n
    g2d.set_color((red, 0, 0))
    g2d.draw_circle((R, R), radius)

g2d.main_loop()
