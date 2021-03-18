#!/usr/bin/env python3

from tkinter import Tk, Button, messagebox

from p5_mat_fifteen import Fifteen

class FifteenGui(Tk):
    def __init__(self, puzzle: Fifteen):
        super().__init__()
        self.title("Fifteen Puzzle")
        self._puzzle = puzzle
        self._cols = puzzle.cols()
        self._rows = puzzle.rows()

        for y in range(self._rows):
            for x in range(self._cols):
                b = Button(self, width=2, height=2, bg="palegreen",
                     command=lambda x=x, y=y: self.handle_click(x, y))
                b.grid(column=x, row=y)
        self.update_all_buttons()

    def handle_click(self, x: int, y: int):
        self._puzzle.play_at(x, y)
        self.update_all_buttons()

    def update_all_buttons(self):
        for y in range(self._rows):
            for x in range(self._cols):
                b = self.grid_slaves(row=y, column=x)[0]
                b["text"] = self._puzzle.value_at(x, y)
        if self._puzzle.finished():
            messagebox.showinfo("Game finished", self._game.message())
            self.destroy()


def main():
    puzzle = Fifteen(3, 3)
    gui = FifteenGui(puzzle)
    gui.mainloop()

if __name__ == '__main__':
    main()
