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
    max_val = 0
    txt = g2d.prompt("Val? ")
    while txt:
        val = float(txt)
        values.append(val)
        if val > max_val:
            max_val = val
        txt = g2d.prompt("Val? ")

    n = len(values)
    for i in range(n):
        v = values[i]
        position = 0, i * H / n
        size = v * W / max_val, (H / n) - 1
        g2d.fill_rect(position, size)

    g2d.main_loop()

main()
