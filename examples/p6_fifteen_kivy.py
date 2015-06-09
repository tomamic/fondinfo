#!/usr/bin/python3

from sys import argv

from kivy.app import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
 
from p5_fifteen_puzzle import FifteenPuzzle


class GridButton(Button):
    grid_pos = ListProperty((0, 0))


class FifteenGui(GridLayout):
    def __init__(self):
        GridLayout.__init__(self, cols=4)
        self._puzzle = FifteenPuzzle(4, 4)
        for y in range(self._puzzle.rows):
            for x in range(self._puzzle.cols):
                btn = GridButton(grid_pos=(x, y),
                                 background_color=(0, 1, 0, 1))
                btn.bind(on_release=self.handle_click)
                self.add_widget(btn)
        self.update_buttons()

    def update_button(self, x: int, y: int):
        val = self._puzzle.get(x, y)
        symbol = chr(ord('A') + val - 1)
        if val == 0: symbol = ' '

        b = self.children[-1 - y * self._puzzle.cols - x]
        b.text = symbol  # children are reversed, in Kivy

    def update_buttons(self):
        for y in range(self._puzzle.rows):
            for x in range(self._puzzle.cols):
                self.update_button(x, y)
                
    def handle_click(self, btn: Button):
        self._puzzle.move_pos(*btn.grid_pos)     # args unpacking
        self.update_button(*self._puzzle.blank)
        self.update_button(*self._puzzle.moved)

        if self._puzzle.finished:
            popup = Popup(title='Congratulations',
                          content=Button(text='Game finished!'))
            popup.content.bind(on_release=popup.dismiss)
            popup.open()
            self._puzzle.shuffle()
            self.update_buttons()

            
if __name__ == '__main__':
    runTouchApp(FifteenGui())
