#!/usr/bin/env python3
from tkinter import Tk, Button, messagebox
from p09_fifteen import Fifteen, BoardGame

from functools import partial

class BoardGameGui(Tk):
    def __init__(self, game: BoardGame):
        super().__init__()
        self.title(type(game).__name__)
        self._game = game

        for y in range(game.rows()):
            for x in range(game.cols()):
                b = Button(self, width=2, height=2, bg="palegreen",
                     command=partial(self.handle_click, x, y))
                b.grid(column=x, row=y)
        self.update_buttons()

    def handle_click(self, x: int, y: int):
        self._game.play_at(x, y)
        self.update_buttons()

    def update_buttons(self):
        for y in range(self._game.rows()):
            for x in range(self._game.cols()):
                b = self.grid_slaves(row=y, column=x)[0]
                b["text"] = self._game.value_at(x, y)
        if self._game.finished():
            messagebox.showinfo("Game finished", self._game.message())
            self.destroy()


def main():
    game = Fifteen(3, 3)
    gui = BoardGameGui(game)
    gui.mainloop()

main()
