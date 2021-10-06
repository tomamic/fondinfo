#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from x3_oop_bounce_game import BounceGame


class BounceGui:
    def __init__(self):
        self._game = BounceGame()
        g2d.init_canvas(self._game.arena().size())
        self._sprites = g2d.load_image("sprites.png")
        g2d.main_loop(self.tick)

    def tick(self):
        self._game.hero().control(g2d.current_keys())
        arena = self._game.arena()
        arena.move_all()  # Game logic

        g2d.clear_canvas()
        for a in arena.actors():
            if a.symbol() != None:
                g2d.draw_image_clip(self._sprites, a.symbol(), a.size(), a.position())
            else:
                g2d.fill_rect(a.position(), a.size())
        lives = "Lives: " + str(self._game.hero().lives())
        toplay = "Time: " + str(self._game.remaining_time())
        g2d.draw_text(lives + " " + toplay, (0, 0), 24)

        if self._game.game_over():
            g2d.alert("Game over")
            g2d.close_canvas()
        elif self._game.game_won():
            g2d.alert("Game won")
            g2d.close_canvas()

gui = BounceGui()
