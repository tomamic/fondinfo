#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from kivy.app import runTouchApp
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import *

from actor import *
from bounce import *


arena = Arena(320, 240)
Ball(arena, 40, 80)
Ball(arena, 80, 40)
Ghost(arena, 120, 80)
turtle = Turtle(arena, 80, 80)

sprites = Image('sprites.png').texture


class GameWidget(Widget):
    def __init__(self):
        Widget.__init__(self)
        Window.size = arena.size()
        self._touch_orig = None
        Clock.schedule_interval(self.advance_game, 1 / 30)

    def on_touch_down(self, touch):
        self._touch_orig = touch.x, touch.y

    def on_touch_up(self, touch):
        turtle.stay()
        self._touch_orig = None
        
    def on_touch_move(self, touch):
        threshold = 10
        dx = touch.x - self._touch_orig[0]
        dy = touch.y - self._touch_orig[1]
        if abs(dx) > abs(dy):
            if dx >= threshold: turtle.go_right()
            elif dx <= -threshold: turtle.go_left()
            else: turtle.stay()
        else:
            if dy >= threshold: turtle.go_up()
            elif dy <= -threshold: turtle.go_down()
            else: turtle.stay()

    def advance_game(self, dt):
        arena.move_all()
        self.draw_game()

    def draw_game(self):
        self.canvas.clear()
        with self.canvas:
            Color(.5, 1, .5)
            Rectangle(size=self.size, pos=self.pos)
            t_orig = self._touch_orig
            if t_orig is not None:
                Color(.8, .8, .8)
                Ellipse(pos=(t_orig[0] - 10, t_orig[1] - 10), size=(20, 20))
            for c in arena.actors():
                x, y, w, h = c.rect()
                Color(1, 1, 1)
                xs, ys = c.symbol()
                img = sprites.get_region(xs, sprites.height - ys - h, w, h)
                Rectangle(texture=img, pos=(x, arena.size()[1] - y - h), size=(w, h))


if __name__ == '__main__':
    runTouchApp(GameWidget())
