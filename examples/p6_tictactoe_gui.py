#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

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
