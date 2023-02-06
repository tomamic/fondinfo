#!/usr/bin/env python3
from tkinter import Tk, Button, Label, messagebox
from boardgame import BoardGame

class BoardGameGui(Tk):
    def __init__(self, game: BoardGame):
        super().__init__()
        self.title(type(game).__name__)
        self._game = game

        cols, rows = game.size()
        for y in range(rows):
            for x in range(cols):
                def clicked(bx=x, by=y):
                    self._game.play(bx, by, "")
                    self.update_buttons()
                b = Button(self, command=clicked)
                b.config(width=2, height=2, bg="palegreen")
                b.grid(column=x, row=y)
        l = Label(self)
        l.grid(column=0, row=rows, columnspan=cols)
        self.update_buttons()

    def update_buttons(self):
        cols, rows = self._game.size()
        for y in range(rows):
            for x in range(cols):
                b = self.grid_slaves(column=x, row=y)[0]
                b["text"] = self._game.read(x, y)
        l = self.grid_slaves(column=0, row=rows)[0]
        l["text"] = self._game.status()
        if self._game.finished():
            messagebox.showinfo("Game finished", self._game.status())
            self.destroy()


if __name__ == "__main__":
    from p09_tictactoe import TicTacToe
    game = TicTacToe()
    gui = BoardGameGui(game)
    gui.mainloop()
