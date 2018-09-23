#!/usr/bin/env python3

import g2d
from boardgame import BoardGame
from time import time

W, H = 40, 40
LONG_PRESS = 0.5

class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._game = g
        self._downtime = 0
        g2d.init_canvas((g.cols() * W, g.rows() * H))
        self.update_buttons()
        g2d.handle_mouse(self.mousedown, self.mouseup)

    def main_loop(self):
        g2d.main_loop()

    def mousedown(self, pos, button):
        self._downtime = time()

    def mouseup(self, pos, button):
        x, y = pos[0] // W, pos[1] // H
        if time() - self._downtime > LONG_PRESS:
            self._game.flag_at(x, y)
        else:
            self._game.play_at(x, y)
        self.update_buttons()

    def update_buttons(self):
        g2d.fill_canvas((255, 255, 255))
        rows, cols = self._game.rows(), self._game.cols()
        for y in range(1, rows):
            g2d.draw_line((0, 0, 0), (0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((0, 0, 0), (x * W, 0), (x * W, rows * H))
        for y in range(rows):
            for x in range(cols):
                g2d.draw_text_centered(self._game.get_val(x, y), (0, 0, 0),
                                       (x * W + W//2, y * H + H//2), H//2)
        g2d.update_canvas()
        if self._game.finished():
            g2d.alert(self._game.message())
            g2d.exit()
##            g2d.draw_text_centered(self._game.message(), (0, 0, 255),
##                                   (cols * W//2, rows * H//2), H//2)
