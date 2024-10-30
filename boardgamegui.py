#!/usr/bin/env python3
"""
@author  Michele Tomaiuolo - https://tomamic.github.io/
@license This software is free - https://opensource.org/license/mit
"""

try:
    from __main__ import g2d
except:
    import g2d
from boardgame import BoardGame

W, H = 40, 40

class BoardGameGui:
    def __init__(self, game: BoardGame):
        self._game = game
        self.update_buttons()

    def tick(self):
        game = self._game
        mouse_x, mouse_y = g2d.mouse_pos()
        x, y = mouse_x // W, mouse_y // H
        released = set(g2d.previous_keys()) - set(g2d.current_keys())
        if game.finished():
            g2d.alert(game.status())
            g2d.close_canvas()
        elif "Escape" in released:  # "Escape" key released
            g2d.close_canvas()
        elif "LeftButton" in released and y < game.rows():
            game.play(x, y, "")
            self.update_buttons((x, y))
        elif "RightButton" in released and y < game.rows():
            game.play(x, y, "flag")
            self.update_buttons((x, y))

    def update_buttons(self, last_move=None):
        cols, rows = self._game.cols(), self._game.rows()
        g2d.set_color((0, 0, 0))
        g2d.draw_rect((0, 0), (cols * W, rows * H + H))
        for y in range(rows):
            for x in range(cols):
                gray = 232 if (x, y) == last_move else 255
                text = self._game.read(x, y)
                _write(text, (x, y), bg=(gray, gray, gray))
        status = self._game.status()
        _write(status, (0, rows), cols)
        
def _write(text, pos, cols=1, bg=(255, 255, 255)):
    x, y = pos
    g2d.set_color(bg)
    g2d.draw_rect((x * W + 1, y * H + 1), (cols * W - 2, H - 2))
    
    chars = max(1, len(text))
    fsize = min(0.75 * H, 1.5 * cols * W / chars)
    center = (x * W + cols * W/2, y * H + H/2)
    g2d.set_color((0, 0, 0))
    g2d.draw_text(text, center, fsize)

def gui_play(game: BoardGame):
    g2d.init_canvas((game.cols() * W, game.rows() * H + H))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
