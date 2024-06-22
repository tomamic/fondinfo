#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io
@license This software is free - https://opensource.org/license/mit
"""

import sys; sys.path.append("../")
import g2d

def main():
    W, H = 600, 400
    g2d.init_canvas((W, H))

    values = []

    while (txt := g2d.prompt("Val? ")):
        values.append(float(txt))

    n, vmax = len(values), max(values)
    if vmax > 0 and n > 0:
        for i, v in enumerate(values):
            w = v * W / vmax
            g2d.draw_rect((0, i * H / n), (w, H / n - 1))

    g2d.main_loop()

main()
