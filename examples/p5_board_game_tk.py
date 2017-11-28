#!/usr/bin/env python3

from tkinter import Tk, Button, messagebox

from p4_board_game import BoardGame, Knights

class BoardGameGui(Tk):
    def __init__(self, g: BoardGame):
        Tk.__init__(self)
        self._game = g

        for y in range(g.rows()):
            for x in range(g.cols()):
                b = Button(self, width=1, height=1, font=('', 16))
                b['command'] = (lambda x=x, y=y:
                                (self._game.play_at(x, y),
                                 self.update_buttons()))
                b.grid(column=x, row=y)
        self.update_buttons()

    def update_buttons(self):
        for y in range(self._game.rows()):
            for x in range(self._game.cols()):
                b = self.grid_slaves(row=y, column=x)[0]
                b['text'] = self._game.get_val(x, y)
        if self._game.finished():
            messagebox.showinfo('Game finished', self._game.message())
            self.destroy()


def main():
    game = Knights(6)
    gui = BoardGameGui(game)
    gui.mainloop()
    
if __name__ == '__main__':
    main()
