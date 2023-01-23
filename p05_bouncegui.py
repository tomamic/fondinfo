#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from p05_bouncegame import BounceGame


class BounceGui:
    def __init__(self):
        self._game = BounceGame()
        g2d.init_canvas(self._game.size())
        g2d.main_loop(self.tick)

    def tick(self):
        g2d.clear_canvas()
        for a in self._game.actors():
            if a.sprite() != None:
                g2d.draw_image_clip("sprites.png", a.pos(), a.sprite(), a.size())
            else:
                pass  # g2d.draw_rect(a.pos(), a.size())
        lives, time = self._game.lives(), self._game.time()
        g2d.draw_text(f"Lives: {lives} Time: {time}", (0, 0), 24)

        if self._game.game_over():
            g2d.alert("Game over")
            g2d.close_canvas()
        elif self._game.game_won():
            g2d.alert("Game won")
            g2d.close_canvas()
        else:
            self._game.tick(g2d.current_keys())  # Game logic


gui = BounceGui()
