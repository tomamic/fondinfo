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
    val = float(g2d.prompt("Val? "))
    while val > 0:
        values.append(val)
        if val > max_val:
            max_val = val
        val = float(g2d.prompt("Val? "))

    if len(values) > 0:
        for i, v in enumerate(values):
            rect = (0, i * H / len(values),
                    v * W / max_val, (H / len(values))-1)
            g2d.fill_rect(rect)

    g2d.main_loop()

main()
