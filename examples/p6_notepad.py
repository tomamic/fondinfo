#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from sys import argv
from PySide.QtGui import (QWidget, QTextEdit, QPushButton, QMainWindow,
                          QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox,
                          QApplication)

class Notepad(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._text_edit = QTextEdit()
        self._open_button = QPushButton(self.tr("&Open"))
        self._save_button = QPushButton(self.tr("&Save"))
        self._exit_button = QPushButton(self.tr("&Exit"))

        button_layout = QVBoxLayout()
        button_layout.addWidget(self._open_button)
        button_layout.addWidget(self._save_button)
        button_layout.addWidget(self._exit_button)
        button_layout.addStretch()

        main_layout = QHBoxLayout()
        main_layout.addWidget(self._text_edit)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        
        self.setWindowTitle(self.tr('Notepad'))
        self._save_button.clicked.connect(self.save)
        self._open_button.clicked.connect(self.open)
        self._exit_button.clicked.connect(self.exit)

    def open(self):
        file_name = QFileDialog.getOpenFileName(self)[0]
        if file_name != '':
            try:
                with open(file_name, mode='rt') as in_file:
                    text = in_file.read()
                    self._text_edit.setText(text)
            except:
                QMessageBox.critical(self, self.tr('Error'),
                                           self.tr('Could not open file'))

    def save(self):
        file_name = QFileDialog.getSaveFileName(self)[0]
        if file_name != '':
            try:
                with open(file_name, mode='wt') as out_file:
                    text = self._text_edit.toPlainText()
                    out_file.write(text)
            except:
                QMessageBox.critical(self, self.tr('Error'),
                                           self.tr('Could not save file'))

    def exit(self):
        button = QMessageBox.question(
            self, self.tr('Notepad - Quit'),
            self.tr('Do you really want to quit?'),
            QMessageBox.Yes | QMessageBox.No)
        if button == QMessageBox.Yes:
            self.window().close()


class NotepadWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._notepad = Notepad(self)
        self.setCentralWidget(self._notepad)

        file_menu = self.menuBar().addMenu(self.tr("&File"))
        open_action = file_menu.addAction(self.tr("&Open"))
        save_action = file_menu.addAction(self.tr("&Save"))
        file_menu.addSeparator()
        exit_action = file_menu.addAction(self.tr("&Exit"))
        
        open_action.triggered.connect(self._notepad.open)
        save_action.triggered.connect(self._notepad.save)
        exit_action.triggered.connect(self._notepad.exit)

        # tool_bar = self.addToolBar(self.tr("File"))
        # tool_bar.addAction(open_action)
        # tool_bar.addAction(save_action)
        # tool_bar.addSeparator()
        # tool_bar.addAction(exit_action);

def main():
    app = QApplication(argv)

    # n = Notepad()
    # n.show()

    w = NotepadWindow()
    w.show()

    app.exec_()

if __name__ == '__main__':
    main()
