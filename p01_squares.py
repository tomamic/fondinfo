#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

L = 500
g2d.init_canvas((L, L))

n = 4        ## int(g2d.prompt("N?"))
l = 200      ## 2 * L / (n + 1)
d_pos = 100  ## l / 2
d_red = 85   ## 255 // max(n - 1, 1)

for i in range(n):
    pos = i * d_pos
    red = i * d_red
    g2d.set_color((red, 0, 0))
    g2d.draw_rect((pos, pos), (l, l))

g2d.main_loop()
