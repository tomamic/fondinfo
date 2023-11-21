#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from boardgame import BoardGame

W, H = 40, 40

class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._game = g
        self.update_buttons()

    def tick(self):
        cols, rows = self._game.size()
        x, y = g2d.mouse_pos()
        bx, by = x // W, y // H
        released = set(g2d.previous_keys()) - set(g2d.current_keys())
        if self._game.finished():
            g2d.alert(self._game.status())
            g2d.close_canvas()
        elif "Escape" in released:  # "Escape" key released
            g2d.close_canvas()
        elif "LeftButton" in released and by < rows:
            self._game.play(bx, by, "")
            self.update_buttons()
        elif "RightButton" in released and by < rows:
            self._game.play(bx, by, "flag")
            self.update_buttons()

    def update_buttons(self):
        g2d.clear_canvas()
        g2d.set_color((0, 0, 0))
        cols, rows = self._game.size()
        for y in range(1, rows):
            g2d.draw_line((0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.draw_line((x * W, 0), (x * W, rows * H))
        for y in range(rows):
            for x in range(cols):
                value = self._game.read(x, y)
                center = x * W + W // 2, y * H + H // 2
                g2d.draw_text_centered(value, center, H // 2)
        g2d.draw_text_centered(self._game.status(),
                               (cols*W//2, rows*H + H//2), H//2)

def gui_play(game: BoardGame):
    cols, rows = game.size()
    g2d.init_canvas((cols * W, rows * H + H))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
