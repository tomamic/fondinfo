#!/usr/bin/python3

from sys import argv
from PySide.QtGui import (QButtonGroup, QGridLayout, QPushButton,
                          QWidget, QMessageBox, QApplication)
from p6_fifteen import Game, Fifteen


class GameGui(QWidget):
    def __init__(self, game: Game):
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
        self.setWindowTitle(self.tr('Fifteen Puzzle'))
        self.show()

    def update_button(self, x: int, y: int):
        val = self._game.get_val(x, y)
        b = self.layout().itemAt(y * self._cols + x).widget()
        b.setText(val)

    def update_all_buttons(self):
        for y in range(self._rows):
            for x in range(self._cols):
                self.update_button(x, y)
                
    def handle_click(self, x: int, y: int):
        self._game.play_at(x, y)
        self.update_all_buttons()
        
        if self._game.finished():
            QMessageBox.information(self,
                                    self.tr('Game finished'),
                                    self.tr(self._game.message()))
            self.window().close()
            

def main():
    app = QApplication(argv)
    game = Fifteen(4, 4)
    gui = GameGui(game)
    app.exec_()

if __name__ == '__main__':
    main()
