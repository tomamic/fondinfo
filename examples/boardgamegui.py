#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from boardgame import BoardGame
from time import time

W, H = 40, 40
LONG_PRESS = 0.5

class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._game = g
        self._mouse_down = 0
        self.update_buttons()

    def tick(self):
        if "LeftButton" in g2d.current_keys() and self._mouse_down == 0:
            self._mouse_down = time()
        elif "LeftButton" not in g2d.current_keys() and self._mouse_down > 0:
            mouse = g2d.mouse_position()
            x, y = mouse[0] // W, mouse[1] // H
            if time() - self._mouse_down > LONG_PRESS:
                self._game.flag_at(x, y)
            else:
                self._game.play_at(x, y)
            self.update_buttons()
            self._mouse_down = 0

    def update_buttons(self):
        g2d.clear_canvas()
        g2d.set_color((0, 0, 0))
        cols, rows = self._game.cols(), self._game.rows()
        for y in range(1, rows):
            g2d.draw_line((0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((x * W, 0), (x * W, rows * H))
        for y in range(rows):
            for x in range(cols):
                value = str(self._game.value_at(x, y))
                center = x * W + W//2, y * H + H//2
                g2d.draw_text_centered(value, center, H//2)
        g2d.update_canvas()
        if self._game.finished():
            g2d.alert(self._game.message())
            g2d.close_canvas()

def gui_play(game: BoardGame):
    g2d.init_canvas((game.cols() * W, game.rows() * H))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
