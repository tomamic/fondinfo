#!/usr/bin/python3

from sys import argv
from PySide.QtGui import (QWidget, QGridLayout, QPushButton,
                          QMessageBox, QApplication)
from p6_tictactoe import TicTacToe


class GameGui(QWidget):
    def __init__(self, game: TicTacToe):
        QWidget.__init__(self)
        self._game = game
        self._cols, self._rows = game.size()
        self.setLayout(QGridLayout())
        for y in range(self._rows):
            for x in range(self._cols):
                b = QPushButton()
                self.layout().addWidget(b, y, x)
                b.clicked.connect(lambda x=x, y=y:
                    self.handle_click(x, y))
        self.update_all_buttons()
        self.setWindowTitle(self.tr('TicTacToe'))
        self.show()
        
    def update_button(self, x: int, y: int):
        val = self._game.get(x, y)
        if val == TicTacToe.NONE: val = ' '
        b = self.layout().itemAt(y * self._cols + x).widget()
        b.setText(val)

    def update_all_buttons(self):
        for y in range(self._rows):
            for x in range(self._cols):
                self.update_button(x, y)
                
    def handle_click(self, x: int, y: int):
        self._game.play_at(x, y)
        self.update_button(x, y)

        winner = self._game.winner()
        if winner != TicTacToe.NONE:
            QMessageBox.information(self, 'Game finished',
                                    'Winner: ' + winner)
            self._game.clear()
            self.update_all_buttons()
            

def main():
    app = QApplication(argv)
    game = TicTacToe(3)
    gui = GameGui(game)
    app.exec_()

if __name__ == '__main__':
    main()
