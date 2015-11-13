#!/usr/bin/python3

from sys import argv

from kivy.app import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
 
from p5_tictactoe import TicTacToe


class GridButton(Button):
    grid_pos = ListProperty((0, 0))


class TicTacToeGui(GridLayout):
    def __init__(self):
        GridLayout.__init__(self, cols=3)
        self._game = TicTacToe(3)
        for y in range(self._game.side()):
            for x in range(self._game.side()):
                btn = GridButton(grid_pos=(x, y),
                                 background_color=(0, 1, 0, 1))
                btn.bind(on_release=self.handle_click)
                self.add_widget(btn)
        self.update_buttons()

    def update_button(self, x, y):
        val = self._game.get(x, y)
        if val == TicTacToe.NONE: val = ' '

        b = self.children[-1 - y * self._game.side() - x]
        b.text = val  # children are reversed, in Kivy

    def update_buttons(self):
        for y in range(self._game.side()):
            for x in range(self._game.side()):
                self.update_button(x, y)
                
    def handle_click(self, btn):
        self._game.play_at(*btn.grid_pos)     # args unpacking
        self.update_button(*btn.grid_pos)

        winner = self._game.winner()
        if winner != TicTacToe.NONE:
            popup = Popup(title='Game finished',
                          content=Button(text=winner + ' has won'))
            popup.content.bind(on_release=popup.dismiss)
            popup.open()
            self._game.clear()
            self.update_buttons()

            
if __name__ == '__main__':
    runTouchApp(TicTacToeGui())
