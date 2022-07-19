#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

def main():
    W, H = 600, 400
    g2d.init_canvas((W, H))

    values = []
    txt = g2d.prompt("Val? ")
    while txt:
        values.append(float(txt))
        txt = g2d.prompt("Val? ")

    n, max_val = len(values), max(values)
    for i, v in enumerate(values):
        pos = 0, i * H / n
        size = v * W / max_val, (H / n) - 1
        g2d.fill_rect(pos, size)

    g2d.main_loop()

main()
