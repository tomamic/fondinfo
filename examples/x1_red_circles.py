#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

radius = 300
g2d.init_canvas((radius * 2, radius * 2))

n = int(g2d.prompt("Circles? "))
i = n
while i > 0:
    r = i * radius / n
    c = 0
    if n > 1:
        c = (i-1) * 255 / (n-1)
    g2d.set_color((c, 0, 0))
    g2d.fill_circle((radius, radius), r)
    i -= 1

g2d.main_loop()
