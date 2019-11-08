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
        
    def handle_keyboard(self):
        hero = self._game.hero()
        if g2d.key_pressed("ArrowUp"):
            hero.go_up(True)
        elif g2d.key_released("ArrowUp"):
            hero.go_up(False)
        if g2d.key_pressed("ArrowRight"):
            hero.go_right(True)
        elif g2d.key_released("ArrowRight"):
            hero.go_right(False)
        if g2d.key_pressed("ArrowDown"):
            hero.go_down(True)
        elif g2d.key_released("ArrowDown"):
            hero.go_down(False)
        if g2d.key_pressed("ArrowLeft"):
            hero.go_left(True)
        elif g2d.key_released("ArrowLeft"):
            hero.go_left(False)
    
    def tick(self):
        self.handle_keyboard()
        arena = self._game.arena()
        arena.move_all()  # Game logic
    
        g2d.clear_canvas()
        for a in arena.actors():
            if a.symbol() != (0, 0, 0, 0):
                g2d.draw_image_clip(self._sprites, a.symbol(), a.position())
            else:
                g2d.fill_rect(a.position())
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
