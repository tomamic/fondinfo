#!/usr/bin/env python3

from tkinter import Tk, Button, messagebox

from p4_board_game import BoardGame, Knights

class BoardGameGui(Tk):
    def __init__(self, game: BoardGame):
        super().__init__()
        self._game = game
        self._cols, self._rows = game.cols(), game.rows()
        
        for y in range(self._rows):
            for x in range(self._cols):
                b = Button(self, width=1, height=1, font=('', 16))
                b['command']=lambda x=x, y=y: self.handle_click(x, y)
                b.grid(column=x, row=y)
        self.update_all_buttons()

    def handle_click(self, x: int, y: int):
        self._game.play_at(x, y)
        self.update_all_buttons()

    def update_all_buttons(self):
        for y in range(self._rows):
            for x in range(self._cols):
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
