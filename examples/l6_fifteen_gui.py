#!/usr/bin/python3

from sys import argv
from PySide.QtGui import (QButtonGroup, QGridLayout, QPushButton,
                          QWidget, QMessageBox, QApplication)
from l5_fifteen_puzzle import FifteenPuzzle


class FifteenGui(QWidget):
    def __init__(self, puzzle: FifteenPuzzle, parent: QWidget = None):
        super().__init__(parent)
        self.setWindowTitle(self.tr('Fifteen Puzzle'))
        self._puzzle = puzzle
        self._buttons = QButtonGroup()
        self.setLayout(QGridLayout())
        for y in range(puzzle.rows):
            for x in range(puzzle.cols):
                b = QPushButton()
                self._buttons.addButton(b, y * puzzle.cols + x)
                self.layout().addWidget(b, y, x)
        self.update_all_buttons()
        self._buttons.buttonClicked[int].connect(self.handle_click)
        self.show()
        
    def update_all_buttons(self):
        for y in range(self._puzzle.rows):
            for x in range(self._puzzle.cols):
                val = str(self._puzzle.get(x, y))
                if val == '0': val = ' '
                i = y * self._puzzle.cols + x
                self._buttons.button(i).setText(val)

    def handle_click(self, i: int):
        y = i // self._puzzle.cols
        x = i % self._puzzle.cols
        self._puzzle.move_position(x, y)
        self.update_all_buttons()
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
