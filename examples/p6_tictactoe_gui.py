#!/usr/bin/python3

from sys import argv
from PySide.QtGui import (QWidget, QGridLayout, QPushButton,
                          QMessageBox, QApplication)

from p6_fifteen_gui import GameGui
from p6_tictactoe import TicTacToe

def main():
    app = QApplication(argv)
    game = TicTacToe(3)
    gui = GameGui(game)
    app.exec_()

if __name__ == '__main__':
    main()
