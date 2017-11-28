#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from sys import argv
from PyQt5.QtWidgets import (QButtonGroup, QGridLayout, QPushButton,
                             QWidget, QMessageBox, QApplication)
from p4_board_game import BoardGame, Knights


class BoardGameGui(QWidget):
    def __init__(self, g: BoardGame):
        QWidget.__init__(self)
        self._game = g
        self.setLayout(QGridLayout())
        for y in range(g.rows()):
            for x in range(g.cols()):
                b = QPushButton()
                self.layout().addWidget(b, y, x)
                b.clicked.connect(lambda state, x=x, y=y:
                                  self.handle_click(x, y))
        self.update_all_buttons()

    def handle_click(self, x: int, y: int):
        self._game.play_at(x, y)
        self.update_all_buttons()

    def update_all_buttons(self):
        for y in range(self._game.rows()):
            for x in range(self._game.cols()):
                val = self._game.get_val(x, y)
                i = y * self._game.cols() + x
                b = self.layout().itemAt(i).widget()
                b.setText(val)
        if self._game.finished():
            QMessageBox.information(self, self.tr('Game finished'),
                                    self.tr(self._game.message()))
            self.window().close()


def main():
    app = QApplication(argv)
    game = Knights(6)  # try creating a Fifteen or a TicTacToe
    gui = BoardGameGui(game)
    gui.show()
    app.exec_()

if __name__ == '__main__':
    main()
