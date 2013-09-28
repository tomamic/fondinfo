#!/usr/bin/python3

from sys import argv
from PySide.QtGui import (QButtonGroup, QGridLayout, QPushButton,
                          QWidget, QMessageBox, QApplication)
from p5_fifteen_puzzle import FifteenPuzzle


class FifteenGui(QWidget):
    def __init__(self, puzzle: FifteenPuzzle):
        super().__init__()
        self._puzzle = puzzle
        self._buttons = []
        self.setLayout(QGridLayout())
        for y in range(puzzle.rows):
            for x in range(puzzle.cols):
                b = QPushButton()
                self._buttons.append(b)
                self.layout().addWidget(b, y, x)
                b.clicked.connect(lambda x=x, y=y:
                    self.handle_click(x, y))
        self.update_all_buttons()
        self.setWindowTitle(self.tr('Fifteen Puzzle'))
        self.show()
        
    def update_button(self, x: int, y: int):
        val = self._puzzle.get(x, y)
        symbol = chr(ord('A') + val - 1)
        if val == 0: symbol = ' '

        b = self._buttons[y * self._puzzle.cols + x]
        b.setText(symbol)

    def update_all_buttons(self):
        for y in range(self._puzzle.rows):
            for x in range(self._puzzle.cols):
                self.update_button(x, y)
                
    def handle_click(self, x: int, y: int):
        self._puzzle.move_pos(x, y)
        self.update_button(*self._puzzle.blank)  # args unpacking
        self.update_button(*self._puzzle.moved)

        if self._puzzle.finished:
            QMessageBox.information(self, self.tr('Congratulations'),
                                    self.tr('Game finished!'))
            self._puzzle.shuffle()
            self.update_all_buttons()
            

def main():
    app = QApplication(argv)
    puzzle = FifteenPuzzle(4, 4)
    gui = FifteenGui(puzzle)
    app.exec_()

if __name__ == '__main__':
    main()
