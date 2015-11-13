#!/usr/bin/python3

from sys import argv
from PySide.QtGui import (QButtonGroup, QGridLayout, QPushButton,
                          QWidget, QMessageBox, QApplication)
from p6_fifteen import Fifteen


class GameGui(QWidget):
    def __init__(self, puzzle: Fifteen):
        super().__init__()
        self._puzzle = puzzle
        self._cols, self._rows = puzzle.size()
        self.setLayout(QGridLayout())
        for y in range(self._rows):
            for x in range(self._cols):
                b = QPushButton()
                self.layout().addWidget(b, y, x)
                b.clicked.connect(lambda x=x, y=y:
                    self.handle_click(x, y))
        self.update_all_buttons()
        self.setWindowTitle(self.tr('Fifteen Puzzle'))
        self.show()

    def update_button(self, x: int, y: int):
        val = self._puzzle.get(x, y)
        symbol = ' '
        if val > 0: symbol = str(val)

        b = self.layout().itemAt(y * self._cols + x).widget()
        b.setText(symbol)

    def update_all_buttons(self):
        for y in range(self._rows):
            for x in range(self._cols):
                self.update_button(x, y)
                
    def handle_click(self, x: int, y: int):
        self._puzzle.move_pos(x, y)
        self.update_all_buttons()
        ##self.update_button(*self._puzzle.blank())  # args unpacking
        ##self.update_button(*self._puzzle.moved())

        if self._puzzle.finished():
            QMessageBox.information(self, self.tr('Congratulations'),
                                    self.tr('Game finished!'))
            self._puzzle.new_game()
            self.update_all_buttons()
            

def main():
    app = QApplication(argv)
    puzzle = Fifteen(4, 4)
    gui = GameGui(puzzle)
    app.exec_()

if __name__ == '__main__':
    main()
