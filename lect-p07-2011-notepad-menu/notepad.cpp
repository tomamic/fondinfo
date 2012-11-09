/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2011
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "notepad.h"

#include <QtGui/QApplication>
#include <QtGui/QMainWindow>
#include <QtGui/QAction>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QToolBar>
#include <QtGui/QFileDialog>
#include <QtGui/QMessageBox>
#include <fstream>

using namespace std;

Notepad::Notepad(QWidget* parent) : QMainWindow(parent)
{
    textEdit = new QTextEdit();

    setCentralWidget(textEdit);

    // Create some actions
    QAction* openAction = new QAction(tr("&Open"), this);
    QAction* saveAction = new QAction(tr("&Save"), this);
    QAction* exitAction = new QAction(tr("E&xit"), this);
    connect(openAction, SIGNAL(triggered()), this, SLOT(open()));
    connect(saveAction, SIGNAL(triggered()), this, SLOT(save()));
    connect(exitAction, SIGNAL(triggered()), this, SLOT(exit()));

    // Add all the actions to a menu
    QMenu* fileMenu = menuBar()->addMenu(tr("&File"));
    fileMenu->addAction(openAction);
    fileMenu->addAction(saveAction);
    fileMenu->addSeparator();
    fileMenu->addAction(exitAction);

    // Add all the actions to a toolbar
    QToolBar* toolBar = addToolBar(tr("&File"));
    toolBar->addAction(openAction);
    toolBar->addAction(saveAction);
    toolBar->addSeparator();
    toolBar->addAction(exitAction);

    setWindowTitle(tr("Notepad"));
    show();
}

Notepad::~Notepad()
{
    /* intentionally empty */
}

void Notepad::open()
{
    QString fileName = QFileDialog::getOpenFileName(
                this, tr("Open File"), "",
                tr("Text Files (*.txt);; C++ Files (*.cpp *.h)"));
    if (fileName != "") {
        ifstream file(fileName.toStdString().c_str());
        if (file.good()) {
            // read application data from file stream
            string content, line;
            while (getline(file, line)) {
                if (content != "") content += "\n";
                content += line;
            }
            textEdit->setText(QString(content.c_str()));
        } else {
            QMessageBox::critical(
                        this, tr("Error"),
                        tr("Could not open file"));
        }
    }
}

void Notepad::save()
{
    QString fileName = QFileDialog::getSaveFileName(
                this,
                tr("Save File"), "",
                tr("Text Files (*.txt);;C++ Files (*.cpp *.h)"));
    if (fileName != "") {
        ofstream file(fileName.toStdString().c_str());
        if (file.good()) {
            // write application data to file stream
            file << textEdit->toPlainText().toStdString();
        } else {
            QMessageBox::critical(
                        this,
                        tr("Error"),
                        tr("Could not open file"));
        }
    }
}

void Notepad::exit()
{
    int button = QMessageBox::question(
                this,
                tr("Quit"),
                tr("Do you really want to quit?"),
                QMessageBox::Yes | QMessageBox::No);

    if (button == QMessageBox::Yes) {
        qApp->quit();
    }
}
