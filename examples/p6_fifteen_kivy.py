#!/usr/bin/python3

from sys import argv

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from p5_fifteen_puzzle import FifteenPuzzle


class FifteenGui(App):
    def build(self):
        self._puzzle = FifteenPuzzle(3, 3)
        self._buttons = []
        grid = GridLayout(cols=self._puzzle.cols)
        for y in range(self._puzzle.rows):
            for x in range(self._puzzle.cols):
                b = Button(background_color=(0, 1, 0, 1))
                b.bind(on_release=lambda btn, x=x, y=y:
                           self.handle_click(x, y))
                grid.add_widget(b)
                self._buttons.append(b)
        self.update_buttons()
        return grid

    def update_button(self, x: int, y: int):
        val = self._puzzle.get(x, y)
        symbol = chr(ord('A') + val - 1)
        if val == 0: symbol = ' '

        b = self._buttons[y * self._puzzle.cols + x]
        b.text = symbol

    def update_buttons(self):
        for y in range(self._puzzle.rows):
            for x in range(self._puzzle.cols):
                self.update_button(x, y)
                
    def handle_click(self, x: int, y: int):
        self._puzzle.move_pos(x, y)
        self.update_button(*self._puzzle.blank)  # args unpacking
        self.update_button(*self._puzzle.moved)

        if self._puzzle.finished:
            popup = Popup(title='Congratulations',
                          content=Button(text='Game finished!'))
            popup.content.bind(on_release=popup.dismiss)
            popup.open()
            self._puzzle.shuffle()
            self.update_buttons()
            

if __name__ == '__main__':
    FifteenGui().run()
